{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO8xs1XJG3U/5d4jZS7uD9h"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "qQ-twfWj_TGE"
      },
      "outputs": [],
      "source": [
        "from flask import Flask, jsonify\n",
        "import gdown\n",
        "app = Flask(__name__)\n",
        "\n",
        "@app.route('/run-colab')\n",
        "def run_colab():\n",
        "    gdown.download('https://colab.research.google.com/drive/17pTDTimDnuDEMlBN62mXA8YC1Mkht2IP', 'colab.ipynb', quiet=False)\n",
        "    return jsonify(message='colab notebook ran successfully')"
      ]
    }
  ]
}
