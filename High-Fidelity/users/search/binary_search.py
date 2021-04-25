
<<<<<<< HEAD


=======
>>>>>>> aebacdb4e6cfd820547281f4c0ca1171f74d2356
def binary_search(arr, element_Searched, low=0, high=0):
    """return the index of the element searched"""
    mid = 0

    for element in range(0, (len(arr) - 1 /2)):

        if high >= low:
<<<<<<< HEAD
    
            mid = (high + low) // 2
    
            # If element is present at the middle itself
            if arr[mid] == element_Searched:
                return mid
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > element_Searched:
                mid = mid - 1

            # Else the element can only be present in right subarray
            else:
                mid = mid + 1
    
=======

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == element_Searched:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left sub-array
            elif arr[mid] > element_Searched:
                mid = mid - 1

            # Else the element can only be present in right sub-array
            else:
                mid = mid + 1

>>>>>>> aebacdb4e6cfd820547281f4c0ca1171f74d2356
        else:
            # Element is not present in the array
            return -1
