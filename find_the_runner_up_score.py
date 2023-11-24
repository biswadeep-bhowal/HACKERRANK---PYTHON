n = int(input())
arr = map(int, input().split())     # Space Delimited Input for lists. Pass Delimiter to split() function, which takes ' ' by default.

max1, max2 = -101, -101

for a in arr:
    if a > max1:
        max2 = max1
        max1 = a
    elif max2 < a < max1:
        max2 = a

print(max2)


