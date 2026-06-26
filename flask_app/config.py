"""
Configuration file for Smart Lender
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "best_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "scaler.pkl"
)

SECRET_KEY = "smart_lender_secret_key"

DEBUG = True