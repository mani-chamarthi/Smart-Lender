"""
Configuration file for Smart Lender
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model Paths

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

# Flask Configuration

SECRET_KEY = "smart_lender_secret_key"

DEBUG = True

# Database Configuration

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "smart_lender.db"
)

SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
SQLALCHEMY_TRACK_MODIFICATIONS = False