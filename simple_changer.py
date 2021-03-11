from stem import Signal
from stem.control import Controller
from time import sleep
from os import system
from subprocess import Popen, PIPE
import sys

colores = {
        "M" :  "\033[1;31m",
        "H" :  "\033[1;32m",
        "K" :  "\033[1;33m",
        "U" :  "\033[1;34m",
        "P" :  "\033[1;35m",
        "C" :  "\033[1;36m",
        "W":  "\033[1;37m",
        "A" :  "\033[90m",

}

class Tor(object):
    def __str__(self):
        return colores["K"]+"""

        
  _____             ___ _                       
 |_   _|__ _ _ ___ / __| |_  __ _ _ _  __ _ ___ 
   | |/ _ \ '_|___| (__| ' \/ _` | ' \/ _` / -_)
   |_|\___/_|      \___|_||_\__,_|_||_\__, \___|
                                      |___/     


    """
    def which(self):
        p = Popen('which tor', shell=True, stdout=PIPE, stderr=PIPE)
        code = p.wait()
        if code == 0:
            return True
        else:
            return False
x = Tor()
print(x)
if not x.which():
    print "Tor no esta instalado"
    print "Ejecute sudo apt install tor"
    sys.exit(1)
else:
    pass

def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="MyStr0n9P")
        controller.signal(Signal.NEWNYM)

for i in range(100):
    x = system("torsocks curl ifconfig.me")
    print ""
    print("Return status: ",x)
    # 0 status ok 
    # 1 status bad (system function error)
    # 1 status bad torsocks not found
    print ""
    renew_tor_ip()
    sleep(5)
