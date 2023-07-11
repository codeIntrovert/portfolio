from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    data = [ # keep it in multiples of 4 for optimal design
        ('Project 1', 'Illustration', '#','portfolio-1.jpg'),
        ('Project 2', 'Branding', '#','portfolio-2.jpg'),
        ('Project 3', 'Design', '#','portfolio-3.jpg'),
        ('Project 4', 'Marketing', '#','portfolio-4.jpg'),
        ('Project 5', 'Marketing', '#','portfolio-5.jpg'),
        ('Project 6', 'Illustration', '#','portfolio-6.jpg'),
        ('Project 7', 'Branding', '#','blog-1.jpg'),
        ('Project 8', 'Design', '#','user-3.jpg'),
        #('Name', 'Type/Description','link','imageName')
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
    html404 = '<body style="background: black; font-family: Arial, Helvetica, sans-serif; display: flex; align-items: center; justify-content: center; margin-top: -50px;"><h1 style="color: white; font-size: 5rem;">404: Page Not Found :(</h1>'
    return html404, 404


if __name__ == '__main__':
    app.run()
