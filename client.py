''' ==================================================================
	--- Name ---
	client.py
	
	--- Author ---
	Gerardo Carmona
	
================================================================== '''

# === Libraries ========================================================
import socket
import time

# === Constants ========================================================
HOST = '10.43.53.161'    		# The remote host at work
PORT = 50008        			# The same port as used by the server

# === Variables ========================================================


# === Init =============================================================
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# === Main Program =====================================================
s.send('H')
s.send('e')
s.send('l')
s.send('l')
s.send('o')
s.send(' ')
s.send('W')
s.send('o')
s.send('r')
s.send('l')
s.send('d')
s.send('Q')

# End of program
s.close()
print "End of program... Bye!"

