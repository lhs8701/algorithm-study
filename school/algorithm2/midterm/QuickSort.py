import random
import timeit

# Partition a[lo~hi] using a[lo] as the partitioning (pivot) item
def partition(a, lo, hi):
    i,j = lo+1,hi

    while True:
        while i<=hi and a[i]<a[lo]: i = i+1
        while j>=lo+1 and a[j]>a[lo]: j = j-1

        if (j <= i): break      # Break if the pointers cross
        a[i],a[j] = a[j],a[i]   # Swap a[i] and a[j]
        i,j = i+1,j-1

    a[lo],a[j] = a[j],a[lo]    # Swap a[j] with the partitioning item    
    return j    # Return the index of item in place    

# Partition a[lo~hi] and then continue to partition each half recursively
def divideNPartition(a, lo, hi):
    if (hi <= lo): return
    j = partition(a, lo, hi)    
    divideNPartition(a, lo, j-1)
    divideNPartition(a, j+1, hi)

def quickSort(a):
    # Randomly shuffle a, so that the partitioning item is chosen randomly
    random.shuffle(a)

    divideNPartition(a, 0, len(a)-1)
    return a

# Find k-th smallest element, where k = 0 ~ len(a)-1
def quickSelect(a, k):
    pass

if __name__ == "__main__":
    correct = True

    print("Correctness test with simple input")
    if quickSelect([4,8,0,10,2,3,2,6,11,3,12,7,1,13,5,9], 0) == 0: print("pass")
    else: 
        print("fail")
        correct = False
    print()

    print("Correctness test with random input")
    n = 100
    a = [i for i in range(n)]
    random.shuffle(a)
    for _ in range(4):
        k = random.randint(0,n-1)
        if quickSelect(a.copy(), k) == k: print("pass")
        else:
            print("fail")
            correct = False
    print()

    print("Speed test with random input")
    if correct:
        n = 100
        a = [i for i in range(n)]
        random.shuffle(a)        

        tQuickSort = timeit.timeit(lambda: quickSort(a.copy()), number=n)/n
        tQuickSelect = timeit.timeit(lambda: quickSelect(a.copy(), random.randint(0,n-1)), number=n)/n
        print(f"For {n} random elements,\n QuickSort takes {tQuickSort:.10f} sec and QuickSelect takes {tQuickSelect:.10f} sec on average")
        if tQuickSort > tQuickSelect*1.5: print("pass for timing")
        else: print("fail for timing")
    else:
        print("fail for timing (since the algorithm is not correct)")
    print()

    print("Speed test with input in descending order")
    if correct:
        n = 100
        a = [i for i in reversed(range(n))]               

        tQuickSort = timeit.timeit(lambda: quickSort(a.copy()), number=n)/n
        tQuickSelect = timeit.timeit(lambda: quickSelect(a.copy(), random.randint(0,n-1)), number=n)/n
        print(f"For {n} elements in reverse order,\n QuickSort takes {tQuickSort:.10f} sec and QuickSelect takes {tQuickSelect:.10f} sec on average")
        if tQuickSort > tQuickSelect*1.5: print("pass for timing")
        else: print("fail for timing")
    else:
        print("fail for timing (since the algorithm is not correct)")
    print()
    