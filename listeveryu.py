from io import BytesIO
import subprocess
import sys

# You don't import the program 😐

def listevery(dir, index):
    process = subprocess.Popen([sys.executable, "-m", "listevery", '\\'.join(__file__.split('\\')[0:-1]) + str('\\' + dir)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()

    string = BytesIO(output).read().decode('utf-8')
    string = string.replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')

    if index == '*':
        return(string)
    else:
        return(string[int(index)])