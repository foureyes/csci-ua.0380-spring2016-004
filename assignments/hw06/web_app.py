from web_objects import Request, Response
import random
        
# routes contains mappings of paths to functions
# for example, the path /dice would map to a function called dice:
# {'/dice': dice}
# that function will be called to generate a response
routes = {}

def route(method, path):
    """decorator (with parameter) for used to map a path to a function
    """
    def decorator(old_f):
        # add path and function to routes dictionary
        routes[method, path] = old_f

        # just give back the old function unmodified
        return old_f

    return decorator

@route('GET', '/')
def home(req, res):
    html = 'The homepage! '
    html += 'Check out <a href="/creatures">creatures</a> '
    html += 'or <a href="/dice">dice</a>.'
    res.set_body(html)
    return res

@route('GET', '/creatures')
def creatures(req, res):
    creatures = ["griffin", "zombie", "skeleton", "unicorn", "yeti"]
    html = 'You encounter these creatures! <ul>'
    for i in range(random.randint(1, 4)):
        html += '<li>{}</li>'.format(creatures[random.randint(0, len(creatures) - 1)])
    html += '</ul>'
    res.set_body(html)
    return res

@route('GET', '/dice')
def dice(req, res):
    html = "Dice Roll: {}".format(random.randint(1, 6))
    res.set_body(html)
    return res

def handle_request(http_request):
    req = Request(http_request)
    route_handler = routes.get((req.method, req.path))

    if route_handler and req.headers['Host'] == 'localhost:5000':
        res = Response(200)
        res = route_handler(req, res)
        res.set_header('Content-Type', 'text/html')
    elif req.headers['Host'] != 'localhost:5000':
        res = Response(400)
        res.body = "Bad Request"
    elif not route_handler:
        res = Response(404)
        res.body = "Not Found"
    return str(res)

