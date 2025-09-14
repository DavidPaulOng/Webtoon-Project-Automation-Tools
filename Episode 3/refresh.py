'''
Refresh Windows Explorer to reflect changes made to files or directories.

Folders are files are created or deleted programmatically, 
Windows Explorer may not immediately reflect these changes. 
This script forces Windows Explorer to refresh and display the updated contents.
'''

import ctypes
ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)
