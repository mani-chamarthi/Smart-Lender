from flask import Flask, render_template, request

import config
from predictor import predict_loan

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY


# HOME PAGE

@app.route("/")
def home():
    return render_template("index.html")


# PREDICTION FORM PAGE

@app.route("/predict")
def predict_page():
    return render_template("predict.html")


# FORM SUBMISSION

@app.route("/predict", methods=["POST"])
def predict_result():

    try:

        education = (
            1 if request.form["education"] == "Graduate"
            else 0
        )

        self_employed = (
            1 if request.form["self_employed"] == "Yes"
            else 0
        )

        features = [

            int(request.form["dependents"]),

            education,

            self_employed,

            float(request.form["income_annum"]),

            float(request.form["loan_amount"]),

            int(request.form["loan_term"]),

            int(request.form["cibil_score"]),

            float(
                request.form[
                    "residential_assets_value"
                ]
            ),

            float(
                request.form[
                    "commercial_assets_value"
                ]
            ),

            float(
                request.form[
                    "luxury_assets_value"
                ]
            ),

            float(
                request.form[
                    "bank_asset_value"
                ]
            )

        ]

        prediction, confidence = predict_loan(features)

        status = (
            "Approved"
            if prediction == 1
            else "Rejected"
        )

        return render_template(
            "result.html",

            prediction=status,
            confidence=confidence,

            dependents=request.form["dependents"],
            education=request.form["education"],
            self_employed=request.form["self_employed"],

            income_annum=request.form["income_annum"],
            loan_amount=request.form["loan_amount"],
            loan_term=request.form["loan_term"],

            cibil_score=request.form["cibil_score"],

            residential_assets=request.form[
                "residential_assets_value"
            ],

            commercial_assets=request.form[
                "commercial_assets_value"
            ],

            luxury_assets=request.form[
                "luxury_assets_value"
            ],

            bank_assets=request.form[
                "bank_asset_value"
            ],

            total_assets=
                float(request.form["residential_assets_value"])
                + float(request.form["commercial_assets_value"])
                + float(request.form["luxury_assets_value"])
                + float(request.form["bank_asset_value"])
        )

    except Exception as e:

        return render_template(
            "error.html",
            error=str(e)
        )

# About page
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)