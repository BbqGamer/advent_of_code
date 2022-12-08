#[cfg(test)]

mod tests {
    use super::super::{part1, part2, parse_input};

    static INPUT: &str = "30373
25512
65332
33549
35390";

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT), 21);
    }

    #[test]
    fn parse_input_test() {
        let expected: Vec<Vec<i32>> = vec![vec![3, 0, 3, 7, 3], 
                                           vec![2, 5, 5, 1, 2], 
                                           vec![6, 5, 3, 3, 2], 
                                           vec![3, 3, 5, 4, 9], 
                                           vec![3, 5, 3, 9, 0]];
        assert_eq!(parse_input(INPUT), expected);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT), 8);
    }
}