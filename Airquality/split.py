from Airquality.wrangle import y

# Split y into training and test sets.
cutoff_test = int(len(y) * 0.9)
y_train = y.iloc[:cutoff_test]
y_test = y.iloc[cutoff_test:]
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)