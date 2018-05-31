import sys, os
from urllib import quote, unquote
import json

def main(argv):
	argv = unquote(argv).split("&")
	argv_list = [a.split("=", 1) for a in argv]
	argv_dict = {}
	for key, value in argv_list:
		argv_dict[key] = value
	json_data = json.dumps(argv_dict)

	pathname = os.path.join(os.path.dirname(__file__), "log")
	if not os.path.exists(pathname):
		os.mkdir(pathname)
	filename = os.path.join(pathname, "log.txt")

	open(filename, 'a').write(";".join(argv)+"\n")
	return json_data

if len(sys.argv) == 2:
	print main(sys.argv[1])
else:
	print "error: no arguments"