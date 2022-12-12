#[cfg(test)]

mod tests {
    use super::super::{part1, part2};

    static INPUT: &str = "Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi";

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT), 31);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT), 29);
    }
}