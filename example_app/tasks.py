import time
import datetime
from .models import MyLog

def log_save(message):
    time.sleep(5)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    MyLog(log_txt=f"{date_str} {message}").save()
