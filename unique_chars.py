def unique_chars_wo_ds(s):
    #sorted return a list. Thus use join to convert it back to string
    s =''.join(sorted(s))
    n=len(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
            return False
    return True

def unique_chars_w_ds(s):
    n=len(s)

    #Direct check if all letters are unique then they cannot extend the list of 256 ASCII chars
    if n > 256:
        False
    d = dict.fromkeys([i for i in range(256)],0)
    for c in s:
        d[ord(c)] += 1
        print(d[ord(c)])
    for j in d.values():
                      if j > 1:
                        return False
    return True
       
#Driver code
s="asdfgha"
print(unique_chars_wo_ds(s))
print(unique_chars_w_ds(s))
    
