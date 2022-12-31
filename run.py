import os,platform
os.system('clear')
print('\033[1;36m[•] \033[1;32mChecking Updates...')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    print('\033[1;32m[•] Congrats! Your Device Support This Tools')
    os.system('xdg-open https://facebook.com/groups/590005482506415/')
    import bot
    bot.menu()
