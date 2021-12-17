from timeit import default_timer as timer 

matrix = [[1,2],[3,4]]

def sum(input):
    the_sum = 0
    for i in input:
        the_sum += sum(i)
    return the_sum

def the_time():
    start = timer()
    res = sum(matrix)
    print("The sum of all the entries in the matrix is : ", res)
    elapsed_time = timer() - start
    print(elapsed_time)
the_time()