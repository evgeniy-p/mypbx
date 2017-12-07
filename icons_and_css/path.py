import os
import re


def windowsed():
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '\\main.qss', 'r') as textfile:
        test = textfile.readline()
        if test == '/*WIN*/\n':
            return print('already in windows style')
        elif test == '/*UNIX*/\n':
            lines = textfile.readlines()
        else:
            lines = textfile.readlines()
            lines.insert(0, test)
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '\\main.qss', 'w') as textfile:
        textfile.write('/*WIN*/\n')
        for line in lines:
            pattern = '^.*:(.*.png).*'
            find = re.compile(pattern)
            textfile.write(find.sub(r'    image: url("{path}/\1");'.format(path='/'.join(os.path.dirname(__file__).split('\\'))), line))


def unixed():
    with open('main.qss', 'r') as textfile:
        test = textfile.readline()
        if test == '/*UNIX*/\n':
            return print('already in unix style')
        elif test == '/*WIN*/\n':
            lines = textfile.readlines()
            pattern = '^.*/(.*.png).*'
        else:
            pattern = '^.*\((:.*.png).*'
            lines = textfile.readlines()
            lines.insert(0, test)
    with open('main.qss', 'w') as textfile:
        textfile.write('/*UNIX*/\n')
        for line in lines:
            find = re.compile(pattern)
            textfile.write(find.sub(r'    image: url(: \1);', line))

