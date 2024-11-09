from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
    
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
# Question 1 : Icing Cupcakes in Zigzag Order
# U - Understand
# Questions to clarify the problem:
# Should we assume the tree is always complete, or could it have missing nodes at some levels?
# How should we handle the zigzag order on each level—should we use specific data structures to simplify alternating directions?
# P - Plan
# Plan in plain English:
# Use a level-by-level traversal, similar to breadth-first search (BFS).
# Track the direction for each level, toggling between left-to-right and right-to-left.
# Store each level’s nodes in a temporary list and, depending on the direction, append the list to the final output list either in normal or reversed order.
# Pseudocode:
# Initialize result list and current_level deque with the root node.
# Set left_to_right to True to start icing from left to right.
# While current_level is not empty:
# Initialize an empty level_result list.
# Iterate over nodes in current_level.
# If left_to_right is True, append children to the right side of next_level.
# Otherwise, append children to the left side.
# Add level_result to result.
# Toggle left_to_right.
# Return result.
# I - Implement
def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
    
    result = []
    queue = deque([cupcakes])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.extend(level)
        left_to_right = not left_to_right
    
    return result
# flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
# cupcakes = build_tree(flavors)
# print_tree(zigzag_icing_order(cupcakes)) 

# Question 2 : Counting Cupcakes in Each Row
# U - Understand
# Questions to clarify the problem:
# Can the value of k be larger than the total number of nodes in the tree, or should we assume that 
# k is always within bounds?
# Is the BST guaranteed to contain unique keys, or could there be duplicate keys?
# P - Plan
# Plan in plain English:
# Since the tree is a binary search tree (BST), an in-order traversal will yield the nodes in ascending order by their spookiness level (key).
# Perform an in-order traversal of the tree to collect the rooms in ascending order of spookiness.
# Return the room's value at the k-1 index in the sorted list (as k is 1-indexed).
# Pseudocode:
# Initialize an empty list rooms.
# Define an in-order traversal function that:
# Adds each node’s value to rooms.
# Stops the traversal early if the length of rooms reaches 
# Call the traversal function on the root node.
# Return the room value at index k−1 in the rooms list.
# I - Implement
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

# def kth_spookiest(root, k):
#     def inorder(node):
#         if not node:
#             return None
        
#         # Traverse the left subtree
#         left = inorder(node.left)
#         if left is not None:
#             return left
        
#         # Increment the count when visiting the node
#         nonlocal count
#         count += 1
#         if count == k:
#             return node.val
        
#         # Traverse the right subtree
#         return inorder(node.right)
    
#     count = 0
#     return inorder(root)
def kth_spookiest(root, k):
    rooms = []
    
    def in_order(node):
        if not node or len(rooms) >= k:
            return
        in_order(node.left)
        if len(rooms) < k:
            rooms.append(node.val)
        in_order(node.right)

    in_order(root)
    return rooms[k - 1] if k <= len(rooms) else None  # Return None if k is out of bounds

# Test cases

rooms1 = [(3, "Lobby"), (1, 101), (4, 102), None, (2, 201)]
hotel1 = build_tree(rooms1)
print(kth_spookiest(hotel1, 1))  # Expected Output: 101

rooms2 = [(5, 'Lobby'), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]
hotel2 = build_tree(rooms2)
print(kth_spookiest(hotel2, 3))  # Expected Output: 201

