# print pattern 1234 using for loop
# nested for loop

#   c1  c2 c3 c4 c5 c6
# r1 1  2  3  4  5  6
# r2 1  2  3  4  5  6
# r3 1  2  3  4  5  6

for row in range(1,4):
    for col in range(1,7):
        print(col,end=" ")

    print()