#[derive(PartialEq, Debug)]
pub enum Operation {
    Add(u64),
    Multiply(u64),
    Square,
}

impl Operation {
    pub fn exec(&self, l: u64) -> u64 {
        match self {
            Operation::Add(r) => l + r,
            Operation::Multiply(r) => l * r,
            Operation::Square => l * l,
        }
    }
}

pub struct Monkey {
    pub items: Vec<u64>,
    pub operation: Operation,
    pub test: (u64, usize, usize),
    pub inspects: u64
} 

impl Monkey {
    pub fn from_entry(entry: &str) -> Monkey {
        let mut attributes = entry.split("\n");
        attributes.next().unwrap(); //first line is monkey id
        let items: Vec<u64> = attributes.next().unwrap().trim()[16..].split(", ").map(|x| x.parse::<u64>().unwrap()).collect();
        let mut it = attributes.next().unwrap().trim().split(" ").skip(4);
        let (op, val) = (it.next().unwrap(), it.next().unwrap());
        let operation = match (op, val) {
            ("+", val) => Operation::Add(val.parse::<u64>().unwrap()),
            ("*", "old") => Operation::Square,
            ("*", val) => Operation::Multiply(val.parse::<u64>().unwrap()),
            _ => panic!("Unknown operation")
        };

        let test = (attributes.next().unwrap().trim().split(" ").nth(3).unwrap().parse::<u64>().unwrap(),
                    attributes.next().unwrap().trim().split(" ").nth(5).unwrap().parse::<usize>().unwrap(), 
                    attributes.next().unwrap().trim().split(" ").nth(5).unwrap().parse::<usize>().unwrap());

        Monkey {
            items,
            operation,
            test,
            inspects: 0
        }
    }

    pub fn inspect(&mut self) -> u64 {
        self.inspects += 1;
        let mut item = self.items.pop().unwrap();
        item = self.operation.exec(item);
        item
    }

    pub fn choose_next(&self, item: u64) -> usize {
        if item % self.test.0 == 0 {
            self.test.1
        } else {
            self.test.2
        }
    }
}