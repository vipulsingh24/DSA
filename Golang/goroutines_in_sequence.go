package main

import (
	"fmt"
	"sync"
)

func printNumber(n int, wg *sync.WaitGroup, ch chan struct{}) {
	defer wg.Done()
	<-ch
	fmt.Println(n)
	ch <- struct{}{}
}

func main() {
	var wg sync.WaitGroup
	ch := make(chan struct{}, 1)

	ch <- struct{}{}
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go printNumber(i, &wg, ch)
	}
	wg.Wait()
}

// func isPalindrome(n int) bool {
// 	s := strconv.Itoa(n)
// 	for i = 0; i < len(s/2); i++ {
// 		if s[i] != s[len(s) - i - 1] {
// 			return false
// 		}
// 	}
// 	return true
// }

// func main() {
// 	num := 121
// 	if isPalindrome(num) {
// 		fmt.Printf("%d is a palindrome number", num)
// 	} else {
// 		fmt.Printf("%d is not a palindrom number", num)
// 	}
// }

// n = 3
// ((()))

// ["((()))","(()())","(())()","()(())","()()()"] -> 6
// n = 1
// ["()"] -> 2
// n = 2
// ["()()", "(())",] -> 4

// func generateParantheses(n int) []string {
// 	var result []string
// 	var generate func(current string, open int, close int)
// 	generate = func(current string, open, close int) {
// 		if len(current) == 2 * n {
// 			result = append(result, current)
// 			return
// 		}

// 		if open > 0 {
// 			generate(current + "(",  open-1, close)
// 		}

// 		if close > open {
// 			generate(current + ")", open, close-1)
// 		}
// 	}

// 	generate("", n, n)
// 	return result
// }

// func main() {
// 	n := 1
// 	paranthesesResult := generateParantheses(n)
// 	fmt.Println(paranthesesResult)
// }

// each go routine will be printing a number upto 5
// write a print function taking a integer input called in loop and passing i value in function
