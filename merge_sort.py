def merge_sort(list):
    """
    Sort a list in ascending order 
    Returns a new sorted list

    Divide: find the mindpoint of the list and divide into sublists 
    Conquer: recursively sort the sublists created in previous step 
    Combine: merge the sorted sublist created in previous step 
    """

    if len(list) <= 1:
        return list
    

    left_half, right_half= split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)


def split(list):
    """
    Divide the unsorted list at mindpoint into sublists 
    Return two sublists - left and right 
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left,right

def merge(left,right):
    """
    Merge two arrays and sorting them in the process 
    Returns a new merged list
    """

    l = []
    i = 0 
    j = 0 


    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else: 
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i+=1 

    while j < len(right):
        l.append(right[j])
        j+=1 

    return l

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[0] and verify_sorted(list[1:])

alist = [54,20,17,8,9,10,23,15,34]

l = merge_sort(alist)
print(l)
print("testt")

