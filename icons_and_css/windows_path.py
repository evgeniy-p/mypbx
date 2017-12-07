import os
import re


if os.name == 'nt':
    print(str(os.path.dirname(os.path.abspath(__file__))) + '\\icons_and_css')
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '\\icons_and_css\\main.qss', 'r') as textfile:
        lines = textfile.readlines()
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '\\icons_and_css\\main.qss', 'w') as textfile:
        for line in lines:
            textfile.write(re.sub(r':*.png'                                      '{fin}'.format(), line))
