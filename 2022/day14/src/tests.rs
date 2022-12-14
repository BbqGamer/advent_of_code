#[cfg(test)]

mod tests {
    use super::super::{part1, part2, read_rocks, printGrid};

    static INPUT: &str = "498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9";

    #[test]
    fn read_rocks_test() {
        let rocks = read_rocks(INPUT);
        printGrid(&rocks.content);
        assert_eq!(rocks.content.len(), 10);
    }

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT), 24);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT), 93);
    }
}