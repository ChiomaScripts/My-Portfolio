import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from pathlib import Path

# Set Page Layout to Wide
st.set_page_config(layout="wide", page_title="Instagram Analytics Dashboard")

# Load Excel Data
file_path = Path.home() / "Downloads" / "Copy of Instagram_Analytics - DO NOT DELETE (for interview purposes).xlsx"
data = pd.read_excel(file_path, sheet_name=["Instagram Profile Overview", "Instagram Post Engagement", "Instagram Age Gender Demographi", "Instagram Top Cities Regions"])

# Extracting Sheets
overview_df = data["Instagram Profile Overview"]
post_engagement_df = data["Instagram Post Engagement"]
demographics_df = data["Instagram Age Gender Demographi"]
cities_df = data["Instagram Top Cities Regions"]

# Total Engagements column
post_engagement_df["Total Engagements"] = (post_engagement_df["Like count"] + post_engagement_df["Comments count"] +
                                             post_engagement_df["Shares"] + post_engagement_df["Unique saves"])
post_engagement_df["Date"] = pd.to_datetime(post_engagement_df["Date"])
overview_df["Date"] = pd.to_datetime(overview_df["Date"])

# Sidebar Filters
st.sidebar.header("Filters")
## Separate Date Filters
start_date = st.sidebar.date_input("Select Start Date", post_engagement_df["Date"].min())
end_date = st.sidebar.date_input("Select End Date", post_engagement_df["Date"].max())
## Media Type Filter
media_type = st.sidebar.multiselect("Select Media Type", post_engagement_df["Media product type"].unique())

## Apply filters
filtered_posts = post_engagement_df[
    (post_engagement_df["Date"] >= pd.to_datetime(start_date)) &
    (post_engagement_df["Date"] <= pd.to_datetime(end_date))
]

if media_type:
    filtered_posts = filtered_posts[filtered_posts["Media product type"].isin(media_type)]


