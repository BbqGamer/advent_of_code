use std::io::{self, Read, Write};
use std::collections::HashSet;
use itertools::Itertools;

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn part1(input: &str) -> u32 {
    return input.lines().map(|b| process_backpack(b.trim()) as u32).sum();
}

fn process_item(item: char) -> u8 {
    let ascii = item as u8;
    if item.is_lowercase() {
        return ascii - 96;
    } else {
        return ascii - 38;
    }
}

fn process_backpack(b: &str) -> u8 {
    let items = b.chars().map(|c| process_item(c));
    let l = items.clone().take(b.len()/2).collect();
    let r = items.skip(b.len()/2).collect();

    let left: HashSet::<u8> = l;
    let right: HashSet::<u8> = r;

    return *left.intersection(&right).next().unwrap();
}

fn part2(input: &str) -> u32 {
    return input.lines().tuples().map(|(x,y,z)| process_group(x, y, z) as u32).sum();
}

fn process_group(x: &str, y: &str, z: &str) -> u8 {
    let a: HashSet::<u8> = x.chars().map(|c| process_item(c)).collect();
    let b: HashSet::<u8> = y.chars().map(|c| process_item(c)).collect();
    let c: HashSet::<u8> = z.chars().map(|c| process_item(c)).collect();

    return *a.intersection(&b).map(|x| *x).collect::<HashSet<u8>>().intersection(&c).next().unwrap();
}