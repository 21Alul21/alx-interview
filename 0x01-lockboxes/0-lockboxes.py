#!/usr/bin/python3
"""Module containing the solution
to the lockboxes algorithmic task
"""


def canUnlockAll(boxes):
    """the method for the
    implementation
    """

    opened_boxes = {0}
    ranges = set(range(1, len(boxes)))
    for box in boxes:
        for key in boxes:
            if key in ranges:
                opened_boxes.add(key)
    return len(opened_boxes) == len(boxes)
