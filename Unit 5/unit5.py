# Print Players Linked List
### 1. U-nderstand
# HAPPY CASE:
# Input: A linked list with nodes isabelle -> saharah -> cj
# Output: "Isabelle -> Saharah -> C.J."
# Explanation: The node values are concatenated with the separator "->".
# EDGE CASE:
# Input: An empty linked list (None).
# Output: ""
# Explanation: Since there are no nodes, the result is an empty string.
# Key Questions:
# How should the function handle an empty linked list?
# Return an empty string.
# Is there any specific constraint on the list length or values?
# There are no explicit time/space constraints mentioned, but the function should handle traversal efficiently.
# 2. M-atch
# Problem Type: Linked List
# Pattern/Strategy:
# Traversing the List: We'll iterate through each node until the end is reached.
# Collecting Values: We'll store each node’s value in a list.
# String Manipulation: We'll concatenate these values using the "->" separator.
#### 3. P-lan
# Steps:
# Initialize an empty list to hold the values of each node.
# Set the current node to the head of the linked list.
# Loop through the nodes while the current node is not None:
# Add the value of the current node to the list.
# Move to the next node.
# Join the values with the separator "->".
# Return the resulting string.
#### 4. I-mplement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(head):
    values = []  # List to store node values
    current = head  # Start at the head of the linked list
    while current:  # Traverse the list
        values.append(str(current.value))  # Append each node's value to the list
        current = current.next  # Move to the next node
    return " -> ".join(values)  # Join the values with '->' separator

# Example Usage:
isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))  # Output: "Isabelle -> Saharah -> C.J."

#  Chase String
### U - Understand
# Share 2 questions you would ask to help understand the question:
# How should the function behave if the linked list is empty? Should it return an empty string?
# Should there be an extra separator ("chases") at the end of the string, or should it stop after the last node?
# P - Plan
# Write out in plain English what you want to do:
# Traverse the linked list, starting from the head, and collect the values of each node. Concatenate these values with the word "chases" as a separator and return the resulting string. If the list is empty, return an empty string.
# Translate each sub-problem into pseudocode:
# Initialize an empty list to store the values of the nodes.
# Set the current node to the head of the linked list.
# While the current node is not None:
# Append the value of the current node to the list.
# Move to the next node.
# Join the node values with the string " chases " and return the result.
# If the head is None, return an empty string.
# I - Implement
# Node class for the linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# chase_list function to concatenate node values with 'chases' separator
def chase_list(head):
    values = []  # List to hold node values
    current = head  # Start at the head of the linked list
    
    # Traverse the linked list
    while current:
        values.append(str(current.value))  # Append current node's value
        current = current.next  # Move to the next node
    
    # Join values with ' chases ' as separator
    return " chases ".join(values)

# Example Usage:
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))  # Output: "Spike chases Tom chases Jerry chases Gouda"

# Edge Case: Empty list
print(chase_list(None))  # Output: ""

# Restocking the Lake
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should happen if the linked list is empty? Should we create a new head node with new_fish?
# Should the new node always be added to the end, even if the list already contains several fish?
# Test Cases
# HAPPY CASE:
# Input: A linked list with fish names Carp -> Dace -> Cherry Salmon, and new_fish = "Rainbow Trout".
# Output: Carp -> Dace -> Cherry Salmon -> Rainbow Trout.
# EDGE CASE:
# Input: An empty linked list (head = None), and new_fish = "Goldfish".
# Output: Goldfish (the new fish becomes the head of the list).
# P - Plan
# Write out in plain English what you want to do:
# If the head is None (empty list), create a new node with new_fish as the head and return it.
# Otherwise, traverse the list to find the last node (where next is None).
# Create a new node for new_fish and append it to the end of the list by setting the next pointer of the last node to the new node.
# Return the head of the modified list.
# Translate each sub-problem into pseudocode:
# If the head is None:
# Return a new node with fish_name as new_fish.
# Otherwise:
# Set current to head.
# Traverse the list while current.next is not None.
# Once at the last node, set current.next to a new node with fish_name as new_fish.
# Return the head of the modified list.
# Node class for the linked list
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# restock function to add a new fish at the end of the list
def restock(head, new_fish):
    # If the list is empty, create a new node and return it
    if head is None:
        return Node(new_fish)
    
    # Otherwise, traverse to the end of the list
    current = head
    while current.next is not None:
        current = current.next
    
    # Append the new fish to the end of the list
    current.next = Node(new_fish)
    
    # Return the modified list (head)
    return head

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

# Example Usage:
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))

# Edge Case: Empty list
empty_list = None
print_linked_list(restock(empty_list, "Goldfish"))

