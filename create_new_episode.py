import os
import ctypes
import shutil
import re

'''
Create a new episode. It's designed for Webtoon episodes.

The script will automatically create a folder template for a new episode
containing an empty folder (meant for Krita Files) alongside useful Python scripts.

It will automatically detect the last available episode,
searching for the "Episode X" format, and creating "Episode X+1".
'''

dirs = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('Episode ')]
last_episode_num = re.findall(r'\d+$', dirs[-1]) if len(dirs) > 0 else ['0']
current_episode_num = int(last_episode_num[0]) + 1 if last_episode_num and last_episode_num[0].isdigit() else 1
episode_name = "Episode " + str(current_episode_num)

if not os.path.exists(episode_name):
    os.makedirs(episode_name)
    os.makedirs(f"{episode_name}/Krita Files")

if os.path.isfile("splicer_auto.py") and os.path.isfile("refresh.py"):
    shutil.copy("splicer_auto.py", f"{episode_name}/splicer_auto.py")
    shutil.copy("refresh.py", f"{episode_name}/refresh.py")
else:
    print("Error: splicer_auto.py or refresh.py not found in the current directory.")
    input("Press Enter to exit...")
    exit(1)

ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)