# -*- coding: utf-8 -*-


import os
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import csv
#import json
from pandas import  ExcelWriter
#import openpyxl


data = {}

'''
def extract_android(folder, file):
    try:
        path = os.path.join(folder, file)
        with open(path) as f:
            r = f.read()
            f.close()

            soup = BeautifulSoup(r, "lxml")
            # print type(soup)
            #
            # print soup.prettify()
            folder_name = os.path.basename(os.path.normpath(folder)).split('-')
            # print folder_name

            file_name = file.split('_')[0:2]
            # print  file_name

            key = str(datetime.datetime(int(folder_name[0]), int(folder_name[1]), int(folder_name[2]),
                                    int(file_name[0]), int(file_name[1]), 0))
            #print  key
            if key not in data:
                data[key] = {}

            android_avg_rating = soup.find("div", {"class": "score"})
            # print (avg_rating.get_text())
            data[key]["android_avg_rating"] = float(android_avg_rating.get_text())

            android_total_ratings = soup.find("span", {"class": "reviews-num"})
            # print (total_ratings.get_text())
            data[key]["android_total_ratings"] = int(android_total_ratings.get_text().replace(",",""))

            android_rating_ = soup.find_all("div", {"class": "rating-bar-container"})
            # print (rating_hists.get_text())

            for rating_hist in android_rating_:
                value = rating_hist.get_text().strip().split()
                # print value[0]
                # print value[1]

                data[key]["android_rating_" + value[0]] = int(value[1].replace(",",""))

            android_file_size = soup.find("div", {"itemprop": "fileSize"})
            # print (file_size.get_text())
            data[key]["android_file_size"] = int(android_file_size.get_text().replace(" ","")[:-1])

            #print data


    except:
        print "error"
'''
'''
def extract_ios(folder, file):
    try:
        path = os.path.join(folder, file)
        with open(path) as f:
            r = f.read()
            f.close()

            soup = BeautifulSoup(r, "lxml")

            folder_name = os.path.basename(os.path.normpath(folder)).split('-')
            # print folder_name

            file_name = file.split('_')[0:2]
            # print  file_name

            key = str(datetime.datetime(int(folder_name[0]), int(folder_name[1]), int(folder_name[2]),
                                    int(file_name[0]), int(file_name[1]), 0))
            # print  key
            if key not in data:
                data[key] = {}

            ios_current_ratings = soup.find("span", {"itemprop": "reviewCount"})
            # print (ios_current_ratings.get_text())
            data[key]["ios_current_ratings"] = int(ios_current_ratings.get_text().split()[0])

            ios_all_ratings = soup.find_all("span", {"class": "rating-count"})
            data[key]["ios_all_ratings"] = int(ios_all_ratings[1].get_text().strip('Ratings'))

            ios_file_size1 = soup.find("ul", {"class": "list"})
            ios_file_size = ios_file_size1.findAll("li")
            data[key]["ios_file_size"] = int(ios_file_size[4].get_text().strip('Size: MB'))

            #print data
    except:
        print "error"
'''
'''
def file_extract(folder,file):
    if file.endswith("android.html"):
        extract_android(folder,file)

    #if file.endswith("ios.html"):
        #extract_ios(folder,file)
    #
    #




def data_extract(folder):
    files = [f for f in os.listdir(folder)]
    # print files
    for f in files:
    # check if folder
        path = os.path.join(folder,f)
        if os.path.isdir(path):
           #print path
           data_extract(path)
        else:
           file_extract(folder,f)

        # if file check for last
        # file data extract logic
data_extract('data/')
'''


#for k,v in data.items():
#print k,v

#CSV File

