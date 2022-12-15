use std::io::{self, Read, Write};
use range_union_find::IntRangeUnionFind;
use std::ops::RangeInclusive;

mod tests;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input)?;

    writeln!(io::stdout(), "Part 1: {}", part1(&input, 2000000))?;
    writeln!(io::stdout(), "Part 2: {}", part2(&input, 4000000))?;

    Ok(())
}

fn part1(input: &str, row_y: i32) -> i32 {
    let areas = parse_lines(input);

    let mut range_holder = IntRangeUnionFind::<i32>::new();
    for area in areas {
        let _ = range_holder.insert_range(&x_range_from_area(&area, row_y));
        if area.closest.1 == row_y {
            let beacon_x = area.closest.0;
            let _ = range_holder.remove_range(&RangeInclusive::new(beacon_x, beacon_x));
        }
        if area.middle.1 == row_y {
            let sensor_x = area.middle.0;
            let _ = range_holder.remove_range(&RangeInclusive::new(sensor_x, sensor_x));
        }
    }

    let ranges: Vec<RangeInclusive<i32>> = range_holder.to_collection();
    ranges.iter().
        map(|r| r.end() - r.start() + 1).
        sum::<i32>()
}

fn x_range_from_area(area: &Area, y_pos: i32) -> RangeInclusive<i32> {
    let diff = (area.middle.1 - y_pos).abs();
    let start = area.middle.0 - area.radius + diff;
    let end = area.middle.0 + area.radius - diff;

    RangeInclusive::new(start, end)
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

type Point = (i32, i32);
struct Area {
    middle: Point,
    closest: Point,
    radius: i32,
}

struct Rectangle {
    left_upper: Point,
    right_down: Point,
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