# *******************************************************************************************
# *******************************************************************************************
#
#		Name : 		ps2codes.py
#		Purpose :	Generate PS/2 tables etc.
#		Date :		11th December 2022
#		Author : 	Paul Robson (paul@robsons.org.uk)
#
# *******************************************************************************************
# *******************************************************************************************

import re 

# *******************************************************************************************
#
#		Creates a table that maps keycodes (0-255) to the ScanCode equivalents
#
# *******************************************************************************************

rawData = open("ps2.data").read(-1).strip().split("\n")
rawData = [x[1:] if x.startswith("/") else x for x in rawData]
keyToScan = [ "0" ] * 256

for s in rawData:
	m = re.match("^([0-9\\sA-F]+)\\:\\:(.*?)\\:",s)
	assert m is not None,"Bad data "+s
	keycode = int(m.group(1).replace(" ",""),16)
	if keycode >= 0x80:
		keycode = (keycode & 0x7F) | 0x80
	if len(m.group(2)) == 1:
		s = m.group(2).replace("'","QUOTE").replace("-","MINUS").replace("=","EQUALS").replace(",","COMMA")
		s = s.replace(";","SEMICOLON").replace(".","PERIOD").replace("[","LEFTBRACKET").replace("]","RIGHTBRACKET")
		s = s.replace("/","SLASH").replace("`","BACKQUOTE").replace("|","BACKSLASH")
		keyToScan[keycode] = "SDLK_"+s
	else:
		s = "SDLK_"+m.group(2).upper()
		s = s.replace("ENTER","RETURN").replace("SPACEBAR","SPACE").replace("LEFTCTRL","LCTRL").replace("RIGHTCTRL","RCTRL")
		s = s.replace("LEFTALT","LALT").replace("RIGHTALT","RALT").replace("LEFTSHIFT","LSHIFT").replace("RIGHTSHIFT","RSHIFT")
		s = s.replace("ESC","ESCAPE")
		keyToScan[keycode] = s

table = ",".join(keyToScan)

print("//\n//\t This file is automatically generated.\n//")
print("static int sdlKeySymbolList[] = {{ {0} }};\n\n".format(table))