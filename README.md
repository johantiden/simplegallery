# simplegallery

Serves image files from the current directory and presents them in a simple listing page.

## Prerequisites
* A working installation of python
* Python pip

## Installation
1. Download the `simplegallery.py` file and put it somewhere memorable e.g. `~/bin`
2. Install required dependency flask if you don't already have it.
```
pip install flask
```

## Usage
Go to a folder you would like to share e.g. `/srv/share/example` and just run the python file!
```
cd /srv/share/example
python ~/bin/simplegallery.py
```
All images in the given folder will be served as a web page at port 80 `http://localhost`.


![example](https://raw.githubusercontent.com/johantiden/simplegallery/master/readme/example.jpg)
