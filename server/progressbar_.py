from time import sleep
from colorama import Fore
from random import randint

def bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '/', printEnd = "", data=False):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = Fore.GREEN + (fill * filledLength) + (Fore.WHITE + ' ' * (length - filledLength))
    if not data:
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    else:
        print(f'\r{prefix} |{bar}| {percent}% {round(iteration/0.80, 1):<4}/{round(total/0.80, 1):<4}KB', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def selfbar(wait):
    var = ''
    char = "#"
    for i in range(20):
        var += char
        print(f"\r|{var:-<20}|{round(len(var)/20, 2)*100}% {round(len(var)/0.80, 2)} KB           ", end="")
        sleep(wait)