# Question 3 : Maximum Icing Difference
# U - Understand
# Questions to clarify the problem:
# Is there a limit to the range of values for sweetness levels, or could they be negative as well?
# Should we consider only direct children for the ancestor relationship, or do all descendants qualify?
# P - Plan
# Plan in plain English:
# Traverse the tree, keeping track of the minimum and maximum sweetness levels encountered along the path from the root to each node.
# For each node, calculate the difference between the node’s sweetness level and both the minimum and maximum values recorded along its path.
# Update the maximum icing difference if the calculated difference is larger than the current maximum.
# Perform this calculation recursively for each node, updating the minimum and maximum values as we descend.
# Pseudocode:
# Define a helper function traverse(node, min_sweetness, max_sweetness).
# Base case: If node is None, return.
# Calculate current_diff as the maximum of:
# The absolute difference between node.val and min_sweetness
# The absolute difference between node.val and max_sweetness
# Update max_diff if current_diff is greater.
# Update min_sweetness and max_sweetness for the current path.
# Recursively call traverse() on the left and right children of node.
# Finally, return the maximum icing difference found.
# I - Implement
class TreeNode:
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def max_icing_difference(root):
    max_diff = 0  # Variable to keep track of the maximum difference

    def traverse(node, min_sweetness, max_sweetness):
        nonlocal max_diff
        if not node:
            return

        # Calculate the icing difference with current node's value
        current_diff = max(abs(node.val - min_sweetness), abs(node.val - max_sweetness))
        max_diff = max(max_diff, current_diff)

        # Update the min and max sweetness values for the path
        new_min_sweetness = min(min_sweetness, node.val)
        new_max_sweetness = max(max_sweetness, node.val)

        # Recursive traversal for left and right children
        traverse(node.left, new_min_sweetness, new_max_sweetness)
        traverse(node.right, new_min_sweetness, new_max_sweetness)

    # Start traversal with root node values as initial min and max
    traverse(root, root.val, root.val)
    return max_diff
# Test case
sweetness_levels = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
display = build_tree(sweetness_levels)
print(max_icing_difference(display))  # Expected Output: 13

# # Question 4 : Topsy Turvy
# U - Understand
# Questions to clarify the problem:
# Are we guaranteed that each node with a left child also has a right child, or could there be some nodes with only one child?
# Should we handle any cases where there might be more than two children at any node, or is it strictly a binary tree?
# P - Plan
# Plan in plain English:
# Use a recursive approach to flip the tree level by level.
# Start from the leftmost child, which will become the new root after the flip.
# Move up the tree, setting each node’s left child as the new root, rotating the original root to become the right child and the original right child to become the left child.
# Repeat this process until the entire tree has been flipped.
# Pseudocode:
# Define a helper function flip(node) that recursively processes the leftmost child.
# Base case: If node or node.left is None, return node (this will be the new root).
# Recursively call flip(node.left) to reach the leftmost node, which becomes the new root.
# Reassign pointers:
# The left child’s left pointer should point to the original right child.
# The left child’s right pointer should point to the original node.
# Set node.left and node.right to None to remove the original connections.
# Return the new root.
# I - Implement
class TreeNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def flip_hotel(hotel):
    if not hotel or not hotel.left:
        return hotel
    
    # Recursively flip the left subtree
    new_root = flip_hotel(hotel.left)
    
    # Perform the reassignments
    hotel.left.left = hotel.right  # The original right child becomes the new left child
    hotel.left.right = hotel       # The original root becomes the new right child
    
    # Set the current root's left and right children to None
    hotel.left = None
    hotel.right = None
    
    return new_root
# Using build_tree() function included at top of page
rooms = [1, 2, 3, 4, 5]
hotel = build_tree(rooms)

# Using print_tree() function included at top of page
print_tree(flip_hotel(hotel))

# Question 5
# U - Understand
# A binary tree (order_tree) with each node representing an order.
# A specific order node, which we need to locate in the tree.
# Goal:
# Identify the next node to fulfill that is on the same level as the given order node.
# If the order is the rightmost node on its level, return None.
# Constraints:
# We cannot use helper functions to build the tree, so we manually construct it.
# We need to maintain level-wise order for traversal and checking neighbors.
# P - Plan
# Level Order Traversal:
# Traverse the tree level by level using a queue, which helps to keep track of nodes in level order.
# For each level, store the nodes in a list and check for the target order node within that level.
# Identify Next Order:
# While processing nodes in a level, check if the order node matches the current node.
# If it does, the next node in the list (if it exists) is the next order to fulfill.
# If no next node is found (rightmost node), return None.
# Pseudocode:
# Initialize a queue with the root node and process each level.
# For each level, process nodes and check if the current node matches the given order.
# If the next node exists, return it; otherwise, return None if it’s the last node in the level.
# I - Implement
class TreeNode:
    def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

from collections import deque

