#[cfg(test)]
mod tests {
    use super::super::{part1,part2};

    #[test]
    fn example_part1() {
        let example_input: &str = "A Y
B X
C Z";

        assert_eq!(part1(example_input), 15);
    }

    #[test]
    fn example_part2() {
        let example_input: &str = "A Y
B X
C Z";

        assert_eq!(part2(example_input), 12);
    }
}