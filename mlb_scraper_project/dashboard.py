import streamlit as st
import pandas as pd
import altair as alt

# Load cleaned MLB data
df = pd.read_csv("my_mlb_data_cleaned.csv")

# Convert Year to numeric and clean data
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df.dropna(subset=["Year"], inplace=True)
df["Year"] = df["Year"].astype(int)

# Sidebar filters
st.sidebar.title("MLB Data Filters")
min_year, max_year = df["Year"].min(), df["Year"].max()
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
avg_threshold = st.sidebar.slider("Minimum Batting Average", 0.2, 0.5, 0.3, 0.01)
leagues = df["League"].dropna().unique().tolist()
selected_leagues = st.sidebar.multiselect("Select League(s)", leagues, default=leagues)

# Filter data according to selections
filtered_df = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["AVG"] >= avg_threshold) &
    (df["League"].isin(selected_leagues))
]

st.title("MLB Batting Average Dashboard")

# 1. Scatter Plot: Player AVG over Years
st.markdown("### Player Batting Average Distribution Over Years")
st.markdown("This scatter plot shows how players' batting averages vary over the years. Each dot represents a player in a specific year and their AVG.")

scatter = alt.Chart(filtered_df).mark_circle(size=60).encode(
    x=alt.X("Year:O", title="Year"),
    y=alt.Y("AVG:Q", title="Batting Average (AVG)"),
    color=alt.Color("League:N", title="League"),
    tooltip=["Player", "Team", "AVG", "Year", "League"]).interactive().properties(width=700, height=400)

st.altair_chart(scatter, use_container_width=True)

# 2. Histogram: Distribution of AVG
st.markdown("### Distribution of Batting Averages Among Players")
st.markdown("This histogram shows how many players fall into different AVG ranges. It helps understand the frequency of various batting averages.")

hist = alt.Chart(filtered_df).mark_bar().encode(
    alt.X("AVG:Q", bin=alt.Bin(maxbins=30), title="Batting Average (AVG)"),
    y='count()',
    color=alt.Color("League:N", legend=None)
).properties(width=700, height=300)

st.altair_chart(hist, use_container_width=True)

# 3. Table: Top 10 Players by AVG
st.markdown("### Top 10 Players by Highest AVG in Selected Period")
st.markdown("This table lists the top players selected based on their maximum AVG within the filtered years and leagues.")

top_players = (
    filtered_df.groupby("Player", as_index=False)
    .agg({"AVG": "max", "Team": "first", "League": "first"})
    .sort_values("AVG", ascending=False)
    .head(10))

top_players["AVG"] = top_players["AVG"].round(3)

st.table(top_players[["Player", "Team", "League", "AVG"]])

# 4. Bar Chart: Number of Leaders by Team
st.markdown("### Number of League Leaders by Team")
st.markdown("This chart shows which teams have the most players appearing as batting average leaders, indicating their strength.")

team_counts = filtered_df["Team"].value_counts().reset_index()
team_counts.columns = ["Team", "Count"]
team_counts = team_counts.head(10)

bar_team = alt.Chart(team_counts).mark_bar().encode(
    x=alt.X("Team:N", sort="-y", title="Team"),
    y=alt.Y("Count:Q", title="Number of Players"),
    color=alt.Color("Team:N", legend=None)
).properties(width=700, height=350)

st.altair_chart(bar_team, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Data collected and cleaned as part of a personal MLB analysis project.")