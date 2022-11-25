<<<<<<< HEAD
#!/usr/bin/python3
"""Send POST"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
=======
#!/usr/bin/python3
"""Send POST"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
        
>>>>>>> 791e1c6f28ca08dc827c57208d1108bdb220cc1d
