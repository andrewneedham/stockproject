from bokeh.plotting import figure, output_notebook, show
from bokeh import embed
import requests
import pandas as pd
from bokeh.palettes import Spectral11
from bokeh.embed import components
from flask import Flask,render_template,request,redirect,session
from bokeh.charts import Histogram
import numpy as np
import bokeh.charts as bc
from bokeh.resources import CDN

app = Flask(__name__)

app.vars={}


@app.route('/')
def main():
  return redirect('/index')


@app.route("/")
def visualisation():
 # Build the dataframe
 df = pd.DataFrame({
 'x': 2*np.pi*i/100,
 'sin': np.sin(2*np.pi*i/100),
 'cos': np.cos(2*np.pi*i/100),
 } for i in range(0,101))

 # Create the plot
 plot = bc.Line(title='Triganometric fun!',
 data=df, x='x', ylabel='y')

 # Generate the script and HTML for the plot
 script, div = components(plot)

 # Return the webpage
 return """
<!doctype html>
<head>
 <title>My wonderful trigonometric webpage</title>
 {bokeh_css}
</head>
<body>
 <h1>Everyone loves trig!
 {div}

 {bokeh_js}
 {script}
</body>
 """.format(script=script, div=div, bokeh_css=CDN.render_css(),
 bokeh_js=CDN.render_js())

if __name__ == '__main__':
    app.run(port=33507)
