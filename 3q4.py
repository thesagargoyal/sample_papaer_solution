s = input()
s = s.upper()
for i in range(65, 91):
    if chr(i) in s:
        pass
    else:
        print('not a anagram')
        break
else:
    print('anagram')
