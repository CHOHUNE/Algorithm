def solution():


    while True:

        single_line = input()

        ankle = []

        if single_line == '.':
            break

        ans = 'yes'

        for each in single_line:

            if each == '.':
                continue

            if each =='(' or each == '[':
                ankle.append(each)


            if each == ')':

                if not ankle:
                    ans = 'no'
                    break

                compare = ankle.pop()

                if compare != '(':
                    ans = 'no'
                    break

            if each == ']':

                if not ankle:
                    ans = 'no'
                    break

                compare = ankle.pop()

                if compare != '[':
                    ans = 'no'
                    break

        
        if len(ankle) >= 1:
            ans='no'
        print(ans)


solution()
