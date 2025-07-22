import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Simple Map App", layout="wide")
st.title("?? Sample Locations Map")

locations = [
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
    {"name": "Melbourne", "lat": -37.8136, "lon": 144.9631},
    {"name": "Brisbane", "lat": -27.4698, "lon": 153.0251},
    {"name": "Perth", "lat": -31.9505, "lon": 115.8605},
    {"name": "Adelaide", "lat": -34.9285, "lon": 138.6007}
]

fig = go.Figure()

for loc in locations:
    fig.add_trace(go.Scattergeo(
        lon=[loc["lon"]],
        lat=[loc["lat"]],
        text=loc["name"],
        mode='markers+text',
        marker=dict(size=8, color='blue'),
        name=loc["name"]
    ))

fig.update_layout(
    title="Major Cities in Australia",
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
    margin=dict(l=0, r=0, t=30, b=0)
)

st.plotly_chart(fig, use_container_width=True)
