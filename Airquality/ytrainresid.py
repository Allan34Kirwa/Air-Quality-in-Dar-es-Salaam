from Airquality.iterating import model
from Airquality.library import plt, plot_acf
# Calculate and display residuals from the training data
y_train_resid = model.resid
y_train_resid.name = "residuals"
y_train_resid.head()

# Plot histogram of residuals
y_train_resid.hist()
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Best Model, Training Residuals");

# Create an ACF plot for y_train_resid
fig, ax = plt.subplots(figsize=(15, 6))
plot_acf(y_train_resid, ax=ax);