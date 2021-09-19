arr = [ 1, 3, 46, 5, 6]
max = arr[0]

length = len(arr)
for i in range(1, length):
    if(arr[i]>max):
        max = arr[i]

print(max)
