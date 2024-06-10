from fpdf import FPDF
import glob
from pathlib import Path

# create list of txt files
directory = glob.glob("Files/*.txt")

# create one pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")
 
for filepath in directory:
    
    pdf.add_page()
    
    filename = Path(filepath).stem
    
    # add content to pdf
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=10, txt=filename.capitalize(), ln=True, align='L')
    
    # Add the content to the PDF, handling multiple lines
    pdf.set_font(family="Times", size=12)
    with open(filepath, 'r') as file:
        for line in file:
            pdf.multi_cell(w=0, h=10, txt=line.strip())
            
pdf.output("output.pdf")