* homework
* examples: gather_strings, all_your_returns_are
* nonlocal
* kwargs
* __name__ and __docstring__
* functools wraps
* parameters to decorators
* classes / callables
* bytes ... represent immutable sequence of 1's and 0's!
    * b'abcde'
    * b"abcde".decode("utf-8") 
    * how are numbers rep'd?
    * how about characters?
    * encoding / scheme to map data to number
    * \x41 ... means upcoming number is hex
    *  b.decode('utf-8')
{% comment %}
    >>> b = b'\x41\x41'
    >>> b
    b'AA'
    >>> str(b)
    "b'AA'"
    >>> b + "asdf"
{% endcomment %}
    * encode byte (...)
* networked computers
    * internet
    * protocols
    * communicate via tcp ip - governs communication
        * format
        * semantics
    * start off higher level than actual protocol... but with just a connection
    * what's a server?
    * a client?
    * what's a socket?
        * abstraction for communication end point
        * port and address
        * address is host name that identifies a computer, ip address
        * port allows multiple services to be
    * connection 
        * 2 end points... socket pair, 4 parts
        * ids two end points of tcp ip connection
    * python's socket library
    * ephemeral port
    * send deals with bytes
    * server
        * create a socket
        * bind the socket to an address and port
        * listen for incoming connections
        * wait for clients (while)
        * accept a client
        * receive and send data (recv, send)
    * client
        * create a socket
        * bind the socket to an address and port
        * send and receive data
    * hello world
        * server just sends back hello (remember, it's in bytes)
        * connect with nc
        * connect with browser 
    * echo server
        * connect with nc
        * connect with browser (erm what happened here?)
    * shout server (uppercase and add exclamation)
    * math server 
        * MULTIPLY, ADD
        * respond with ANSWER .... or ERROR
* http
    * request response
    * req... 
        * request line method path version
        * optional headers
        * body
    * res...
        * status line version statuscode reason
        * optional headers
        * body
    * connect to cs.nyu.edu
        * netcat
    * response codes
* now


