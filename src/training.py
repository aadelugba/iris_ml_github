from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier, export_text, plot_tree
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.model_selection import KFold,train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import _tree
import numpy as np
from matplotlib import pyplot as plt


class BasicModel:
    '''
    Class for creating a base model

    Input Params:
        Pandas df
        String indicating model
        Params dictionary to be unpacked
    '''

    def __init__(self, df, model='rf', **params):
        self.df = df
        self.params = params
        if model == 'dt':
            self.model = DecisionTreeClassifier(**self.params)
        elif model == 'svc':
            self.model = SVC(**self.params)
        elif model == 'et':
            self.model = ExtraTreeClassifier(**self.params)
        elif model == 'gp':
            self.model = GaussianProcessClassifier(**self.params)
        elif model == 'rf':
            self.model = RandomForestClassifier(**self.params)
        elif model == 'knn':
            self.model = KNeighborsClassifier(**self.params)
        elif model == 'lr':
            self.model = LogisticRegression(**self.params)  


    def fit(self, X, y):
        '''
        Fit function to fit model to Training Set
        '''

        pipelines = transformation_pipeline(self.model)

        self.trained_model = pipelines.fit(X, y)
    
    def predict(self, X):
        '''
        Predict function to predict the Response/Dependent variable based on the Regressor/Explanatory/Independent/Manipulated/Predictor imputted.

        Input Params:
            X_test attribute of class instantiated
        
        Return Value:
            Predicted values
        '''

        predictions = self.trained_model.predict(X)

        return predictions