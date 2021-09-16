def sortArray(int_arr):
    # Super quick bubble sort implementation
    isSorted = False
    while not isSorted:
        isSorted = True # Changes to false if we have to swap; if we don't swap that's a clean pass and we can break
        for i in range(0, len(int_arr) - 1):
            if int_arr[i] > int_arr[i+1]: # Need to swap
                isSorted = False
                temp = int_arr[i]
                int_arr[i] = int_arr[i+1]
                int_arr[i+1] = temp
    return int_arr
