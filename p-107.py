import csv
import plotly.express as px
import pandas as pd

read = pd.read_csv('data.csv')

mean  = read.groupby(['student_id','level'], as_index = False )['attempt'].mean()
fig = px.scatter(mean,x= 'student_id', y = 'level', size= 'attempt', color='attempt')
fig.show()