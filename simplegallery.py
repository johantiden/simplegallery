from flask import Flask, send_from_directory
from jinja2 import Template
from pathlib import Path
import os

workingDir = os.getcwd()

app = Flask(
    __name__
)

def listImages():


    fileTypes = ['*.png', '*.jpg', '*.gif', '*.webp']
    images = [f for f_ in [Path('').rglob(e) for e in fileTypes] for f in f_]
    for filepath in images:
        print(filepath)
    return images

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(workingDir, path)

@app.route('/')
def index():
    images = listImages()
    t = Template(
        '''
        <html>
            <head>
                <title>Temporary image server</title>
                <style>
                    body {
                        background-color: #DDDDDD
                    }
                    a {
                        color: black;
                    }
                    p {
                        font-size: xx-small;
                    }
                    img {
                        box-shadow: 2px 2px 5px #444444;
                        background-color: white
                    }
                    .imageBox {
                        display: inline-block;
                     }
                </style>
            </head>
            <body>
                <div><h1>Serving {{ images|length }} images from {{ workingDir }}</div>
                
                {% for image in images %}
                <div class="imageBox">
                    <a href="{{ image }}">
                        <img src="{{ image }}" height="200"/>
                        <p>{{ image }}</p>
                    </a>
                </div>
                {% endfor %}
            </body>
        </html>
        '''
    )
    return t.render(images=images, workingDir=workingDir)




if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=80)

