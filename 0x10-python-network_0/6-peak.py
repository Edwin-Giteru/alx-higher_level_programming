def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        
        # If the middle element is less than its right neighbor, move to the right half
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    # The left will eventually point to a peak element
    return list_of_integers[left]

