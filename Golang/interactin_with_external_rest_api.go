package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type User struct {
	Id   int    `json:"id"`
	Name string `json:"name"`
}

func main() {
	url := "https://api.test.com/user/123"
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error while fetching request: ", err)
		return
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		fmt.Println("Request failed with status code: ", resp.StatusCode)
		return
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error while reading response body: ", err)
		return
	}

	var user User
	err = json.Unmarshal(body, &user)
	if err != nil {
		fmt.Println("Error while parsing json response: ", err)
		return
	}

	fmt.Println("User: %v", user)
}
