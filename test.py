import subprocess, sys
result = subprocess.run([sys.executable, "-m", "listevery", '\\'.join(__file__.split('\\')[0:-1]) +'\\'+ sys.argv[1]])
