from Airquality.explore import y
from Airquality.library import plt

# Create a timeseries plot of PM2.5 levels in Dar es Salaam over time
fig, ax = plt.subplots(figsize=(15, 6))
y.plot(title="Dar es Salaam PM2.5 Levels", xlabel="Date", ylabel="PM2.5 Level", ax=ax);