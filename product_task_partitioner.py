import random

class Task:
    def __init__(self, name, complexity, impact):
        self.name = name
        self.complexity = complexity  # Represents the level of effort or difficulty
        self.impact = impact  # Represents the potential impact on the user or business

class ProductPartitioner:
    def __init__(self, main_task):
        self.main_task = main_task  # The main product area to enhance
        self.subtasks = []  # List of smaller tasks after partitioning

    def partition_task(self, subtask_complexity_threshold):
        # Create random subtasks based on complexity and impact
        subtask_names = ["UI Overhaul", "Feature Addition", "Bug Fixes", "Performance Optimization"]
        
        for name in subtask_names:
            complexity = random.randint(1, 10)
            impact = random.randint(1, 10)
            
            # Partition based on complexity threshold
            if complexity <= subtask_complexity_threshold:
                subtask = Task(name, complexity, impact)
                self.subtasks.append(subtask)

        # Sort subtasks by impact for prioritization
        self.subtasks.sort(key=lambda x: -x.impact)

    def display_partitioned_tasks(self):
        print(f"Main Task: {self.main_task}")
        print("Partitioned Subtasks:")
        for subtask in self.subtasks:
            print(f"- {subtask.name}: Complexity={subtask.complexity}, Impact={subtask.impact}")

# Define the main product enhancement or project
main_task = "Revamp User Interface (UI) for Enhanced Usability"

# Instantiate the ProductPartitioner
product_partitioner = ProductPartitioner(main_task)

# Partition the main task based on a complexity threshold
product_partitioner.partition_task(subtask_complexity_threshold=7)

# Display the partitioned tasks
product_partitioner.display_partitioned_tasks()
