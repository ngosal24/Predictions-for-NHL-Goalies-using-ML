import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

goalieData = pd.read_csv("data.csv", header = 0)

# create linear regressions for the three most important features of the model
X_sv_pct = goalieData[['sv_pct']]
y = goalieData['next_sv_pct']

X_rebounds = goalieData[['rebounds']]

X_blocked_shots = goalieData[['blocked_shot_attempts']]

sv_pct_reg = linear_model.LinearRegression().fit(X_sv_pct,y)
rebounds_reg = linear_model.LinearRegression().fit(X_rebounds,y)
blocked_shots_reg = linear_model.LinearRegression().fit(X_blocked_shots,y)

y_pred_sv_pct = sv_pct_reg.predict(X_sv_pct)
y_pred_rebounds = rebounds_reg.predict(X_rebounds)
y_pred_blocked_shots = blocked_shots_reg.predict(X_blocked_shots)

print("Coefficient of determination for save percentage: %.5f" % r2_score(y, y_pred_sv_pct))
print("Coefficient of determination for rebounds allowed: %.5f" % r2_score(y, y_pred_rebounds))
print("Coefficient of determination for blocked shots: %.5f" % r2_score(y, y_pred_blocked_shots))

plt.figure(figsize=(24, 8))

# plot sv% regression
plt.subplot(1, 3, 1)
plt.scatter(X_sv_pct, y, color='black')
plt.plot(X_sv_pct, y_pred_sv_pct, color='blue')
plt.title("sv% vs Next Season's sv%")
plt.xlabel('sv%')
plt.ylabel('next sv%')


# plot rebounds regression
plt.subplot(1, 3, 2)
plt.scatter(X_rebounds, y, color='black')
plt.plot(X_rebounds, y_pred_rebounds, color='blue')
plt.title("Rebounds Allowed vs Next Season's sv%")
plt.xlabel('rebounds')
plt.ylabel('next sv%')

# plot blocked shots regression
plt.subplot(1, 3, 3)
plt.scatter(X_blocked_shots, y, color='black')
plt.plot(X_blocked_shots, y_pred_blocked_shots, color='blue')
plt.title("Blocked Shots vs Next Season's sv%")
plt.xlabel('blocked shots')
plt.ylabel('next sv%')

plt.show()
