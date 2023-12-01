package main

import (
    "fmt"
)

var mapping = map[string]int {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
    

func main() {
    // Scan lines from stdin untill EOF
    var s string
    result := 0
    for {
        _, err := fmt.Scanln(&s)
        if err != nil {
            break
        }

        
        found := false
        for i := 0; i < len(s); i++ {
            if found {
                break
            }

            if s[i] >= '0' && s[i] <= '9' {
                result += int(s[i] - '0') * 10
                break
            }

            for pattern := range mapping {
                if i + len(pattern) < len(s) && s[i:i+len(pattern)] == pattern {
                    result += mapping[pattern] * 10
                    found = true
                    break
                }
            }
        }

        found = false
        for i := len(s) - 1; i >= 0; i-- {
            if found {
                break
            }

            if s[i] >= '0' && s[i] <= '9' {
                result += int(s[i] - '0')
                break
            }

            for pattern := range mapping {
                if i - len(pattern) >= 0 && s[i+1-len(pattern):i+1] == pattern {
                    result += mapping[pattern]
                    found = true  
                    break
                }
            }
        }
    }
    fmt.Print(result)
}
