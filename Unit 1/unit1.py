# Locate Thistles Problem
# U - Understand
# Questions to Ask:
# Are we only looking for exact matches of the string "thistle" or any variations (e.g., case-sensitive)?
# What should be returned if no "thistle" is found in the list?
# P - Plan
# Plan in Plain English:
# I want to check each item in the list. If the item is "thistle", I will record the index (position) of that item. If no "thistle" is found, I will return an empty list.
# Pseudocode:
# Start with an empty list called thistle_lst.
# Loop through each item in the items list.
# If the current item is "thistle", append its index to thistle_lst.
# After the loop finishes, return thistle_lst.
# I - Implement
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


