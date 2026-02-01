def is_lowercase(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

def is_uppercase(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def is_alpha(c):
    return is_lowercase(c) or is_uppercase(c)

def is_digit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def is_alphanumeric(c):
    return is_alpha(c) or is_digit(c)

def to_uppercase(c):
    if is_lowercase(c):
        return chr(ord('z') - ord(c) + ord('A'))
    return c

def to_lowercase(c):
    if is_uppercase(c):
        return chr(ord('Z') - ord(c) + ord('a'))
    return c

# time: O(len(s))
def split(s,d):
    if not s:
        return []
    res = []
    buf = []
    for c in s:
        if c == d:
            res.append("".join(buf))
            buf = []
        else:
            buf.append(c)
    res.append("".join(buf))
    buf = []
    return res

def join(arr,s):
    buf = []
    for i in range(len(arr)):
        if i != 0:
            buf.append(s)
        for c in arr[i]:
            buf.append(c)
    res = "".join(buf)
    return res


def index_of(s,t):
    res = -1
    s_len = len(s)
    t_len = len(t)
    for i in s_len-t_len:
        flag = True
        for j in t_len:
            if not s[i+j] == t[j]:
                flag = False
        if flag:
            return i
    return res
