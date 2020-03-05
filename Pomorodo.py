import time
import webbrowser

count = 1
times_break = 5
while count < times_break:
    print 'Begin ', count, 'Pomorodo', '- Current time: ', time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=Tjbdg1emdzo")
    time.sleep(25*60)
    if count == 4:
        print 'Take a long break: 20 mitues'
        webbrowser.open('https://www.youtube.com/watch?v=I2X2SoLEK6E')
        break
    print 'Take a short break: 5 minutes'
    webbrowser.open('https://www.youtube.com/watch?v=Tjbdg1emdzo')
    time.sleep(5*60)
    count += 1

