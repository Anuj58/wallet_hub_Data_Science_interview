import pickle
from math import sqrt
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor 
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    ### Loading the model and other files ###
    
    xgb=pickle.load( open("/home/anuj/model.pkl", 'rb'))
    norm_values=pickle.load(open("/home/anuj/norm_values.pkl",'rb'))
    del norm_values["x001"]
    columns=pickle.load(open("/home/anuj/columnsTrain.pkl",'rb'))
    col=pickle.load(open("/home/anuj/genuineCol.pkl",'rb'))
    categorical_variables=pickle.load(open("/home/anuj/catvariables.pkl",'rb'))

    ### Reading the input from command line ####
    input=pd.read_csv(sys.argv[1])
#     print (input.head(2))
    
    ### Removing unwanted features ###
    input=input[col]

    ### Feature Engineering- categorical -onhot encoded ###
    input_cat = input[categorical_variables]
    # Do the one Hot encoding of the categorical features
    input_cat_encoded = pd.get_dummies(input_cat, columns = categorical_variables)
    
    ### Feature Engineering- Continous -z value###
    input_tmp=input.drop(['x001'], 1)
    input_cont = input_tmp.drop(categorical_variables,1)
    input_cont.fillna(norm_values.loc["mean"], inplace=True)
    input_cont_normalized = input_cont - norm_values.loc["mean"]
    input_cont_normalized = input_cont_normalized/norm_values.loc["std"]
    
    ### Feature Engineering- merging categorical and continous variable ###
    input_X= pd.concat([input['x001'],input_cat_encoded,input_cont_normalized],axis =1)
    
    ### Treatment for missing feature from training model ###
    missing_cols=set(columns)-set( input_X.columns ) 
    feature_difference_df_tmp =pd.DataFrame(norm_values.loc["mean"]).T
    feature_difference_df=feature_difference_df_tmp[missing_cols]
    # feature_difference_df = pd.DataFrame(data=np.zeros((input_X.shape[0], len(missing_cols))),
    #                                  columns=list(missing_cols))
    ids=input_X['x001']
    input_X = input_X.join(feature_difference_df)
    input_X=input_X[columns]
    input_X.fillna(0, inplace=True)
    
    ### Executing the model ###
    predictions = xgb.predict(input_X)
    output=pd.DataFrame(ids)
    output.columns=["x001"]
    output["predictions"] = predictions
    
    ### writing the output ###
    output.to_csv("./output.csv",index=False)

