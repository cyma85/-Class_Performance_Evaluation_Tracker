import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# =========================
# Sample CSV Data
# =========================
csv_data = """
Student Name,Attendance (%),Assignments,Quizzes,Midterm,Final,Grade
Ali,90,8,7,78,85,A
Amina,85,7,6,82,80,B
Bilal,75,6,5,70,72,C
Sara,95,9,9,88,90,A
Usman,80,7,6,75,78,B
"""

# Convert CSV string to DataFrame
df = pd.read_csv(StringIO(csv_data))

# =========================
# Streamlit App
# =========================
st.set_page_config(page_title="Class Performance Tracker", page_icon="📊", layout="wide")

st.title("📊 AI-Based Class Performance Evaluation Tracker")

# Show Data Table
st.subheader("📋 Student Performance Table")
st.dataframe(df)

# Pie chart for Grades
st.subheader("📈 Grade Distribution")
grade_counts = df['Grade'].value_counts()
fig, ax = plt.subplots()
ax.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

# Bar chart for Attendance
st.subheader("📊 Attendance Comparison")
fig, ax = plt.subplots()
df.plot(x="Student Name", y="Attendance (%)", kind="bar", ax=ax, legend=False)
plt.ylabel("Attendance (%)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Line chart for Marks
st.subheader("📉 Marks Overview")
fig, ax = plt.subplots()
df.plot(x="Student Name", y=["Midterm", "Final"], kind="line", marker="o", ax=ax)
plt.ylabel("Marks")
plt.xticks(rotation=45)
st.pyplot(fig)
