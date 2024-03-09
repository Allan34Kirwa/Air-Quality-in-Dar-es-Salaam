from Airquality.library import AutoReg, mean_absolute_error, time, pd
from Airquality.split import y_train

# Create range to test different lags
p_params = range(1, 31)

# Create empty list to hold mean absolute error scores
maes = []

# Iterate through all values of p in `p_params`
for p in p_params:
    
    # start timing
    start_time = time.time()
    # Build model
    model = AutoReg(y_train, lags=p).fit()
    
    # Calcuulate elapsed timing
    elapsed_time = round(time.time() - start_time, 2)
    print(f"Trained AutoReg Model {p} in {elapsed_time}seconds")
    
    # Make predictions on training data, dropping null values caused by lag
    y_pred = model.predict().dropna()

    # Calculate mean absolute error for training data vs predictions
    mae = mean_absolute_error(y_train.iloc[p:], y_pred)

    # Append `mae` to list `maes`
    maes.append(mae)

# Put list `maes` into Series with index `p_params`
mae_series = pd.Series(maes, name="mae", index=p_params)

# Inspect head of Series
mae_series.head()