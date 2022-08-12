import joblib
import pandas as pd

model = joblib.load('trained_model/model.joblib')

class Predict_Data:
      
    def __init__(self,data):
        self.data = data
        
    def predict(self):
        predict = model.predict(data)[0]
        print(f"This Species of the Flower is: {predict}\n")
                
if __name__ == "__main__":
    print("************************")
    print("Statup Iris Flower Prediction")
    print("************************\n\n")

    # sepal_length,sepal_width,petal_length,petal_width
    sepal_length = float(input('Enter Sepal Length: '))
    sepal_width = float(input('Enter Sepal Width: '))
    petal_length = float(input('Enter Petal Length: '))
    petal_width = float(input('Enter Petal Width: '))
    data = pd.DataFrame([sepal_length,sepal_width,petal_length,petal_width],index=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']).T
    obj = Predict_Data(data)
    obj.predict()