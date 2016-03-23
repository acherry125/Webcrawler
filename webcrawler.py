#!usr/bin/python
import socket
import sys
import datetime

def log(string):
  sys.stderr.write(datetime.datetime.now().strftime("%H:%M:%S.%f") + " " + string + "\n")

# requests a page/resource
def request_page(link, cookies=None, type='GET', body='', ):
    if cookies is None:
        cookies = []
    global sock
    global sock_addr
    #log('starting request {} {}'.format(type, link))
    # is there a body
    if body:
        content_length = 'Content-Length: {}\r\n'.format(len(body))
    else:
        content_length = ''
    # display as string 'cookie_name:value; cookie_name:value'
    if cookies:
        cookie_value = 'Cookie: {}\r\n'.format('; '.join(cookies))
    else:
        cookie_value = ''
    request = ('{} {} HTTP/1.1\r\n'
                'Host: fring.ccs.neu.edu\r\n'
                'Connection: keep-alive\r\n'
                '{}'
                '{}'
                'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
                'Accept-Language: en-US,en;q=0.8)\r\n\r\n'
                '{}').format(type, link, content_length, cookie_value, body)
    #log('request created {} {}'.format(type, link))
    sock.sendto(request, sock_addr)
    #log('sent {} {}'.format(type, link))
    # sends headers first
    header = sock.recvfrom(100000000)[0]
    #print header
    #log('rec1 {} {}'.format(type, link))
    msg_body = ''
    received = 0
    length = get_length(header)
    # use get_chunked somehow to figure out what to do for chunked pages
    if length > 0:
        #while received < length:
        # sends body next
        server_msg2 = sock.recvfrom(100000000)[0]
        #print server_msg2
        #print 'dlfhds'
        received += len(server_msg2)
        log('rec2 {} {} {}'.format(type, link, len(server_msg2)))
        msg_body = msg_body + server_msg2
    #print get_status_code(header)
    return (header, msg_body)

# gets the cookies in a response header
def get_cookies(header):
    return get_helper(header, 'Set-Cookie: ', ';')

def get_status_code(header):
    return get_helper(header, '1.1 ', ' OK')

# find all hyperlinks in an html document
def get_links(html, old_links):
    all_links = set(get_helper(html, '<a href="', '"'))
    good_links = [x for x in all_links if (x[0] == '/' or (len(x) >= 25 and x[:25] == 'http://fring.ccs.neu.edu/')) and x not in old_links]
    old_links += good_links
    return good_links


def get_length(html):
    length = get_helper(html, 'Content-Length: ', '\r\n')
    if length:
        return int(length[0])
    else:
        return 0

def get_chunked(header):
    chunked = get_helper(header, 'Transfer-Encoding: ', '\r\n')
    if chunked == 'chunked':
        return True
    else:
        return False

def get_secret_flags(html):
    # may have to add space after FLAG: later
    result = get_helper(html, "class='secret_flag' style=\"color:red\">FLAG: ", '</h2>', )
    # might be able to factor down to just 'return result', but this is just ot be safe
    if result:
        return result
    else:
        return False

# helps the parsers
def get_helper(resource, start, end):
    found = []
    loc = 0
    offset = len(start)
    while True:
        # find cookie 1
        loc = resource.find(start, loc + 1, len(resource))
        if loc == -1:
            break
        val_loc = loc + offset
        end_loc = resource.find(end, val_loc, len(resource))
        if end_loc == -1:
            print resource
            raise ValueError("the resource is formatted wrong")
        found.append(resource[val_loc: end_loc])
    return found

# connects the socket to the server
def connect_to_server(server='fring.ccs.neu.edu', port=80):
    global addrinfo
    global sock_addr
    global socket_info
    global sock
    addrinfo = socket.getaddrinfo(server, port)[0]
    sock_addr = addrinfo[-1]

    socket_info = addrinfo[:3]

    sock = socket.socket(*socket_info)

    sock.connect(sock_addr)

# for debugging purposes, logging in take a bit
login = False

if login:
    # initial connection
    connect_to_server()
    log('connected')
    # the login page path
    login_post = '/accounts/login/'
    # get the initial login page
    (header, msg_body) = request_page(login_post)
    log('got login page')
    # username=<username_here>&password=<password_here>&csrfmiddlewaretoken=<csrftoken_here>&next=%2Ffakebook%2F
    cookies = get_cookies(header)
    log('got cookies')
    # assume that cookies[0] is csrftoken
    csrf = cookies[0].split('=')
    # dont merge these
    csrf_val = csrf[1]

    login_data = 'username=001783626&password=8XOD2QE4&csrfmiddlewaretoken={}&next=/'.format(csrf_val)
    log('made login data')
    (login_redirect_header, login_ignore) = request_page(login_post, cookies, 'POST', login_data)
    log('made login request')

    # get the new session id
    session_id = get_cookies(login_redirect_header)
    log('got session id')
    # have to reset the connection for some reason
    connect_to_server()
    log('connected to server again')
    (success_header, fakebook_home) = request_page('/fakebook/', session_id)
    log('succeeded')
    #---------------------------------------------------------------------------------
    # WE ARE LOGGED IN

    # start link gathering and searching (make sure not to go infinitely when experimenting)
    # here is a template for collecting the links to all friends on page one of a user's friend list
    # from this point on, it should just be a matter of checking all of the links you find for the secret flags
    master_list = ['/fakebook/']
    master_pointer = 0
    secret_flags = []
    print master_list

    # have to deal with chunk-encoding
    while True:
        if secret_flags:
            print len(secret_flags)
        iter = master_list[master_pointer:]
        for link in iter:
            connect_to_server()
            (header, html) = request_page(link, session_id)
            if html == '':
                connect_to_server()
                (header, html) = request_page(link, session_id)
                if html == '':
                    print header
                    raise ValueError('the page is empty!')
            key = get_secret_flags(html)
            if key:
                print key
                #sys.exit(0)
                secret_flags.append(key)
                if len(secret_flags) > 4:
                    break
            get_links(html, master_list)
            master_pointer += 1
        print master_pointer

#connect_to_server()
#answ = request_page('/accounts/login/')
#print answ

# just some little unit tests... we should use these more
#assert get_links('where is the link???? <a href="/login"> oh it was right there', []) == ["/login"]
#assert get_secret_flags('there is a secret key in here! where <h2 class=\'secret_flag\' style="color:red">FLAG: 3243424235345345</h2> is it????') == ['3243424235345345']

#assert get_chunked('here is the Transfer-Encoding: chunked\r\n chunk') == 'chunked'



connect_to_server()
(a, b) = request_page('/accounts/login/')
print(a, b)
print('ab printed')
cookies = get_cookies(a)
print(cookies)
# assume that cookies[0] is csrftoken
csrf = cookies[0].split('=')
# dont merge these
csrf_val = csrf[1]
connect_to_server()
login_data = 'username=001783626&password=8XOD2QE4&csrfmiddlewaretoken={}&next=/'.format(csrf_val)
(d, e) = request_page('/accounts/login/', cookies, 'POST', login_data)
print(d)
print('post printed')
session_id = get_cookies(d)
print session_id
(f,g) = request_page('/fakebook/', session_id)
print f
print ('printed f')
print g
print 'printed g'
master = ['/fakebook/']

links = get_links(f, master)
print links
#request_page(links[0], session_id)
#print links
