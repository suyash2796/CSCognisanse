package main
import ("fmt")

func Kadane(Array []int32) ([]int32, int32) {

	indexMax := len(Array)
	var sumVal = [20][20]int32{}

	result := int32(-2147483648)
	rArray := []int32{}

	for j := 1; j < indexMax+1; j++ {
		for i := 0; i < indexMax; i++ {
			if i+j > indexMax {
				continue
			}

			if j == 1 {
				sumVal[i][i+j] = Array[i]
				if Array[i] > result {
					result = Array[i]
					rArray = make([]int32, j)
					copy(rArray, Array[i:i+j])
				}
				continue
			}

			sumVal[i][i+j] = sumVal[i][i+j-1] + Array[i+j-1]
			if sumVal[i][i+j] > result {
				result = sumVal[i][i+j]
				rArray = make([]int32, j)
				copy(rArray, Array[i:i+j])
			}
		}
	}
	return rArray, result
}

func main() {
	// 2 example arrays to work off of
	Arr1 := []int32{-6, -8, 12, -8, 9, 3, -4, 1, -25, 5}
	Arr2 := []int32{-7, -9, -12, -5, -1, -4, -17, -6, -2, -4, -3}
	fmt.Println(" ")
	
	// Kadanes algorithm with array1
	rArray, result := Kadane(Arr1)
	fmt.Println("Array 1: ", Arr1)
	fmt.Println("Best array: ", rArray) 
	fmt.Println("Answer: ", result)
	fmt.Println(" ")

	// Kadanes algorithm with array2
	rArray, result = Kadane(Arr2)
	fmt.Println("Array 2: ", Arr2)
	fmt.Println("Best array: ", rArray)
	fmt.Println("Answer: ", result)
	
}
