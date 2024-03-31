import math

def bytes_to_size(bytes: int) -> str:
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', "PB", "EB", "ZB", "YB"]

    # Check for zero or non-integer values
    try:
        bytes = int(bytes)
    except ValueError:
        return 'Invalid input'

    # Check for negative values
    if bytes < 0:
        return 'Invalid input'

    # Get the index of the appropriate size
    i = int(math.floor(math.log(bytes) / math.log(1024)))

    # Convert the bytes to the appropriate size
    return f"{(bytes / (1024 ** i)):.1f} {sizes[i]}"
