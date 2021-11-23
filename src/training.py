from functions import BasicModel
from sklearn.linear_model import LogisticRegression
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from joblib import dump

curr_path = os.getcwd().replace('''\\''' ,"/")
dataset = pd.read_csv(curr_path +  "/dataset/iris.csv")
X = dataset.drop('species', axis=1).values
y = dataset['species'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)


# model = BasicModel(dataset, model=None, max_iter = 100)

# model.fit(X_train, y_train)
# # y_pred = model.predict(X_test)
# # print(model.scoring(X_test, y_pred))

model = LogisticRegression()

model.fit(X_train, y_train)

dump(model, 'trained_model/model.joblib')
