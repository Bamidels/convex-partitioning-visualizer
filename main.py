import random
from polygon_utils import Polygon, intersects_multiple_segments, split_polygon

L = 10  # Side length of the square
S = Polygon([(0, 0), (L, 0), (L, L), (0, L)])  # Initialize the square S as a single polygon

def partition_square(S, line_segments):
    Z = [S]
    # Shuffle line segments randomly
    random.shuffle(line_segments)
    
    for l in line_segments:
        for polygon in Z:
            if intersects_multiple_segments(polygon, line_segments):
                # Choose the first segment that intersects the polygon
                # Split the polygon into two using the segment
                Q, R = split_polygon(polygon, l)
                Z.remove(polygon)
                Z.extend([Q, R])
                break
    return Z

# Example line segments
line_segments = [
    ((1, 1), (5, 5)),
    ((2, 2), (8, 2)),
    ((3, 3), (7, 7))
]

# Run the partitioning algorithm
result = partition_square(S, line_segments)
print("Number of polygons:", len(result))
