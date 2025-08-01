def to_binary(n):
    """Converts a decimal integer to its binary string representation."""
    if n == 0:
        return "0"

    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n //= 2
    return binary_str

def to_hexadecimal(n):
    """Converts a decimal integer to its hexadecimal string representation."""
    if n == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    while n > 0:
        remainder = n % 16
        hex_str = hex_chars[remainder] + hex_str
        n //= 16
    return hex_str

# Main script execution
if __name__ == "__main__":
    try:
        num = int(input())
        print(to_binary(num))
        print(to_hexadecimal(num))
    except (ValueError, IndexError):
        print("Invalid input. Please enter a single non-negative integer.")