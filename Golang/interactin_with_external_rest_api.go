package main

import (
	"fmt"
	"net/http"
)

func main() {
	url := "https://api.test.com/user/123"
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error while fetching request: ", err)
		return
	}
	defer resp.Body.Close()
}
