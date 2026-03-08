pass  # YOUR CODE HERE
def manhattan(a,b):
    d_x = abs(a[0]-b[0])
    d_y = abs(a[1]-b[1])
    distances = abs(d_x + d_y)
    return distances
