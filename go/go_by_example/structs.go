package main

import "fmt"

/* Go's structs are TYPED COLLECTIONS of fields.*/

// person struct
type person struct {
	name        string
	age         int
	favoriteDog dog
}

// dog struct
type dog struct {
	name   string
	isGood bool
	woof   string
}

// new person constructor - this is a "method"
func newPerson(name string, age int) *person {
	p := person{
		name:        name,
		age:         age,
		favoriteDog: dog{},
	}

	return &p
}

func structs() {
	var basicDog dog = dog{
		name:   "Fido",
		isGood: true,
		woof:   "arf",
	}

	var chris person = *newPerson("Chris", 42)
	chris.favoriteDog = basicDog

	fmt.Println(chris)

	fmt.Println(chris.name)
	fmt.Println(chris.age)
	fmt.Println(chris.favoriteDog.name)

	// anonymouse struct
	randomDog := struct {
		name   string
		isGood bool
	}{
		name:   "Arfur",
		isGood: false,
	}

	fmt.Println(randomDog)

}
