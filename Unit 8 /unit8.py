# Flower Fields
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Can the tree contain duplicate flower names, or are all values unique?
# What should the function return if the root is None (an empty tree)? Should it return False?
# P - Plan
# Write out in plain English what you want to do:
# I want to search the tree for the target flower by traversing all nodes.
# If I find the target flower in any node, I will return True.
# If I finish traversing the entire tree and don’t find the target flower, I will return False.
# I will use recursion for this problem since a binary tree naturally lends itself to recursive traversal.
# Translate each sub-problem into pseudocode:
# If the root is None, return False.
# If the root’s value matches the target flower, return True.
# Recursively search the left and right subtrees:
# If either subtree returns True, return True.
# Otherwise, return False.
# I - Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
    # Base case: if the current node is None, return False
    if not root:
        return False
    
    # Check if the current node's value matches the target flower
    if root.val == flower:
        return True
    
    # Recursively search in the left and right subtrees
    return find_flower(root.left, flower) or find_flower(root.right, flower)

# Example Usage
flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                        TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))   # Output: True
print(find_flower(flower_field, "Hibiscus"))  # Output: False

# Ocean Layers
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should we return if the tree is empty (i.e., root is None)? Should it return 0 or -1?
# Are all nodes guaranteed to have either 0, 1, or 2 children, or could the tree structure vary in unexpected ways?
# P - Plan
# Write out in plain English what you want to do:
# The goal is to determine the depth (or height) of the binary tree.
# I will use recursion to traverse the tree.
# For each node, I will recursively calculate the height of its left and right subtrees.
# The height of the tree at any node will be 1 plus the maximum of the heights of its left and right children.
# If the input tree is empty (root is None), the depth should be 0.
# Translate each sub-problem into pseudocode:
# If the root is None, return 0 (empty tree).
# Recursively compute the depth of the left and right subtrees.
# Take the maximum of the left and right subtree depths and add 1 to account for the current node.
# Return the computed depth.
# I - Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def ocean_depth(root):
    # Base case: if the current node is None, return 0
    if not root:
        return 0
    
    # Recursively calculate the depth of the left and right subtrees
    left_depth = ocean_depth(root.left)
    right_depth = ocean_depth(root.right)
    
    # Return the maximum depth between left and right subtrees + 1 for the current node
    return max(left_depth, right_depth) + 1

# Example Usage
ocean = TreeNode("Sunlight", 
                 TreeNode("Twilight", 
                          TreeNode("Abyss", TreeNode("Trenches")), 
                          TreeNode("Anglerfish")),
                 TreeNode("Squid", TreeNode("Giant Squid")))

tidal_zones = TreeNode("Spray Zone", 
                       TreeNode("Beach"), 
                       TreeNode("High Tide", 
                                TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))  # Output: 4
print(ocean_depth(tidal_zones))  # Output: 4
# Twinning Trees
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should the function return if both trees are empty (root1 and root2 are None)? Should it return True?
# Do we need to compare only the structure, or both the structure and values of the nodes?
# P - Plan
# Write out in plain English what you want to do:
# I want to recursively compare the two trees, node by node.
# For two trees to be identical:
# Both nodes at corresponding positions in each tree must have the same value.
# Both trees must have identical structures.
# If we encounter a None node in one tree but not the other, the trees are not identical.
# If both root nodes are None, the trees are identical, so I return True.
# Translate each sub-problem into pseudocode:
# If both root1 and root2 are None, return True (both trees are empty).
# If either root1 or root2 is None but not both, return False (one tree is empty).
# If the values of root1 and root2 are different, return False.
# Recursively check if the left subtrees are identical and if the right subtrees are identical.
# Return True only if both left and right subtrees match.
# I - Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    # Base case: both nodes are None, the trees are identical
    if not root1 and not root2:
        return True
    
    # If only one of the nodes is None, the trees are not identical
    if not root1 or not root2:
        return False

    # If values of the current nodes don't match, return False
    if root1.val != root2.val:
        return False

    # Recursively check the left and right subtrees
    return (is_identical(root1.left, root2.left) and 
            is_identical(root1.right, root2.right))

# Example Usage
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))  # Output: True
print(is_identical(root3, root4))  # Output: False

# Coral Reef Symmetry
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should the function return if the tree has only one node (root with no children)?
# Are we allowed to use a recursive or iterative solution to check the symmetry of the tree?
# P - Plan
# Write out in plain English what you want to do:
# To determine if a binary tree is symmetric, we need to compare the left and right subtrees.
# Two subtrees are mirror images if:
# Both are empty (None).
# The values of the roots match.
# The right subtree of the first tree matches the left subtree of the second tree, and vice-versa.
# We will solve this problem recursively by comparing the left and right children of the root, ensuring they mirror each other.
# Translate each sub-problem into pseudocode:
# If the root is None, return True (an empty tree is symmetric).
# Write a helper function is_mirror that:
# Returns True if both nodes are None.
# Returns False if only one node is None.
# Checks if the values of the nodes match.
# Recursively compares:
# The left subtree of the first node with the right subtree of the second node.
# The right subtree of the first node with the left subtree of the second node.
# Call the helper function with the left and right children of the root.
# I - Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_symmetric(root):
    # Helper function to check if two subtrees are mirrors of each other
    def is_mirror(left, right):
        # If both nodes are None, they are mirrors
        if not left and not right:
            return True
        # If only one node is None, they aren't mirrors
        if not left or not right:
            return False
        # Check if the values match and recursively compare children in mirror order
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))

    # If the root is None, it's symmetric
    if not root:
        return True
    
    # Check if the left and right subtrees are mirrors
    return is_mirror(root.left, root.right)

