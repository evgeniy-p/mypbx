import os
import re


def windowsed():
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '\\main.qss', 'r') as textfile:
        line = textfile.readline()
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '\\main.src', 'r') as textfile:
        lines = textfile.readlines()
        lines.insert(0, test)
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '\\main.qss', 'w') as textfile:
        for line in lines:
            pattern = '^.*:(.*.png).*'
            find = re.compile(pattern)
            textfile.write(find.sub(r'    image: url("{path}/\1");'.format(path='/'.join(os.path.dirname(__file__).split('\\'))), line))

            pattern1 = '^.*image:.*:(.*).png.*'
            find1 = re.compile(pattern1)
            pattern2 = '^.*border-image:.*:(.*).png.*'
            find2 = re.compile(pattern2)
            if find1.match(line):
                textfile.write(
                    find1.sub(r'    image: url("{path}/\1.png");'.format(path=os.path.dirname(__file__)), line))
            elif find2.match(line):
                textfile.write(
                    find2.sub(r'    border-image: url("{path}/\1.png");'.format(path=os.path.dirname(__file__)), line))
            else:
                textfile.write(line)


def unixed():
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '/main.qss', 'r') as textfile:
        line = textfile.readline()
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '/main.src', 'r') as textfile:
        lines = textfile.readlines()
    with open(str(os.path.dirname(os.path.abspath(__file__))) + '/main.qss', 'w') as textfile:
        for line in lines:
            pattern1 = '^.*image:.*:(.*).png.*'
            find1 = re.compile(pattern1)
            pattern2 = '^.*border-image:.*:(.*).png.*'
            find2 = re.compile(pattern2)
            if find1.match(line):
                textfile.write(find1.sub(r'    image: url({path}/\1.png);'.format(path=os.path.dirname(__file__)), line))
            elif find2.match(line):
                textfile.write(find2.sub(r'    border-image: url({path}/\1.png);'.format(path=os.path.dirname(__file__)), line))
            else:
                textfile.write(line)
