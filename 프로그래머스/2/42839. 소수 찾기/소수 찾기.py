from itertools import permutations
import math
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    digits = list(numbers)
    nums = set()
    for i in range(1, len(digits) +1):
        for perm in permutations(digits,i):
            number= int(''.join(perm))
            nums.add(number)
            
    answer =0
    for num in nums:
        if is_prime(num):
            answer +=1

    return answer