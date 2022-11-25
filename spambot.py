import time
import webbrowser

print('██     ██  ██████  ██████  ██      ██████   ██     ██  █████  ██      ██          ██████   ██████  ████████ ')
print('██     ██ ██    ██ ██   ██ ██      ██   ██  ██     ██ ██   ██ ██      ██          ██   ██ ██    ██    ██')
print('██  █  ██ ██    ██ ██████  ██      ██   ██  ██  █  ██ ███████ ██      ██          ██████  ██    ██    ██  ')
print('██ ███ ██ ██    ██ ██   ██ ██      ██   ██  ██ ███ ██ ██   ██ ██      ██          ██   ██ ██    ██    ██  ')
print(' ███ ███   ██████  ██   ██ ███████ ██████    ███ ███  ██   ██ ███████ ███████     ██████   ██████     ██   ')
print('')
print('████████████████████████████████████████████████████████████████████████████████████████████████████████████')

game = input('Input the game type:')

code = input('Iput the game id:')

prefix = input('Enter bot prefix:')

if game == 'maze':
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '1&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '2&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '3&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '4&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '5&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '6&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '7&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '8&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '9&mode=1&activityId=' + code + '&templateId=49')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '10&mode=1&activityId=' + code + '&templateId=49')

    done = 'true'

elif game == 'missing word':
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '1&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '2&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '3&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '4&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '5&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '6&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '7&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '8&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '9&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    webbrowser.open('https://wordwall.net/leaderboardajax/addentry?score=999999999&time=999999999&name=' + prefix + '10&mode=1&activityId=' + code + '&templateId=36')
    time.sleep (0.1)
    done = 'true'
    

else:
    print('invalid input')
    done = 'false'

time.sleep (2)

if done == 'true':
    print("done")

input('Press any key to exit:')
