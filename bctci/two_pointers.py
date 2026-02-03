# inward pointers 
def palindrome(s):
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

# fast and slow pointers
def smaller_prefixes(arr):
    n = len(arr) # assume its even and greater than 0
    sp = 0
    fp = 0
    k = 0
    k2 = 0
    for _ in range(n//2):
        k += arr[sp]
        k2 += arr[fp] + arr[fp+1]
        if not k < k2:
            return False
        sp += 1
        fp += 2
    return True

# parallel pointers
def common_elements(arr1,arr2):
    # assume they are sorted
    p1 = 0
    p2 = 0
    res = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]: 
            res.append(arr1[p1])
            p1+=1
            p2+=1
        elif arr1[p1] < arr2[p2]:
            p1+=1
        else:
            p2+=1
    return res

# inward pointers
def palindromic_sentence(s):
    # skip whitespace and non-alpha characters
    l = 0
    r = len(s) - 1
    while l <= r:
        if not s[l].isalpha():
            l+=1
        elif not s[r].isalpha():
            r-=1
        else: 
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
    return True


def reverse_case_match(s):
    # assume len is even
    def get_val(c):
        if c.islower():
            return ord(c) - ord('a')
        else:
            return ord(c) - ord('A')
    low = 0
    upp = len(s) - 1
    while low < len(s) and upp >= 0:
        if not s[low].islower():
            low+=1
        elif not s[upp].isupper():
            upp -= 1
        else:
            if not (get_val(s[low]) == get_val(s[upp])):
                return False
            low+=1
            upp-=1
    return True
