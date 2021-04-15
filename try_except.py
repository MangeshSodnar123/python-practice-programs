def divide42by(divideby):
    try:
        return 42/divideby
    except Exception as e:
        print(e)
print(divide42by(1))
print(divide42by(2))
print(divide42by(0)) #this line will throw the ZeroDividionError, so use try and except to tackle this thing.
print(divide42by(7))