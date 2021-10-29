"""Simple implementation of a webscraping python application"""

import time
import webbrowser



total_break = 3
break_count = 0
print("This program began to run at:", time.ctime())
while break_count<total_break:
    print("This program began to run at:", time.ctime())
    time.sleep(5)
    webbrowser.open("http://www.google.com")
    break_count += 1
