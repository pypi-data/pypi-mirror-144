use pyo3::prelude::*;
use std::sync::mpsc;
use std::thread::Builder;
use std::{
    collections::{BinaryHeap, HashSet},
    vec,
};

#[pyfunction]
fn solve_the_problem(
    initial: [Option<u32>; 9],
    target: [Option<u32>; 9],
    mode: u32,
) -> PyResult<(u32, u32, Vec<[Option<u32>; 9]>)> {
    let (tx, rx) = mpsc::channel();
    let mut agent = Agent::new();
    //创建栈空间为32MB的线程求解问题
    let child = Builder::new()
        .stack_size(32 * 1024 * 1024)
        .spawn(move || {
            agent.try_to(initial, target, mode);
            tx.send((agent.deep, agent.cost, agent.result)).unwrap();
        })
        .unwrap();
    child.join().unwrap();
    Ok(rx.recv().unwrap())
}

/// A Python module implemented in Rust.
#[pymodule]
fn tjai_eight_puzzle(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(solve_the_problem, m)?)?;
    Ok(())
}
//求解问题的智能体
struct Agent {
    //Agent的记忆，用来存储以及探测过的情况
    memory: HashSet<[Option<u32>; 9]>,
    mode: u32,
    beg: [Option<u32>; 9],
    end: [Option<u32>; 9],
    deep: u32,
    cost: u32,
    result: Vec<[Option<u32>; 9]>,
}
impl Agent {
    //step:Agent每一步所付出的代价权重
    //h:启发函数
    fn new() -> Agent {
        Agent {
            memory: HashSet::new(),
            mode: 0,
            beg: [None; 9],
            end: [None; 9],
            deep: 0,
            cost: 0,
            result: vec![],
        }
    }
    fn try_to(&mut self, beg: [Option<u32>; 9], end: [Option<u32>; 9], mode: u32) {
        self.mode = mode;
        self.beg = beg;
        self.end = end;
        self.astar(beg, 1);
    }
    //执行a*算法
    fn astar(&mut self, now: [Option<u32>; 9], deep: u32) -> bool {
        //记忆当前情况
        if now == self.end {
            return true;
        }

        let mut now = now;
        let acts = ok_mov(&now);
        let mut facs = BinaryHeap::new();
        for act in acts {
            mov(&mut now, act);
            if self.memory.contains(&now) {
                mov(&mut now, deact(act));
                continue;
            }
            self.memory.insert(now);
            self.cost += 1;

            let h1 = h(self.mode, &now, &self.end);
            let g = deep * 2;
            facs.push(((g + h1) as i32 * -1, now));
            mov(&mut now, deact(act));
        }
        let mut result = false;
        while !facs.is_empty() {
            let next = facs.pop().unwrap().1;
            if self.astar(next, deep + 1) == true {
                result = true;
                //找到解后存放结果
                self.result.push(next);
                if self.deep < deep {
                    self.deep = deep;
                }
                break;
            }
        }
        result
    }
}
fn h(mode: u32, now: &[Option<u32>; 9], end: &[Option<u32>; 9]) -> u32 {
    match mode {
        1 => h1(now, end),
        2 => h2(now, end),
        3 => h3(now, end),
        4 => h4(now, end),
        _ => panic!("unexpected"),
    }
}
//启发函数1
//计算不在正确位置的数的个数
fn h1(now: &[Option<u32>; 9], end: &[Option<u32>; 9]) -> u32 {
    let mut count = 0;
    for i in 0..9 {
        if now[i] != end[i] {
            count += 1;
        }
    }
    count
}
//启发函数2
//计算曼哈顿距离
fn h2(now: &[Option<u32>; 9], end: &[Option<u32>; 9]) -> u32 {
    let sub_abs = |x: usize, y: usize| {
        if x >= y {
            x - y
        } else {
            y - x
        }
    };
    let mut count = 0;
    for i in 0..9 {
        let beg_loc = num_loc(now, i);
        let end_loc = num_loc(end, i);
        count += sub_abs(beg_loc.0, end_loc.0);
        count += sub_abs(beg_loc.1, end_loc.1);
    }
    count as u32
}
// 启发函数3
//如果方块和目标不在同一列，count+1
//如果方块和目标不在同一行，count+1
fn h3(now: &[Option<u32>; 9], end: &[Option<u32>; 9]) -> u32 {
    let mut count = 0;
    for i in 0..3 {
        for j in 0..3 {
            count += 1;
            for k in 0..3 {
                if now[find((i, j))] == end[find((i, k))] {
                    count -= 1;
                    break;
                }
            }
            count += 1;
            for k in 0..3 {
                if now[find((i, j))] == end[find((k, j))] {
                    count -= 1;
                    break;
                }
            }
        }
    }
    count
}
//启发函数4
//考虑线性冲突，如果同一line的不在位棋子目标也在同一line上，则count+3/4
//计算曼哈顿距离的改进版
fn h4(now: &[Option<u32>; 9], end: &[Option<u32>; 9]) -> u32 {
    let sub_abs = |x: usize, y: usize| {
        if x >= y {
            x - y
        } else {
            y - x
        }
    };
    let mut count = 0;
    for i in 0..9 {
        let beg_loc = num_loc(now, i);
        let end_loc = num_loc(end, i);
        count += sub_abs(beg_loc.0, end_loc.0);
        count += sub_abs(beg_loc.1, end_loc.1);
    }
    for i in 0..3 {
        let mut a = HashSet::new();
        let mut n = 0;
        for j in 0..3 {
            if now[find((i, j))] != end[find((i, j))] {
                a.insert(now[find((i, j))]);
                a.insert(end[find((i, j))]);
                n += 2;
            }
        }
        n -= a.len();
        count += n;
    }
    for j in 0..3 {
        let mut a = HashSet::new();
        let mut n = 0;
        for i in 0..3 {
            if now[find((i, j))] != end[find((i, j))] {
                a.insert(now[find((i, j))]);
                a.insert(end[find((i, j))]);
                n += 2;
            }
        }
        n -= a.len();
        count += n;
    }
    count as u32
}
#[derive(Debug, Clone, Copy)]
enum Action {
    Up,
    Down,
    Left,
    Right,
}
fn deact(act: Action) -> Action {
    match act {
        Action::Up => Action::Down,
        Action::Down => Action::Up,
        Action::Left => Action::Right,
        Action::Right => Action::Left,
    }
}
fn empty_loc(beg: &[Option<u32>; 9]) -> (usize, usize) {
    let mut loc = (0, 0);
    for i in 0..3 {
        for j in 0..3 {
            if beg[find((i, j))] == None {
                loc = (i, j);
                break;
            }
        }
    }
    loc
}
fn mov(beg: &mut [Option<u32>; 9], act: Action) {
    let loc = empty_loc(beg);
    match act {
        Action::Up => beg.swap(find(loc), find((loc.0, loc.1 - 1))),
        Action::Down => beg.swap(find(loc), find((loc.0, loc.1 + 1))),
        Action::Left => beg.swap(find(loc), find((loc.0 - 1, loc.1))),
        Action::Right => beg.swap(find(loc), find((loc.0 + 1, loc.1))),
    }
}
fn find(loc: (usize, usize)) -> usize {
    loc.0 + loc.1 * 3
}
fn num_loc(arr: &[Option<u32>; 9], num: u32) -> (usize, usize) {
    for i in 0..3 {
        for j in 0..3 {
            if Some(num) == arr[find((i, j))] {
                return (i, j);
            }
        }
    }
    (0, 0)
}
fn ok_mov(beg: &[Option<u32>; 9]) -> Vec<Action> {
    let loc = empty_loc(beg);
    let mut result = vec![];
    if loc.0 >= 1 {
        result.push(Action::Left);
    }
    if loc.0 <= 1 {
        result.push(Action::Right);
    }
    if loc.1 >= 1 {
        result.push(Action::Up);
    }
    if loc.1 <= 1 {
        result.push(Action::Down);
    }
    result
}
