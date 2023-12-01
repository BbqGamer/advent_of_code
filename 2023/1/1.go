package main

import (
    "fmt"
)

func main() {
    // Scan lines from stdin untill EOF
    var s string
    result := 0
    for {
        _, err := fmt.Scanln(&s)
        if err != nil {
            break
        }
        
        for i := 0; i < len(s); i++ {
            if s[i] >= '0' && s[i] <= '9' {
                result += int(s[i] - '0') * 10
                break
            }
        }

        for i := len(s) - 1; i >= 0; i-- {
            if s[i] >= '0' && s[i] <= '9' {
                result += int(s[i] - '0')
                break
            }
        }
    }
    fmt.Print(result)
}
