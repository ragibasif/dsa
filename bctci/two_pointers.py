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

def three_merge(arr1,arr2,arr3):
    # merge three sorted arrays, no duplicates
    seen = set()
    res = []
    prev = float("inf")
    for i in range(len(arr1)):
        if arr1[i] == prev or arr1[i] in seen:
            arr1[i] = float("inf")
        else:
            seen.add(arr1[i])
            prev = arr1[i]
    prev = float("inf")
    for i in range(len(arr2)):
        if arr2[i] == prev or arr2[i] in seen:
            arr2[i] = float("inf")
        else:
            seen.add(arr2[i])
            prev = arr2[i]
    prev = float("inf")
    for i in range(len(arr3)):
        if arr3[i] == prev or arr3[i] in seen:
            arr3[i] = float("inf")
        else:
            seen.add(arr3[i])
            prev = arr3[i]

    p1 = 0
    p2 = 0
    p3 = 0
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == float("inf"):
            p1+=1
        elif arr2[p2] == float("inf"):
            p2+=1
        elif arr3[p3] == float("inf"):
            p3+=1
        elif arr1[p1] < arr2[p2] and arr1[p1] < arr3[p3]:
            res.append(arr1[p1])
            p1+=1
        elif arr2[p2] < arr1[p1] and arr2[p2] < arr3[p3]:
            res.append(arr2[p2])
            p2+=1
        elif arr3[p3] < arr1[p1] and arr2[p2] > arr3[p3]:
            res.append(arr3[p3])
            p3+=1
    while p1 < len(arr1):
        if arr1[p1] < float("inf"):
            res.append(arr1[p1])
        p1+=1
    while p2 < len(arr2):
        if arr2[p2] < float("inf"):
            res.append(arr2[p2])
        p2+=1
    while p3 < len(arr3):
        if arr3[p3] < float("inf"):
            res.append(arr3[p3])
        p3+=1

    return res

def valley(arr):
    if arr[0] < arr[1]:
        return arr
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] > arr[r]:
            l+=1
            r-=1
        else:
            break
    print(arr,arr[l:],arr[:r+1])
print(valley([8,4,2,6]))
print(valley([1,2]))
print(valley([2,2,1,1]))
