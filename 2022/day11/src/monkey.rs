#[derive(PartialEq, Debug)]
pub enum Operation {
    Add(i32),
    Multiply(i32),
    Square,
}

impl Operation {
    pub fn exec(&self, l: i32) -> i32 {
        match self {
            Operation::Add(r) => l + r,
            Operation::Multiply(r) => l * r,
            Operation::Square => l * l,
        }
    }
}

pub struct Monkey {
    pub items: Vec<i32>,
    pub operation: Operation,
    pub test: (i32, i32, i32)
} 

impl Monkey {
    pub fn from_entry(entry: &str) -> Monkey {
        let mut attributes = entry.split("\n");
        attributes.next().unwrap(); //first line is monkey id
        let items: Vec<i32> = attributes.next().unwrap().trim()[16..].split(", ").map(|x| x.parse::<i32>().unwrap()).collect();
        let mut it = attributes.next().unwrap().trim().split(" ").skip(4);
        let (op, val) = (it.next().unwrap(), it.next().unwrap());
        let operation = match (op, val) {
            ("+", val) => Operation::Add(val.parse::<i32>().unwrap()),
            ("*", "old") => Operation::Square,
            ("*", val) => Operation::Multiply(val.parse::<i32>().unwrap()),
            _ => panic!("Unknown operation")
        };

        let test = (attributes.next().unwrap().trim().split(" ").nth(3).unwrap().parse::<i32>().unwrap(),
                        attributes.next().unwrap().trim().split(" ").nth(5).unwrap().parse::<i32>().unwrap(), 
                        attributes.next().unwrap().trim().split(" ").nth(5).unwrap().parse::<i32>().unwrap());

        Monkey {
            items,
            operation,
            test
        }
    }
}