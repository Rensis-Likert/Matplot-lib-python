import matplotlib.pyplot as plt
import numpy as np

# Simulated exam scores for 100 students (0–100)
scores = np.random.normal(70, 15, 100)  # mean=70, std=15, 100 students

# Plot histogram
plt.hist(scores, bins=10, color='skyblue', edgecolor='black')

# Labels and title
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")

# Show grid
plt.grid(axis='y', alpha=0.75)

plt.show()