'''
#CSV File
filename = 'Data.csv'
df.to_csv(filename, index=True, encoding='utf-8')
#print df


#XLS File

filename1 = 'Data.xlsx'
writer = ExcelWriter(filename1)
df.to_excel(writer,'Sheet1')
writer.save()

# JSON File
filename2 = 'Data.json'
df.to_json(filename2 , orient="index")


#Neat JSON
with  open("Data1.json","w") as write_json:
    json.dump(df,write_json,indent=4)



#Avg = df.mean(numeric_only= True)
#print Avg


#
# files = [f for f in os.listdir('./pokemon_5378')]
# for f in files:
#         print f
'''
#with open('Originaldata.csv', 'rb') as f:
    #reader = csv.reader(f)
    
df = pd.read_csv('Android.csv')
df1 = pd.read_csv('Dataios.csv')

df2 = pd.read_csv('Originaldata.csv')
df2.describe()
#scatter matrix plot
scatter_matrix(df2, figsize=(40,40))

#ridge_regression
array = df.values
array1 = df1.values
from sklearn import linear_model
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
x = array[:,3:10]
y = array[:,2]
x1 = array1[:,[1,3]]
y1 = array1[:,2]
seed = 1
kfold = KFold(n_splits = 3, random_state = 1)
#android & ios prediction row
android_predict = df.iloc[-1,3:]
ios_predict = df1.iloc[-1,[1,3]]
model = linear_model.Ridge()
model1 = linear_model.Ridge()
model.fit(x,y)
model1.fit(x1,y1)
results = cross_val_score(model,x,y, cv=kfold)
android_prediction_rating = model.predict(android_predict)
ios_prediction_rating = model1.predict(ios_predict)
#android & ios total rating prediction
print android_prediction_rating
print ios_prediction_rating
#Handling Na's
'''
df.fillna(method='ffill',inplace=True)
df.to_csv('Test.csv',index=True,encoding ='utf-8')
df1.fillna(method='ffill',inplace=True)
df1.to_csv('ios.csv',index=True,encoding ='utf-8')
df2.fillna(method='ffill',inplace=True)
df2.to_csv('Originaldata.csv',index=True,encoding ='utf-8')
'''
#Pearson's Coefficient
correlation1 = np.corrcoef(df2['android_total_ratings'],df2['ios_all_ratings'])
correlation2 = np.corrcoef(df2['android_total_ratings'],df2['android_rating_1'])
correlation3 = np.corrcoef(df2['android_total_ratings'],df2['android_rating_4'])
correlation4 = np.corrcoef(df2['android_total_ratings'],df2['android_rating_5'])
correlation5 = np.corrcoef(df2['android_total_ratings'],df2['android_rating_2'])
correlation6 = np.corrcoef(df2['android_total_ratings'],df2['android_rating_3'])
correlation7 = np.corrcoef(df2['ios_all_ratings'],df2['android_rating_1'])
correlation8 = np.corrcoef(df2['ios_all_ratings'],df2['android_rating_2'])
correlation9 = np.corrcoef(df2['ios_all_ratings'],df2['android_rating_3'])
correlation10 = np.corrcoef(df2['ios_all_ratings'],df2['android_rating_4'])
correlation11 = np.corrcoef(df2['ios_all_ratings'],df2['android_rating_5'])
correlation12 = np.corrcoef(df2['android_rating_1'],df2['android_rating_2'])
correlation13 = np.corrcoef(df2['android_rating_1'],df2['android_rating_3'])
correlation14 = np.corrcoef(df2['android_rating_1'],df2['android_rating_4'])
correlation15 = np.corrcoef(df2['android_rating_1'],df2['android_rating_5'])
correlation16 = np.corrcoef(df2['android_rating_4'],df2['android_rating_3'])
correlation17 = np.corrcoef(df2['android_rating_4'],df2['android_rating_2'])
correlation18 = np.corrcoef(df2['android_rating_4'],df2['android_rating_5'])
correlation19 = np.corrcoef(df2['android_rating_5'],df2['android_rating_2'])
correlation20 = np.corrcoef(df2['android_rating_5'],df2['android_rating_3'])
correlation21 = np.corrcoef(df2['android_rating_2'],df2['android_rating_3'])


