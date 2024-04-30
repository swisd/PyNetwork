import os

db = os.getcwd() + '/db/'
count = 0
_fil = open('C:/Network/server/scan/db_scanned.html', 'w')

_fil.write('<html><head><style>body{margin:4px;font-family:"OCR A";}</style></head>')

def scan_dir(dir):
    filestr = ''
    for filename in os.listdir(dir):
        _f = os.path.join(dir, filename)
        _s = os.path.join(dir, filename)
        # checking if it is a file
        if os.path.isfile(_f):
            print('FILE:', (_f.removeprefix('C:\\')).removeprefix('Network/'))
            filestr += '<br>' + (_f.removeprefix('C:\\')).removeprefix('Network/')        
            
        if os.path.isdir(_s):
            print('DIR:', _s)
            filestr += '<br>' + (_f.removeprefix('C:\\')).removeprefix('Network/')
            filestr += scan_dir(_s)

    return filestr



_fil.write(scan_dir(db))
_fil.write('</body></html>')
_fil.close()