import os
import cv2
import ctypes

'''
This script splices images into multiple pages of standard Webtoons size (800x1280).

Place the images you want to splice in the same directory as this script and run it.
The spliced images will be saved in a folder named "Spliced".
Large images will be resized to fit the standard size. If you want to do this, make sure  
the image dimensions are a multiple of the standard size (800x1280). 
If not, the image will be squashed to fit the standard size.
'''

WIDTH, HEIGHT = 800, 1280 # Webtoons page size standard

# # CREATING OUTPUT DIRECTORY
if not os.path.exists("Spliced"):
    os.makedirs("Spliced")

idx_img = 1
for file in os.listdir('.'):
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
        image = cv2.imread(file)

        # COUNT NUMBER OF PAGES
        scale = image.shape[1] // WIDTH
        pages = image.shape[0] // (HEIGHT * scale)

        if scale == 0 or pages == 0:
            print(f"❌ Error: Image {file} is in the wrong orientation or is too small to be spliced into {WIDTH}x{HEIGHT} pages.")
            input("Press Enter to exit...")
            exit(1)  
        if image.shape[1] % WIDTH != 0:
            print(f"⚠️ Warning: Image {file} width is not a multiple of {WIDTH}. The image will be squashed.")
            input("Press Enter to Continue...")
        if image.shape[0] % (HEIGHT * scale) != 0:
            print(f"⚠️ Warning: Image {file} height is not a multiple of {HEIGHT}. The image will be squashed.")
            input("Press Enter to Continue...")

        # RESIZE IMAGE
        image = cv2.resize(image, (WIDTH, HEIGHT*pages))

        # SPLICE IMAGE
        idx_page = 1
        for page in range(pages):
            spliced_img = image[(page)*HEIGHT:(page+1)*HEIGHT,:,:]
            cv2.imwrite(f"Spliced/{idx_img}.{idx_page}.png", spliced_img)
            idx_page += 1
        idx_img += 1

# # REFRESHING EXPLORER
ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)

