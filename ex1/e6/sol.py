import sys

# PART 1: The Function Definition (The "Brain")
# This part defines WHAT to do, but doesn't run on its own.
def universal_calculator(*args, **kwargs):
    """
    Calculates the sum or product of a variable number of arguments,
    with an option to round the result.
    """
    if kwargs.get('operation') == 'multiply':
        result = 1
        for num in args:
            result *= num
    else:
        result = sum(args)

    if 'round_to' in kwargs:
        try:
            decimal_places = int(kwargs['round_to'])
            result = round(result, decimal_places)
        except (ValueError, TypeError):
            pass

    return result

# --------------------------------------------------------------------

# PART 2: The Script Execution (The "Engine")
# This code runs when the judge executes the file.
if __name__ == "__main__":
    lines = sys.stdin.readlines()
    
    args = []
    kwargs = {}

    # Parse the input from stdin
    if lines:
        first_line = lines[0].strip()
        if first_line:
            try:
                args = [float(x) for x in first_line.split()]
            except ValueError:
                args = []

    if len(lines) > 1:
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if '=' in line:
                key, value = line.split('=', 1)
                kwargs[key] = value

    # Call the function and print its result
    final_answer = universal_calculator(*args, **kwargs)
    print(final_answer)