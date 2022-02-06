import os
from fpdf import FPDF

#Global and essential variables
title = 'ADRIAN R. ESGUERRA' # Additional text for design purpose only
fn='ESGUERRA_ADRIAN.pdf' # Output name stored on a variable
jsonFile = "myresume.json" # JSON file which I manually created with a dictioanaries type of data

class PDF(FPDF):
    def header(self):
        # Font setting
        self.set_font('helvetica', 'B', 32)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((255 - w) / 2)
        # Colors of frame, background and text
        self.set_fill_color(250, 250, 250)
        self.set_text_color(0, 0, 0)
        # Title
        self.cell(w, 48, title)
        # Line break
        self.ln(10)
    
    def add_image(self):
        #Add image
        self.image("D1.png",10, -54, 50, 0)
        self.image("croppedme.png",10, 10, 50, 0)
    
    def chapter_body(self, name):
        # Read json file
        with open(jsonFile) as fh:
            jf = fh.read()
        # helvetica 12
        self.set_font("helvetica", "", 12)
        # Output justified text
        self.multi_cell(0, 5, jf)
        # Line break
        self.ln(5)

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_body(name)
        self.add_image()

pdf = PDF()
pdf.set_title(title)
pdf.print_chapter(1, "", jsonFile)

# To initiate a pdf file format
pdf.output(fn)
# To automatically run the output(pdf)
os.startfile(fn)