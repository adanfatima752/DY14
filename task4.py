class MatrixDimensionError(Exception):
    """Custom exception for matrix dimension mismatches."""
    pass

class MatrixContentError(Exception):
    """Custom exception for invalid matrix content."""
    pass

def add_matrices(matrix1, matrix2):
    # Check if both matrices have the same dimensions
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise MatrixDimensionError("Matrices must have the same dimensions.")
    
    # Check if all elements are numbers
    for matrix in [matrix1, matrix2]:
        for row in matrix:
            if not all(isinstance(element, (int, float)) for element in row):
                raise MatrixContentError("Matrices must contain only numbers.")
    
    # Add the matrices
    result_matrix = [
        [element1 + element2 for element1, element2 in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]
    
    return result_matrix

# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

try:
    result = add_matrices(matrix1, matrix2)
    print("Sum of matrices:")
    for row in result:
        print(row)
except (MatrixDimensionError, MatrixContentError) as e:
    print(f"Error: {e}")
