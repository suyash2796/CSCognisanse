package main

import (
	"fmt"
)

func Kadane(Array []int32) ([]int32, int32) {

	// declare variables
	MaxStart := 0
	MaxEnd := 1
	Start := 0
	End := 1
	sum := Array[0]
	maxSum := Array[0]

	// traverse through arrays with Kadanes Algorithm
	for i := 1; i < len(Array); i++ {
		if Array[i] > Array[i]+sum {
			sum = Array[i]
			Start = i
			End = i + 1
		} else {
			sum += Array[i]
			End = i + 1
		}
		if sum > maxSum {
			maxSum = sum
			MaxStart = Start
			MaxEnd = End
		}
	}

	// declare and initialize BestArray and Array1/2
	BestArray := make([]int32, MaxEnd-MaxStart)
	copy(BestArray, Array[MaxStart:MaxEnd])
	return BestArray, maxSum
}

func main() {
	// Example Arrays
	Array1 := []int32{-6, -8, 12, -8, 9, 3, -4, 1, -25, 5}
	Array2 := []int32{-9, -12, -5, -1, -4, -17, -6, -2, -4, -3}
	fmt.Println(" ")

	// Calculate Array 1
	BestArray, Sum := Kadane(Array1)
	//You may view array by removing comments of the line below
	fmt.Println("Array 1: ", Array1)
	fmt.Println("Best Sub-array: ", BestArray)
	fmt.Println("Max Sum: ", Sum)
	fmt.Println(" ")

	// Calculate Array 2
	BestArray, Sum = Kadane(Array2)
	//You may view array by removing comments of the line below
	fmt.Println("Array 2: ", Array2)
	fmt.Println("Best Sub-array: ", BestArray)
	fmt.Println("Max Sum: ", Sum)
	fmt.Println(" ")
}
