import base64
from datetime import datetime
import random
from flask import Flask, render_template, request
from flask_cors import CORS
import pdfkit

app = Flask(__name__)
CORS(app)


@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    data = request.json
    student_id = data.get("student_id", "")
    form = data.get("form", "")
    name = data.get("name", "")
    email = data.get("email", "")
    contact = data.get("contact", "")
    amount_paid = float(data.get("amount_paid", ""))
    recipt_no = f"{random.randint(100000, 999999)}"
    date = datetime.now().date()
    amount_owed = float(data.get("amount_owed", ""))
    amount_due = amount_owed - amount_paid

    # Make a PDF straight from HTML in a string.
    html = render_template(
        "index.html",
        amount_due=amount_due,
        amount_owed=amount_owed,
        amount_paid=amount_paid,
        student_id=student_id,
        form=form,
        name=name,
        email=email,
        contact=contact,
        recipt_no=recipt_no,
        date=date,
    )
    pdf = pdfkit.from_string(html, False, css="static/style.css")
    pdf = base64.b64encode(pdf).decode("utf-8")
    return {"responseCode": 200, "responseMessage": "Successful", "data": pdf}
