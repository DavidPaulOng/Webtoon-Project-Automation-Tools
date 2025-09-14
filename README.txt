1. create_new_episode
Create a new episode. It's designed for Webtoon episodes.
The script will automatically create a folder template for a new episode
containing an empty folder (meant for Krita Files) alongside useful Python scripts.
It will automatically detect the last available episode,
searching for the "Episode X" format, and creating "Episode X+1".

2. refresh
Refresh Windows Explorer to reflect changes made to files or directories.
Folders are files are created or deleted programmatically,
Windows Explorer may not immediately reflect these changes.
This script forces Windows Explorer to refresh and display the updated contents.

3. splicer_auto
This script splices images into multiple pages of standard Webtoon size (800x1280).
Place the images you want to splice in the same directory as this script and run it.
The spliced images will be saved in a folder named "Spliced".
Large images will be resized to fit the standard size. If you want to do this, make sure
the image dimensions are a multiple of the standard size (800x1280).
If not, the image will be squashed to fit the standard size.