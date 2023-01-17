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
    amount = data.get("amount", "")
    recipt_no = f"{random.randint(100000, 999999)}"
    date = datetime.date()
    amount_due = 600 - float(amount)

    # Make a PDF straight from HTML in a string.
    html = render_template(
        "/templates/index.html",
        amount=amount,
        student_id=student_id,
        form=form,
        name=name,
        email=email,
        contact=contact,
        recipt_no=recipt_no,
        date=date,
        amount_due=amount_due,
    )
    pdf = pdfkit.from_string(html, False)
    pdf = base64.b64encode(pdf).decode("utf-8")
    return {"responseCode": 200, "responseMessage": "Successful", "data": pdf}
