import latex_to_aiken
import subprocess
import platform
import os

if __name__=="__main__":
    try:
        tex_filename='tex_input.tex'
        output_file = latex_to_aiken.convert(tex_filename)
        print("File saved with name : " + output_file)
        # open PDF with platform-specific command
        if platform.system().lower() == 'windows':
            os.startfile(output_file)
        elif platform.system().lower() == 'linux':
            subprocess.run(['xdg-open', output_file])
        else:
            raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))
    except:
        print("Some Error Occured")

