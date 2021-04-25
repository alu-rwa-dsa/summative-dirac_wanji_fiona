
def binary_search(arr, element_Searched, low=0, high=0):
    """return the index of the element searched"""
    mid = 0

    for element in range(0, (len(arr) - 1 /2)):

        if high >= low:

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

        else:
            # Element is not present in the array
            return -1
