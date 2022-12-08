#[cfg(test)]

mod tests {
    use super::super::{part1, part2, parse_data};

    static INPUT: &str = "    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2";

    #[test]
    fn parse_data_test() {
        let inp = parse_data(INPUT);
        let mut crates = inp.crates; 

        assert_eq!(crates[0].pop(), Some('N' as u8));
        assert_eq!(crates[0].pop(), Some('Z' as u8));

        assert_eq!(crates[1].pop(), Some('D' as u8));
        assert_eq!(crates[1].pop(), Some('C' as u8));

        let insts = inp.instructions;
        assert_eq!(insts[0].number, 1);
        assert_eq!(insts[0].from, 2);
        assert_eq!(insts[0].to, 1);

        assert_eq!(insts[3].number, 1);
        assert_eq!(insts[3].from, 1);
        assert_eq!(insts[3].to, 2);

    }

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT), "CMZ");
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT), "MCD");
    }
}