# Example Usage
coral1 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                  TreeNode('B', TreeNode('D'), TreeNode('C')))

coral2 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                  TreeNode('B', TreeNode('C'), TreeNode('D')))

print(is_symmetric(coral1))  # Output: True
print(is_symmetric(coral2))  # Output: False

# Remove Plant
# Understand (U)
# Given the root of a Binary Search Tree (BST), we need to:
# Remove a node (representing a plant) with the specified name.
# Update the tree structure so that the BST properties remain valid:
# If the node to be removed has:
# No children: Remove the node directly.
# One child: Replace the node with its child.
# Two children: Replace the node with its inorder predecessor (the rightmost node in the left subtree). Then, delete the predecessor node.
# Plan (P)
# Steps to Solve the Problem:
# Find the node to remove:
# If the current node’s value is greater than the target name, search the left subtree.
# If the current node’s value is less than the target name, search the right subtree.
# Handle different cases:
# Case 1: No children – Set the parent's pointer to None.
# Case 2: One child – Replace the node with its child.
# Case 3: Two children –
# Find the inorder predecessor.
# Replace the node's value with the predecessor's value.
# Recursively remove the predecessor node from the tree.
# Implement (I)
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    if collection is None:
        return collection
    
    # Step 1: Find the node to be removed
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        # Node with the same name found
        # Step 2: Node has no children (leaf node)
        if collection.left is None and collection.right is None:
            return None
        
        # Step 3: Node has one child
        if collection.left is None:
            return collection.right
        elif collection.right is None:
            return collection.left
        
        # Step 4: Node has two children
        # Find the inorder predecessor (rightmost node in the left subtree)
        predecessor = max_value_node(collection.left)
        # Replace the node's value with the predecessor's value
        collection.val = predecessor.val
        # Remove the inorder predecessor
        collection.left = remove_plant(collection.left, predecessor.val)
    
    return collection

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)
print_tree(remove_plant(collection, "Pilea"))  # Output: ['Money Tree', 'Hoya', None, 'Ivy', 'Orchid', 'ZZ Plant']

# Minimum Difference in Pearl Size
# Understand (U)
# The problem asks us to find the minimum difference between the sizes of any two pearls stored in a Binary Search Tree (BST). Since the tree is a BST, inorder traversal will give the sizes in sorted order, making it easier to find the minimum difference between consecutive pearl sizes.
# Key Observations:
# Inorder traversal will yield pearl sizes in ascending order.
# The minimum difference will always occur between two adjacent values in the inorder traversal result.
# Plan (P)
# Inorder traversal of the tree to collect pearl sizes in ascending order.
# Iterate through the sorted sizes and compute the difference between every two consecutive pearls.
# Keep track of the minimum difference encountered.
# Return the minimum difference after processing all pairs.
# Implement (I)
class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(root):
    # Helper function to perform inorder traversal and collect pearl sizes
    def inorder(node, sizes):
        if not node:
            return
        inorder(node.left, sizes)
        sizes.append(node.val)  # Add current pearl size to the list
        inorder(node.right, sizes)

    # Collect pearl sizes in sorted order using inorder traversal
    sizes = []
    inorder(root, sizes)

    # Initialize the minimum difference with a large value
    min_diff = float('inf')

    # Iterate over consecutive pearl sizes to find the minimum difference
    for i in range(1, len(sizes)):
        diff = sizes[i] - sizes[i - 1]  # Difference between consecutive pearls
        min_diff = min(min_diff, diff)  # Update the minimum difference if needed

    return min_diff

# Helper function to build a tree from a list
def build_tree(values):
    nodes = [Pearl(v) if v is not None else None for v in values]
    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
    return nodes[0] if nodes else None

# Example Usage
values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)

print(min_diff_in_pearl_sizes(pearls))  # Output: 1
class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(root):
    # Helper function to perform inorder traversal and collect pearl sizes
    def inorder(node, sizes):
        if not node:
            return
        inorder(node.left, sizes)
        sizes.append(node.val)  # Add current pearl size to the list
        inorder(node.right, sizes)

    # Collect pearl sizes in sorted order using inorder traversal
    sizes = []
    inorder(root, sizes)

    # Initialize the minimum difference with a large value
    min_diff = float('inf')

    # Iterate over consecutive pearl sizes to find the minimum difference
    for i in range(1, len(sizes)):
        diff = sizes[i] - sizes[i - 1]  # Difference between consecutive pearls
        min_diff = min(min_diff, diff)  # Update the minimum difference if needed

    return min_diff

