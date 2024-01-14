#!/usr/bin/python3
"""Module containing the solution
to the lockboxes algorithmic task
"""


def canUnlockAll(boxes):
    """the method for the
    implementation
    """

    # Set to keep track of opened boxes
    opened_boxes = {0}
    
    # Set to keep track of keys that need to be explored
    keys_to_explore = set(boxes[0])

    # Iterate through keys to explore
    while keys_to_explore:
        key = keys_to_explore.pop()
        
        # Check if the key opens a box
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys_to_explore.update(boxes[key])

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
