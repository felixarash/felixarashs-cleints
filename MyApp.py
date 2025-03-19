import streamlit as st
import pandas as pd
import numpy as np
 
st.write("""
# Felix Arash
Client *Population!*
""")
 
# Create some sample data instead of reading from file
data = {
    'date': pd.date_range('2023-01-01', periods=10),
    'value': np.random.randint(0, 100, size=10)
}
df = pd.DataFrame(data)

st.line_chart(df.set_index('date'))

st.text("Throughout this year Fozan Ahmed got higest clients ratio in 2024")

# Update the map section to display data points around Karachi, Pakistan
karachi_lat, karachi_lon = 24.8607, 67.0011

# Creating random data points around Karachi
df_karachi = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [karachi_lat, karachi_lon],
    columns=["lat", "lon"],
)

# Display the map with a caption
st.subheader("Karachi, Pakistan Map")
st.map(df_karachi)