#[cfg(test)]

mod tests {

    use super::super::{part1, part2, rectangle_contained, Rectangle, Area, x_range_from_area};

    static INPUT: &str = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3";

    #[test]
    fn example_part1() {
        assert_eq!(part1(INPUT, 10), 26);
    }

    #[test]
    fn example_part2() {
        assert_eq!(part2(INPUT, 20), 56000011);
    }

    #[test]
    fn test_quare_contained() {
        assert_eq!(rectangle_contained(&Rectangle {left_upper: (-2, -2), right_down: (2,2)}, &vec![Area{
            middle: (0,0),
            closest: (2,2),
            radius: 4
        }]), true);

        assert_eq!(rectangle_contained(&Rectangle {left_upper: (1, 1), right_down: (2,2)}, &vec![Area{
            middle: (0,0),
            closest: (2,2),
            radius: 4
        }]), true);

        assert_eq!(rectangle_contained(&Rectangle {left_upper: (1, 1), right_down: (3,3)}, &vec![Area{
            middle: (0,0),
            closest: (2,2),
            radius: 4
        }]), false);
    }

    #[test]
    fn check_x_range_from_area() {
        let a = Area {
            middle: (1,1),
            radius: 4,
            closest: (4, 1)
        };

        let r = x_range_from_area(&a, 0);
        assert_eq!(*r.start(), -2);
        assert_eq!(*r.end(), 4);
    }
}