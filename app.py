from flask import Flask, render_template
from bokeh.plotting import figure, output_notebook, show
from bokeh import embed
import requests
import pandas
from bokeh.plotting import figure
from bokeh.palettes import Spectral11
from bokeh.embed import components
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Bokeh example</h1><a href=/graph>Go to plot page</a>'

def make_my_plot():
    a = 10
    # prepare some data
    x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    y0 = [i**2 for i in x]
    y1 = [a**i for i in x]
    y2 = [a**(i**2) for i in x]

    # create a new plot
    p = figure(
       tools="",
       y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
       x_axis_label='sections', y_axis_label='particles'
    )

    # add some renderers
    p.line(x, x, legend="y=x")
    p.circle(x, x, legend="y=x", fill_color="white", size=8)
    p.line(x, y0, legend="y=x^2", line_width=3)
    p.line(x, y1, legend="y=10^x")
    p.circle(x, y1, legend="y=10^x", size=6)
    p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

    # show the results
    return p

@app.route('/graph')
def hello():
script, div = components(plot)
return render_template('graph.html', script=script, div=div)