def find_next_order(order_tree, order):
    if not order_tree:
        return None
    
    # Use a queue for level order traversal
    queue = deque([order_tree])
    
    while queue:
        level_size = len(queue)
        
        # Process each level
        for i in range(level_size):
            current = queue.popleft()
            
            # If we find the current node is the target 'order', return the next node in the queue
            if current == order:
                # Return the next node in this level if it's not the last node
                return queue[0] if i < level_size - 1 else None
            
            # Add children to the queue for the next level
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return None  # Return None if the order node is not found or is the last in its level

# Example Usage:
# Create nodes
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

# Construct tree
cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

# Test cases
next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)

print(next_order1.val if next_order1 else None)  # Expected Output: Eclair
print(next_order2.val if next_order2 else None)  # Expected Output: None

# Question 6 : Sectioning Off Cursed Zones
# U - Understand
# Questions to clarify the problem:
# What is the structure of the tree (e.g., binary tree)? Does each room (node) have only up to two children?
# How do we define "smallest subtree"? Is it the one with the shallowest root that includes all the deepest nodes?
# Goal:
# We need to find the smallest subtree that includes all the deepest nodes in the tree. This subtree should start from a node that has the maximum depth among all paths to the deepest nodes.
# P - Plan
# Find the Depth of Each Node:
# Traverse the tree to determine the depth of each node and identify the maximum depth. Nodes at this depth are considered the deepest nodes.
# Find the Smallest Subtree Including All Deepest Nodes:
# Using a helper function, recursively determine for each node:
# Its maximum depth.
# Whether it contains the deepest nodes in its left and right subtrees.
# The smallest subtree rooted at a node with this property is our answer.
# Algorithm Strategy (Plain English):
# Perform a depth-first search (DFS) to find the maximum depth.
# Traverse from the root, checking each subtree's depth and whether it contains all the deepest nodes. If both the left and right subtrees contain nodes at the maximum depth, the current node is the root of the smallest subtree containing all deepest nodes.
# Pseudocode:
# Define Helper Function:
# Create a function find_deepest_subtree that:
# Takes a node and current depth as arguments.
# Returns the maximum depth of the subtree rooted at the node and whether it includes all the deepest nodes.
# Traverse the Tree Using DFS:
# Use recursion to explore left and right children.
# If both subtrees contain the deepest nodes at the maximum depth, return the current node as the smallest subtree root.
# I - Implement
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_depth_and_lca(node):
    # Base case
    if not node:
        return 0, None
    
    # Recur for left and right subtrees
    left_depth, left_lca = find_depth_and_lca(node.left)
    right_depth, right_lca = find_depth_and_lca(node.right)
    
    # Current node's depth is 1 + max of left and right subtree depths
    current_depth = 1 + max(left_depth, right_depth)
    
    # If left and right depths are equal, current node is the LCA
    if left_depth == right_depth:
        return current_depth, node
    # Otherwise, the LCA is in the subtree with greater depth
    elif left_depth > right_depth:
        return current_depth, left_lca
    else:
        return current_depth, right_lca

def smallest_subtree_with_deepest_rooms(hotel):
    depth, lca = find_depth_and_lca(hotel)
    return lca
    
# Example Usage:
rooms = ["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"]
hotel1 = build_tree(rooms)

rooms = ["Lobby", 101, 102, None, "💀"]
hotel2 = build_tree(rooms)

print_tree(smallest_subtree_with_deepest_rooms(hotel1))  # [202, '😱', '👻']
print_tree(smallest_subtree_with_deepest_rooms(hotel2))  # ['💀']

