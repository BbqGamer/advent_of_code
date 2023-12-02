package main

import (
    "fmt"
    "strings"
    "strconv"
    "bufio"
    "os"
)

var (
    m = map[string]int{
        "red": 12,
        "green": 13,
        "blue": 14,
    }
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    part1 := 0
    part2 := 0
    for scanner.Scan() {
        buf := scanner.Text()
        
        s := strings.SplitN(buf, " ", 3);
        g := s[1]
    
        gamen, err := strconv.Atoi(g[:len(g)-1])
        if err != nil {
            fmt.Errorf("Error converting game number to int")
            break
        }

        possible := true
        rounds := strings.Split(s[2], "; ")
        
        mincol := map[string]int {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for round := range rounds {
            items := strings.Split(rounds[round], ", ")
            for item := range items {
                i := strings.Split(items[item], " ")
                num, err := strconv.Atoi(i[0])
                if err != nil {
                    fmt.Errorf("Error converting item number to int")
                }
                col := i[1]
                if num > m[col] {
                    possible = false
                }

                if num > mincol[col] {
                    mincol[col] = num
                }
            }
        }
        if possible {
            part1 += gamen
        }
        part2 += mincol["red"] * mincol["green"] * mincol["blue"]
    }
    fmt.Printf("Part 1: %d\n", part1)
    fmt.Printf("Part 2: %d\n", part2)
}
