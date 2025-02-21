def my_function(x):
    if x == 0:
        return 0
    else:
        return my_function(x - 1) + x

# This will cause a RecursionError for large values of x
print(my_function(1000))