def heaps_algorithm(arr):
    n = len(arr)
    c = [0] * n

    yield tuple(arr)

    i = 1
    while i < n:
        if c[i] < i:
            if i & 1 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            
            yield tuple(arr)
            
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1


'''
Example use case:

if __name__ == "__main__":
    my_array = ['A', 'B', 'C', 'D', 'E', 'F']
    for perm in heaps_algorithm(my_array):
        print(perm)
'''