# Update Rankings
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should happen if the target is out of bounds? Should we return the original list without any modification?
# Should the swap be performed only if target - 1 exists, and what should be done if the list contains fewer than target nodes?
# Test Cases
# HAPPY CASE:
# Input: A linked list with players Mario -> Peach -> Luigi -> Daisy, and target = 3.
# Output: Mario -> Luigi -> Peach -> Daisy.
# EDGE CASES:
# Input: A list with players Mario -> Luigi, and target = 1.
# Output: Mario -> Luigi (no change as the first player can't be moved up).
# Input: head = None, and target = 1.
# Output: None (empty list, no operation).
# P - Plan
# Write out in plain English what you want to do:
# If the list is empty, return None.
# If target == 1, return the head as no swap is possible.
# Traverse the list to the node at target - 1 (the node before the target).
# Swap the target node with the target - 1 node.
# Return the head of the modified list.
# Translate each sub-problem into pseudocode:
# If head == None:
# Return None.
# If target == 1:
# Return the original head.
# Otherwise:
# Traverse to the node at position target - 1.
# Perform a swap by changing pointers so the target node moves one place up.
# Return the updated head of the list.
class Node:
  def __init__(self, player, next=None):
      self.player = player
      self.next = next

# For testing
def print_linked_list(head):
  current = head # Start at the head of the linked list
  while current: # Traverse the list until the end
      print(current.player, end=" -> " if current.next else "\n") # Print the player's name with separator
      current = current.next # Move to the next node

def increment_rank(head, target): # Function to swap the target node with the previous node
  if target <= 1 or head is None or head.next is None: # If the list is empty or target is 1, return the original list
      return head

  index = 1 # Initialize index to track the current node position
  prev = None # Initialize a pointer to the node before the target
  current = head  # Start at the head of the linked list

  # Traverse the list to the target index
  while index < target:  # Loop until the target index is reached
      prev = current # Update the previous node
      current = current.next # Move to the next node
      index += 1 # Increment the index

  # Swap the values between the node at target-1 and the node at target
  temp = prev.player # Store the value of the previous node
  prev.player = current.player # Update the previous node's value with the target node's value
  current.player = temp # Update the target node's value with the stored value

  return head  # Return the head of the modified list
# Example Usage:
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))  # Output: Mario -> Luigi -> Peach -> Daisy
print_linked_list(increment_rank(racers2, 1))  # Output: Mario -> Luigi (unchanged)
print_linked_list(increment_rank(None, 1))     # Output: None


# Print Backwards
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Should I print the values separated by spaces without a newline at the end?
# What should the function do if the list is empty (i.e., if the tail is None)?
# Test Cases
# HAPPY CASE:
# Input: A doubly linked list with nodes Isabelle <-> K.K. Slider <-> Saharah, and the tail being Saharah.
# Output: "Saharah K.K. Slider Isabelle".
# EDGE CASE:
# Input: The tail = None (an empty list).
# Output: No output or just an empty line.
# P - Plan
# Write out in plain English what you want to do:
# Starting from the tail of the list, traverse backward (using the prev pointer) and collect the values of each node.
# Print the values in reverse order, separated by spaces.
# Translate each sub-problem into pseudocode:
# If the tail is None, return without doing anything.
# Otherwise, initialize a current pointer starting at the tail.
# While current is not None:
# Print the value of the current node.
# Move the current pointer to the previous node.
# Print the values separated by a space.
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail): # Function to print the linked list in reverse order
    current = tail # Start at the tail of the linked list
    while current: # Traverse the list until the beginning is reached
        if current.prev: # Check if there is a previous node
            print(current.value, end=" ") # Print the value with a space separator
        else: # If the current node is the head
            print(current.value) # Print the value without a space
        current = current.prev # Move to the previous node
# Example Usage:
isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")

# Setting up the doubly linked list
isabelle.next = kk_slider
kk_slider.next = saharah
kk_slider.prev = isabelle
saharah.prev = kk_slider

# Linked List: Isabelle <-> K.K. Slider <-> Saharah
print_reverse(saharah)  # Output: Saharah K.K. Slider Isabelle

# Find Length of Doubly Linked List from Any Node
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Should I include the node passed to the function as part of the total count of the list's length?
# What should happen if the node is part of an isolated list segment (i.e., it is not fully connected to a head or tail)?
# Test Cases
# HAPPY CASE:
# Input: A doubly linked list with nodes Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain, and the node Rainbow Road as input.
# Output: 4.
# EDGE CASE:
# Input: A single node that doesn't connect to other nodes.
# Output: 1.
# P - Plan
# Write out in plain English what you want to do:
# Start at the given node, and traverse forward and backward to count the number of nodes in both directions.
# Combine the counts from the forward and backward traversals and return the total length.
# Translate each sub-problem into pseudocode:
# Initialize the length as 1 to account for the given node.
# Set the current pointer to the input node.
# Traverse forward using the next pointer and increment the count.
# Traverse backward using the prev pointer and increment the count.
# Return the total count.
def get_length(node):
    if node is None:
        return 0

    # Find the start of the list
    start = node # Initialize start as the given node
    while start.prev: # Traverse to the beginning of the list
        start = start.prev # Move to the previous node

    # Traverse from start to end, counting nodes
    length = 0 # Initialize the length counter
    current = start    # Start at the beginning of the list
    while current: # Traverse the list until the end
        length += 1 # Increment the length counter
        current = current.next # Move to the next node

    return length # Return the total length of the list

