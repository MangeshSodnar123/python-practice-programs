N = 10
K = 5
M = int(input("Input value : "))
if(M>N) or (M > 5) or (M == 0):
    print("INVALID INPUT")
    print("NUMBER OF CANDIES AVAILABLE :", N)
else:
    N = N - M
    print("NUMBER OF CANDIES SOLD :", M)
    print("NUMBER OF CANDIES AVAILABLE :", N)
