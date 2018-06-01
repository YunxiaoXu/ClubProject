import sys, os
from urllib import quote, unquote
import json

def main(argv):
	argv = unquote(argv).split("&")
	argv_list = [a.split("=", 1) for a in argv]
	argv_dict = {}
	try:
		for key, value in argv_list:
			argv_dict[key] = value
		json_data = json.dumps(argv_dict)
	except:
		json_data = json.dumps(None)

	pathname = os.path.join(os.path.dirname(__file__), "log")
	if not os.path.exists(pathname):
		os.mkdir(pathname)
	filename = os.path.join(pathname, "log.txt")


	if "time" in argv_dict:
		open(filename, 'a').write(argv_dict["time"]+" ")
	for key in argv_dict:
		if key!="time":
			open(filename, 'a').write("{}: {}; ".format(key, argv_dict[key]))
	open(filename, 'a').write("\n")
	#open(filename, 'a').write("; ".join(argv).replace("=",": ")+"\n")
	return json_data