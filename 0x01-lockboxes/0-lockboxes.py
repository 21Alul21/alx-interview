#!/usr/bin/python3
"""
module containing my solution
to the ALX algorithmic task 
on lockboxes
"""


def canUnlockAll(boxes):
    """ function for checking if all boxes 
    can be unlocked, it returns True if so,
    and False if it cant't.
    """

    # retrieve valid non-repetitive keys
    keys = set()
    final_list = list()
    for index, box in enumerate(boxes):
        for key in box:
            if key != index:
                keys.add(key)
   

    # unlocking the boxes
    keys.add(0)
    for box in boxes:
        if boxes.index(box) in keys:
            final_list.append(box) 
            
    return len(final_list) == len(boxes)