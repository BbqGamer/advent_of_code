#[cfg(test)]

mod tests {
    use crate::overlap;

    use super::super::{part1, part2, is_containted_in};

    static INPUT: &str = "2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8";

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT), 2);
    }

    #[test]
    fn is_containted_in_test() {
        assert_eq!(is_containted_in(2,4,6,8), false);
        assert_eq!(is_containted_in(2,3,4,5), false);
        assert_eq!(is_containted_in(2,6,4,8), false);
        assert_eq!(is_containted_in(2,8,3,7), true);
        assert_eq!(is_containted_in(6,6,4,6), true);
        assert_eq!(is_containted_in(1,4,1,4), true);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT), 4);
    }

    #[test]
    fn overlap_test() {
        assert_eq!(overlap(5, 7, 7, 9), true);
        assert_eq!(overlap(2, 4, 6, 8), false);
        assert_eq!(overlap(2, 5, 2, 5), true);
        assert_eq!(overlap(2, 6, 4, 8), true);
        assert_eq!(overlap(6, 6, 4, 6), true);
    }
}