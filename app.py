from flask import Flask, render_template, jsonify

from main import get_nifty50, get_sensex, get_financial_news_headline, get_random_quote
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    formatted_date_time = datetime.now().strftime("Today %d %B, %I:%M %p")
    nifty50 = get_nifty50()
    sensex = get_sensex()
    headline = get_financial_news_headline()
    quote = get_random_quote()
    return render_template('index.html', formatted_date_time=formatted_date_time, nifty50=nifty50, sensex=sensex, headline=headline, quote=quote)

if __name__ == '__main__':
    app.run()
