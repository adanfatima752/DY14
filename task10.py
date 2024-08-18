import numpy as np

def normalize_and_stats(numbers):
    """
    Normalizes a list of numbers to a range of 0 to 1 and returns basic statistical measures.
    
    Args:
    - numbers: A list of numbers to normalize and analyze.
    
    Returns:
    - A dictionary containing:
      - 'mean': The mean of the normalized numbers.
      - 'median': The median of the normalized numbers.
      - 'variance': The variance of the normalized numbers.
    
    Raises:
    - ValueError: If the list contains non-numeric values or is empty.
    """
    # Validate the input
    if not numbers:
        raise ValueError("The list is empty.")
    
    # Ensure all values are numeric
    try:
        numbers = [float(num) for num in numbers]
    except ValueError:
        raise ValueError("The list contains non-numeric values.")
    
    # Normalize the numbers to a range of 0 to 1
    min_val = min(numbers)
    max_val = max(numbers)
    
    if min_val == max_val:
        # If all values are the same, normalization will result in a list of zeros
        normalized_numbers = [0.0] * len(numbers)
    else:
        normalized_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]
    
    # Calculate statistical measures
    mean = np.mean(normalized_numbers)
    median = np.median(normalized_numbers)
    variance = np.var(normalized_numbers)
    
    return {
        'mean': mean,
        'median': median,
        'variance': variance
    }

# Example usage:
numbers = [10, 20, 30, 40, 50]
stats = normalize_and_stats(numbers)
print("Statistics:", stats)
