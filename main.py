import graphviz
import re
import os

# Directory containing .dot files
dot_files_dir = 'dotfiles'

# Read .dot files from the directory
dot_files = {}
for filename in os.listdir(dot_files_dir):
    if filename.endswith('.dot'):
        with open(os.path.join(dot_files_dir, filename), 'r') as file:
            dot_files[filename] = file.read()

# Graph directions
directions = ["TB", "LR", "BT", "RL"]

# User selects a graph
print("Select a graph:")
for i, key in enumerate(dot_files.keys(), 1):
    print(f"{i}. {key}")

graph_choice = int(input("Enter choice: ")) - 1
selected_graph_name = list(dot_files.keys())[graph_choice]
selected_graph = dot_files[selected_graph_name]

# Extract and print nodes
nodes = set(re.findall(r'\b[A-Za-z]\b', selected_graph))
print("\nNodes in the selected graph:")
for node in nodes:
    print(node)

# User selects a direction
print("\nSelect a direction:")
for i, dir_ in enumerate(directions, 1):
    print(f"{i}. {dir_}")

direction_choice = int(input("Enter choice (1/2/3/4): ")) - 1
selected_direction = directions[direction_choice]

# Modify the .dot content with the selected direction
dot_with_direction = selected_graph.replace("digraph G {", f"digraph G {{\n    rankdir={selected_direction};")

# Print the final .dot content
print("\nGenerated .dot file content:")
print(dot_with_direction)

# Optional: Render the graph and save as an image
dot = graphviz.Source(dot_with_direction)
dot.render("output_graph", format="png", cleanup=False)

print("\nGraph has been saved as 'output_graph.png'")
