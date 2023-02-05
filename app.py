from crypt import methods
from flask import Flask, jsonify, request
from firebase_admin import credentials, firestore, initialize_app
import add_test_data
from metrics import metrics
from ocr import scan_text
from difficulty import final_function



