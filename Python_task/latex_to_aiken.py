import os
import subprocess

def convert(tex_filename):
    filename, ext = os.path.splitext(tex_filename)
    pdf_filename = filename + '.pdf'
    # pdflatex helps in rendering the content of Latex file
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
    # check if PDF is successfully generated
    if not os.path.exists(pdf_filename):
        raise RuntimeError('PDF output not found')
    return pdf_filename
