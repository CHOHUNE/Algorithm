def is_valid(s):
    stack =[]
    
    for each in s:
        if each in "({[":
            stack.append(each)
        elif each in ")}]":
            if not stack:
                return False
            last = stack.pop()
            
            if last == "(" and each != ")" or last == "[" and each != "]" or last == "{" and each != "}":
                return False
    return len(stack) == 0
        

def solution(s):
    ans = 0
    for i in range(len(s)):
        rotate_word = s[i:] + s[:i]
        
        if is_valid(rotate_word):
            ans += 1        
    
    return ans