use std::io::{self, Read, Write};
use itertools::Itertools;

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn parts(input: &str, f: &dyn Fn(i32,i32,i32,i32) -> bool) -> i32 {
    return input.lines()
    .map(|l| l
        .split(['-',','])
        .map(|c| c.parse()
                  .unwrap())
        .collect_tuple::<(i32,i32,i32,i32)>()
        .unwrap()
    ).filter(|(a0, a1, b0, b1)| 
        f(*a0, *a1, *b0, *b1)
    ).count() as i32;
}   

fn part1(input: &str) -> i32 {
    return parts(input, &is_containted_in);
}

fn is_containted_in(a0: i32, a1: i32, b0: i32, b1: i32) -> bool {
    return (a0 >= b0 && a1 <= b1) || (b0 >= a0 && b1 <= a1);
}

fn part2(input: &str) -> i32 {
    return parts(input, &overlap);
}

fn overlap(a0: i32, a1: i32, b0: i32, b1: i32) -> bool {
    return (a0 >= b0 && a0 <= b1) || (a1 >= b0 && a1 <= b1) 
        || (b0 >= a0 && b0 <= a1) || (b1 >= a0 && b1 <= a1);
}