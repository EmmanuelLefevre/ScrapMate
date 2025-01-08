import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json


# Initialiser application Flask
app = Flask(__name__)


# Application de CORS (middleware)
CORS(app, resources={
    r"/api/scrap": {
        "origins": "*",
        "methods": ["POST"]
    }
})


# Scrapper la page
@app.route('/api/scrap', methods=['POST'])
def scrap_page():
  