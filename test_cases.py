from main import partition_square, S
from polygon_utils import Polygon

# Example test cases for the partitioning algorithm

def run_test():
    line_segments = [
        ((1, 1), (5, 5)),
        ((2, 2), (8, 2)),
        ((3, 3), (7, 7)),
        ((4, 1), (6, 5))
    ]
    
    result = partition_square(S, line_segments)
    print("Test Case 1: Number of polygons created:", len(result))
    assert len(result) > 1, "Expected more than 1 polygon"

run_test()
