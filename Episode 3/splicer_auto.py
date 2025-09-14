import os
import cv2
import ctypes


WIDTH, HEIGHT = 800, 1280 # Webtoons page size standard

# # CREATING OUTPUT DIRECTORY
if not os.path.exists("Spliced"):
    os.makedirs("Spliced")

for idx_img, file in enumerate(os.listdir('.')):
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
        image = cv2.imread(file)

        # COUNT NUMBER OF PAGES
        magnification = image.shape[1] // WIDTH
        if magnification == 0:
            print(f"❌ Error: Image {file} is too small to be spliced into {WIDTH}x{HEIGHT} pages.")
            input("Press Enter to exit...")
            exit(1)  
        if image.shape[1] % WIDTH != 0:
            print(f"⚠️ Warning: Image {file} width is not a multiple of {WIDTH}. The image will be squashed.")
            input("Press Enter to Continue...")
        if image.shape[0] % (HEIGHT * magnification) != 0:
            print(f"⚠️ Warning: Image {file} height is not a multiple of {HEIGHT}. The image will be squashed.")
            input("Press Enter to Continue...")
        pages = image.shape[0] // (HEIGHT * magnification)

        # RESIZE IMAGE
        image = cv2.resize(image, (WIDTH, HEIGHT*pages))

        # SPLICE IMAGE
        idx_page = 1
        for page in range(pages):
            spliced_img = image[(page)*HEIGHT:(page+1)*HEIGHT,:,:]
            cv2.imwrite(f"Spliced/{idx_img+1}.{idx_page}.png", spliced_img)
            idx_page += 1

# # REFRESHING EXPLORER
ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)

