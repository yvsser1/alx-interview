#!/usr/bin/python3
"""Module containing function to validate UTF-8 encoding"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers where each integer represents 1 byte of data

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7
    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits
        num = num & 0xFF

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Count number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False

        # If this byte is a continuation of a UTF-8 character
        else:
            # Check if the byte has the proper format (10xxxxxx)
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    # Check if all characters were complete
    return n_bytes == 0
