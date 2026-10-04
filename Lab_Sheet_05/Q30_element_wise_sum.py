# Find element-wise sum of two tuples

tuple1 = tuple(map(int, input("Enter first tuple numbers: ").split()))
tuple2 = tuple(map(int, input("Enter second tuple numbers: ").split()))

if len(tuple1) == len(tuple2):
    result = ()

    for i in range(len(tuple1)):
        result += (tuple1[i] + tuple2[i],)

    print("Element-wise sum:", result)
else:
    print("Both tuples must have the same length.")