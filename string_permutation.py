def string_permutation(str1,str2):
    str_len1=len(str1)
    str_len2=len(str2)
    ascii_dict = dict.fromkeys([i for i in range(256)],0)

    if (str_len1 != str_len2):
        return False

    for c in str1:
        ascii_dict[ord(c)]+=1
    for ch in str2:
        ascii_dict[ord(ch)]-=1
    for key in ascii_dict:
        if  ascii_dict[key] > 0:
            return False
    return True

def string_permutation_sort(str1,str2):
    str_len1=len(str1)
    str_len2=len(str2)
    
    s1=''.join(sorted(str1))
    s2=''.join(sorted(str2))
    if (str_len1 != str_len2):
        return False

    for c in range(str_len1):
        if s1[c] != s2[c]:
            return False
    return True
        
            
s1="asdfghh"
s2="asdfghh"
print(string_permutation(s1,s2))
print(string_permutation_sort(s1,s2))
