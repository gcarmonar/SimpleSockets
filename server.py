''' ==================================================================
    --- Name ---
    server.py

    --- Author ---
    Gerardo Carmona

================================================================== '''

# === Libraries ========================================================
import time
import socket

# === Constants ========================================================
HOST = ''               	# The remote host (Raspberry Pi)
PORT = 50008                # The same port as used by the server


# === Variables ========================================================


# === Init =============================================================
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
time.sleep(1)
s.send('Ready!')

# === Main Program =====================================================
while (True):
	command = control.read(1)
	if not (command == 'Q'):
		s.send(command)
	else:
		s.send(command)
		break
s.close()           # close socket communication
print "Bye!!"
