// m := make(map[strig]int)

package main

import (
	"fmt"
)

type UserInfo struct {
	Name string
	Id   int
}

type CustomMap struct {
	Data []UserInfo
}

func NewCustomMap() *CustomMap {
	return &CustomMap{
		Data: []UserInfo{},
	}
}

func (cm *CustomMap) Insert(key string, value int) {
	for i, kv := range cm.Data {
		if kv.Name == key {
			cm.Data[i].Id = value
			return
		}
	}
	cm.Data = append(cm.Data, UserInfo{Name: key, Id: value})
}

func (cm *CustomMap) Retrieve(key string) (int, bool) {
	for _, kv := range cm.Data {
		if kv.Name == key {
			return kv.Id, true
		}
	}
	return 0, false
}

func main() {
	cm := NewCustomMap()
	cm.Insert("Vipul", 10)
	cm.Insert("Sachin", 20)
	cm.Insert("Vipul", 30)

	// Retreive
	if value, exists := cm.Retrieve("Test"); exists {
		fmt.Println("Vipul value: ", value)
	} else {
		fmt.Println("Name not found")
	}

	fmt.Println(cm)
}
