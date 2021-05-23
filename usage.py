from io import BytesIO
import subprocess
import sys

process = subprocess.Popen([sys.executable, "-m", "listevery", '\\'.join(__file__.split('\\')[0:-1]) + str('\\' + sys.argv[1])], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, error = process.communicate()

string = BytesIO(output).read().decode('utf-8')
string = string.replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')

print(string)