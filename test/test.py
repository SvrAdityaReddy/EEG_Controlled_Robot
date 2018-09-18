import os
import subprocess
import time

for i in range(1024):
    os.system('echo 1234 >> t.csv')
    data=subprocess.check_output(['tail', '-1', "t.csv"])
    print(data)
    time.sleep(1.0/256)