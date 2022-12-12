use std::{io::{self, Read, Write}, u8, collections::HashSet};
use std::collections::BinaryHeap;
use std::cmp::Reverse;
use itertools::Itertools;

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

type Map = Vec<Vec<u8>>; 
type Point = (usize, usize);

struct Data {
    map: Map,
    start: Point,
    end: Point,
}

fn part1(input: &str) -> usize {
    let data = read_input(input);
    let res = dijkstra(&data.map, data.start, is_max_one_higher);
    res[data.end.0][data.end.1]
}

fn part2(input: &str) -> usize {
    let data = read_input(input);

    let distances = dijkstra(&data.map, data.end, is_max_one_lower);

    let n = data.map.len();
    (0..n).cartesian_product(0..n)
            .filter(|(a,b)| data.map[*a][*b] == 'a' as u8)
            .map(|(a,b)| distances[a][b])
            .min()
            .unwrap()

}

fn read_input(input: &str) -> Data {
    let mut map: Map = input
        .lines()
        .map(|line| line.as_bytes().to_vec())
        .collect();
    
    let mut start = (0, 0);
    let mut end = (0, 0);

    for i in 0..map.len() {
        for j in 0..map[i].len() {
            if map[i][j] == 'S' as u8 {
                map[i][j] = 'a' as u8;
                start = (i, j);
            }
            if map[i][j] == 'E' as u8 {
                map[i][j] = 'z' as u8;
                end = (i, j);
            }
        }
    }

    Data {
        map,
        start,
        end
    }
}

type FilterFunc = fn(&Map, Point, Point) -> bool;

fn dijkstra(map: &Map, start: Point, filter: FilterFunc) -> Vec<Vec<usize>> {
    let mut distances: Vec<Vec<usize>> = vec![vec![u32::MAX as usize; map[0].len()]; map.len()];

    let mut visited: HashSet<(usize, usize)> = HashSet::new();
    let mut queue = BinaryHeap::new();
    queue.push(Reverse((0, start)));

    while !queue.is_empty() {
        let (distance, point) = queue.pop().unwrap().0;
        if visited.contains(&point) {
            continue;
        }
        visited.insert(point);
        distances[point.0][point.1] = distance;

        for neighbor in get_neighborhood(map, point, filter) {
            if visited.contains(&neighbor) {
                continue;
            }
            queue.push(Reverse((distance+1, neighbor)));
        }
    }

    distances
}

fn get_neighborhood(map: &Map, (i, j): Point, filter: FilterFunc) -> Vec<Point> {
    let mut res: Vec<Point> = Vec::new();

    if i > 0 && filter(&map, (i,j), (i-1,j)) {
        res.push((i-1, j));
    }
    if i < map.len() - 1 && filter(&map, (i,j), (i+1,j)) {
        res.push((i+1, j));
    }
    if j > 0 && filter(&map, (i,j), (i,j-1)) {
        res.push((i, j-1));
    }
    if j < map[i].len() - 1 && filter(map, (i,j), (i,j+1)) {
        res.push((i, j+1));
    }

    res
}


fn is_max_one_higher(map: &Map, a: Point, b: Point) -> bool {
    map[b.0][b.1] as i8 - map[a.0][a.1] as i8 <= 1
}

fn is_max_one_lower(map: &Map, a: Point, b: Point) -> bool {
    map[b.0][b.1] as i8 - map[a.0][a.1] as i8 >= -1
}