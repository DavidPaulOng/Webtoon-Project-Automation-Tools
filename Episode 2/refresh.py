import ctypes
ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)
