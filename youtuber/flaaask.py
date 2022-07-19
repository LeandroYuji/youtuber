from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        link = request.form.get('name')
        yt = YouTube(link)
        if request.form.get('Áudio') == 'Áudio':
            # pass
            yt.streams.filter(only_audio=True)[0].download()
        elif request.form.get('Vídeo') == 'Vídeo':
            # pass # do something else
            yt.streams.get_highest_resolution().download()
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
