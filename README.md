# Docker Dragnet

Set up a basic [Flask](http://flask.pocoo.org/) server for [Dragnet](https://github.com/dragnet-org/dragnet)

Usage:
- Set up Docker container (exposes port 5000 by default)
- POST a web request body (with header `content-type: text/plain`) to either `/content` or `/content-comments`
