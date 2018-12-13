import os 
from datetime import datetime

created = os.stat('date.py').st_ctime

print(datetime.fromtimestamp(created))