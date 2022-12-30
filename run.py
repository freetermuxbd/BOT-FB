import os, sys 
print ("\t\033[1;35mChecking for Update")
os.system("git pull")
try:
    __import__("bot").main()
          baner()
    
