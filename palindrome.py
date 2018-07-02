def check_palindrome(str):
    char_dict = {c:0 for c in str}
    for ch in s:
        char_dict[ch] += 1
    
    #Only one character can be odd
    odd_cnt = 0
    for i in char_dict:
        if char_dict[i] % 2 == 1:
            odd_cnt +=1
    if odd_cnt > 1:
        return False
    return True

s="aassddfgggf"
print(check_palindrome(s))
