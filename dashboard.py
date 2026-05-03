import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#page setup
st.set_page_config(page_title="Productivity Dashboard", layout="centered")

#setup the file
st.title("Smart Productivity Dashboard")
st.write("Analyze how daily habits like study, sleep, and screen time affect productivity.")

#load csv
df=pd.read_csv("data.csv")

#filter section
st.sidebar.header("Filters")

min_study = st.sidebar.slider("Minimum Study Hours", 0, 10, 0)
filtered_df = df[df["study_hours"] >= min_study]
if filtered_df.empty:
    st.warning("No data available for selected filter.")
    st.stop()

#show dataset
st.subheader("Dataset Preview")
st.write(filtered_df)

st.markdown("---")

#add key metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Study Hours", round(filtered_df["study_hours"].mean(), 2))
col2.metric("Avg Sleep Hours", round(filtered_df["sleep_hours"].mean(), 2))
col3.metric("Avg Productivity", round(filtered_df["productivity_score"].mean(), 2))

st.markdown("---")

#add first chart
st.subheader("Study vs Productivity")

fig, ax = plt.subplots(figsize=(4,2))
ax.scatter(filtered_df["study_hours"], filtered_df["productivity_score"])
ax.set_xlabel("Study Hours")
ax.set_ylabel("Productivity Score")
ax.set_title("Study vs Productivity")
st.pyplot(fig)

#add second chart 
st.subheader("Screen Time vs Productivity")

fig, ax = plt.subplots(figsize=(4,2))
ax.scatter(filtered_df["screen_time"], filtered_df["productivity_score"])
ax.set_xlabel("Screen Time")
ax.set_ylabel("Productivity Score")
ax.set_title("Screen Time Impact")
st.pyplot(fig)
#add bar chart
st.subheader("Average Comparison")

avg = filtered_df[["study_hours", "sleep_hours", "screen_time"]].mean()

fig, ax = plt.subplots(figsize=(4,2))
avg.plot(kind="bar", ax=ax)
ax.set_ylabel("Average Values")
ax.set_title("Average Habit Comparison")
st.pyplot(fig)

st.markdown("---")

#add insights
st.subheader("Insights")

if filtered_df["study_hours"].mean() > 5:
    st.success("Good study habits observed.")
else:
    st.warning("Study hours could be improved.")

if filtered_df["screen_time"].mean() > 4:
    st.warning("High screen time may reduce productivity.")
else:
    st.success("Screen time is under control.")

if filtered_df["sleep_hours"].mean() >= 7:
    st.success("Healthy sleep pattern detected.")
else:
    st.warning("Sleep hours are below recommended levels.")
