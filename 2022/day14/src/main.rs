use std::{io::{self, Read, Write}, thread::sleep, time::Duration, num};
use itertools::Itertools;

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn part1(input: &str) -> usize {
    let grid = read_rocks(input);
    let mut g = grid.content;

    //printGrid(&g);

    let mut bottom = false;
    let mut num_particles = 0;

    loop {
        let (mut s_x, mut s_y) = (500 - grid.normalize_x, 0);
        num_particles += 1;
        loop {
            if s_y == g[0].len() - 1 || s_x == 0 || s_x == g.len() - 1 {
                //we reached the bottom
                bottom = true;
                break;
            }
            if !g[s_x][s_y+1] {
                s_y += 1; //fall down
            } else {
                if !g[s_x-1][s_y+1] {
                    s_x -= 1; //fall down left
                    s_y += 1; 
                } else if !g[s_x+1][s_y+1] {
                    s_x += 1; //fall down left
                    s_y += 1; 
                } else{
                    //we are blocked
                    g[s_x][s_y] = true;
                    break;
                }
            }

            //sleep(Duration::from_micros(10));
        }

        //printGrid(&g);

        if bottom {
            break;
        }
    }


    num_particles - 1
}

fn part2(input: &str) -> usize {
    let grid = read_rocks_2(input);
    let mut g = grid.content;

    //printGrid(&g);

    let mut bottom = false;
    let mut num_particles = 0;
    let start = (500 - grid.normalize_x, 0);

    loop {
        let (mut s_x, mut s_y) = start;
        num_particles += 1;
        loop {
            if s_y == g[0].len() - 1 || s_x == 0 || s_x == g.len() - 1 {
                //we reached the bottom
                //println!("bottom reached, if part2: try increasing grid size");
                bottom = true;
                break;
            }
            if !g[s_x][s_y+1] {
                s_y += 1; //fall down
            } else {
                if !g[s_x-1][s_y+1] {
                    s_x -= 1; //fall down left
                    s_y += 1; 
                } else if !g[s_x+1][s_y+1] {
                    s_x += 1; //fall down left
                    s_y += 1; 
                } else{
                    //we are blocked
                    if (s_x, s_y) == start {
                        //We are blocked at the start
                        return num_particles;
                    }
                    g[s_x][s_y] = true;
                    break;
                }
            }

            //sleep(Duration::from_micros(10));
        }

        //printGrid(&g);

        if bottom {
            break;
        }
    }


    num_particles - 1
}

struct Grid {
    normalize_x: usize,
    content: Vec<Vec<bool>>,
}

fn read_rocks(input: &str) -> Grid {
    let a = input.split("\n")
            .map(|line| line.split(" -> ")
                .map(|point| {
                    let mut it = point.split(",");
                    (it.next().unwrap().parse::<usize>().unwrap(),
                     it.next().unwrap().parse::<usize>().unwrap())
                }));
    
    //Find min x and y and max x and y from all the points
    let (min_x, min_y, max_x, max_y) = a.clone()
        .flatten()
        .fold((usize::MAX, usize::MAX, usize::MIN, usize::MIN), |(min_x, min_y, max_x, max_y), (x, y)| {
            (min_x.min(x), min_y.min(y), max_x.max(x), max_y.max(y))
        });
    
    let g = vec![vec![false; max_y + 1]; max_x - min_x + 1];
    let mut grid = Grid {
        normalize_x: min_x,
        content: g
    };


    for line in a {
        for (a, b) in line.tuple_windows() {
            write_line(a, b, &mut grid);
        }
    }

    grid
}

fn write_line(a: (usize, usize), b: (usize, usize), grid: &mut Grid) {
    //append points in line from a to b to the grid
    if a.0 == b.0 {
        //vertical line
        for y in a.1.min(b.1)..=a.1.max(b.1) {
            grid.content[a.0 - grid.normalize_x][y] = true;
        }
    } else {
        //horizontal line
        for x in a.0.min(b.0)..=a.0.max(b.0) {
            grid.content[x - grid.normalize_x][a.1] = true;
        }
    }
}

fn printGrid(grid: &Vec<Vec<bool>>) {
    for i in 0..grid[0].len() {
        for j in 0..grid.len() {
            if grid[j][i] {
                print!("# ");
            } else {
                print!(". ");
            }
        }
        println!();
    }
}

fn read_rocks_2(input: &str) -> Grid {
    let a = input.split("\n")
            .map(|line| line.split(" -> ")
                .map(|point| {
                    let mut it = point.split(",");
                    (it.next().unwrap().parse::<usize>().unwrap(),
                     it.next().unwrap().parse::<usize>().unwrap())
                }));
    
    //Find min x and y and max x and y from all the points
    let (min_x, min_y, max_x, max_y) = a.clone()
        .flatten()
        .fold((usize::MAX, usize::MAX, usize::MIN, usize::MIN), |(min_x, min_y, max_x, max_y), (x, y)| {
            (min_x.min(x), min_y.min(y), max_x.max(x), max_y.max(y))
        });
    
    let g = vec![vec![false; max_y + 3]; max_x + min_y + 100];
    let mut grid = Grid {
        normalize_x: 0,
        content: g
    };


    for line in a {
        for (a, b) in line.tuple_windows() {
            write_line(a, b, &mut grid);
        }
    }

    let n = grid.content[0].len();
    for x in 0..grid.content.len() {
        grid.content[x][n-1] = true;
        grid.content[x][n-1] = true;
    }

    grid
}