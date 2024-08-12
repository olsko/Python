import ctypes
import win32gui

from PIL import Image

def get_window_rect(hwnd):
    """Get the rectangle of the window with the specified handle."""
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return (x, y, w, h)

def take_screenshot(hwnd):
    """Take a screenshot of the window with the specified handle."""
    # Get the dimensions of the window
    rect = get_window_rect(hwnd)
    x, y, w, h = rect
    
    # Create a device context for the window
    hdc = ctypes.windll.user32.GetDC(hwnd)
    
    # Create a device context for the screen
    hdc_screen = ctypes.windll.user32.GetDC(0)
    
    # Create a memory device context
    hdc_mem = ctypes.windll.gdi32.CreateCompatibleDC(hdc_screen)
    
    # Create a bitmap
    hbitmap = ctypes.windll.gdi32.CreateCompatibleBitmap(hdc_screen, w, h)
    
    # Select the bitmap into the memory device context
    hbitmap_old = ctypes.windll.gdi32.SelectObject(hdc_mem, hbitmap)
    
    # Copy the window to the memory device context
    ctypes.windll.user32.PrintWindow(hwnd, hdc_mem, 0)
    
    # Create a BITMAPINFO structure
    class BITMAPINFO(ctypes.Structure):
        _fields_ = [
            ('bmiHeader', ctypes.c_ulong),
            ('bmiColors', ctypes.c_ulong * 3),
        ]
    bitmap_info = BITMAPINFO()
    
    # Set the BITMAPINFO structure fields
    bitmap_info.bmiHeader = ctypes.sizeof(BITMAPINFO)
    ctypes.windll.gdi32.GetDIBits(hdc_mem, hbitmap, 0, h, ctypes.byref(bitmap_info), ctypes.byref(bitmap_info), 0)
    
    # Create an image from the bitmap
    image = Image.frombuffer('RGB', (w, h), bitmap_info, 'raw', 'BGRX', 0, 1)
    
    # Clean up
    ctypes.windll.gdi32.SelectObject(hdc_mem, hbitmap_old)
    ctypes.windll.gdi32.DeleteObject(hbitmap)
    ctypes.windll.gdi32.DeleteDC(hdc_mem)
    ctypes.windll.user32.ReleaseDC(0, hdc_screen)
    ctypes.windll.user32.ReleaseDC(hwnd, hdc)
    
    # Save the image to a file
    image.save('screenshot.png')

# Find the window with the specified title
hwnd = win32gui.FindWindow(None, 'Kalkulator')

# Take a screenshot of the window
take_screenshot(hwnd)