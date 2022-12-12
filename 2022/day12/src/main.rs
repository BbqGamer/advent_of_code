use std::{io::{self, Read, Write}, u8, collections::HashSet};
use std::collections::BinaryHeap;
use std::cmp::Reverse;

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn part1(input: &str) -> usize {
    //get from input to two dimensional vector of ascii numbers
    let mut square = read_input(input);
    
    let mut s_i: usize = 0;
    let mut s_j: usize = 0;
    let mut e_i: usize = 0;
    let mut e_j: usize = 0;

    //Find 'S' set it to 1 and start DFS
    for i in 0..square.len() {
        for j in 0..square[i].len() {
            if square[i][j] == 'S' as u8 {
                square[i][j] = 'a' as u8;
                s_i = i;
                s_j = j;
            }
            if square[i][j] == 'E' as u8 {
                square[i][j] = 'z' as u8;
                e_i = i;
                e_j = j;
            }
        }
    }

    let res = dijkstra(&square, (s_i, s_j), is_max_one_higher);
    res[e_i][e_j]
}

fn read_input(input: &str) -> Vec<Vec<u8>> {
    input
        .lines()
        .map(|line| line.as_bytes().to_vec())
        .collect()
}

type FilterFunc = fn(&Vec<Vec<u8>>, (usize, usize), (usize, usize)) -> bool;

fn dijkstra(square: &Vec<Vec<u8>>, (s_i, s_j): (usize, usize),
    filter: FilterFunc) -> Vec<Vec<usize>> {
    let mut distances: Vec<Vec<usize>> = vec![vec![u32::MAX as usize; square[0].len()]; square.len()];

    let mut visited: HashSet<(usize, usize)> = HashSet::new();
    let mut queue = BinaryHeap::new();
    queue.push(Reverse((0,(s_i, s_j))));

    while !queue.is_empty() {
        let (d,(i, j)) = queue.pop().unwrap().0;
        if visited.contains(&(i,j)) {
            continue;
        }
        visited.insert((i, j));
        distances[i][j] = d;

        for (n_i, n_j) in get_neighborhood(square, i, j, filter) {
            if visited.contains(&(n_i, n_j)) {
                continue;
            }
            queue.push(Reverse((d+1, (n_i, n_j))));
        }
    }

    distances
}

fn get_neighborhood(square: &Vec<Vec<u8>>, i: usize, j: usize, filter: FilterFunc) -> Vec<(usize, usize)> {
    let mut res: Vec<(usize, usize)> = Vec::new();

    if i > 0 && filter(&square, (i,j), (i-1,j)) {
        res.push((i-1, j));
    }
    if i < square.len() - 1 && filter(&square, (i,j), (i+1,j)) {
        res.push((i+1, j));
    }
    if j > 0 && filter(&square, (i,j), (i,j-1)) {
        res.push((i, j-1));
    }
    if j < square[i].len() - 1 && filter(square, (i,j), (i,j+1)) {
        res.push((i, j+1));
    }

    res
}


fn is_max_one_higher(square: &Vec<Vec<u8>>, a: (usize, usize), b: (usize, usize)) -> bool {
    let diff = square[b.0][b.1] as i8 - square[a.0][a.1] as i8;
    return diff <= 1;
}

fn is_max_one_lower(square: &Vec<Vec<u8>>, a: (usize, usize), b: (usize, usize)) -> bool {
    let diff = square[b.0][b.1] as i8 - square[a.0][a.1] as i8;
    return diff >= -1;
}

fn part2(input: &str) -> usize {
    let mut square = read_input(input);
    
    let mut e_i: usize = 0;
    let mut e_j: usize = 0;

    //Find 'S' set it to 1 and start DFS
    for i in 0..square.len() {
        for j in 0..square[i].len() {
            if square[i][j] == 'S' as u8 {
                square[i][j] = 'a' as u8;
            }
            if square[i][j] == 'E' as u8 {
                square[i][j] = 'z' as u8;
                e_i = i;
                e_j = j;
            }
        }
    }

    let distances = dijkstra(&square, (e_i, e_j), is_max_one_lower);

    let mut minimum: usize = 100000000;
    for i in 0..square.len() {
        for j in 0..square[i].len() {
            if square[i][j] == 'a' as u8 {
                let res = distances[i][j];
                if res < minimum {
                    minimum = res;
                }
            }
        }
    }

    minimum
}