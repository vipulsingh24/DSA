package main

import (
	"errors"
	"fmt"
	"sort"
)

type Driver struct {
	Name      string
	RideCount int
}

type RideRequest struct {
	Id        int
	Passenger string
	Driver    *Driver
}

type RideSharingApp struct {
	Drivers []Driver
	Rides   []RideRequest
}

// NewRideSharingApp initialized a new ride sharing app
func NewRideSharingApp(drivers []Driver) *RideSharingApp {
	return &RideSharingApp{
		Drivers: drivers,
		Rides:   []RideRequest{},
	}
}

func (app *RideSharingApp) findDriverWithLeastRides() (*Driver, error) {
	if len(app.Drivers) == 0 {
		return nil, errors.New("no drivers available")
	}

	sort.Slice(app.Drivers, func(i, j int) bool {
		return app.Drivers[i].RideCount < app.Drivers[j].RideCount
	})
	return &app.Drivers[0], nil
}

func (app *RideSharingApp) AddRideRequest(passenger string) error {
	driver, err := app.findDriverWithLeastRides()
	if err != nil {
		return err
	}

	ride := RideRequest{
		Id:        len(app.Rides) + 1,
		Passenger: passenger,
		Driver:    driver,
	}

	app.Rides = append(app.Rides, ride)
	driver.RideCount++
	return nil
}

func main() {
	drivers := []Driver{{Name: "A", RideCount: 0}, {Name: "B", RideCount: 0}}
	app := NewRideSharingApp(drivers)
	err := app.AddRideRequest("Passenger 1")
	if err != nil {
		fmt.Println("error for passenger 1: ", err)
	}

	err = app.AddRideRequest("Passenger 2")
	if err != nil {
		fmt.Println("error for passenger 2: ", err)
	}

	err = app.AddRideRequest("Passenger  3")
	if err != nil {
		fmt.Println("error for passenger 3: ", err)
	}
}
