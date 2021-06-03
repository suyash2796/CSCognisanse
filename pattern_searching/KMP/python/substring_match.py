
def substring_match(main_string, substring):
    pattern_table = make_pattern(substring)
    is_match = check_for_match(main_string, substring, pattern_table)
    return is_match # return bool

def make_pattern(substring):
    pattern = [-1 for i in substring]

    left = 0
    right = 1

    while right<len(substring):
        if substring[right]==substring[left]:
            pattern[right] = left
            left+=1
            right+=1
        elif left>0:
            left=pattern[left-1]+1
        else:
            right+=1
    print(pattern)
    return pattern

def check_for_match(main_string, substring, pattern_table):
    left=0
    right=0
    while right + len(substring) -left <= len(main_string):
        if substring[left] == main_string[right]:
            if left == len(substring) -1:
                return True
            left+=1
            right+=1
        elif left>0:
            left = pattern_table[left-1] +1
        else:
            right+=1
    return False




if __name__ == '__main__':
    print(substring_match('ababbababab', 'bbababs'))


