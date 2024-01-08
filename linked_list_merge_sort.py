from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorted a linked list in ascending order 
   - Recursively divide the linked list into sublists containing a single node 
   - Repeatedly merge the sublists to produce sorted sublists until one remains 

   returns a sorted linked list 
    """

    if linked_list.size() == 1: 
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

    def split(list):
        """

        Divide the unsorted list at midpoint into sublists 
        """

        if linked_list == None or linked_list.head == None:
            left_half = linked_list
            right_half = None
            
            return left_half, right_half
        else:
            size = linked_list.size
            mid = size//2


            mid_node = linked_list.node_at_index(mid-1)

            left_half = linked_list
            right_half = LinkedList()
            right_half.head = mid_node.next_nodes
            mid_node.next_node = None


def merge (left,right):
    """
    Merge two linked lists, sorting by data in nodes 
    Returns a new merged list 
    """

    # create a new linked list that containsnodes from
    #merging left and right 
    merged = LinkedList()

    #add a fake head that is discarded later
    merge.add(0)

    #Set current to the head of the linked list 
    current = merge.head

    #obtain head nodes of left and right linked lists 
    left_head = left.head
    right_head = right.head

    #Iterating over left and right until we reach the tail node 
    while left_head or right_head:
        #if the head node of left is none, we're past the tail 
        # Add the node from right to merged linked list 

        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to false 
            right_head = right_head.next_node
         #if the head node of right is none, we're past the tail 
        #add the tail node from left to merged linked list 
        elif right_head is None:
            current.next_node = left_head
            #Call nect on left to set loop condition to false 
            left_head = left_head.next_node
        else:
            #Not at either tail node 
            #obtain node data to perform comparison operations

            left_data = left_head.data
            right_data = right_head.data 
            #if data on left is less than right, set current to left node 
            if left_data < right_data: 
                current.next_node= left_head
                #Move left head to next node
                left_head = left_head.next_node
                # if data on left is greater than right 
            else:
                current.next_node = right_head
                #move right head to next node 
                right_head = right_head.next_node

            #Move current to next node 
            current = current.next_node


        #Discard fake head and set first merged node as head 
        head = merged.head.next_node
        merged.head = head 

        return merged 
    
# l = LinkedList()
# l.add(10)
# l.add(24)
# l.dd(9)
# l.add(87)

