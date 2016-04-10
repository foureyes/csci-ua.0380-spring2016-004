class Request:
    """Represents an HTTP request. Parses a request and creates properties
    on this request instance. For example... if the request is:

    GET /dice HTTP/1.1
    User-Agent: p4a browser ftw! 
    Host: localhost:5000
    Accepts: text/html

    Then a Request object representing the above request (where req is an
    instance of Request):

    req.path --> "/dice"
    req.method --> "/GET"
    req.http_version --> "HTTP/1.1"
    req.headers --> {
        "User-Agent": "p4a browser ftw!",
        "Host": "localhost:5000",
        "Accepts": "text/html"
    }

    """

    def __init__(self, request_text):
        self.parse_request(request_text)
        
    def parse_request(self, request_text):
        """Extract path, method and http version from string version of HTTP
        request. Save in instance variables.
        """
        # grab the first line (split by carriage return \r and newline \n - 
        # http specs mention that \r\n represents newlines)
        request_parts = request_text.split('\r\n')
        parts = request_parts[0].split(' ')
        self.method, self.path, self.http_version = parts

        headers = {}
        line_num = 1
        while ':' in request_parts[line_num]:
            h = request_parts[line_num]
            i = h.index(':')
            name = h[:i].strip()
            value = h[i + 1:].strip()
            headers[name] = value
            line_num += 1
        self.headers = headers
        self.body = request_parts[line_num + 1]

    def __str__(self):
        s = "{} {} {}\r\n".format(self.method, self.path, self.http_version)
        s += "\r\n".join(["{}: {}".format(k, v) for k, v in self.headers.items()])
        s += "\r\n\r\n{}".format(self.body)
        return s

class Response:

    STATUS_TEXT = {
        200: "OK", 
        400: "Bad Request", 
        404: "Not Found", 
        500: "Server Error"
    }

    def __init__(self, status, http_version="HTTP/1.1"):
        self.status = status if status in Response.STATUS_TEXT else 200
        self.http_version = http_version
        self.headers = {}
        self.body = ''

    def set_header(self, header_name, header_value):
        self.headers[header_name] = header_value

    def set_body(self, body):
        self.body = body
    
    def __str__(self):
        s = "{} {} {}\r\n".format(self.http_version, self.status, Response.STATUS_TEXT[self.status])
        s += "\r\n".join(["{}: {}".format(k, v) for k, v in self.headers.items()])
        s += "\r\n\r\n{}".format(self.body)
        return s
        
        
if __name__ == '__main__':
    
    """
    GET /dice HTTP/1.1
    User-Agent: p4a browser ftw! 
    Host: localhost:5000
    Accepts: text/html

    """

    http_req = "GET /dice HTTP/1.1\r\nUser-Agent: p4a browser ftw!\r\nHost: localhost:5000\r\nAccepts: text/html\r\n\r\n"
    req = Request(http_req)
    print(req.method)
    print(req.path)
    print(req.headers)
    print(req.body)
    print(req)

    """
    POST /stuff/add HTTP/1.1
    User-Agent: p4a browser ftw!
    Host: localhost:5000
    
    foo=bar
    """
    http_req = "POST /stuff/add HTTP/1.1\r\nUser-Agent: p4a browser ftw!\r\nHost: localhost:5000\r\n\r\nfoo=bar"
    req = Request(http_req)
    print(req.path)
    print(req.headers)
    print(req.body)
    print(req)

    res = Response(200)
    res.set_header('Content-Type', 'text/html')
    res.set_header('Server', 'p4a server ftw!')
    res.set_body('<h1>stuff</h1>')
    print(res)

    res = Response(777)
    res.set_body('everything is fine!')
    print(res)

    print(Response.STATUS_TEXT[200])
    print(Response.STATUS_TEXT[404])
