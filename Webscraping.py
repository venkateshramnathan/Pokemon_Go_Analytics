import os
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import json
from pandas import  ExcelWriter
import openpyxl
import traceback


data = {}


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
            if android_avg_rating is not None:
                data[key]["android_avg_rating"] = float(android_avg_rating.get_text())
            else:
                data[key]["android_avg_rating"] = None


            android_total_ratings = soup.find("span", {"class": "reviews-num"})
            # print (total_ratings.get_text())
            if android_total_ratings is not None:
                data[key]["android_total_ratings"] = int(android_total_ratings.get_text().replace(",",""))
            else:
                data[key]["android_total_ratings"] = None


            android_file_size = soup.find("div", {"itemprop": "fileSize"})
            # print (file_size.get_text())
            if android_file_size is not None:
                data[key]["android_file_size"] = int(android_file_size.get_text().replace(" ","")[:-1])
            else:
                data[key]["android_file_size"] = None

            android_rating_ = soup.find_all("div", {"class": "rating-bar-container"})
            # print (rating_hists.get_text())

            for rating_hist in android_rating_:
                value = rating_hist.get_text().strip().split()
                # print value[0]
                # print value[1]

                data[key]["android_rating_" + value[0]] = int(value[1].replace(",", ""))



                        #print data
        print "Success in android file:" + str(folder) + "/" + str(file)

    except:
        print "error in android file : " +  str(folder) + "/" +  str(file)
        traceback.print_exc()


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
            if (ios_current_ratings is not None):
                data[key]["ios_current_ratings"] = int(ios_current_ratings.get_text().split()[0])
            else:
                data[key]["ios_current_ratings"] = None

            ios_all_ratings = soup.find_all("span", {"class": "rating-count"})
            if ios_all_ratings is not None:
                data[key]["ios_all_ratings"] = int(ios_all_ratings[1].get_text().strip('Ratings'))
            else:
                data[key]["ios_all_ratings"] = None

            ios_file_size1 = soup.find("ul", {"class": "list"})
            ios_file_size = ios_file_size1.findAll("li")
            if ios_file_size is not None:
                data[key]["ios_file_size"] = int(ios_file_size[4].get_text().strip('Size: MB'))
            else:
                data[key]["ios_file_size"] = None

            #print data
            print "Success in ios file:" + str(folder) + "/" + str(file)
    except:
        print "error in ios file : " + str(folder) + "/" + str(file)
        traceback.print_exc()


def file_extract(folder,file):
    if file.endswith("android.html"):
        extract_android(folder,file)

    if file.endswith("ios.html"):
        extract_ios(folder,file)






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
data_extract('pokemon_5378/data')



#for k,v in data.items():
#print k,v

#CSV File
df = pd.DataFrame.from_dict(data,orient='index',dtype=None)
#df = pd.read_csv("Data.csv")
s = df.describe()
print  s


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



s = df.describe()
print s




#
# files = [f for f in os.listdir('./pokemon_5378')]
# for f in files:
#         print f
