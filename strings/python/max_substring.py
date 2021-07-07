# We have to find the longest substring without repeating the characters. 
# So if the string is like “ABCABCBB”, then the result will be 3, 
# as there is a substring that is repeating, of length 3. That is “ABC”.

def len_max_substring(main_str):
    if len(main_str)==0:
        return 0
    cnt = {}
    i=0
    j=0
    size = len(main_str)
    ans=0
    while j < size:
        if main_str[j] not in cnt or i>cnt[main_str[j]]:
            ans = max(ans,(j-i+1))
            cnt[main_str[j]] = j
        else:
            i = cnt[main_str[j]]+1
            ans = max(ans,(j-i+1))
            j-=1
        j+=1
    return ans


if __name__ == '__main__':
    print(len_max_substring('suysash'))


