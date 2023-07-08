from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    data = [ # keep it in multiples of 4 for optimal design
        ('Project 1', 'Illustration', '#'),
        ('Project 2', 'Branding', '#'),
        ('Project 3', 'Design', '#'),
        ('Project 4', 'Marketing', '#'),
        ('Project 5', 'Marketing', '#'),
        ('Project 6', 'Illustration', '#'),
        ('Project 7', 'Branding', '#'),
        ('Project 8', 'Design', '#'),
    ]

    links = {
        'spotify': "https://open.spotify.com/embed/track/2tpWsVSb9UEmDRxAl1zhX1?utm_source=generator",
        'twitter': "https://twitter.com/@HasanMonke",
        'github': "https://github.com/codeintrovert",
        'linkedin': "https://linkedin.com/in/introvertCoder/",
        'youtube': "https://youtube.com/introvertcoder",
        'songcreator' : "ONE REPUBLIC"
    }

    return render_template('index.html', links=links, data=data)

@app.errorhandler(404)
def page_not_found(e):
    # Render the 404.html template with the 404 status code
    html404 = '<body style="background: black; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0;"><h1 style="color: white; font-size: 10rem;">404</h1>'
    return html404, 404


if __name__ == '__main__':
    app.run()
