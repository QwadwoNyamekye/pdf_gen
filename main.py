import base64
from flask import Flask, render_template, request
from flask_weasyprint import HTML, render_pdf
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

    # Make a PDF straight from HTML in a string.
    html = render_template(
        "index.html",
        amount=amount,
        student_id=student_id,
        form=form,
        name=name,
        email=email,
        contact=contact,
    )
    pdf = pdfkit.from_string(html, False)
    # pdf = HTML(string=html).write_pdf()
    pdf = base64.b64encode(pdf).decode('utf-8')
    return {
        "responseCode": 200,
        "responseMessage":"Successful",
        "data":pdf
    }
