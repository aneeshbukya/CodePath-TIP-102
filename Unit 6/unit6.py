# Volume Control
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Are the head and tail nodes of the linked list guaranteed to always exist, or do we need to handle cases where the list has fewer than 3 nodes?
# Are the values of the nodes guaranteed to be integers, or should we consider edge cases with different data types?
# P - Plan
# Write out in plain English what you want to do:
# I want to traverse the linked list while tracking three consecutive nodes at a time. I'll check if the current node is either a local minima (both the previous and next node values are larger) or a local maxima (both the previous and next node values are smaller). If it is, I'll increment a counter. The first and last nodes are not considered, so I'll start from the second node and stop at the second-to-last node.
# Translate each sub-problem into pseudocode:
# Initialize pointers: prev, current, and next_node.
# Traverse the list:
# For each current node, check if it is a local minima or maxima by comparing its value with prev and next_node.
# If a critical point is found (either minima or maxima), increment the counter.
# Move prev, current, and next_node forward to continue checking the rest of the list.
# When the list is fully traversed, return the counter.
# I - Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Function to count critical points
def count_critical_points(song_audio): 
    if not song_audio or not song_audio.next or not song_audio.next.next: # Check if there are less than 3 nodes 
        return 0  # There can't be any critical points if there are less than 3 nodes

    count = 0 # Initialize counter for critical points
    prev = song_audio # Initialize pointers 
    current = song_audio.next   # Initialize pointers
    next_node = current.next  

    while next_node: # Traverse the list
        if (current.value > prev.value and current.value > next_node.value) or \
           (current.value < prev.value and current.value < next_node.value): # Check for critical points
            count += 1 # Increment counter if critical point is found
        
        # Move the pointers forward
        prev = current    
        current = next_node 
        next_node = next_node.next

    return count
# Example usage:
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))  # Output: 3

# Magic Loop
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Function to find the start of the loop
def loop_start(path_start): 
    if not path_start:
        return None 

    slow = path_start
    fast = path_start

    # Step 1: Detect cycle using slow and fast pointers
    while fast and fast.next: # Traverse the list
        slow = slow.next # Move slow
        fast = fast.next.next # Move fast 

        if slow == fast: # Cycle detected
            # Step 2: Find the start of the cycle
            slow = path_start # Reset slow pointer to the start
            while slow != fast: # Traverse until slow and fast meet
                slow = slow.next # Move slow
                fast = fast.next # Move fast
 
            return slow.value   # Return the value of the start of the loop

    # No cycle found
    return None

# Example usage
path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1  # Cycle here

print(loop_start(path_start))  # Expected output: "Troll's Bridge"

# Grouping Experiments
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Can the list have only one experiment result, and if so, should it remain unchanged?
# If the linked list has an even number of nodes, how should the last even node be connected?
# P - Plan
# Write out in plain English what you want to do:
# We want to separate the nodes of the linked list into two groups: one for odd-positioned nodes and one for even-positioned nodes.
# We will traverse the list once, keeping track of the odd and even nodes as we go.
# After grouping, we’ll connect the last odd-positioned node to the first even-positioned node to merge the two lists, and the last even-positioned node will point to None.
# Translate each sub-problem into pseudocode:
# If the linked list is empty or has only one node, return it as is.
# Create two pointers, odd_head and even_head, to track the heads of the odd and even lists.
# Traverse the linked list:
# Add nodes at odd positions to the odd list.
# Add nodes at even positions to the even list.
# After traversal, connect the last node of the odd list to the head of the even list.
# Set the next pointer of the last even node to None.
# Return the modified list starting from odd_head.
# I - Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def odd_even_experiments(exp_results): # Function to group experiments
    if not exp_results or not exp_results.next: # Check if the list is empty or has only one node
        return exp_results  # Return the list as is
    
    odd = exp_results # Initialize pointers for odd and even lists
    even = exp_results.next # Initialize pointers for odd and even lists
    even_head = even  # Save the head of the even list
    
    while even and even.next: # Traverse the list
        odd.next = even.next  # Link current odd node to the next odd node
        odd = odd.next  # Move odd pointer to the next odd node
        even.next = odd.next  # Link current even node to the next even node
        even = even.next  # Move even pointer to the next even node
    
    odd.next = even_head  # Link the last odd node to the head of the even list
    
    return exp_results

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
# Example usage
experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print_linked_list(odd_even_experiments(experiment_results1))  # Output: 1 -> 3 -> 5 -> 2 -> 4
print_linked_list(odd_even_experiments(experiment_results2))  # Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4