yoshi_falls = Node("Yoshi Falls")
moo_moo_farm = Node("Moo Moo Farm")
rainbow_road = Node("Rainbow Road")
dk_mountain = Node("DK Mountain")
yoshi_falls.next = moo_moo_farm
moo_moo_farm.next = rainbow_road
rainbow_road.next = dk_mountain
dk_mountain.prev = rainbow_road
rainbow_road.prev = moo_moo_farm
moo_moo_farm.prev = yoshi_falls

# List: Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain
print(get_length(rainbow_road))  # Expected Output: 4

# Careful Reverse
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Should I maintain the original order of the nodes after the first k elements are reversed?
# If the value of k is equal to or larger than the length of the list, should the entire list be reversed?
# Test Cases
# HAPPY CASE:
# Input: A list apple -> cherry -> orange -> peach -> pear and k = 3.
# Output: orange -> cherry -> apple -> peach -> pear.
# EDGE CASE (k larger than list length):
# Input: A list apple -> cherry -> orange -> peach -> pear and k = 7 (where k is larger than the list length).
# Output: pear -> peach -> orange -> cherry -> apple.
# P - Plan
# Write out in plain English what you want to do:
# Traverse through the linked list and reverse the first k elements.
# If k is larger than the length of the list, reverse the entire list.
# Once the reversal is done for the first k elements, reattach the remaining part of the list.
# Translate each sub-problem into pseudocode:
# Initialize a counter to track how many elements have been reversed.
# Use three pointers: prev, current, and next_node to reverse the nodes.
# Continue reversing nodes until the counter reaches k or the end of the list.
# After the first k elements have been reversed, reattach the reversed segment to the remaining part of the list.
# Return the new head of the list.
def reverse_first_k(head, k): # Function to reverse the first k nodes of a linked list
    if not head or k <= 1: # If the list is empty or k is less than or equal to 1, return the original list
        return head # Return the original list
    
    current = head # Start at the head of the linked list
    prev = None # Initialize a pointer to the previous node
    next_node = None # Initialize a pointer to the next node
    count = 0 # Counter to track the number of nodes
    
    # Reverse the first k nodes
    while current and count < k: # Loop until k nodes are reversed or the end of the list is reached
        next_node = current.next # Store the next node for traversal
        current.next = prev # Reverse the pointer to the previous node
        prev = current # Move the prev pointer to the current node
        current = next_node # Move the current pointer to the next node
        count += 1 # Increment the counter
     
    # Connect the reversed part with the rest of the list
    if head: # If the list is not empty
        head.next = current # Connect the head to the remaining part of the list
    
    return prev  # New head of the list is the last node of the reversed part
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Example Usage:
head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))  # Output: orange -> cherry -> apple -> peach -> pear

# Symmetrical Linked List
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Should the function return True for an empty list or a single-node list, since both could be considered symmetrical?
# Can I assume the values of the linked list nodes are always comparable, such as strings or integers?
# Test Cases
# HAPPY CASE:
# Input: A list Bitterling -> Crawfish -> Bitterling
# Output: True (the list reads the same forwards and backwards).
# EDGE CASE (different values):
# Input: A list Bitterling -> Carp -> Koi
# Output: False (the list does not read the same forwards and backwards).
# EDGE CASE (single element):
# Input: A list Bitterling
# Output: True (a single-element list is considered symmetrical).
# P - Plan
# Write out in plain English what you want to do:
# Traverse through the list and store the values of the nodes.
# Use the two-pointer technique to compare the values stored in the list from the front and back.
# If all the values are equal when checked from both ends, return True. Otherwise, return False.
# Translate each sub-problem into pseudocode:
# Initialize an empty list values to store the values of the linked list.
# Traverse the linked list from head to end, appending each node's value to values.
# Initialize two pointers: one starting at the beginning (left = 0) and one at the end (right = len(values) - 1).
# Compare the values at the two pointers:
# If they are equal, move both pointers towards the center.
# If they are not equal, return False.
# If all values match, return True.
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def is_symmetric(head):
    if head is None or head.next is None: # Check for empty list or single node 
        return True  # A list with 0 or 1 element is symmetric

    # Find the middle of the list
    slow = fast = head # Initialize slow and fast pointers
    while fast and fast.next: # Move slow by 1 and fast by 2
        slow = slow.next  # Slow pointer moves by 1
        fast = fast.next.next # Fast pointer moves by 2
    
    # Reverse the second half of the list
    prev = None # Initialize prev pointer for reversing
    while slow: # Reverse the second half of the list
        next_node = slow.next # Store the next node
        slow.next = prev # Reverse the pointer
        prev = slow # Move prev to the current node
        slow = next_node # Move slow to the next node
    
    # Compare the first half and  the reversed second half
    left, right = head, prev # Initialize pointers for comparison
    while right:  # Only need to compare till the end of the second half
        if left.value != right.value: # If values don't match, return False
            return False
        left = left.next # Move left pointer forward
        right = right.next # Move right pointer backward
    
    return True

# Example Usage:
head1 = Node("Bitterling", Node("Crawfish", Node("Bitterling")))
head2 = Node("Bitterling", Node("Carp", Node("Koi")))

print(is_symmetric(head1))  # Output: True
print(is_symmetric(head2))  # Output: False