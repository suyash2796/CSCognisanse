def pattern_search(main_str, sub_str):
    l_main = len(main_str)
    l_sub = len(sub_str)
    for i in range(l_main-l_sub+1):
        cnt=0
        for j in range(l_sub):
            if (main_str[i + j] != sub_str[j]):
                break
            cnt+=1
        if cnt==l_sub:
            print('sub string matched')
            return True
    print('substr not matched')
    return False   


if __name__ == '__main__':
    pattern_search('ababba','xt')
    pattern_search('ababba','ab')
    pattern_search('ababba','babb')
    pattern_search('ababba','ababba')
    pattern_search('ababba','suyash')
