from flask import Flask, request, Response, render_template, jsonify
import data
import time
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/hiphop", methods=["POST"])
def hiphop():
    context = request.form['context']
    loaded_data = data.hiphop_text(context)
    return loaded_data

# Health Check
@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)