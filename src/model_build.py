import pandas as pd
import numpy as np
import os
import sklearn
import yaml

from sklearn.ensemble import RandomForestClassifier
import pickle

def load_params(params_path : str) -> float:
    try:
        with open(params_path, 'r') as file:
            params = yaml.safe_load(file)
        return params['model_building']['n_estimators']
    except Exception as e:
        raise Exception(f"Error Loading parameters from {params_path} : {e}")

#n_estimators = yaml.safe_load(open("params.yaml", 'r'))["model_building"]['n_estimators']       

def load_data(filepath: str) -> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error Loading Data from {filepath}: {e}")
#train_data = pd.read_csv('./data/processed/train_processed.csv')

# x_train = train_data.iloc[:, 0:-1].values
# y_train = train_data.iloc[:, -1].values

def prepare_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    try:
        X = data.drop(columns=['Potability'], axis=1)
        y = data['Potability']
        return X, y
    except Exception as e:
        raise Exception(f"Error Preparing Data: {e}")
    
# x_train = train_data.drop(columns=['Potability'], axis=1)
# y_train = train_data['Potability']

def train(x: pd.DataFrame, y: pd.DataFrame, n_estimators: int) -> RandomForestClassifier:
    try:
        clf = RandomForestClassifier(n_estimators=n_estimators)
        clf.fit(x, y)
        return clf
    except Exception as e:
        raise Exception(f"Error training model : {e}")
    
def save_model(model: RandomForestClassifier, filepath: str) -> None:
    try:
         #save
        with open(filepath, "wb") as file:
            pickle.dump(model, file)

    except Exception as e:
        raise Exception(F"Error saving model to {filepath}: {e}")
    
def main():
    try:
        params_path  = "params.yaml"
        data_path = "./data/processed/train_processed.csv"
        model_name = "model.pkl"

        n_estimators = load_params(params_path)
        train_data = load_data(data_path)
        x_train, y_train = prepare_data(train_data)

        model = train(x_train, y_train, n_estimators)
        save_model(model, model_name)
    except Exception as e:
        raise Exception(f"An error occured : {e}")
    
if __name__ == "__main__":
    main()