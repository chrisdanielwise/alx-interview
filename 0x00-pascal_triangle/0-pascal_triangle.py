def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        previous_row = triangle[-1]
        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
