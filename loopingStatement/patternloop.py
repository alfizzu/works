# 1
# 1 2
# 1 2 3
# 1 2 3 4

# \t is tab space
# col here should only work upto row+1 times

for row in range(1,5):
    for col in range(1,row+1):
        print(col,end="\t")
    print()