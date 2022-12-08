use std::{io::{self, Read, Write}, collections::VecDeque};

mod tests;

#[derive(Debug)]
struct Instruction {
    number: usize,
    from: usize,
    to: usize,
}
struct Data {
    crates: Vec<Vec<u8>>,
    instructions: Vec<Instruction>,
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn parse_data(input: &str) -> Data {
    let (first, second) = input.split_once("\n\n").unwrap();

    let num_crates = (first.split_once("\n").unwrap().0.len() + 1) / 4;
    let mut crates: Vec<Vec<u8>> = vec![vec![]; num_crates];

    let mut curr: usize = 0;
    for crat in first.as_bytes().chunks(4) {
        
        match crat {
            [b'[', x, b']', b' ' | b'\n'] => {crates[curr].push(*x);},
            _ => {}
        }

        match crat {
            [_, _, _, b'\n'] => {curr = 0;},
            _ => {curr += 1;}
        }        
    }

    let mut data = Data {
        crates,
        instructions: vec![],
    };

    for line in second.lines() {
        let mut spl = line.split(" ");
        
        spl.next();
        let number: usize = spl.next().unwrap().parse().unwrap();

        spl.next();
        let from: usize = spl.next().unwrap().parse().unwrap();

        spl.next();
        let to: usize = spl.next().unwrap().parse().unwrap();


        let inst = Instruction {
            number,
            from,
            to
        };

        data.instructions.push(inst);
    }

    data.crates = data.crates.into_iter().map(|mut x| {x.reverse(); x}).collect();

    data
}

fn crates_to_res(crates: &Vec<Vec<u8>>) -> String {
    let mut res = String::from("");
    for s in crates {
        match s.last() {
            Some(x) => res.push(char::from(*x)),
            None => res += " "
        }
    }

    res
}

fn part1(input: &str) -> String {
    let inp = parse_data(input);
    let mut crates = inp.crates;
    let instructions = inp.instructions;

    for inst in instructions {
        for _ in 0..inst.number {
            let item = crates[inst.from-1].pop().unwrap();
            crates[inst.to-1].push(item);
        }
    }

    crates_to_res(&crates)
}

fn part2(input: &str) -> String {
    let inp = parse_data(input);
    let mut crates = inp.crates;
    let mut deque: VecDeque<u8> = VecDeque::new();
    let instructions = inp.instructions;

    for inst in instructions {
        for _ in 0..inst.number {
            let item = crates[inst.from-1].pop().unwrap();
            deque.push_front(item);
        }
        while !deque.is_empty() {
            crates[inst.to-1].push(deque.pop_front().unwrap());
        }
    }

    crates_to_res(&crates)
}