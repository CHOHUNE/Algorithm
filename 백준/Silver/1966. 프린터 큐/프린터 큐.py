from collections import deque

def solition():


    TestCaseNum = int(input())

    for _ in range(TestCaseNum):

        num_range, num_idx  = map(int,input().split())
        lis = list(map(int,input().split()))

        deque_lis = deque()
        for idx,each in enumerate(lis):

            deque_lis.append((idx,each))

        cnt = 0


        while deque_lis :

            cur_idx,cur_value = deque_lis[0] 
            #앞에만 확인해도 되는 게 어차피 append, popleft 함

            max_value =max(deque_lis,key = lambda x :x[1])
            #value 기준으로 max value 찾음

            if cur_value != max_value[1]:
                # 더 큰 값이 있다면 popleft 후 append
                change = deque_lis.popleft()
                deque_lis.append(change)
                

            elif cur_value == max_value[1]:

                cnt += 1
                deque_lis.popleft()

                if cur_idx == num_idx:
                    print(cnt)
                    break

solition()

