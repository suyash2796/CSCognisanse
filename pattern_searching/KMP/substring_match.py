
def substring_match(main_string, substring):
    pattern_table = make_pattern(substring)
    is_match = check_for_match(main_string, substring, pattern_table)
    return True # return bool

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
    # TODO: implement string match logic
    return True

if __name__ == '__main__':
    print(substring_match('ababbababab', 'bbaba'))


