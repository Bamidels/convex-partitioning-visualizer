# convex-partitioning-visualizer
A Python tool that partitions a square into convex polygons using disjoint line segments. Implements an efficient O(n log n) algorithm, visualizes each step, and tracks performance metrics. Ideal for learning computational geometry, debugging algorithms, and exploring partitioning techniques.
Key Features
Efficient Partitioning Algorithm: Implements an O(nlogn) algorithm for optimal performance.
Detailed Step-by-Step Visualization: Illustrates each step of the partitioning process to aid understanding.
Performance Tracking: Measures and reports computational metrics, allowing for analysis of algorithm efficiency.
Learning Tool: Perfect for students, developers, and researchers interested in computational geometry and convex polygon partitioning.
Getting Started
Clone the Repository:

Install Dependencies (if any):

For example, install matplotlib for visualizations:
bash

pip install matplotlib

Run the Program:

bash

python main.py

Usage
Define Your Input: Specify the line segments and the square boundary in the code.
Run Partitioning: The program will process the input and display the step-by-step partitioning.
View Results: Observe the final set of convex polygons and analyze the performance metrics.
Example
Provide example code here (or screenshots) to showcase a sample run, if applicable.

python
Copy code
# Example line segments
line_segments = [
    ((1, 1), (5, 5)),
    ((2, 2), (8, 2)),
    ((3, 3), (7, 7))
]

# Run partitioning
result = partition_square(S, line_segments)
print("Number of polygons:", len(result))
Contributing
Feel free to open issues, discuss ideas, or submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
