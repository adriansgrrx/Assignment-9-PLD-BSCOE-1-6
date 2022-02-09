import os
from fpdf import FPDF
import json

"""
global variables section
"""
jsonF = "myresume.json"                                                         # JSON file where my data are stored
filename = "ESGUERRA_ADRIAN.pdf"                                                # The output name of the file in pdf format
title = "ADRIAN R. ESGUERRA"                                                    # The main title of the resume
subtitle = "Computer Engineering Student"                                       # The sub-title of the resume
tagline= "Creative, Artistic, Colligial, Competent, and Reliable Tech-Person"   # The tagline of the resume

pdf = FPDF("P", "mm", "Letter") # FPDF library stored on a variable later to be accessed 

# Reading and opening of the json file
with open(jsonF, "r") as resume:    # with statement is used to close the file automatically
    json_object = json.loads(resume.read())

"""
Main title, sub-title and tagline positioning and editing section
"""
def mainTitle():
    pdf.set_font('helvetica', 'B', 35)
    # Calculate width of title and position
    w = pdf.get_string_width(title) + 6
    pdf.set_x((275 - w) / 2)
    pdf.set_text_color(0, 0, 0)
    # Title
    pdf.cell(w, 40, title, ln = True)

def subTitle():
    pdf.set_font("helvetica", "", 28)
    # Calculate width of title and position
    w = pdf.get_string_width(subtitle) + 6
    pdf.set_x((273 - w) / 2)
    pdf.set_text_color(0, 0, 0)
    # Subtitle
    pdf.cell(w, -22, subtitle)

def tagline_i():
    pdf.set_font("helvetica", "", 13)
    # Calculate width of title and position
    w = pdf.get_string_width(tagline) + 6
    pdf.set_x((273 - w) / 2)
    pdf.set_text_color(0, 0, 0)
    # Title
    pdf.cell(w, -6, tagline, ln = True)
"""
Data structuring sectoin including its positionings and reading json file
"""
def basicDetails():
    pdf.set_font("helvetica", "", 15)
    pdf.set_font(style="B")
    pdf.cell(0, 18, "", ln = True)
    pdf.cell(195, 7, "PERSONAL INFORMATION", ln = True, border = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 7, "Full-Name: " + str(json_object["basicDetails"][0]["Full-Name"]), ln = True)
    pdf.cell(70, 7, "Sex: " + str(json_object["basicDetails"][0]["Sex"]), ln = True)
    pdf.cell(70, 7, "Age: " + str(json_object["basicDetails"][0]["Age"]), ln = True)
    pdf.cell(70, 7, "Weight(kg): " + str(json_object["basicDetails"][0]["Weight"]), ln = True)
    pdf.cell(70, 7, "Height(ft): " + str(json_object["basicDetails"][0]["Height"]), ln = True)
    pdf.cell(70, 7, "Address: " + str(json_object["basicDetails"][0]["Address"]), ln = True)

def contactDetails():
    pdf.set_font("helvetica", "", 15)
    pdf.set_font(style="B")
    pdf.cell(195, 7, "CONTACT DETAILS", ln = True, border = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 7, "E-mail: " + str(json_object["contactDetails"][0]["E-mail"]), ln = True)
    pdf.cell(70, 7, "Cell-phone number: " + str(json_object["contactDetails"][0]["Cell-phone number"]), ln = True)
    
def education():
    pdf.set_font("helvetica", "", 15)
    pdf.set_font(style="B")
    pdf.cell(195, 7, "EDUCATION", ln = True, border = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 7, "Elementary: " + str(json_object["education"][0]["Elem"]), ln = True)
    pdf.cell(70, 7, "Junior High School: " + str(json_object["education"][0]["JHS"]), ln = True)
    pdf.cell(70, 7, "Senior High School: " + str(json_object["education"][0]["SHS"]), ln = True)
    pdf.cell(70, 7, "College: " + str(json_object["education"][0]["Tert"]), ln = True)

def achievements():
    pdf.set_font("helvetica", "", 15)
    pdf.set_font(style="B")
    pdf.cell(195, 7, "ACHIEVEMENTS/AWARDS", ln = True, border = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 7, "> " + str(json_object["achievements"][0]["1"]), ln = True)
    pdf.cell(70, 7, "> " + str(json_object["achievements"][0]["2"]), ln = True)
    pdf.cell(70, 7, "> " + str(json_object["achievements"][0]["3"]), ln = True)
    pdf.cell(70, 7, "> " + str(json_object["achievements"][0]["4"]), ln = True)
    pdf.cell(70, 7, "> " + str(json_object["achievements"][0]["5"]), ln = True)

def organization():
    pdf.set_font("helvetica", "", 15)
    pdf.set_font(style="B")
    pdf.cell(195, 7, "CLUBS & ASSOCIATIONS", ln = True, border = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(70, 7, "> " + str(json_object["organizations"][0]["yessci"]), ln = True)
    pdf.cell(70, 7, "> " + str(json_object["organizations"][0]["ssg"]), ln = True)

def skills():
    pdf.set_font("helvetica", "", 15)
    pdf.set_font(style="B")
    pdf.cell(195, 7, "SKILLS", ln = 20, border = True)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(99, 5.5, "" + str(json_object["skills"][0]["MS"]), ln = True, align="C")
    pdf.cell(125, 5.5, "" + str(json_object["skills"][0]["Ps"]), ln = True, align="C")
    pdf.cell(115, 5.5, "" + str(json_object["skills"][0]["DR"]), ln = True, align="C")
    pdf.cell(79, 5.5, "" + str(json_object["skills"][0]["TDraw"]), ln = True, align="C")
"""
Image section
"""
def addImages():
    pdf.image("D1.png", 13, -55, 50, 0)
    pdf.image("croppedme.png", 13, 9, 50, 0)
    pdf.image("graph.png", 90, 238, 70, 0)

"""
Calling functions section
"""   
def execute():
    pdf.add_page()
    addImages()
    mainTitle()
    subTitle()
    tagline_i()
    basicDetails()
    contactDetails()
    education()
    achievements()
    organization()
    skills()

"""
Execution of the whole program
"""
execute()

pdf.output(filename)    # The output name of the generated pdf
os.startfile(filename)  # To start the file automatically