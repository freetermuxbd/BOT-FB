import os, sys 
print ("\t\033[1;35mChecking for Update")
os.system("git pull")
try:
    __import__("h4x").main()
except Exception as e:
    print(f"{er}{e}")
