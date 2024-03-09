from Airquality.split import y_train
from Airquality.library import mean_absolute_error

# Establish the baseline mean absolute error for your model.
y_train_mean = y_train.mean()
y_pred_baseline = [y_train_mean] * len(y_train)
mae_baseline = mean_absolute_error(y_train, y_pred_baseline )
# Display the Mean P2 reading & baseline MAE
print("Mean P2 Reading:", y_train_mean)
print("Baseline MAE:", mae_baseline)