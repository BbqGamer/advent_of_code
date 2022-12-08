use std::io::{self, Read, Write};

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input))?;

    Ok(())
}

fn part1(input: &str) -> i32 {
    let forrest_map: Vec<Vec<i32>> = parse_input(input);
    
    let mut is_visible_map: Vec<Vec<bool>> = vec![vec![false; forrest_map.len()]; forrest_map.len()];
    //set edges to visible
    for i in 0..forrest_map.len() {
        is_visible_map[0][i] = true;
        is_visible_map[forrest_map.len()-1][i] = true;
        is_visible_map[i][0] = true;
        is_visible_map[i][forrest_map.len()-1] = true;
    }
    
    
    horizontal_visible(&mut is_visible_map, &forrest_map);
    vertical_visible(&mut is_visible_map, &forrest_map);

    //println!("is_visible_map: {:?}", is_visible_map);

    is_visible_map.into_iter().flatten().filter(|&x| x).count() as i32

}

fn horizontal_visible(is_visible_map: &mut Vec<Vec<bool>>, forrest_map: &Vec<Vec<i32>>) {
    for i in 1..forrest_map.len()-1 {
        let mut highest = forrest_map[i][0];
        for j in 1..forrest_map.len()-1 {
            if forrest_map[i][j] > highest {
                is_visible_map[i][j] = true;
                highest = forrest_map[i][j];
            }
        }
    }

    for i in 1..forrest_map.len()-1 {
        let mut highest = forrest_map[i][forrest_map.len()-1];
        for j in (1..forrest_map.len()-1).rev() {
            if forrest_map[i][j] > highest {
                is_visible_map[i][j] = true;
                highest = forrest_map[i][j];
            }
        }
    }
}

fn vertical_visible(is_visible_map: &mut Vec<Vec<bool>>, forrest_map: &Vec<Vec<i32>>) {
    for i in 1..forrest_map.len()-1 {
        let mut highest = forrest_map[0][i];
        for j in 1..forrest_map.len()-1 {
            if forrest_map[j][i] > highest {
                is_visible_map[j][i] = true;
                highest = forrest_map[j][i];
            }
        }
    }

    for i in 1..forrest_map.len()-1 {
        let mut highest = forrest_map[forrest_map.len()-1][i];
        for j in (1..forrest_map.len()-1).rev() {
            if forrest_map[j][i] > highest {
                is_visible_map[j][i] = true;
                highest = forrest_map[j][i];
            }
        }
    }
}


fn parse_input(input: &str) -> Vec<Vec<i32>> {
    let mut forres_map: Vec<Vec<i32>> = Vec::new();
    for line in input.lines() {
        let mut line_array: Vec<i32> = Vec::new();
        for c in line.chars() {
            line_array.push(c.to_digit(10).unwrap() as i32);
        }
        forres_map.push(line_array);
    }
    forres_map
}

fn part2(input: &str) -> i32 {
    let forrest_map: Vec<Vec<i32>> = parse_input(input);

    return -1;
}

