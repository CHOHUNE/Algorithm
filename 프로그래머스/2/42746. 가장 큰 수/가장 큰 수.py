def solution(numbers):
    from functools import cmp_to_key
    
    def compare(x, y):
        if str(x) + str(y) > str(y) + str(x):
            return -1
        else : 
            return 1
    numbers.sort(key=cmp_to_key(compare))
    result = ''.join(map(str,numbers))
    return str(int(result)) # 000 을 0으로 다시 처리하는 부분