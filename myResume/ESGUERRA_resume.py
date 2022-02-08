import os
from re import sub
from fpdf import FPDF
import json

jsonF = "myresume.json"
filename = "ESGUERRA_ADRIAN.pdf"
title = "ADRIAN R. ESGUERRA"
subtitle = "Software Engineer / IT Specialist"
tagline= "Creative, Artistic, Colligial, Competent, and Reliable Tech-Person"

pdf = FPDF("P", "mm", "Letter")

with open(jsonF, "r") as resume:
    json_object = json.loads(resume.read())

def mainTitle():
    pdf.set_font('helvetica', 'B', 35)
        # Calculate width of title and position
    w = pdf.get_string_width(title) + 6
    pdf.set_x((275 - w) / 2)
        # Colors of frame, background and text
    pdf.set_text_color(0, 0, 0)
        # Title
    pdf.cell(w, -170, title, ln = True)
        # Line break
    pdf.ln(5)

def subTitle():
    pdf.set_font("helvetica", "", 25)
        # Calculate width of title and position
    w = pdf.get_string_width(subtitle) + 6
    pdf.set_x((265 - w) / 2)
        # Colors of frame, background and text
    pdf.set_text_color(0, 0, 0)
        # Title
    pdf.cell(w, 180, subtitle)
        # Line break
    pdf.ln(5)

def tagline_i():
    pdf.set_font("helvetica", "", 13)
        # Calculate width of title and position
    w = pdf.get_string_width(tagline) + 6
    pdf.set_x((270 - w) / 2)
        # Colors of frame, background and text
    pdf.set_text_color(0, 0, 0)
        # Title
    pdf.cell(w, 185, tagline, ln = True)
        # Line break
    pdf.ln(5)

def basicDetails():
    pdf.set_font("helvetica", "", 12)
    pdf.set_font(style="B")
    pdf.cell(0, 60, "", ln = True)
    pdf.cell(70, 10, "PERSONAL INFORMATION", ln = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 10, "Age: " + str(json_object["basicDetails"][0]["Age"]), ln = True)
    pdf.cell(70, 10, "Weight: " + str(json_object["basicDetails"][0]["Weight"]), ln = True)
    pdf.cell(70, 10, "Address: " + str(json_object["basicDetails"][0]["Address"]), ln = True)

    
def contactDetails():
    pdf.set_font("helvetica", "", 12)
    pdf.set_font(style="B")
    pdf.cell(70, 10, "CONTACT DETAILS", ln = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 10, "E-mail: " + str(json_object["contactDetails"][0]["E-mail"]), ln = True)
    pdf.cell(70, 10, "Cell-phone number: " + str(json_object["contactDetails"][0]["Cell-phone number"]), ln = True)
    
def education():
    pdf.set_font("helvetica", "", 12)
    pdf.set_font(style="B")
    pdf.cell(70, 10, "EDUCATION", ln = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 10, "Elementary: " + str(json_object["education"][0]["Elem"]), ln = True)
    pdf.cell(70, 10, "Junior High School: " + str(json_object["education"][0]["JHS"]), ln = True)
    pdf.cell(70, 10, "Senior High School: " + str(json_object["education"][0]["SHS"]), ln = True)
    pdf.cell(70, 10, "College: " + str(json_object["education"][0]["Tert"]), ln = True)
    pdf.cell(70, 10, "Course: " + str(json_object["education"][0]["Course"]), ln = True)


def addImages():
    pdf.image("D1.png", 13, -55, 50, 0)
    pdf.image("croppedme.png", 13, 9, 50, 0)

    
def execute():
    pdf.add_page()
    basicDetails()
    addImages()
    mainTitle()
    subTitle()
    tagline_i()
    contactDetails()
    education()


execute()

pdf.output(filename)
os.startfile(filename)