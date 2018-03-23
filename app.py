import requests
import pandas
import simplejson as json
from bokeh.plotting import figure
from bokeh.palettes import Spectral11
from bokeh.embed import components 
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

def TICKER():
    r = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=M3p5d4UYShekAzwokawN')
    x = r.json()
    df = pd.DataFrame(x)
    s=df.iloc[3:4, 0:1]
    newdf=df.iloc[3:4, 0:1]
    df2 = newdf['dataset_data'].apply(pd.Series)
    df3 = df2.T
    df4=df3
    df4['data']= df4['data'].astype(str)
    df4.columns = ['all']
    df5 = df4['all'].str.split(',\s+', expand=True)
    column_namesdf=df.iloc[2:3, 0:1]
    column_names = column_namesdf['dataset_data'].values.tolist()
    df5.columns = (column_names)
    df6=df5
    df6['Date'] = df6['Date'].str.replace(r"[\',\[']", '')
    df6['Adj. Volume'] = df6['Adj. Volume'].str.replace(r"[\',\]']", '')
    df6['Date'] = pd.to_datetime(df6['Date'])
    output_file("datetime.html")
    p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
    p.line(df6['Date'], df6['Close'], color='navy', alpha=0.5)
    return show(p)


@app.route('/index', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/bokeh')
def bokeh():

    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure(plot_width=600, plot_height=600)
    fig.vbar(
        x=[1, 2, 3, 4],
        width=0.5,
        bottom=0,
        top=[1.7, 2.2, 4.6, 3.9],
        color='navy'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)

if __name__ == '__main__':
    app.run(port=33507)
