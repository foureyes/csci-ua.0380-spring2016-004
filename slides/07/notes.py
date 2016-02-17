"""
## file and open
* file object
* open
* r, w, a
* remember to close

## read
* reading 
* for loop
* readlines
* readline
* read

## write
with open('foo.txt', 'w') as f:
    f.write("bar")


urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)



## split

## csv
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

response = request.urlopen('http://data.nba.com/data/15m/json/cms/noseason/game/20121126/0021200013/boxscore.json')
response.read()
json.dumps
json.loads

>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
        >>> r.json()



"""
