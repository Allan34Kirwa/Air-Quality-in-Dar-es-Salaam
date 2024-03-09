from Airquality.library import plt
from Airquality.wrangle import df

# Plot the rolling average of the readings in y. Use a window size of 168 
fig, ax = plt.subplots(figsize=(15, 6))

# Plot the rolling average
(
    df["P2"].rolling(168).mean()
    .plot(ax=ax, ylabel="PM2.5", title="Dar es Salaam PM2.5 Levels, 7-Day Rolling Average")
    );