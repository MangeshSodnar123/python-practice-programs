# interval1 = [2,3,4,5,6,7,8,9]

# flag = 1
# def primeNum(interval):
#     for i in interval:
#         if i == 0 or i == 1:
#             continue
#         flag = 1
#         for j in range(1,((interval[-1]//2)+1),1):
#             if i % j == 0:
#                 flag = 0
#                 break 

#         if flag == 1:
#             print(i)

# primeNum(interval1)

# this program is not working, I'll work on it later.

start = 23
end = 77
for i in range(start, end+1):
    if i >1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)


