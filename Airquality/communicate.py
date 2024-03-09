from Airquality.library import px, pd
from Airquality.evaluation import y_pred_wfv 
from Airquality.split import y_test

# # Create a line plot showing actual vs. predicted PM2.5 levels in Dar es Salaam using WFV
df_pred_test = pd.DataFrame({"y_test": y_test, "y_pred_wfv": y_pred_wfv})
fig = px.line(df_pred_test, labels={"value":"PM2.5"})
fig.update_layout(
    title="Dar es Salaam, WFV Predictions",
    xaxis_title="Date",
    yaxis_title="PM2.5 Level",df_pred_test = pd.DataFrame({"y_test": y_test, "y_pred_wfv": y_pred_wfv})
)

fig.show()