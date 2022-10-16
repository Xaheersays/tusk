# https://www.geeksforgeeks.org/first-uppercase-letter-in-a-string-iterative-and-recursive/

s = "geeksforgeeKs"
def Solve(s,i ,n):
    if i == n:
        return 0
    elif 64 < ord(s[i])<91:
        return i
    return Solve(s,i+1,n)
print(Solve(s,0,len(s)))