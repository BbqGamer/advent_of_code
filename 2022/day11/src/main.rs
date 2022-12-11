use std::io::{self, Read, Write};
use monkey::{Monkey, Operation};

mod monkey;
mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn part1(input: &str) -> i32 {
    let monkeys = parse_input(input);
    for monkey in monkeys {
        println!("{:?}", monkey.operation);
    }

    return -1;
}

fn part2(input: &str) -> &str {
    return "not solved yet";
}

fn parse_input(input: &str) -> Vec<Monkey> {
    let mut monkeys: Vec<Monkey> = Vec::new();    
    for entry in input.split("\n\n") {
        monkeys.push(Monkey::from_entry(entry));
    }

    monkeys
}