import os

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

from weasyprint import HTML

def makepdf():
    """Generate a PDF file from a string of HTML."""
    htmldoc = HTML(filename="templates/mytemplate.html")
    return htmldoc.write_pdf("ttesstt.pdf")

makepdf()
