use std::io::{self, Read, Write};

mod tests;

type Point = (i32, i32);
struct Area {
    middle: Point,
    closest: Point,
    radius: i32,
}

struct Line {
    start: Point,
    length: i32,
}

struct Rectangle {
    left_upper: Point,
    right_down: Point,
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input, 2000000))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input, 4000000))?;

    Ok(())
}

fn part1(input: &str, row_y: i32) -> i32 {
    let areas = parse_lines(input);
    let min_x = -20000000;
    let max_x = 20000000;

    let initial = Line {
        start: (min_x, row_y),
        length: max_x - min_x,
    };

    let mut count = 0;
    let mut stack = vec![initial];

    while !stack.is_empty() {
        let line = stack.pop().unwrap();

        let (x, y) = line.start;

        if line_contained(&line, &areas) {
            count += line.length;
            continue;
        }

        if line.length == 1 {
            continue;
        }

        //if crosses
        if !line_crosses(&line, &areas) {
            continue;
        }

        let lenght = line.length / 2;
        stack.push(Line {
            start: (x, y),
            length: lenght,
        });

        stack.push(Line {
            start: (x + lenght, y),
            length: line.length - lenght,
        });
    }

    //get list of unique closest beacons from all areas
    let mut beacons = vec![];
    for area in areas {
        if !beacons.contains(&area.closest) {
            beacons.push(area.closest);
        }
    }
    for beacon in beacons {
        if beacon.1 == row_y {
            count -= 1;
        }
    }
    
    count
}

fn line_contained(line: &Line, areas: &Vec<Area>) -> bool {
    for area in areas {
        let radius = area.radius;

        let (x, y) = line.start;

        if manhattan_distance((x,y), area.middle) <= radius
        && manhattan_distance((x + line.length - 1, y), area.middle) <= radius {
            return true;
        }
    }
    return false;
}

fn line_crosses(line: &Line, areas: &Vec<Area>) -> bool {
    for area in areas {
        let radius = area.radius;

        let (x, y) = line.start;

        if manhattan_distance((x,y), area.middle) <= radius {
            return true;  
        } 

        if manhattan_distance((x + line.length - 1, y), area.middle) <= radius {
            return true;
        }

        if area.middle.0 < x || area.middle.0 > x + line.length {
            continue;
        }

        if (area.middle.1 - y).abs() <= radius {
            return true;
        }
    }
    return false;
}

fn part2(input: &str, limit: i32) -> i128 {
    let areas = parse_lines(input);
    
    let initial = Rectangle {
        left_upper: (0, 0),
        right_down: (limit, limit),
    };

    let mut stack = vec![initial];
    while !stack.is_empty() {
        let rectangle = stack.pop().unwrap();
        
        let (x, y) = rectangle.left_upper;
        let (x1, y1) = rectangle.right_down;

        if rectangle_contained(&rectangle, &areas) {
            continue;
        }

        if rectangle.left_upper == rectangle.right_down {
            if !rectangle_contained(&rectangle, &areas) {
                return rectangle.left_upper.0 as i128 * 4000000 + rectangle.left_upper.1 as i128;
            } else {
                continue;
            }
        }

        let width = x1 - x;
        let height = y1 - y;

        if width > height {
            let new_width = width / 2;
            stack.push(Rectangle { left_upper: (x, y), right_down: (x+new_width ,y1)});
            stack.push(Rectangle { left_upper: (x+new_width+1, y), right_down: (x1 ,y1)});
        } else {
            let new_height = height / 2;
            stack.push(Rectangle { left_upper: (x, y), right_down: (x1 ,y+new_height)});
            stack.push(Rectangle { left_upper: (x, y+new_height+1), right_down: (x1 ,y1)});
        }
    }

    return -1;
}

fn rectangle_contained(rectangle: &Rectangle, areas: &Vec<Area>) -> bool {
    for area in areas {
        let radius = area.radius;

        let (x, y) = rectangle.left_upper;
        let (x1, y1) = rectangle.right_down;

        if manhattan_distance((x,y), area.middle) <= radius
        && manhattan_distance((x1, y), area.middle) <= radius
        && manhattan_distance((x, y1), area.middle) <= radius
        && manhattan_distance((x1, y1), area.middle) <= radius
        {
            return true;
        }
    }
    return false;
}

fn manhattan_distance(x: Point, y: Point) -> i32 {
    (x.0 - y.0).abs() + (x.1 - y.1).abs()
}

fn parse_lines(input: &str) -> Vec<Area> {
    input
        .lines()
        .filter_map(|line| parse_line(line))
        .collect()
}

fn parse_line(line: &str) -> Option<Area> {
    let mut parts = line.split(": ");
    let sensor_part = parts.next()?;
    let beacon_part = parts.next()?;

    let mut sensor_coords = sensor_part.split(" at x=");
    let _ = sensor_coords.next()?;
    let sensor_coords = sensor_coords.next()?;
    let sensor_coords: Vec<&str> = sensor_coords.split(", y=").collect();

    let mut beacon_coords = beacon_part.split(" at x=");
    let _ = beacon_coords.next()?;
    let beacon_coords = beacon_coords.next()?;
    let beacon_coords: Vec<&str> = beacon_coords.split(", y=").collect();

    let sensor_x = sensor_coords[0].parse::<i32>().ok()?;
    let sensor_y = sensor_coords[1].parse::<i32>().ok()?;
    let beacon_x = beacon_coords[0].parse::<i32>().ok()?;
    let beacon_y = beacon_coords[1].parse::<i32>().ok()?;

    Some(
        Area {
            middle: (sensor_x, sensor_y),
            closest: (beacon_x, beacon_y),
            radius: manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y)),
        }
    )
}