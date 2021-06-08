#O(2^n) solution
#Not a good solution because along with its complex recursion tree,
# it also take O(N) space in stack for N function calls
def fibonacci_term(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_term(n-1) + fibonacci_term(n-2)

#Good solution using Memoization
#This solution is O(N)
#This sol avoids duplicate calculations and make use of hash table to memoize prev sols
#O(N) space for memoization
def fibonacci_memoize(n):
    #hash table initialization
    mem = {1:0,2:1}
    if n in mem:
        return mem[n]
    else:
        mem[n] = fibonacci_memoize(n-1)+ fibonacci_memoize(n-2)
        return mem[n]

#Best solution for fibonacci will always be to loop till n and calc nth fibonacci
#which will be O(N) and O(1) in space
#Since that solution doesn't folllow recursive paradigm so not added here


if __name__==  '__main__':
    print(fibonacci_term(10))
    print(fibonacci_memoize(10))
    