from bokeh.plotting import figure, output_notebook, show
from bokeh import embed
import requests
import pandas as pd
from bokeh.palettes import Spectral11
from bokeh.embed import components
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
from bokeh.charts import Histogram
from bokeh.embed import components

app = Flask(__name__)

# Load the  Data Set
df = pd.DataFrame({'A':[3, 5, 7],'B':[1, 12, 25],'C':[5, 20, 30]})
feature_names = df.columns[0:-1].values.tolist()

# Create the main plot
def create_figure(current_feature_name, bins):
	p = Histogram(df, current_feature_name, title=current_feature_name, 
	 	bins=bins, legend='top_right', width=600, height=400)

	# Set the x axis label
	p.xaxis.axis_label = current_feature_name

	# Set the y axis label
	p.yaxis.axis_label = 'Count'
	return p

# Index page
@app.route('/')
def index():
	# Determine the selected feature
	current_feature_name = request.args.get("feature_name")
	if current_feature_name == None:
		current_feature_name = "A"

	# Create the plot
	plot = create_figure(current_feature_name, 1)
		
	# Embed plot into HTML via Flask Render
	script, div = components(plot)
	return render_template("iris_index1.html", script=script, div=div,
		feature_names=feature_names,  current_feature_name=current_feature_name)


if __name__ == '__main__':
    app.run(port=33507)
