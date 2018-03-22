from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')


# coding: utf-8

# ##Milestone Project: Clone the Flask Demo repository and create your own Flask app on Heroku 
# that accepts a stock ticker input from the user and plots closing price data for the last month. 
# The Quandle WIKI dataset provides this data for free, and you can use Python's Requests library along
# with simplejson to access it in Python via API. You can analyze the data using pandas and plot using
# Bokeh. By the end you should have some kind of interactive visualization viewable from the Internet.

# In[11]:

import pandas as pd
import bokeh
import flask
import pip
import requests
import simplejson as json


# My API from quandl is M3p5d4UYShekAzwokawN so let's try

# In[16]:

r = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=M3p5d4UYShekAzwokawN')
x = r.json()
print(x)


# In[ ]:




# In[87]:

df = pd.DataFrame(x)
df.head()


# In[88]:

s=df.iloc[3:4, 0:1]
print(s)


# In[89]:

newdf=df.iloc[3:4, 0:1]
newdf.head()


# In[ ]:




# In[90]:

df2 = newdf['dataset_data'].apply(pd.Series)
df2.head()


# In[98]:

df3 = df2.T
print(df3)




# In[101]:

df4=df3
df4['data']= df4['data'].astype(str)
df4.columns = ['all']
df4.head()


# In[110]:

df5 = df4['all'].str.split(',\s+', expand=True)
df5.head()


# In[ ]:




# In[ ]:




# In[113]:

column_namesdf=df.iloc[2:3, 0:1]
column_names = column_namesdf['dataset_data'].values.tolist()
print(column_names)


# In[114]:

df5.columns = (column_names)
df5.head()


# In[117]:

df6=df5
df6['Date'] = df6['Date'].str.replace(r"[\',\[']", '')
df6['Adj. Volume'] = df6['Adj. Volume'].str.replace(r"[\',\]']", '')
df6.head()


# In[125]:

df6['Date'] = pd.to_datetime(df6['Date'])


# In[ ]:




# In[126]:

from bokeh.plotting import figure, output_file, show, output_notebook

output_file("datetime.html")
output_notebook()

# create a new plot with a datetime axis type
p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")

p.line(df6['Date'], df6['Close'], color='navy', alpha=0.5)

show(p)


#

if __name__ == '__main__':
  app.run(port=33507)
