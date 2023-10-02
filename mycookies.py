#!/usr/bin/python3
# Nathan Wooddell     ----     TC56612

# Import Statements
from os import environ                                          # Used in the retrevial of cookies
import cgi                                                      # Imports CGI
from http import cookies                                        # Used for setting cookies (maybe)

ck1_name = 'umbcid'
ck1_value = ''

ck2_name = 'name'
ck2_value = ''

ck3_name = 'dept'
ck3_value = ''



# Cookies must be sent before declaring the content type
#print("Set-Cookie: Expires")


# Headers for my HTML page
print("Content-type: text/html")                                # Defines content type
print("Host: mywebserver")                                      # Defines server host

# Seperate Headers from content
print()

# Web Content / Page body
print("<html>")                                                 # Beginning of html block
print("<body>")
print("<h1>Cookie Testing Webpage</h1>")
print("This page is used to test setting and eventually recieving cookies with custom values and expirations.")


# cookie umbcid - will be sent by browser if accessed before 60s
print("<br> <br> <h2>umbcid Cookie Creation</h2>")
print("The cookie created below will expire in 60s. If it has not expired it will be sent to the accessed webpage.<br>")
print("In the event that the cookie has expired the cookie will not be sent.<br>")
print("This aligns with the requirements in the document for the umbcid cookie whuich we were instructed to produce.<br>")

# Form to set cookie variables
print('<br><form action = "/cgi-bin/mycookies.py" method = "POST" target = "_blank">')
print(ck1_name)
print(f'<br><input type="text" name="{ck1_name}" value="{ck1_value}" /><br>')
print('<br><input type = "submit" value = "Create Cookie" />')
print('</form>')


# cookie name - will be sent if webpage is accessed within 300s
print("<br><br> <h2>name Cookie Creation</h2>")
print("This cookie is intended to work similarly to the cookie described above.<br>")
print("This cookie differs in that it will be sent if accessing a web page within 300s, as opposed to 60s.<br>")

# Form to set cookie variables
print('<br><form action = "/cgi-bin/mycookies.py" method = "POST" target = "_blank">')
print(ck2_name)
print(f'<br><input type="text" name="{ck2_name}" value="{ck2_value}" /><br>')
print('<br><input type="submit" value="Create Cookie" />')
print('</form>')


# cookie dept - will only be sent when accessing the url indicated by the
print('<br><br> <h2>dept Cookie Creation</h2>')
print("This cookie will be provided by with a value determined by the input into the field below. <br>")
print("Once the cookie is recieved it will only be sent to the server as represented by the URL: <br>")
print("http://TC56612.umbc.local:32769/welcome.html <br>")
print("Otherwise the cookie should not be sent. This will require me to make an entry for domains on my host.<br>")

# Form to set cookie variables
print('<br><form action = "cgi-bin/mycookies.py" method = "POST" target = "_blank">')
print(ck3_name)
print(f'<br><input type="text" name="{ck3_name}" value="{ck3_value}" /><br>')
print('<br><input type="submit" value="Create Cookie" />')
print('</form>')


print("</body>")
print("</html>")                                                # End of html block 

 # Form to set cookie variables
