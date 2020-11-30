import csv
import plotly.express as px
import numpy as np

def plot():
    with open('Student Marks vs Days Present.csv') as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Marks In Percentage', y = 'Days Present')
        fig.show()
def getData(data_path):
    size_of_tv = []
    average_time = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            size_of_tv.append(float(row['Marks In Percentage']))
            average_time.append(float(row['Days Present']))
        return {'x' : size_of_tv, 'y' : average_time}
def correlation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print('The correlation for the given data is ', correlation[0,1])
def setup():
    data_path = 'Student Marks vs Days Present.csv'
    datasource = getData(data_path)
    correlation(datasource)
    plot()

setup()