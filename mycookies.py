#!/usr/bin/python3
# Nathan Wooddell     ----     TC56612

# This is heavily based off of the provided cookiex.py file.

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

ck4_name = 'course'
ck4_value = ''

# create a cookie object and then get the environment for an HTTP cookie
user_cookie = cookies.SimpleCookie()
cookie_string = environ.get('HTTP_COOKIE')

if cookie_string is not None and cookie_string != "":
    cookie_arr = cookie_string.split(';')
    for cookie_item in cookie_arr:
        cookie_item = cookie_item.strip()
        (cookie_key, cookie_value) = cookie_item.split("=")
        if cookie_key == ck1_name:
            ck1_value = cookie_value
        if cookie_key == ck2_name:
            ck2_value = cookie_value
        if cookie_key == ck3_name:
            ck3_value == cookie_value
        if cookie_key == ck4_name:
            ck4_value == cookie_value

# Headers for my HTML page
print("Content-type: text/html")                                # Defines content type
print("Host: mywebserver")                                      # Defines server host

# Cookies must be declared before the body of the html, but after the headers
Cookie_form = cgi.FieldStorage()                                # Gathers the form from the doc below
if ck1_name in Cookie_form:                                     # checking for the umbcid cookie
    umbcid = Cookie_form[ck1_name].value
    print(f"Set-Cookie:{ck1_name} = {umbcid}; Max-Age = {30}")  # Will expire after 30 seconds
if ck2_name in Cookie_form:
    name = Cookie_form[ck2_name].value
    print(f'Set-Cookie:{ck2_name} = {name}; Max-Age = {300}')   # Will expire after 300 seconds
if ck3_name in Cookie_form:
    name = Cookie_form[ck3_name].value
    print(f'Set-Cookie:{ck3_name} = {name}; Domain = tc56612.umbc.local')
if ck4_name in Cookie_form:
    name = Cookie_form[ck4_name].value
    print(f'Set-Cookie:{ck4_name} = {name}; Path = /tc56612')



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
print('<br><form action = "/cgi-bin/mycookies.py" method = "POST" target = "_blank">')
print(ck3_name)
print(f'<br><input type="text" name="{ck3_name}" value="{ck3_value}" /><br>')
print('<br><input type = "submit" value = "Create Cookie" />')
print('</form>')



# cookie course - will only be sent when accessing a webpage with a certain path
print('<br><br> <h2>course Cookie Creation</h2>')
print('A cookie will be created with a path value /TC56612 <br>')
print('This path value will prevent the cookie from being sent when the a url outside of this one is visited.<br>')

# Form to set cookie variables
print('<br><form action = "/cgi-bin/mycookies.py" method = "POST" target = "_blank">')
print(ck4_name)
print(f'<br><input type="text" name="{ck4_name}" value="{ck4_value}" /><br>')
print('<br><input type = "submit" value = "Create Cookie" />')
print('</form>')


print("</body>")
print("</html>")                                                # End of html block 

 # Form to set cookie variables
