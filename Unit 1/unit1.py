# Locate Thistles Problem
### U - Understand
# Questions to Ask:
# Are we only looking for exact matches of the string "thistle" or any variations (e.g., case-sensitive)?
# What should be returned if no "thistle" is found in the list?
### P - Plan
# Plan in Plain English:
# I want to check each item in the list. If the item is "thistle", I will record the index (position) of that item. If no "thistle" is found, I will return an empty list.
# Pseudocode:
# Start with an empty list called thistle_lst.
# Loop through each item in the items list.
# If the current item is "thistle", append its index to thistle_lst.
# After the loop finishes, return thistle_lst.
### I - Implement
# Final Python Solution:

def locate_thistles(items):
  thistle_lst = [] 
  for i in range(len(items)):
    if items[i] == "thistle":
      thistle_lst.append(i)
  return thistle_lst

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))


# Shuffle Problem
### U - Understand
# Questions to Ask:
# Are the input lists always guaranteed to have an even number of elements?
# Should the function handle any special types of elements, or is it assumed that all elements are of the same type (like integers or strings)?
#### P - Plan
# Plan in Plain English:
# First, split the cards list into two equal halves.
# Then, interleave the two halves, where we take one element from the first half and one from the second half alternately.
# Finally, return the new shuffled list.
# Pseudocode:
# Get the length n of the first half, which is half the length of the entire cards list.
# Split the cards list into first_half and second_half.
# Create an empty list shuffled to store the shuffled elements.
# Loop through the indices of the first half:
# For each index, append the element from the first_half to shuffled.
# Append the corresponding element from the second_half to shuffled.
# Return the shuffled list.
### I - Implement
# Final Python Solution:
def shuffle(cards):
    n = len(cards) // 2
    first_half = cards[:n]
    second_half = cards[n:]
    
    shuffled = []
    for i in range(n):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])
    
    return shuffled

# Example usage:
cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))  # Expected Output: ['Joker', 3, 'Queen', 'Ace', 2, 7]

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))  # Expected Output: [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]

cards = [10, 10, 2, 2]
print(shuffle(cards))  # Expected Output: [10, 2, 10, 2]
