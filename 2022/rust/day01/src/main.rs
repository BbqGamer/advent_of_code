use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let mut lines = io::stdin().lock().lines();

    let mut cur: i32 = 0;

    let mut top_three: [i32; 3] = [0, 0, 0];

    while let Some(line) = lines.next() {
        let food = line.unwrap();
        
        if food != "" {
            match food.parse::<i32>() {
                Ok(v) => cur += v,
                Err(e) => println!("Error parsing to int: {}",e),
            }
        } else {
            put_into_ranking(cur, &mut top_three);
            cur = 0;
        }
    }
    put_into_ranking(cur, &mut top_three);

    println!("Task 1: {}", top_three[0]);
    let sum: i32 = top_three.iter().sum();
    println!("Task 2: {}", sum);

    Ok(())
}

fn put_into_ranking(x: i32, ranking: &mut [i32]) {
    for i in 0..3 {
        if x > ranking[i] {
            for j in ((i+1)..3).rev() {
                ranking[j] = ranking[j-1];
            }
            ranking[i] = x;
            return;
        }
    }
}