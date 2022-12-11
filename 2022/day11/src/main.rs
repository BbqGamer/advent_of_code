use std::io::{self, Read, Write};
use monkey::Monkey;

mod monkey;
mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn part1(input: &str) -> u64 {
    let mut monkeys = parse_input(input);
    simulate_monkeys(&mut monkeys, 20, true);
    monkey_business(&monkeys)
}

fn part2(input: &str) -> u64 {
    let mut monkeys = parse_input(input);
    simulate_monkeys(&mut monkeys, 10000, false);
    monkey_business(&monkeys)
}

fn simulate_monkeys(monkeys: &mut Vec<Monkey>, rounds: i32, relief: bool) {
    let lcm = least_common_multiple(&monkeys.iter().map(|x| x.test.0).collect::<Vec<u64>>());

    for _ in 0..rounds {
        for m in 0..monkeys.len() {
            while !monkeys[m].items.is_empty() {

                let mut new_item = monkeys[m].inspect();
                new_item = (if relief {new_item / 3} else {new_item}) % lcm;

                let next = monkeys[m].choose_next(new_item);
                monkeys[next].items.push(new_item);
            }
        }
    }    
}

fn parse_input(input: &str) -> Vec<Monkey> {
    let mut monkeys: Vec<Monkey> = Vec::new();    
    for entry in input.split("\n\n") {
        monkeys.push(Monkey::from_entry(entry));
    }

    monkeys
}

fn greatest_common_divisor(a : u64, b : u64) -> u64 {
    let mut a = a;
    let mut b = b;
    while b != 0 {
        let tmp = b;
        b = a % b;
        a = tmp;
    }
    a
}

fn least_common_multiple(numbers: &Vec<u64>) -> u64 {
    let mut lcm = numbers[0];
    for i in 1..numbers.len() {
        lcm = lcm * numbers[i] / greatest_common_divisor(lcm, numbers[i]);
    }
    lcm
}

fn monkey_business(monkeys: &Vec<Monkey>) -> u64 {
    let mut inspections = monkeys.iter().map(|x| x.inspects).collect::<Vec<u64>>();
    inspections.sort_by(|a, b| b.cmp(a));
    inspections[0] * inspections[1]
}