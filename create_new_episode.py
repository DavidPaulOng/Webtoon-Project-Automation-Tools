import os
import ctypes
import shutil
import re
import json

'''
Create a new episode. It's designed for Webtoon episodes.

The script will automatically create a folder template for a new episode
containing various useful Python scripts.

It will automatically detect the last available episode,
searching for the "Episode X" format, and creating "Episode X+1".
'''

TEMPLATE_PATH = "templates"

# GET CURRENT EPISODE NUMBER
dirs = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('Episode ')]
last_episode_num = re.findall(r'\d+$', dirs[-1]) if len(dirs) > 0 else ['0']
current_episode_num = int(last_episode_num[0]) + 1 if last_episode_num and last_episode_num[0].isdigit() else 1
episode_name = "Episode " + str(current_episode_num)

# CREATE EPISODE FOLDER
if not os.path.exists(episode_name):
    os.makedirs(episode_name)

# COPY FILES
for dir in os.listdir(TEMPLATE_PATH):
    if dir.endswith('.py'):
        print(dir)
        shutil.copy(f"{TEMPLATE_PATH}/{dir}", f"{episode_name}/{dir}")

ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)