import statistics
import timeit
import random
from multiprocessing import Pool, Process


def sort_list(n):
    new_list = []
    for i in range(n):
        new_list.append(random.random())
    sorted_list = sorted(new_list)
    return sorted_list


# function from https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def file_write(n):
    for i in range(n):
        # print('i', i)
        with open(f'file-{i}.txt', 'w') as f:
            f.write('Here we go testing M1 Macs')
            f.writelines(['Here we go testing the M1 Macs'] * n)
            # for j in range(n):
            #     print('\tj', j)
            #     f.write(str(random.random()) + '\n')


def file_read(n):
    for i in range(n):
        with open(f'file-{i}.txt', 'r') as f:
            lines = f.readlines()


def test_multithreading(p, n):
    # for i in range(p):
    #     proc = Process(target=fibonacci, args=(p,))
    #     proc.start()
    # proc.join()
    with Pool(p) as p:
        p.map(fibonacci, [x for x in range(1, n)])


if __name__ == '__main__':

    result = timeit.timeit(stmt='sort_list(10)', setup='from __main__ import sort_list; import random;')
    print('Sorted list - mean:', result)

    result = timeit.timeit(stmt='for i in range(1, 10): fibonacci(i)', setup='from __main__ import fibonacci')
    print('Fibonacci - mean:', result)

    result = timeit.timeit(stmt='file_write(100)', setup='from __main__ import file_write; import random;', number=100)
    print('File write - mean:', result)

    result = timeit.timeit(stmt='file_read(100)', setup='from __main__ import file_read', number=100)
    print('File read - mean:', result)

    result = timeit.timeit(stmt='test_multithreading(4, 10)',
                           setup='from multiprocessing import Pool; from __main__ import fibonacci, test_multithreading', number=200)
    print('Multithreading w/ 4 threads - mean:', result)

    result = timeit.timeit(stmt='test_multithreading(8, 10)',
                           setup='from multiprocessing import Pool; from __main__ import fibonacci, test_multithreading;', number=200)
    print('Multithreading w/ 8 threads - mean:', result)
