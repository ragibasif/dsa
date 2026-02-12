"""
Bit Manipulation Utilities
A collection of custom functions for common bitwise operations.
"""


def get_bit(x: int, i: int) -> int:
    """
    Get the i-th bit of x.

    Args:
        x: The number to extract the bit from
        i: The bit position (0-indexed from the right)

    Returns:
        1 if the i-th bit is set, 0 otherwise

    Example:
        >>> get_bit(5, 0)  # 5 = 0b101
        1
        >>> get_bit(5, 1)
        0
    """
    return (x >> i) & 1


def set_bit(x: int, i: int) -> int:
    """
    Set the i-th bit of x to 1.

    Args:
        x: The number to modify
        i: The bit position (0-indexed from the right)

    Returns:
        The number with the i-th bit set to 1

    Example:
        >>> set_bit(5, 1)  # 5 = 0b101, set bit 1
        7  # 0b111
    """
    return x | (1 << i)


def clear_bit(x: int, i: int) -> int:
    """
    Clear the i-th bit of x (set it to 0).

    Args:
        x: The number to modify
        i: The bit position (0-indexed from the right)

    Returns:
        The number with the i-th bit set to 0

    Example:
        >>> clear_bit(5, 0)  # 5 = 0b101, clear bit 0
        4  # 0b100
    """
    return x & ~(1 << i)


def is_power_of_two(n: int) -> bool:
    """
    Check if n is a power of 2.

    Args:
        n: The number to check

    Returns:
        True if n is a power of 2, False otherwise

    Example:
        >>> is_power_of_two(8)
        True
        >>> is_power_of_two(6)
        False
    """
    return n > 0 and (n & (n - 1)) == 0


def is_even(n: int) -> bool:
    """
    Check if n is an even number.

    Args:
        n: The number to check

    Returns:
        True if n is even, False otherwise

    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    return (n & 1) == 0


def is_odd(n: int) -> bool:
    """
    Check if n is an odd number.

    Args:
        n: The number to check

    Returns:
        True if n is odd, False otherwise

    Example:
        >>> is_odd(4)
        False
        >>> is_odd(7)
        True
    """
    return (n & 1) == 1


def clear_lowest_set_bit(n: int) -> int:
    """
    Clear the lowest set bit in n.

    Args:
        n: The number to modify

    Returns:
        The number with the lowest set bit cleared

    Example:
        >>> clear_lowest_set_bit(12)  # 12 = 0b1100
        8  # 0b1000
    """
    return n & (n - 1)


def get_lowest_set_bit(n: int) -> int:
    """
    Get the lowest set bit in n (as a value, not position).

    Args:
        n: The number to extract the bit from

    Returns:
        The value of the lowest set bit

    Example:
        >>> get_lowest_set_bit(12)  # 12 = 0b1100
        4  # 0b100 (the lowest set bit)
    """
    return n & -n


def xor_equals_zero(a: int, b: int) -> bool:
    """
    Check if a XOR b equals 0 (i.e., a == b).

    Args:
        a: First number
        b: Second number

    Returns:
        True if a and b are equal, False otherwise

    Example:
        >>> xor_equals_zero(5, 5)
        True
        >>> xor_equals_zero(5, 3)
        False
    """
    return (a ^ b) == 0


def xor_differs(a: int, b: int) -> bool:
    """
    Check if a XOR b equals 1 (i.e., a != b for single bits).

    Args:
        a: First bit or number
        b: Second bit or number

    Returns:
        True if a and b are different (for bits), False otherwise

    Example:
        >>> xor_differs(1, 0)
        True
        >>> xor_differs(1, 1)
        False
    """
    return (a ^ b) == 1


# Additional utility functions


def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in n.

    Args:
        n: The number to count bits in

    Returns:
        The number of set bits

    Example:
        >>> count_set_bits(7)  # 7 = 0b111
        3
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def toggle_bit(x: int, i: int) -> int:
    """
    Toggle the i-th bit of x (flip it).

    Args:
        x: The number to modify
        i: The bit position (0-indexed from the right)

    Returns:
        The number with the i-th bit toggled

    Example:
        >>> toggle_bit(5, 1)  # 5 = 0b101, toggle bit 1
        7  # 0b111
    """
    return x ^ (1 << i)


if __name__ == "__main__":
    # Test examples
    print("=== Bit Manipulation Tests ===\n")

    # Get bit
    print(f"get_bit(5, 0) = {get_bit(5, 0)}")  # 1
    print(f"get_bit(5, 1) = {get_bit(5, 1)}")  # 0

    # Set bit
    print(f"\nset_bit(5, 1) = {set_bit(5, 1)}")  # 7

    # Clear bit
    print(f"clear_bit(5, 0) = {clear_bit(5, 0)}")  # 4

    # Power of 2
    print(f"\nis_power_of_two(8) = {is_power_of_two(8)}")  # True
    print(f"is_power_of_two(6) = {is_power_of_two(6)}")  # False

    # Even/Odd
    print(f"\nis_even(4) = {is_even(4)}")  # True
    print(f"is_odd(7) = {is_odd(7)}")  # True

    # Clear lowest set bit
    print(f"\nclear_lowest_set_bit(12) = {clear_lowest_set_bit(12)}")  # 8

    # Get lowest set bit
    print(f"get_lowest_set_bit(12) = {get_lowest_set_bit(12)}")  # 4

    # XOR properties
    print(f"\nxor_equals_zero(5, 5) = {xor_equals_zero(5, 5)}")  # True
    print(f"xor_differs(1, 0) = {xor_differs(1, 0)}")  # True

    # Additional utilities
    print(f"\ncount_set_bits(7) = {count_set_bits(7)}")  # 3
    print(f"toggle_bit(5, 1) = {toggle_bit(5, 1)}")  # 7
