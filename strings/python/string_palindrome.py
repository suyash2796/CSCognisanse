## check if a given string is palindrome of not

def check_palindrome(string):
    left=0
    right = len(string)-1
    for i in range(len(string)):
        if string[left]==string[right]:
            left+=1
            right-=1
            continue
        else:
            return False
    return True

if __name__=="__main__":
    print(check_palindrome('nitin'))
    print(check_palindrome('suyash'))
    print(check_palindrome('noon'))
    print(check_palindrome('racecar'))
    print(check_palindrome('demo'))
