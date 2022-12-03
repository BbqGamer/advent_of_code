use std::io::{self, Read, Write};

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn part1(input: &str) -> i32 {
    let res: i32 = input.lines().map(|x| {
        let mut split = x.split(" ").map(|i| parse_move(i));
        match_eval1(split.next().unwrap(), split.next().unwrap())
    }).sum();

    return res;
}

#[derive(Copy, Clone)]
enum Move {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

fn parse_move(mov: &str) -> Move {
    return match mov {
        "A" | "X" => Ok(Move::Rock),
        "B" | "Y" => Ok(Move::Paper),
        "C" | "Z" => Ok(Move::Scissors),
        _ => Err("Invalid move".to_string()),
    }.unwrap();
}

fn match_eval1(a: Move, b: Move) -> i32 {
    let mut res: i32 = match(a,b) {
        (Move::Rock, Move::Rock) => {3},
        (Move::Paper, Move::Paper) => {3},
        (Move::Scissors, Move::Scissors) => {3},
        (Move::Scissors, Move::Rock) => {6},
        (Move::Rock, Move::Paper) => {6},
        (Move::Paper, Move::Scissors) => {6},
        _ => {0},
    };

    res += b as i32;

    return res;
}



fn part2(input: &str) -> i32 {
    let res: i32 = input.lines().map(|x| {
        let mut split = x.split(" ");
        match_eval2(parse_move(split.next().unwrap()), parse_res(split.next().unwrap()))
    }).sum();

    return res;
}

#[derive(Copy, Clone)]
enum Res {
    Defeat = 0,
    Tie = 3,
    Victory = 6,
}

fn parse_res(mov: &str) -> Res {
    return match mov {
        "X" => Ok(Res::Defeat),
        "Y" => Ok(Res::Tie),
        "Z" => Ok(Res::Victory),
        _ => Err("Invalid result".to_string()),
    }.unwrap();
}

fn match_eval2(a: Move, b: Res) -> i32 {
    let mut res: i32 = match(a,b) {
        (_, Res::Tie) => a as i32,
        (Move::Scissors, Res::Victory) => Move::Rock as i32,
        (Move::Rock, Res::Victory) => Move::Paper as i32,
        (Move::Paper, Res::Victory) => Move::Scissors as i32,
        (Move::Rock, Res::Defeat) => Move::Scissors as i32,
        (Move::Paper, Res::Defeat) => Move::Rock as i32,
        (Move::Scissors, Res::Defeat) => Move::Paper as i32,
    };

    res += b as i32;

    return res;
}