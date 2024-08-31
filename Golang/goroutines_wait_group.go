// package GoRoutinesWG
package main

import (
	"fmt"
	"sync"
)

func sender(ch chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	texts := []string{"Hello", "World"}
	for _, msg := range texts {
		ch <- msg
	}
	close(ch)
}

func receiver(ch chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	for msg := range ch {
		fmt.Println("Received: ", msg)
	}
	fmt.Println("Channel closed")
}

func main() {
	ch := make(chan string)
	var wg sync.WaitGroup
	wg.Add(2)

	go sender(ch, &wg)
	go receiver(ch, &wg)
	wg.Wait()
	fmt.Println("Completed")
}
