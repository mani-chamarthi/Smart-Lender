import csv
from io import StringIO
from flask import Flask, render_template, Response, request
from flask import redirect, url_for, flash

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import config

from extensions import db, login_manager
from auth_utils import admin_required

from models.user import User
from models.prediction import Prediction

from predictor import predict_loan


app = Flask(__name__)

app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
    config.SQLALCHEMY_TRACK_MODIFICATIONS
)

db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
        
            flash(
                "Passwords do not match.",
                "danger"
            )
            return redirect(url_for("register"))

        existing_user = User.query.filter(
            (User.username == username) |
            (User.email == email)
        ).first()

        if existing_user:
            flash(
                "Username or Email already exists.",
                "danger"
            )
            return redirect(url_for("register"))

        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            role="customer"
        )

        db.session.add(new_user)
        db.session.commit()

        flash(
            "Registration successful. Please login.",
            "success"
        )

        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password_hash,
            password
        ):

            login_user(user)

            if user.role == "admin":
                return redirect(
                    url_for("admin_dashboard")
                )

            return redirect(
                url_for("home")
            )

        flash(
            "Invalid email or password",
            "danger"
        )

    return render_template("login.html")


# ---------------- LOGOUT ----------------

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(
        url_for("home")
    )

# --------------- Dashboard ---------------

@app.route("/dashboard")
@login_required
def dashboard():

    total_predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).count()

    approved_predictions = Prediction.query.filter_by(
        user_id=current_user.id,
        prediction="Approved"
    ).count()

    rejected_predictions = Prediction.query.filter_by(
        user_id=current_user.id,
        prediction="Rejected"
    ).count()

    recent_predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Prediction.created_at.desc()
    ).limit(5).all()

    return render_template(
        "dashboard.html",

        total_predictions=total_predictions,
        approved_predictions=approved_predictions,
        rejected_predictions=rejected_predictions,
        recent_predictions=recent_predictions
    )

# ---------------- ADMIN ----------------

@app.route("/admin")
@login_required
@admin_required
def admin_dashboard():

    total_users = User.query.count()

    total_predictions = Prediction.query.count()

    approved_loans = Prediction.query.filter_by(
        prediction="Approved"
    ).count()

    rejected_loans = Prediction.query.filter_by(
        prediction="Rejected"
    ).count()

    approval_rate = 0

    if total_predictions > 0:
        approval_rate = round(
            approved_loans * 100 / total_predictions,
            2
        )

    return render_template(
        "admin_dashboard.html",

        total_users=total_users,
        total_predictions=total_predictions,
        approved_loans=approved_loans,
        rejected_loans=rejected_loans,
        approval_rate=approval_rate
    )


@app.route("/admin/users")
@login_required
@admin_required
def admin_users():

    users = User.query.all()

    return render_template(
        "admin_users.html",
        users=users
    )


@app.route("/admin/predictions")
@login_required
@admin_required
def admin_predictions():

    predictions = Prediction.query.order_by(
        Prediction.created_at.desc()
    ).all()

    return render_template(
        "admin_predictions.html",
        predictions=predictions
    )


# ---------------- PREDICT ----------------

@app.route("/predict")
@login_required
def predict_page():
    return render_template("predict.html")


@app.route("/predict", methods=["POST"])
@login_required
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
            float(request.form["residential_assets_value"]),
            float(request.form["commercial_assets_value"]),
            float(request.form["luxury_assets_value"]),
            float(request.form["bank_asset_value"])
        ]

        prediction, confidence = predict_loan(features)

        status = (
            "Approved"
            if prediction == 1
            else "Rejected"
        )

        residential_assets = float(
            request.form["residential_assets_value"]
        )
        commercial_assets = float(
            request.form["commercial_assets_value"]
        )
        luxury_assets = float(
            request.form["luxury_assets_value"]
        )
        bank_assets = float(
            request.form["bank_asset_value"]
        )

        total_assets = (
            residential_assets +
            commercial_assets +
            luxury_assets +
            bank_assets
        )

        history = Prediction(
            user_id=current_user.id,
            prediction=status,
            confidence=confidence,
            loan_amount=float(
                request.form["loan_amount"]
            ),
            income_annum=float(
                request.form["income_annum"]
            ),
            cibil_score=int(
                request.form["cibil_score"]
            )
        )

        db.session.add(history)
        db.session.commit()

        education_label = (
            "Graduate"
            if request.form["education"] == "Graduate"
            else "Not Graduate"
        )

        self_employed_label = (
            "Yes"
            if request.form["self_employed"] == "Yes"
            else "No"
        )

        return render_template(
            "result.html",
            prediction=status,
            confidence=confidence,
            dependents=int(request.form["dependents"]),
            education=education_label,
            self_employed=self_employed_label,
            income_annum=float(request.form["income_annum"]),
            loan_amount=float(request.form["loan_amount"]),
            loan_term=int(request.form["loan_term"]),
            cibil_score=int(request.form["cibil_score"]),
            residential_assets=residential_assets,
            commercial_assets=commercial_assets,
            luxury_assets=luxury_assets,
            bank_assets=bank_assets,
            total_assets=total_assets,
            decision_1=f"Prediction confidence: {confidence}%",
            decision_2=f"CIBIL score: {request.form['cibil_score']}",
            decision_3=f"Loan amount requested: ₹{request.form['loan_amount']}",
            decision_4=f"Total assets: ₹{total_assets:.2f}"
        )

    except Exception as e:

        return render_template(
            "error.html",
            error=str(e)
        )


# ---------------- HISTORY ----------------

@app.route("/history")
@login_required
def history():

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Prediction.created_at.desc()
    ).all()

    return render_template(
        "history.html",
        predictions=predictions
    )

# ------------ History Export ------------

@app.route("/history/export")
@login_required
def export_history():

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Prediction.created_at.desc()
    ).all()

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "Date",
        "Prediction",
        "Confidence",
        "Loan Amount",
        "Income",
        "CIBIL"
    ])

    for p in predictions:
        writer.writerow([
            p.created_at,
            p.prediction,
            p.confidence,
            p.loan_amount,
            p.income_annum,
            p.cibil_score
        ])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=prediction_history.csv"
        }
    )

# ---------------- ABOUT ----------------

@app.route("/about")
def about():
    return render_template("about.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)