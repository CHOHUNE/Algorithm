str = input()
ans =""
for each in str:
    if each.islower():
        ans+= each.upper()
    else:
        ans+= each.lower()

print(ans)