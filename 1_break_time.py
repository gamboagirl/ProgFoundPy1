import time
import webbrowser

breaks = 3;
break_cnt = 0;

print("This program started on " + time.ctime())
while (break_cnt < 3):
    # sleep for 2 hours between loops
    time.sleep(7200)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_cnt = break_cnt + 1
