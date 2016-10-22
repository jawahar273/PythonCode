"""
to find the smallest +ve number with following condition

e = len(input()) # as (b0)
1) lenght of may be upto 'n' without negative numbers.
2) if the lenght of string and number string(b1) is equal then print the time  or 
3) find the current length of b1 check it is equal.
4) try to continue with recursive function.
step 1:# 9999 -> 4 and 9999 != 4
step 2:# 4 -> 1 and 4 != 1
step 3:# 1 ->1 and 1==1 # break

"""
def rec(e, c=1):
    if int(e) == len(e):
        return c
    return rec(str(len(e)), c+1)

print( rec('9999') )# 3
print( rec('0') )#2

"""
step 1: len('0') = 1 and 0 != 1 
step 2: len('1') = 1 and  1 == 1
"""
print( rec('1') )#1

"""
step 1: len('1') = 1 and 1 != 1 # break return 1
"""
