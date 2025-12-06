1. create_new_episode
Create a new episode. It's designed for Webtoon episodes.
The script will automatically create a folder template for a new episode
containing various useful Python scripts.
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

4. create_krita_files
Automatically creates a specified number of Krita files with the dimensions:
BASE WIDTH X SCALE X (BASE HEIGHT X SCALE X PAGES). 
Each of these variables is customizable as an option. 
Base Width and Base Height are multiplied by Scale to get the final size of a page.
A higher scale allows you to create more detailed images, which can translate to higher
quality images after resize.

5. export_images
Export saved images from all Krita files in the directory.
Place this script in the same directory as your .kra files and run it.
The exported images will be saved as .png files with the same name as the .kra files in
the same directory. 
