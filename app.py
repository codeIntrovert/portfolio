from flask import Flask, render_template, jsonify

from main import get_nifty50, get_sensex, get_financial_news_headline, get_random_quote
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    update = '<body style="background: black; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0;"><h1 style="color: white; font-size: 8rem;">This Page Is Under Construction</h1>'
    return update

@app.route('/billu')
def attend():
    formatted_date_time = datetime.now().strftime("Today %d %B, %I:%M %p")
    nifty50 = get_nifty50()
    sensex = get_sensex()
    headline = get_financial_news_headline()
    quote = get_random_quote()
    return render_template('index.html', formatted_date_time=formatted_date_time, nifty50=nifty50, sensex=sensex, headline=headline, quote=quote)

@app.errorhandler(404)
def page_not_found(e):
    # Render the 404.html template with the 404 status code
    html404 = '<body style="background: black; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0;"><h1 style="color: white; font-size: 10rem;">404</h1>'
    return html404, 404


if __name__ == '__main__':
    app.run()
