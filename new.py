import pygmt
import pandas as pd

# Sample data: Cities with latitude and longitude
data = pd.DataFrame({
    "latitude": [40.7128, 34.0522, 51.5074],
    "longitude": [-74.0060, -118.2437, -0.1278],
    "size": [0.5, 0.5, 0.5]
})

# Create a figure
fig = pygmt.Figure()

# Plot coastlines
fig.coast(region="g", projection="M6i", land="gray", water="skyblue", frame=True)

# Plot data points
fig.plot(x=data["longitude"], y=data["latitude"], style="c0.2c", color="red", pen="black")

fig.show()
