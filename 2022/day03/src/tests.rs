#[cfg(test)]

mod tests {
    use super::super::{part1, part2, process_backpack, process_item};

    static INPUT: &str = "vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw";

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT), 157);
    }

    #[test]
    fn process_backpack_test() {
        let b = "ttgJtRGJQctTZtZT";
        assert_eq!(process_backpack(b), 20);
    }

    #[test]
    fn process_item_test() {
        assert_eq!(process_item('A'), 27);
        assert_eq!(process_item('a'), 1);
        assert_eq!(process_item('Z'), 52);
        assert_eq!(process_item('z'), 26);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT), 70);
    }
}