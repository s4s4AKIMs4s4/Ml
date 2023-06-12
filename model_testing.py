import pandas as pd

df=pd.read_csv("test/test_preprocessing.csv")

X=df.drop("price", axis=1)
y=df.price

import pickle

filename = 'final_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X,y)
print(result)