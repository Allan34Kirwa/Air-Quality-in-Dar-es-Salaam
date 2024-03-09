from Airquality.library import AutoReg
from Airquality.split import y_train
from Airquality.iterating import p

# Determiningthe best model
best_p = 5

best_model = AutoReg(y_train, lags=p).fit()