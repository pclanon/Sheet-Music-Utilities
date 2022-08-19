"""Break up big PDF of charts into single files with correct titles. 
    Start with one big PDF and a .txt file of the titles on separate lines"""

from PyPDF2 import PdfFileReader, PdfFileWriter

basepath = '/Users/paulclanon/Downloads/PDFs/'
one_big_pdf = f"{basepath}set_jam session.pdf"
titles = f"{basepath}titles.txt"

# Read the titles file line by line. Clean out special charactes and make a valid filename

with open(titles, 'r') as titles:
     all_titles = titles.readlines()

# Make valid filenames by stripping whitespace, special characters, and newlines

def clean_up_titles(titles_list):
    
    cleaned_titles = []
    
    for t in all_titles:
        t = "".join(c for c in t if c.isalnum())
        cleaned_titles.append(t)
    
    return cleaned_titles[:-1] # Slice to drop the empty string at the end caused by the newline
        
cleaned_titles = clean_up_titles(all_titles)

# Break the big PDF into separate PDFs one to a page, and save with title

inputpdf = PdfFileReader(open(one_big_pdf , "rb"))

num_pages = len((cleaned_titles))

# Save each page with title from titles.txt

for i in range(num_pages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    
    output_fname = f'{basepath}{cleaned_titles[i]}.pdf'

    with open(output_fname, 'wb') as outputStream:
        output.write(outputStream)