# Question 7 : Vertical Bakery Display
# U - Understand
# Questions to clarify the problem:
# What order should items appear in if two nodes share the same row and column position?
# How should nodes be organized within each column (left-to-right as they appear in the tree)?
# Objective:
# Perform a vertical order traversal on the binary tree, outputting a list of lists where each inner list represents nodes in a specific vertical column.
# P - Plan
# Track Column and Row Positions:
# Use a dictionary to store nodes by their column index. Each key (column) will map to a list of tuples containing row index and node values for that column.
# Traverse Tree with BFS and Store Nodes by Position:
# Use a queue for a breadth-first search (BFS), where each entry includes the node, its column, and row. Process each node by adding its left and right children to the queue with updated column and row indices.
# As we traverse, add each node’s value to the dictionary under its column, using the row as a secondary key to help order nodes in the same column.
# Sort and Collect Results:
# After traversal, sort columns from left to right. Within each column, sort nodes by row and left-to-right order.
# Extract values for each column and compile them into the final list format.
# Pseudocode:
# Initialize Data Structures:
# Create a dictionary column_table to store nodes by their column.
# Use a queue deque to perform BFS with initial entries for the root node, at column 0 and row 0.
# BFS Traversal:
# For each node, add its value to column_table at the node’s column with a tuple of (row, value).
# Enqueue left and right children with updated column and row values.
# Extract and Sort Results:
# Sort columns and within each column, sort by row.
# Collect sorted values into the final result.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_inventory_display(root):
    if not root:
        return []
    
    # Dictionary to hold lists of nodes by their column index
    column_table = {}
    
    # Queue to hold nodes along with their column index
    queue = deque([(root, 0)])
    
    while queue:
        node, column = queue.popleft()
        
        if node:
            # If the column is not already in the dictionary, initialize it with an empty list
            if column not in column_table:
                column_table[column] = []
                
            column_table[column].append(node.val)
            
            # If there is a left child, it goes to column - 1
            queue.append((node.left, column - 1))
            
            # If there is a right child, it goes to column + 1
            queue.append((node.right, column + 1))
    
    # Sort columns and prepare the final output
    sorted_columns = sorted(column_table.keys())
    return [column_table[col] for col in sorted_columns]
    
# Example Usage:
inventory_items = ["Bread", "Croissant", "Donut", None, None, "Bagel", "Tart"]
inventory1 = build_tree(inventory_items)

inventory_items = ["Bread", "Croissant", "Donut", "Muffin", "Scone", "Bagel", "Tart", None, None, "Pie", None, "Cake"]
inventory2 = build_tree(inventory_items)

print(vertical_inventory_display(inventory1))  # [['Croissant'], ['Bread', 'Bagel'], ['Donut'], ['Tart']]
print(vertical_inventory_display(inventory2))  # [['Muffin'], ['Croissant', 'Pie'], ['Bread', 'Scone', 'Bagel'], ['Donut', 'Cake'], ['Tart']]

# Question 8 : Step by Step Directions to Hotel Room
# U - Understand
# Clarifications:
# The tree is binary, meaning each node has at most two children.
# We need to provide directions using:
# "L" (Left) when moving to the left child,
# "R" (Right) when moving to the right child, and
# "U" (Up) when moving back to the parent.
# Objective:
# Find the shortest path from the start node s to the destination node t, represented as a series of steps (L, R, U).
# P - Plan
# Find Paths to Nodes (DFS):
# Use depth-first search (DFS) to find the paths from the root node to both s (start) and t (target). Store each path as a sequence of moves (L or R) in a list.
# Identify the Lowest Common Ancestor (LCA):
# Compare the paths to s and t to determine their common prefix, which leads up to the LCA. This gives the node where the paths to s and t diverge.
# Construct the Directions:
# From the LCA:
# Move up to s by counting the steps from s back up to the LCA (each step will be an "U").
# Move down from the LCA to t by following the remaining steps from the LCA path to t.
# Combine the Directions:
# Concatenate the upward steps to reach the LCA, followed by the downward steps to reach t.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, target, path):
    if not root:
        return False
    
    if root.val == target:
        return True
    
    # Try to find the target in the left subtree
    path.append('L')
    if find_path(root.left, target, path):
        return True
    path.pop()  # Backtrack if not found
    
    # Try to find the target in the right subtree
    path.append('R')
    if find_path(root.right, target, path):
        return True
    path.pop()  # Backtrack if not found
    
    return False

def get_directions(root, start_value, dest_value):
    start_path = []
    dest_path = []
    
    # Find paths from the root to the start and destination nodes
    find_path(root, start_value, start_path)
    find_path(root, dest_value, dest_path)
    
    # Find the lowest common ancestor (LCA)
    i = 0
    while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
        i += 1
    
    # 'U' moves to go up from start to LCA
    directions = 'U' * (len(start_path) - i)
    
    # Append the remaining path to the destination
    directions += ''.join(dest_path[i:])
    
    return directions

# Example Usage:
room_nums = [5, 1, 2, 3, None, 6, 4]
hotel1 = build_tree(room_nums)
print(get_directions(hotel1, 3, 6))  # Output: "UURL"