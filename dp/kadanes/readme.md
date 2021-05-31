**Maximum sum subarray**

Kadane's Algorithm is used to find maximum sum that can be obtained by summing up all the integers of contingious subaarray of the given array.

Concept of Dynamic Programming is used to obtain solution for this as we make use of previous calculated results to get solution.

The simple idea of Kadane’s algorithm is below:
1) look for all positive contiguous segments of the array.
2) keep track of maximum sum contiguous segment among all positive segments.
3) Each time we get a positive-sum compare it with current max and update current max if it is greater than current max 
