num=4
i=1
pattern=""
sum=0

while(i<=num):
    pattern=pattern+str(num)
    print(pattern)
    sum=sum+int(pattern)
    i=i+1

print(sum)