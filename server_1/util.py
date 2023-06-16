import json
import pickle
import pandas as pd
import numpy as np

__category = None
__data_columns = None
__model = None

def get_category_names():
    load_saved_artifacts()
    return __category


import csv


# Function to retrieve brands based on the selected category
def get_brands(category):
    brands_list = []

    with open('./artifacts/flipkart3 - flipkart3.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        df = pd.DataFrame(reader)

        # Print the first few rows
        print(df.head())

        selected_rows = df[df[2] == category]

        # Get the unique brands from the selected rows and append them to a list
        brands_list = selected_rows[6].unique().tolist()
        print(brands_list)
    return brands_list


def get_products(category,brand):
    products_list = []

    with open('./artifacts/flipkart3 - flipkart3.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        df = pd.DataFrame(reader)

        # Print the first few rows
        print(df.head())

        selected_rows = df[(df[2] == category) & (df[6] == brand)]

        # Get the unique brands from the selected rows and append them to a list
        products_list = selected_rows[1].unique().tolist()
        # print(products_list)
    return products_list

def predict_price(pro_name,brand,category,discount):
     with open('./artifacts/encoded_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        enc_data = pd.DataFrame(reader)
        # print(enc_data.head())
        df_filtered = enc_data[(enc_data[10] == pro_name)&(enc_data[12] ==category ) &(enc_data[11] == brand)]
        # print(df_filtered)
        first_row_first_10 = df_filtered.values[0][:10].tolist()
        x=np.zeros(17)
        x[0]=first_row_first_10[0]
        x[1]=first_row_first_10[1]
        x[2]=first_row_first_10[2]
        x[3]=first_row_first_10[3]
        x[4]=first_row_first_10[4]
        x[5]=first_row_first_10[5]
        x[6]=first_row_first_10[6]
        x[7]=first_row_first_10[7]
        x[8]=first_row_first_10[8]
        x[9]=first_row_first_10[9]
        with open('./artifacts/data.csv', 'r', encoding='utf-8') as file:
              reader = csv.reader(file)
              data= pd.DataFrame(reader)
              filtered_df = data.loc[(data[0] == first_row_first_10[0]) & (data[1] == first_row_first_10[1]) & (data[2] == first_row_first_10[2]) & (data[3] == first_row_first_10[3]) & (data[4] == first_row_first_10[4]) & (data[5] == first_row_first_10[5]) & (data[6] == first_row_first_10[6]) & (data[7] == first_row_first_10[7]) & (data[8] == first_row_first_10[8]) & (data[9] == first_row_first_10[9])]
              # print(filtered_df.head())

              retail_price = filtered_df[10].iloc[0]
              print(retail_price)
              dis_per=((int(retail_price) - int(discount)) / int(retail_price)) * 100
              # print(retail_price)
              # print(dis_per)
              x[10]=discount
              x[11]= 4
              x[12]= dis_per
              x[13]= 0
              x[14]= 10
              x[15]= 1
              x[16]= 2021
              with open("./artifacts/lgbm_model.pkl", 'rb') as f:
                model = pickle.load(f)
     return model.predict([x])[0],dis_per,int(retail_price)

def load_saved_artifacts():
    print("Loading the saved artifacts")
    global __data_columns
    global __category
    global __model
    with open("./artifacts/category.json",'r') as f:
        __data_columns=json.load(f)['categories']
        __category=__data_columns[:]
    with open("./artifacts/lgbm_model.pkl",'rb') as f:
        __model=pickle.load(f)
    print("loading of saved artifacts...done")
if __name__ == "__main__":
    load_saved_artifacts()
    print(get_category_names())
    print(predict_price("3a AUTOCARE Car Mat Chevrolet Beat",'3a AUTOCARE','''["Automotive >> Accessories & Spare parts >> Car Interior & Exterior >> Car Interior >> Car Mats"]''',1490))
    # get_brands(category)
    # print(estimated_price('1st Phase JP Nagar',1000,2,2,2))
    # print(estimated_price('Indira Nagar',1000,2,1,2))
    # print(estimated_price('Indira Nagar',1000,3,1,3))
    # print(estimated_price('1st Phase JP Nagar',1000,3,2,3))
    # app.run()