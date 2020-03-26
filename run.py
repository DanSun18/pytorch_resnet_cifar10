# ported run.sh into python code for easier development and maintenance
# incorporated shutdown capability as well, from run-and-shutdown.sh

import os

shutdown = False #boolean indicating whether to shutdown machine after program execution

if shutdown:
    cmd = 'sudo shutdown -h now'
    os.system(cmd)
    