# Next Contestant to Beat
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should happen if two nodes have the same score? Should we still look for the next node with a strictly higher score, or will the next node be considered the next greater score if it is equal?
# If the list contains only one node, should we return [0] since there is no next node to compare?
# P - Plan
# Write out in plain English what you want to do:
# We need to traverse the linked list and, for each node, find the next node that has a greater score than the current one.
# We can use a stack to store indices of nodes we have seen but haven’t found the next higher value for yet.
# As we traverse, whenever we find a score greater than the score at the top of the stack, we pop nodes from the stack and update the result array with the current score as the next higher value.
# If there is no greater node found for a given node, we store 0 in the result array.
# Translate each sub-problem into pseudocode:
# Initialize an empty list answer with all elements set to 0 (since if there's no greater node, we set the value to 0).
# Create a stack to store the indices of the nodes whose next greater node hasn't been found yet.
# Traverse the linked list while maintaining the index of each node:
# For each node, check if the current score is greater than the score at the index on top of the stack.
# If so, pop the index from the stack and update the answer list at that index with the current score.
# Return the answer list.
# I - Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def next_highest_scoring_contestant(contestant_scores):
    # Step 1: Convert linked list to an array
    values = [] # Store the values of the linked list in an array
    current = contestant_scores # Initialize current pointer
    while current: # Traverse the linked list
        values.append(current.value) # Add the value to the array
        current = current.next # Move to the next node

    # Step 2: Initialize result list and stack
    n = len(values) # Get the length of the array
    answer = [0] * n # Initialize the result list with zeros
    stack = [] # Initialize a stack to store indices

    # Step 3: Traverse through the list to find next greater values
    for i in range(n): # Traverse the array
        while stack and values[i] > values[stack[-1]]: # Check if the current value is greater than the value at the top of the stack
            idx = stack.pop() # Pop the index from the stack
            answer[idx] = values[i] # Update the result list with the current value
        stack.append(i) # Add the index to the stack

    return answer # Return the result list

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Example usage
contestant_scores1 = Node(2, Node(1, Node(5)))
contestant_scores2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print(next_highest_scoring_contestant(contestant_scores1))  # Output: [5, 5, 0]
print(next_highest_scoring_contestant(contestant_scores2))  # Output: [7, 3, 5, 6, 7, 7, 0]

# Adding Up the Evidence
# U - Understand
# Share 2 questions you would ask to help understand the question:
# How do we handle cases where the two linked lists are of different lengths? For example, if one number has more digits than the other, do we assume the missing digits are zeros?
# Is it possible for the sum to result in an additional carry-over at the end of the lists, i.e., an extra node representing a new digit?
# P - Plan
# Write out in plain English what you want to do:
# We need to traverse both linked lists simultaneously, adding the corresponding digits from each list. If the sum of two digits exceeds 9, we need to carry over the extra value (like regular addition).
# We’ll continue adding the digits from both lists until we reach the end of both, including any remaining carry from the last addition.
# If one list is longer than the other, treat the missing digits in the shorter list as 0.
# Translate each sub-problem into pseudocode:
# Initialize variables for tracking the current nodes in both lists and a variable carry to handle any value greater than 9 during addition.
# Initialize a new linked list result_head to store the result.
# Traverse through both linked lists:
# Add the values of the current nodes from both lists and the carry value.
# Store the ones place of the sum in the result linked list and update carry with the tens place (if any).
# Move to the next nodes in both linked lists.
# If there's still a carry after processing both lists, append a new node with that carry value.
# Return the head of the new linked list.
# I - Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Function to add two numbers represented as linked lists
def add_two_numbers(head_a, head_b):
    temp_head = Node(0)  # Temporary head node for the result list
    current = temp_head # Pointer to the current node in the result list
    carry = 0 # Initialize carry value

    while head_a or head_b or carry: # Traverse both lists and handle any remaining carry
        sum_value = carry # Initialize sum with the carry value
        if head_a:  # Add the value of the current node from list A
            sum_value += head_a.value   # Add the value of the current node from list A
            head_a = head_a.next # Move to the next node in list A
        if head_b: # Add the value of the current node from list B
            sum_value += head_b.value # Add the value of the current node from list B
            head_b = head_b.next # Move to the next node in list B

        carry = sum_value // 10 # Update carry with the tens place of the sum
        current.next = Node(sum_value % 10) # Store the ones place of the sum in the result list
        current = current.next # Move to the next node in the result

    return temp_head.next # Return the head of the result list
# Example usage
head_a = Node(2, Node(4, Node(3)))  # 342
head_b = Node(5, Node(6, Node(4)))  # 465

print_linked_list(add_two_numbers(head_a, head_b))  # Output: 7 -> 0 -> 8

