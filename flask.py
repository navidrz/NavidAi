from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1k2AEHUm3kb9qsApvzQ4jtdJvspliwGA6', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
