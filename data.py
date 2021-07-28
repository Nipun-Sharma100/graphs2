import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    sleepinhours=[]
    coffee=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleepinhours.append(float(row["sleep in hours"]))

        return{"x":sleepinhours,"y":coffee}

def findcorellation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation is ",correlation[0,1])

def setup():
    data_path="data4.csv"
    datasource=getDataSource(data_path)
    findcorellation(datasource)

setup()