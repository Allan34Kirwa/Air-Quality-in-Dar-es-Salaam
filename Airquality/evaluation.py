from Airquality.library import pd, AutoReg, mean_absolute_error
from Airquality.split import y_train, y_test

# Perform walk-forward validation for your model for the entire test set y_test.
y_pred_wfv = pd.Series()
history = y_train.copy()
for i in range(len(y_test)):
    best_model = AutoReg(history, lags=26).fit()
    next_pred = best_model.forecast()
    y_pred_wfv = y_pred_wfv.append(next_pred)
    history = history.append(y_test[next_pred.index])

test_mae = mean_absolute_error(y_test, y_pred_wfv)
print("Test MAE (walk forward validation):", round(test_mae, 2))


    
y_pred_wfv.name = "prediction"
y_pred_wfv.index.name = "timestamp"
y_pred_wfv.head()