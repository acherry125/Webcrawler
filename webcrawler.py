#!usr/bin/python
import socket

'''
# info about http http://www.jmarshall.com/easy/http/

# GET: get a resource
# HEAD: get the header only in the response
# POST: request to send data to the server (this is when you use the body lines)
#       also usually includes headers Content-Type and Content-Length

# standard format for http
# -- initial line
# -- header 1: key1: value1
# -- header 2  key2: value2
# -- header ... key... :value...
# -- header n: keyn: valuen (where n is the number of headers)
# blank line with \r\n
# body lines which can be as many as you need where your request/response goes


# example Chrome request to Fakebook for the icon it should display at the top of the tab
print(
    # initial line
    'GET /favicon.ico HTTP/1.1\r\n'
    # headers
    'Host: fring.ccs.neu.edu\r\n'
    'Connection: keep-alive\r\n'
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36\r\n'
    'Accept: */*\r\n'
    'Referer: http://fring.ccs.neu.edu/accounts/login/?next=/fakebook/\r\n'
    'Accept-Encoding: gzip, deflate, sdch\r\n'
    'Accept-Language: en-US,en;q=0.8\r\n'
    'Cookie: csrftoken=7e9ea60b8b86b0189db4cda3daf66f01; sessionid=59fc1cef910c3153cfa76baa8de231e0\r\n')

# example Fakebook Response to above request (with HOPEFULLY the correct linbe formatting I put the \r\n's in myself)

print (
    # initial line
    'HTTP/1.1 404 Not Found\r\n'
    # headers
    'Date: Sat, 19 Mar 2016 16:47:45 GMT\r\n'
    'Server: Apache/2.2.22 (Ubuntu)\r\n'
    'Vary: Accept-Encoding\r\n'
    'Content-Encoding: gzip\r\n'
    'Content-Length: 240\r\n'
    'Keep-Alive: timeout=5, max=98\r\n'
    'Connection: Keep-Alive\r\n'
    'Content-Type: text/html; charset=iso-8859-1\r\n')

# Google Chrome requesting the login page from fring.ccs.neu.edu (header only)

# request login page
GET /accounts/login/?next=/fakebook/ HTTP/1.1
# the host domain
Host: fring.ccs.neu.edu
# we should do this
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
# we probably only need text/html if at all
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
# might be necessary, but I dont think so
Referer: http://fring.ccs.neu.edu/
# we just want gzip
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
# this is going to matter
Cookie: csrftoken=7e9ea60b8b86b0189db4cda3daf66f01; sessionid=59fc1cef910c3153cfa76baa8de231e0


# Fakebook responding to Chrome (header only)

# the resource exists, here you go
HTTP/1.1 200 OK
# kk
Date: Sat, 19 Mar 2016 16:47:44 GMT
# cool
Server: Apache/2.2.22 (Ubuntu)
# good
Content-Language: en-us
# great
Content-Encoding: gzip
# is this when the page will automatically reload?
Expires: Sat, 19 Mar 2016 16:47:44 GMT
Vary: Cookie,Accept-Language,Accept-Encoding
Cache-Control: max-age=0
Set-Cookie: csrftoken=7e9ea60b8b86b0189db4cda3daf66f01; expires=Sat, 18-Mar-2017 16:47:44 GMT; Max-Age=31449600; Path=/
Set-Cookie: sessionid=59fc1cef910c3153cfa76baa8de231e0; expires=Sat, 02-Apr-2016 16:47:44 GMT; Max-Age=1209600; Path=/
Content-Length: 585
Last-Modified: Sat, 19 Mar 2016 16:47:44 GMT
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
Request Headers
view parsed



#INITIAL LINE

# initial request line
# get me this resource (use 1.1 in real thing)
print ("GET /path/to/file/index.html HTTP/1.0")

# initial response line
# version response_status_code english_reason_phrase_for_code
print ("HTTP/1.0 200 OK")
# status codes:
# 1xx: info
# 2xx: success e.g 200 OK
# 3xx: redirecting client
# 4xx: client erro e.g 404 Resource not Found
# 5xx: server error

# HEADER LINES

# header lines beginning with space or tab are still part of the previous line
# HOST is required in HTTP 1.1 but not 1.0, nothing else is mandatory
# each line should end in \r\n (referred to as CRLF) though sometimes only \n is used

# The server will send big files in chunks and tell us with this
# Transfer-Encoding: chunked

# may receive spontaneous responses with code 100 just to show that the server is still responding
# we can probably ignore these, but we need to account for them
# it is always followed by a complete response

'''

chrome_example = ('GET /accounts/login/?next=/fakebook/ HTTP/1.1\r\n'
'Host: fring.ccs.neu.edu\r\n'
#'Connection: keep-alive\r\n'
#'Pragma: no-cache\r\n'
#'Cache-Control: no-cache\r\n'
#'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
#'Upgrade-Insecure-Requests: 1\r\n'
#'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36\r\n'
#'Referer: http://fring.ccs.neu.edu/\r\n'
#'Accept-Encoding: gzip, deflate, sdch\r\n'
#'Accept-Language: en-US,en;q=0.8)\r\n\r\n')
'\r\n')

# -------------------------------------------------------------------------------------------------------------

addrinfo = socket.getaddrinfo('fring.ccs.neu.edu', 80)[0]

sock_addr = addrinfo[-1]

socket_info = addrinfo[:3]

sock = socket.socket(*socket_info)

sock.connect(sock_addr)


login_req = ('GET /accounts/login/?next=/fakebook/ HTTP/1.1\r\n'
'Host: fring.ccs.neu.edu\r\n'
'Connection: keep-alive\r\n'
'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
#'Accept-Encoding: gzip, deflate, sdch\r\n'
'Accept-Language: en-US,en;q=0.8)\r\n\r\n')


# operation resource_path HTTP/1.1\r\nHost:hostname
sock.sendto(login_req, sock_addr)



# sends headers first
server_msg = sock.recvfrom(100000000)
header = server_msg[0]
# sends body next
server_msg2 = sock.recvfrom(100000000)
msg_body = server_msg2[0]


#print server_msg[0]
#print server_msg2[0]

# find all links to go through
def parse_for_links(html):
    last = len(html)
    links = []
    # start from the beginning
    first_a = 0
    while True:
        first_a = html.find('<a href=', first_a + 1, last)
        if first_a == -1:
            break
        first_letter = first_a + 9
        end_quote = html.find('"', first_letter, last)
        if end_quote == -1:
            raise ValueError("the html is formatted wrong")
        links.append(html[first_letter: end_quote])
    return links



x = parse_for_links(msg_body)

print x

