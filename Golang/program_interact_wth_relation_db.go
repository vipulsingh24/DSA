package main

import (
	"database/sql"
	"fmt"
	"log"
)

func createUser(db *sql.Db, username, email string) error {
	query := `INSERT INTO users (username, email) VALUES ($1, $2)`
	_, err := db.Exec(query, username, email)
	return err
}

func main() {
	connStr := "user=username password=password dbname=testDb sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	if err := db.Ping(); err != nil {
		log.Fatal("Cannot connect to the database: ", err)
	}

	fmt.Println("Connected to the database successfull!!")
	userInsertionErr := createUser(db, "Test", "test@test.com")
	if userInsertionErr != nil {
		log.Fatal("error while inserting user to the database: ", err)
	}
}
