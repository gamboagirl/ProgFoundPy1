import time
import webbrowser

breaks = 3; # total number of breaks that this will run
break_cnt = 0; # current break count

# note the time this starts
print("This program started on " + time.ctime())

# run this the number of total breaks
while (break_cnt < breaks):
    # sleep for 2 hours (7200 seconds) between loops
    time.sleep(7200)
    # open the web browser to a Rick roll
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # increment the break count by 1
    break_cnt = break_cnt + 1
