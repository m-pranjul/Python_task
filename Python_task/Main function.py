import latex_to_aiken
import subprocess
import platform
import os

if __name__=="__main__":
    try:
        tex_filename='tex_input.tex'
        output_file_name = latex_to_aiken.convert(tex_filename)
        print("File saved with name : " + output_file_name)
        # open PDF with platform-specific command
        if platform.system().lower() == 'windows':
            os.startfile(output_file_name)
        elif platform.system().lower() == 'linux':
            subprocess.run(['xdg-open', output_file_name])
        else:
            raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))
    except:
        print("Some Error Occured")

