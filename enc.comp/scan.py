import os

db = os.getcwd() + '/db/'
count = 0


def scan_dir(dir):
    filestr = ''
    for filename in os.listdir(dir):
        _f = os.path.join(dir, filename)
        _s = os.path.join(dir, filename)
        # checking if it is a file
        if os.path.isfile(_f):
            print('FILE:', _f)
            filestr += '<br>' + _f.removeprefix('C:\PyDev\\Network/')        
            
        if os.path.isdir(_s):
            print('DIR:', _s)
            filestr += '<br>' + _f.removeprefix('C:\PyDev\\Network/')
            filestr += scan_dir(_s)

    return filestr


_fil = open(os.getcwd() + '/server/' + '/scan/db_scanned.html', 'w')
_fil.write(scan_dir(db))
_fil.close()