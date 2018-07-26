# https://www.hackerrank.com/challenges/py-set-add/problem
s = set()
for i in range(int(input())):
    s.add(input())
print(len(s))
#
# # https://www.hackerrank.com/challenges/py-check-strict-superset/problem
s = set(input().split())
ans = True
for i in range(int(input())):
    t = set(input().split())
    if (s > t) == False:
        ans = False
        break
print(ans)



# https://www.hackerrank.com/challenges/py-check-subset/problem
for i in range(int(input())): #More than 4 lines will result in 0 score. Do not leave a blank line also. 
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print (A == B&A)
    
