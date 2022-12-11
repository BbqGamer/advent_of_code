#[cfg(test)]

mod tests {
    use super::super::{part1, part2, Monkey, monkey::Operation};

    static INPUT: &str = "Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1";

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT), 10605);
    }
    
    #[test]
    fn monkey_from_entry() {
        let monkey: Monkey = Monkey::from_entry("Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3");

      assert_eq!(monkey.items, vec![79, 98]);   
      assert_eq!(monkey.operation, Operation::Multiply(19));
      assert_eq!(monkey.test, (23, 2, 3));
    }

    #[test]
    fn monkey_from_entry_2() {
        let monkey: Monkey = Monkey::from_entry("Monkey 3:
          Starting items: 58, 67, 66
          Operation: new = old * old
          Test: divisible by 7
            If true: throw to monkey 6
            If false: throw to monkey 1");

      assert_eq!(monkey.items, vec![58, 67, 66]);   
      assert_eq!(monkey.operation, Operation::Square);
      assert_eq!(monkey.test, (7, 6, 1));
    }


    #[test]
    fn test_operation() {
      assert_eq!(Operation::Add(5).exec(3), 8);
      assert_eq!(Operation::Multiply(5).exec(3), 15);
      assert_eq!(Operation::Square.exec(3), 9);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT), 2713310158);
    }
}