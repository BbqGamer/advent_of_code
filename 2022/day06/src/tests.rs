#[cfg(test)]

mod tests {
    use super::super::{part1, part2, are_distinct};

    #[test]
    fn example_part1() {
        assert_eq!(part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7);
        assert_eq!(part1("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5);
        assert_eq!(part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10);
        assert_eq!(part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11);
    }

    #[test]
    fn test_are_distinc() {
        assert_eq!(are_distinct(&['a', 'b', 'c', 'd']), true);
        assert_eq!(are_distinct(&['a', 'b', 'c', 'a']), false);
        assert_eq!(are_distinct(&['a', 'b', 'a', 'b']), false);
        assert_eq!(are_distinct(&['a', 'a', 'a', 'a']), false);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 19);
    }
}