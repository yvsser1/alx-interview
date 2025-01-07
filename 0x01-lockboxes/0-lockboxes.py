#!/usr/bin/python3
"""Module for determining if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (List[List[int]]): List of lists where each inner list has keys
            to other boxes. boxes[i] contains keys that can open boxes[j].

    Returns:
        bool: True if all boxes can be opened, else False

    The function uses a depth-first search approach to track which boxes
    can be reached starting from box 0, which is initially unlocked.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return False

    # Keep track of visited (unlocked) boxes
    unlocked = set([0])
    # Stack for boxes to explore (starting with box 0)
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Check each key in the current box
        for key in boxes[current_box]:
            # If the key opens a new box (within valid range)
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    # Return True if we can unlock all boxes
    return len(unlocked) == n
