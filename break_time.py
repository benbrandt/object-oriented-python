import time
import webbrowser

breaks = 0

while breaks < 3:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    breaks += 1
