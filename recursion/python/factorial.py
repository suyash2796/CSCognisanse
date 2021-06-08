
def nth_facto(n):
    #base case
    if n==1:
        return 1
    else:
        return n*nth_facto(n-1)

def nth_facto_memoize(n):
    mem = {0:1,1:1,2:2,3:6}
    if n in mem:
        return mem[n]
    else:
        mem[n] = n*nth_facto_memoize(n-1)
        return mem[n]


if __name__=='__main__':
    print(nth_facto(10))
    print(nth_facto_memoize(10))