from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,BaggingClassifier
from xgboost import XGBRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pandas as pd
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df=pd.read_csv("train/train_preprocessing.csv")

X=df.drop("price", axis=1)
y=df.price

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2, shuffle = True)
xgr = XGBRegressor(random_state=43)

xgr = XGBRegressor(gamma= 0, learning_rate=0.1, max_depth=7, min_child_weight=1, n_estimators=100)
xgr = xgr.fit(x_train, y_train)

test_predictions = xgr.predict(x_test)

mse = mean_squared_error(y_test, test_predictions)
r2 = r2_score(y_test, test_predictions)

print(f"Mean Squared Error: {mse:.3f}")
print(f"R-squared: {r2:.3f}")

filename = 'final_model.sav'
pickle.dump(xgr, open(filename, 'wb'))

