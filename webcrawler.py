#!usr/bin/python

# info about http

# standard format for http
# -- initial line
# -- header 1: key1: value1
# -- header 2  key2: value2
# -- header ... key... :value...
# -- header n: keyn: valuen (where n is the number of headers)
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

'''INITIAL LINE'''

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

''' HEADER LINES '''

# header lines beginning with space or tab are still part of the previous line
# HOST is required in HTTP 1.1 but not 1.0, nothing else is mandatory
# each line should end in \r\n (referred to as CRLF) though sometimes only \n is used


