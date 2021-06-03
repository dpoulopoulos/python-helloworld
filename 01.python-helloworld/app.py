import json
import logging

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("ssss")

    return "Hello World!"


@app.route("/status")
def status():
    app.logger.info("Status endpoint was reached.")

    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json')

    return response


@app.route("/metrics")
def metrics():
    app.logger.info("Metrics endpoint was reached.")

    response = app.response_class(
        response=json.dumps({"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json')

    return response


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="app.log")
    app.run(host='0.0.0.0')