# Custom CSS for Box Styling
st.markdown("""
    <style>
        .chart-box {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)


# Dashboard Title
st.markdown("# 📊 Instagram Analytics Dashboard")
#st.markdown("---")


# KPI Styling: Custom Font Size & Boxes
st.markdown("""
    <style>
        .kpi-box {
            width: 160px;
            padding: 8px;
            border-radius: 8px;
            text-align: left;
            font-size: 18px;
            font-weight: bold;
            color: white;
            font-style: italic;
        }
        .likes { background-color: #CE29A2; }
        .comments { background-color: #ff7f0e; }
        .engagements { background-color: #50b3c7; }
        .reach { background-color: #c75b50; }
        .engagement-rate { background-color: #9467bd; }
    </style>
""", unsafe_allow_html=True)

# Layout for KPI Metrics in Custom Boxes
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown('<div class="kpi-box likes">👍Likes <br> {} </div>'.format(int(filtered_posts["Like count"].sum())), unsafe_allow_html=True)

with col2:
    st.markdown('<div class="kpi-box comments">💬Comments <br> {} </div>'.format(int(filtered_posts["Comments count"].sum())), unsafe_allow_html=True)

with col3:
    st.markdown('<div class="kpi-box engagements">🔥Engagements <br> {} </div>'.format(int(filtered_posts["Total Engagements"].sum())), unsafe_allow_html=True)

with col4:
    st.markdown('<div class="kpi-box reach">📢 Reach <br> {} </div>'.format(int(overview_df["Profile reach"].sum())), unsafe_allow_html=True)

# Calculate Engagement Rate (Using Precomputed Total Engagements)
total_engagements = post_engagement_df["Total Engagements"].sum()
total_reach = post_engagement_df["Media reach"].sum()
average_engagement_rate = (total_engagements / total_reach) * 100 if total_reach > 0 else 0  # Avoid division by zero

with col5:
    st.markdown('<div class="kpi-box engagement-rate"> Engagement Rate <br> {:.2f}% </div>'.format(average_engagement_rate), unsafe_allow_html=True)
st.markdown("---")


# Engagement Trend Chart
#st.markdown('<div class="chart-box">', unsafe_allow_html=True)
st.markdown("### 📈 Engagement Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_posts["Date"], filtered_posts["Total Engagements"], label="Post Engagements", color="blue", marker="o", linestyle="-")
ax.set_title("Engagement Trends Over Time", fontsize=14, fontweight="bold")
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Total Engagements", fontsize=12)
ax.legend(loc="upper left", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
st.pyplot(fig)
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")


# **Row Layout for Charts**
row1_col1, row1_col2 = st.columns(2)

# **Row 1: Engagement by Media Type & Profile Impression**
# Engagement by Media Type
with row1_col1:
    st.markdown("### 📊 Engagement by Media Type")
    grouped_data = filtered_posts.groupby('Media product type')['Total Engagements'].sum()
    colors = {"FEED": "navy", "REELS": "green"}

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(grouped_data.index, grouped_data.values, color=[colors.get(cat, "gray") for cat in grouped_data.index])  # Default color if category not found
    ax.set_title("Total Engagement of Reels vs. Static Posts", fontweight="bold", fontsize=14)
    ax.set_xlabel("Media Product Type", fontsize=12)
    ax.set_ylabel("Total Engagements", fontsize=12)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    # Display in Streamlit
    st.pyplot(fig)
    #st.markdown("---")


# Profile Impressions by Day of the Week
with row1_col2:
    st.markdown("### 📆 Profile Impressions by Day of the Week")
    overview_df["Day of Week"] = overview_df["Date"].dt.day_name()
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    grouped_data = overview_df.groupby("Day of Week")["Profile impressions"].sum().reindex(day_order)
    cmap = plt.get_cmap("Pastel1")  # You can use 'viridis', 'Set2', 'Pastel1', etc.
    colors = [cmap(i) for i in range(len(grouped_data))]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(grouped_data.index, grouped_data.values, color=colors)
    ax.set_title("Profile Impressions by Day of the Week", fontsize=14, fontweight="bold")
    ax.set_xlabel("Day of the Week", fontsize=12)
    ax.set_ylabel("Total Profile Impressions", fontsize=12)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(fig)

st.markdown("---")


# Engagement Rate Over Time
st.markdown("### 🔥 Engagement Rate Over Time")
overview_df["Engagement Rate"] = overview_df["Engagement"] / overview_df["Profile reach"] * 100
fig2 = px.line(overview_df, x="Date", y="Engagement Rate", title="Engagement Rate Over Time", template="plotly_dark")
st.plotly_chart(fig2)
st.markdown("---")

# Followers by City
st.markdown("### 🌍 Followers by City")
fig4 = px.bar(cities_df.sort_values(by="Profile followers", ascending=False),
              x="City", y="Profile followers", title="Followers by City", color="City", template="plotly_dark")
st.plotly_chart(fig4)
st.markdown("---")

# Follower Demographics (Age & Gender)
st.subheader("👥 Follower Demographics (Age & Gender)")
fig, ax = plt.subplots(figsize=(10, 6))
genders = demographics_df["Gender"].unique()
colors = {"male": "royalblue", "female": "hotpink", "undefined": "purple"}

# Plot bars for each gender category
for gender in genders:
    subset = demographics_df[demographics_df["Gender"] == gender]
    ax.bar(subset["Age"], subset["Profile followers"], label=gender, color=colors.get(gender, "gray"))

ax.set_title("Follower Demographics (Age & Gender)", fontsize=14, fontweight="bold")
ax.set_xlabel("Age Group", fontsize=12)
ax.set_ylabel("Number of Followers", fontsize=12)
ax.legend(title="Gender")
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)
st.markdown("---")


# Top Performing Posts
st.markdown('<div class="chart-box">', unsafe_allow_html=True)
st.markdown("### 🚀 Top Performing Posts")
top_posts = filtered_posts.sort_values(by="Total Engagements", ascending=False).reset_index(drop=True).head(5)
st.dataframe(top_posts[["Media caption", "Total Engagements"]], hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)

# Open the terminal and run the code below to display in the browser:
# streamlit run instagram_dashboard.py
