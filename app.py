from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH, start_server
import argparse

from flask import *
import pickle

import matplotlib.pyplot as plt

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


def predict():
    year = input("Enter Year", type=NUMBER)
    import_ = input("Import in millions", type=NUMBER)
    export_ = input("Export in millions", type=NUMBER)
    industrial_production = input("Industrial Production", type=FLOAT)
    inflation_rate = input("Inflation rate (%)", type=FLOAT)
    exchange_rate = input("Exchange rate (USD)", type=FLOAT)
    population = input("Population Growth Rate in %", type=FLOAT)
    stock_market = input("Stock market sales", type=FLOAT)
    unemployment = input("Unemployment rate (%)", type=FLOAT)
    sensex_index = input("Sensex Index(Gain/Loss)", type=FLOAT)
    prediction = model.predict([[year, import_, export_, industrial_production, inflation_rate, exchange_rate, population,
                                 stock_market, unemployment, sensex_index]])
    output_1 = round(prediction[0], 2)

    put_text('GDP increased from last year will be: ', output_1)
    years = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
             2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, year]
    gdp_Values = [1.06, 5.48, 4.75, 6.66, 7.57, 7.55, 4.05, 6.18, 8.85, 3.84, 4.82, 3.8, 7.86, 7.92, 7.92, 8.06, 7.66,
                  3.09, 7.86, 8.5, 5.24, 5.46, 6.39, 7.41, 8, 8.26, 7.04, 6.12, 4.18, output_1]
    plt.barh(years, gdp_Values, align='center')
    plt.savefig('fig_.png')
    img = open('fig_.png', 'rb').read()
    put_image(img)


app.add_url_rule('/', 'webio_view', webio_view(predict), methods=['GET', 'POST', 'OPTIONS'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(predict, port=args.port)

#app.run(host='localhost', port=80)
