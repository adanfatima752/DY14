def flatten_list(nested_list):
    """
    Flattens a nested list of lists (of arbitrary depth) into a single list and calculates the depth.
    
    Args:
    - nested_list: The nested list to flatten.
    
    Returns:
    - A tuple containing:
      1. The flattened list.
      2. The depth of the original nested structure.
    """
    def flatten_recursive(lst, depth):
        flat_list = []
        max_depth = depth
        
        for item in lst:
            if isinstance(item, list):
                # Recursive call to handle nested lists
                nested_flat_list, nested_depth = flatten_recursive(item, depth + 1)
                flat_list.extend(nested_flat_list)
                max_depth = max(max_depth, nested_depth)
            else:
                # If item is not a list, append it to the flat list
                flat_list.append(item)
        
        return flat_list, max_depth
    
    # Start the recursion with depth 1
    flattened_list, original_depth = flatten_recursive(nested_list, 1)
    
    return flattened_list, original_depth

# Example usage:
nested_list = [1, [2, [3, [4, [5]]]], 6]
flattened, depth = flatten_list(nested_list)
print("Flattened List:", flattened)
print("Original Depth:", depth)
