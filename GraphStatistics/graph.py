import matplotlib.pyplot as plt

# Given data
algorithms = [
    "MERGE SORT", "INSERTION SORT", "BUBBLE SORT",
    "HEAP SORT", "QUICK SORT", "SELECTION SORT", "BOGO SORT"
]
times = [1.816, 8.959, 5.032, 1.81, 1.28, 9.038, 16.828]

# Creating the bar graph
plt.figure(figsize=(10,6))
bars = plt.barh(algorithms, times, color='skyblue')

plt.xlabel('Average Time (s)')
plt.title('Average Time of Sorting Algorithms')

# Annotate each bar with its value
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1,  # x position
             bar.get_y() + bar.get_height()/2,  # y position
             f'{width:.1f}',  # text
             va='center',  # vertical alignment
             ha='left',  # horizontal alignment
             color='black')

plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

