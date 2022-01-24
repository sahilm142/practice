from collections import Counter
def isPalindrome(s):
    return s==s[::-1]
    
s = input()
cnt = Counter(s)
player = 'Second'
x = [i for i in cnt.items() if i[1]%2 == 1]

if isPalindrome(s) or len(x) <= 1:
    player = 'First'
else:
    if len(x)%2!=0:
        player = 'First'
    

print(player)
