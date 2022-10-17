# https://www.geeksforgeeks.org/program-for-length-of-a-string-using-recursion/

s = "geeksforgeeKs"
def Solve(s):
    if s == "":
        print(s)
        return 0
    else:
        print(s)
        return 1+Solve(s[1:])

print(Solve(s))
