#!/usr/bin/python

import ConfigParser
import signal
import SimpleHTTPServer
import SocketServer
import sys

PORT = 8888
SSP_VERSION = "ssp/"

# http://stackoverflow.com/a/25375077
class SSPHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	# Set the server version
	SimpleHTTPServer.SimpleHTTPRequestHandler.server_version = SSP_VERSION

	def log_message(self, format, *args):
		"""
			Format the log messages generated by requests to the server.
		"""
		
		# Print log message per request to the web server
		print("[%s]: %s ==> %s" % (self.log_date_time_string(), self.client_address[0], format%args))
		print(args[1])

class sspserver():
	
	def __init__(self):
		"""
			Constructor for main server class.
		"""
		
		self.config = ConfigParser.RawConfigParser(allow_no_value=True)
		self.config.read("config.ssp")
		
		PORT = int(self.config.get("setup", "port"))
		SSP_VERSION = self.config.get("setup", "ssp_version")
		
		try:
			Handler = SSPHTTPHandler
			httpd = SocketServer.TCPServer(("", PORT), Handler)
			print "Serving on port " + str(PORT)
			httpd.serve_forever()
		except KeyboardInterrupt:
			sys.exit(0)
	
if __name__ == "__main__":
	s = sspserver()