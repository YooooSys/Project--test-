from flask import Flask, Response, render_template, request, jsonify
import subprocess
import os
app = Flask(__name__)

# Ensure the uploads directory exists
@app.route('/')
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)