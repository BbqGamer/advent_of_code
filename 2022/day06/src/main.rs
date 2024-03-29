use std::io::{self, Read, Write};

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;
    
    Ok(())
}

fn part1(input: &str) -> usize {
    let chars: Vec<char> = input.chars().collect();
    for i in 3..chars.len() {
        if are_distinct(&chars[i - 3..i+1]) {
            return i + 1;
        }
    }

    return 0;
}

fn part2(input: &str) -> usize {
    let chars: Vec<char> = input.chars().collect();
    for i in 13..chars.len() {
        if are_distinct(&chars[i - 13..i+1]) {
            return i + 1;
        }
    }

    return 0;
}

fn are_distinct(chars: &[char]) -> bool {
    let mut set = std::collections::HashSet::new();    
    for c in chars {
        if set.contains(c) {
            return false;
        }
        set.insert(c);
    }
    return true;
}