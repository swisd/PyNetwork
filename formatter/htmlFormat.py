# similar to scan.py

import os

def scan_dir(dir: str) -> None:
    filestr = ''
    for filename in os.listdir(dir):
        _f = os.path.join(dir, filename)
        _s = os.path.join(dir, filename)
        # checking if it is a file
        if os.path.isfile(_f):
            if not dir.startswith("C:/Network/.git") or dir.startswith("C:/Network/.venv") or ".gitignore" in filename:
                print("FILE:", _f)
                with open(_f, "r", errors='ignore') as readr:
                    temp_str = readr.read()

                if not os.path.exists((_f.replace("C:/Network/", "C:/Network/pages/"))):
                    os.makedirs((_f.replace("C:/Network/", "C:/Network/pages/")))

                with open((_f.replace("C:/Network/", "C:/Network/pages/")) + ".html", "x", errors='ignore') as file:
                    file.write("<body><plaintext>" + temp_str)
                    file.close()


        if os.path.isdir(_s):
            print('DIR:', _s)
            scan_dir(_s)


scan_dir("C:/Network/")