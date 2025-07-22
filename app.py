import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="Dynamic City Map", layout="wide")
st.title("🗺️ Australian Cities Map")

# Define a list of cities with coordinates
all_cities = [
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
    {"name": "Melbourne", "lat": -37.8136, "lon": 144.9631},
    {"name": "Brisbane", "lat": -27.4698, "lon": 153.0251},
    {"name": "Perth", "lat": -31.9505, "lon": 115.8605},
    {"name": "Adelaide", "lat": -34.9285, "lon": 138.6007},
    {"name": "Canberra", "lat": -35.2809, "lon": 149.1300},
    {"name": "Darwin", "lat": -12.4634, "lon": 130.8456},
    {"name": "Hobart", "lat": -42.8821, "lon": 147.3272}
]

# Sidebar multiselect to choose active cities
city_names = [city["name"] for city in all_cities]
selected_cities = st.sidebar.multiselect("Select Active Cities", city_names, default=city_names)

# Filter cities based on selection
active_cities = [city for city in all_cities if city["name"] in selected_cities]

# Create Plotly map
fig = go.Figure()

for city in active_cities:
    fig.add_trace(go.Scattergeo(
        lon=[city["lon"]],
        lat=[city["lat"]],
        text=city["name"],
        mode='markers+text',
        marker=dict(size=8, color='blue'),
        name=city["name"]
    ))

fig.update_layout(
    title="Active Cities in Australia",
    geo=dict(
        scope='world',
        projection_type='equirectangular',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        countrycolor='rgb(204, 204, 204)',
        center=dict(lat=-25.0, lon=135.0),
        lataxis=dict(range=[-45, -10]),
        lonaxis=dict(range=[110, 155])
    ),
    margin=dict(l=0, r=0, t=30, b=0),
    height=800
)

# Display the map
st.plotly_chart(fig, use_container_width=True)

# Create a DataFrame for active cities
active_df = pd.DataFrame(active_cities)

# Button to generate and download Excel file
st.subheader("📥 Download Active Cities Table")
if st.button("Generate Excel File"):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        active_df.to_excel(writer, index=False, sheet_name='Active Cities')
    st.download_button(
        label="Download Excel File",
        data=output.getvalue(),
        file_name="active_cities.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