# Helper function to build a tree from a list
def build_tree(values):
    nodes = [Pearl(v) if v is not None else None for v in values]
    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
    return nodes[0] if nodes else None

# Example Usage
values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)

print(min_diff_in_pearl_sizes(pearls))  # Output: 1

# Find the Lowest Common Ancestor in a Plant Tree Based on Species Names
# Understand (U)
# The task is to find the Lowest Common Ancestor (LCA) of two plant species in a binary tree where nodes represent species.
# The LCA of two nodes 
# p and q in a binary tree is the lowest node that has p and
# q as descendants (including the nodes themselves).
# The tree is lexicographically organized, and each node references its parent.
# We need to return the species name (string) of the LCA.
# Plan (P)
# The parent pointers provide an opportunity to trace paths from both nodes to the root, so we don’t need to traverse the entire tree.
# Approach:
# Trace the path from both nodes to the root using the parent pointers.
# Store the ancestors of one node in a set for quick lookup.
# Move up the tree from the second node until you find a common ancestor in the set of the first node’s ancestors.
# Return the common ancestor as the LCA.
# Implementation (I)
class TreeNode:
    def __init__(self, species, parent=None, left=None, right=None):
        self.val = species
        self.parent = parent  # Reference to parent node
        self.left = left
        self.right = right

def lca(root, p, q):
    # Helper function to find a node by species name
    def find_node(root, species):
        if not root:
            return None
        if root.val == species:
            return root
        # Recursively search in the left and right subtrees
        left = find_node(root.left, species)
        return left if left else find_node(root.right, species)

    # Find the nodes for p and q
    node_p = find_node(root, p)
    node_q = find_node(root, q)

    # Step 1: Collect all ancestors of p in a set
    ancestors = set()
    while node_p:
        ancestors.add(node_p)
        node_p = node_p.parent

    # Step 2: Traverse the ancestors of q to find the first common ancestor
    while node_q:
        if node_q in ancestors:
            return node_q.val  # Return the species name of the LCA
        node_q = node_q.parent

    return None  # If no LCA found (shouldn't happen for valid input)

# Example Usage
fern = TreeNode("fern")
cactus = TreeNode("cactus", fern)
rose = TreeNode("rose", fern)
bamboo = TreeNode("bamboo", cactus)
dahlia = TreeNode("dahlia", cactus)
lily = TreeNode("lily", rose)
oak = TreeNode("oak", rose)

fern.left, fern.right = cactus, rose
cactus.left, cactus.right = bamboo, dahlia
rose.left, rose.right = lily, oak

print(lca(fern, "cactus", "rose"))  # Output: "fern"
print(lca(fern, "bamboo", "oak"))   # Output: "fern"
print(lca(fern, "bamboo", "dahlia"))  # Output: "cactus"

# Distributing Sunken Treasure
# Understand (U)
# We need to distribute coins in a binary tree so that each node has exactly one coin.
# In one move, we can move a coin between two adjacent nodes (either parent ↔ child).
# Each node starts with a certain number of coins (given as node.val).
# The total number of coins equals the number of nodes in the tree, so every node must eventually hold exactly one coin.
# Our task is to minimize the total number of moves required to achieve this distribution.
# Plan (P)
# Observations:
# If a node has more than 1 coin, the excess coins need to be moved to other nodes.
# If a node has no coins (or less than 1), it needs to receive coins from other nodes.
# This problem can be solved bottom-up by post-order traversal:
# First solve the coin distribution in the left and right subtrees, and then adjust the coin count at the current node.
# Key Idea:
# After processing a node's children:
# Calculate the net balance of coins at each node.
# Net balance: node.val - 1
# If net balance > 0: The node has excess coins to distribute.
# If net balance < 0: The node needs coins from its parent.
# As we traverse the tree, we accumulate the number of moves required to balance the coins.
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def distribute_coins(root):
    # Initialize the total moves required to 0
    total_moves = 0

    # Helper function to perform post-order traversal
    def dfs(node):
        nonlocal total_moves
        if not node:
            return 0  # No coins needed from an empty node

        # Recursively process left and right children
        left_balance = dfs(node.left)
        right_balance = dfs(node.right)

        # Calculate the total moves required for this node
        total_moves += abs(left_balance) + abs(right_balance)

        # Return the net balance of coins for this node
        # (positive = surplus, negative = deficit)
        return node.val + left_balance + right_balance - 1

    # Start post-order traversal from the root
    dfs(root)
    return total_moves

# Example Usage:
# Tree 1
root1 = TreeNode(3, TreeNode(0), TreeNode(0))
print(distribute_coins(root1))  # Output: 2

# Tree 2
root2 = TreeNode(0, TreeNode(3), TreeNode(0))
print(distribute_coins(root2))  # Output: 3


