<h1 align="center">Tor change IP</h1>
<h4 align="center">Change Tor IP every 5 seconds</h4>
<p align="center">
	<img src="http://ForTheBadge.com/images/badges/made-with-python.svg" title="python" alt="python">
	<img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" title="Apache-License" alt="Apache-license">

## Installation / Instalacion
	$ git clone https://github.com/OverflowShell/tor_change
	$ cd tor_change
	$ sudo pip2 install stem requests pycurl pysocks
	$ sudo apt install tor torsocks
	$ python2 simple_changer.py
## Configuration / Configuracion
	tor --hash-password MyStr0n9P (Execute in your terminal,this is your hashed password for tor)
	Add this on your torrc config file  
	-sudo nano /etc/tor/torrc
	HashedControlPassword 16:A6E9CE3898AEC79A60814EF18CF75880D26279CAC6266A99640C41E221
	CookieAuthentication 0
	ControlPort 9051
## Code modification / Modificacion del codigo
	In the line 54 you can modify the threads of the IP change	
	In the line 63 you can modify the time of the IP change
	In the line 50 you can modify the controlport of Tor
	In the line 51 you can modify the password of Tor
	In the line 55 you can modify ordering tor IP to web with torsocks
