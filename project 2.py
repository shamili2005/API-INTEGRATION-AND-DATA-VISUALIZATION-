

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet

# ===============================
# 1. Load Data from CSV
# ===============================
# Create a sample CSV if not available
sample_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [85, 92, 78, 88, 95],
    "Age": [20, 21, 19, 22, 20]
}
df = pd.DataFrame(sample_data)
df.to_csv("students.csv", index=False)   # save sample file
df = pd.read_csv("students.csv")         # load file

# ===============================
# 2. Analyze Data
# ===============================
summary = df.describe()   # summary statistics

# ===============================
# 3. Create Visualization
# ===============================
plt.figure(figsize=(6,4))
sns.barplot(x="Name", y="Score", data=df, hue="Name",dodge=False,palette="viridis",legend=False)
plt.title("Student Score Comparison")
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

# ===============================
# 4. Generate PDF Report
# ===============================
doc = SimpleDocTemplate("Task2_Report.pdf")
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("CODTECH Internship - Task 2", styles['Title']))
elements.append(Spacer(1, 20))

# Intro
elements.append(Paragraph("Automated Report Generation using Python", styles['Heading2']))
elements.append(Spacer(1, 12))
elements.append(Paragraph(
    "This report reads student data from a CSV file, analyzes it, "
    "and generates this formatted PDF with summary statistics and visualization.",
    styles['Normal']
))
elements.append(Spacer(1, 20))

# Table: Summary statistics
elements.append(Paragraph("Summary Statistics", styles['Heading2']))
elements.append(Spacer(1, 12))
summary_table = Table([summary.columns.to_list()] + summary.round(2).values.tolist())
elements.append(summary_table)
elements.append(Spacer(1, 20))

# Chart
elements.append(Paragraph("Visualization", styles['Heading2']))
elements.append(Spacer(1, 12))
elements.append(Image("chart.png", width=400, height=250))

# Build PDF
doc.build(elements)

print("✅ Task 2 completed: Task2_Report.pdf generated successfully!")
