from collections import Counter

def solution(s):
    count = Counter(s)
    ans = ""
    for char in count:
        if count[char] == 1:
            ans += char
            
    return ''.join(sorted(ans))
    