# Merging Trail Segments
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Are the values between two markers (0s) guaranteed to always sum up to at least one node? In other words, will there always be nodes between the zeros, or should we handle cases where two 0s are adjacent?
# Do we assume the trail always starts and ends with 0, as in the examples, or can a trail segment appear at the beginning or end without a marker?
# P - Plan
# Write out in plain English what you want to do:
# We'll traverse the linked list and merge values between markers (represented by 0s). Whenever we hit a 0, we will sum all values until the next 0 is encountered, then replace those values with a single node containing the sum.
# The temporary markers (0s) should be removed from the final linked list.
# Once we’ve processed the entire list, return the head of the modified linked list.
# Translate each sub-problem into pseudocode:
# Initialize a new linked list for the result. Use a pointer current_result to track where we are in the new list.
# Traverse the input list (trailhead):
# When we encounter a node with value 0, skip over it and begin summing the values of subsequent nodes.
# Once another 0 is encountered, append a node to the result linked list containing the sum of the values.
# Continue traversing until the entire list has been processed.
# Return the new linked list without any 0s.
# I - Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Function to merge trail segments
def merge_trail(trailhead): # Function to merge trail segments
    if not trailhead: # Check if the list is empty
        return None
    
    new_head = Node(0)  # Temp node to simplify list creation
    tail = new_head  # Pointer to the last node in the new list
    current = trailhead.next  # Start after the first 0
    segment_sum = 0 # Initialize sum for the current segment
    
    while current: # Traverse the list
        if current.value == 0: # Check for marker
            if segment_sum > 0: # Check if there are values to sum
                tail.next = Node(segment_sum) # Add the sum to the new list
                tail = tail.next # Move the tail pointer
            segment_sum = 0 # Reset the sum for the next segment
        else:
            segment_sum += current.value # Add the value to the current segment sum
        current = current.next # Move to the next node
    
    return new_head.next # Return the new list without the markers
# Example usage
trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(4, Node(2, Node(0)))))))))
trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

print_linked_list(merge_trail(trail1))  # Output: 4 -> 11
print_linked_list(merge_trail(trail2))  # Output: 1 -> 3 -> 4

# Double Listening Count
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Is the linked list guaranteed to represent a valid non-negative integer (e.g., no negative signs)?
# Can the list contain very large integers, and should we account for the possibility of overflow when doubling the value?
# P - Plan
# Write out in plain English what you want to do:
# We need to double the integer represented by the linked list. To do this, we will traverse the list to extract the number, double it, and then reconstruct a new linked list representing the doubled value.
# The input list stores digits of a number in normal order (i.e., the most significant digit comes first), and the same format should be preserved in the output.
# Translate each sub-problem into pseudocode:
# Extract the integer: Traverse the linked list and build the integer represented by the nodes.
# Double the integer: Multiply the extracted integer by 2.
# Rebuild the linked list: Convert the doubled integer into a new linked list where each node holds one digit of the result.
# Return the head of the new linked list.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def double_listeners(monthly_listeners):
    # Step 1: Convert linked list to integer
    current = monthly_listeners
    num = 0
    while current:
        num = num * 10 + current.value
        current = current.next
    
    # Step 2: Double the integer
    doubled_num = num * 2
    
    # Step 3: Convert the doubled integer back into a linked list
    # Convert the doubled number into a string, then build the new linked list
    head = None
    for digit in str(doubled_num):
        if not head:
            head = Node(int(digit))
            current = head
        else:
            current.next = Node(int(digit))
            current = current.next
    
    return head

# Example usage
monthly_listeners1 = Node(1, Node(8, Node(9)))  # 189
monthly_listeners2 = Node(9, Node(9, Node(9)))  # 999

print_linked_list(double_listeners(monthly_listeners1))  # Expected output: 3 -> 7 -> 8
print_linked_list(double_listeners(monthly_listeners2))  # Expected output: 1 -> 9 -> 9 -> 8

# Book Similarity
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Can two books be considered similar if they are separated by a book that is not in the subset?
# Is the order of the subset array significant, or do we only care about the consecutive nature of the books in the linked list?
# P - Plan
# Write out in plain English what you want to do:
# We need to count the number of "similar book components" in the subset. A component is a group of books in the subset that appear consecutively in the linked list.
# Traverse the linked list and check each book. If the current book is in the subset and the next book is also in the subset, they form a similar component. If a book is in the subset and the next book is not, this marks the end of the current component.
# Translate each sub-problem into pseudocode:
# Traverse the linked list: Start at the head and iterate through the list.
# Track components: If a book from the subset appears and either it's the end of the list or the next book is not part of the subset, this marks the end of a similar component.
# Count components: Keep a running count of how many such components we encounter.
# Return the total: At the end of the traversal, return the total number of similar components.
# I - Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def similar_book_count(all_books, subset):
    subset_set = set(subset) # Convert the subset list to a set for faster lookup
    current = all_books  # Start at the head of the linked list
    similar_count = 0 # Initialize counter for similar components
    in_component = False # Flag to track if we are in a similar component
    
    while current: # Traverse the linked list
        if current.value in subset_set: # Check if the current book is in the subset
            if not in_component: # Check if we are starting a new component
                similar_count += 1 # Increment the counter if starting a new component
                in_component = True # Update the flag to indicate we are in a component
        else:
            in_component = False # Update the flag if the current book is not in the subset
        
        current = current.next # Move to the next book
     
    return similar_count
# Example usage
all_books1 = Node(0, Node(1, Node(2, Node(3))))
subset1 = [0, 1, 3]

all_books2 = Node(0, Node(1, Node(2, Node(3, Node(4)))))
subset2 = [0, 3, 1, 4]

print(similar_book_count(all_books1, subset1))  # Expected output: 2
print(similar_book_count(all_books2, subset2))  # Expected output: 2