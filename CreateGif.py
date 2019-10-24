import glob
from PIL import Image

fp_in = "C:/Users/Zulman/Desktop/PythonScripts/screenshot/image_*.png"
fp_out = "C:/Users/Zulman/Desktop/PythonScripts/screenshot/image.gif"

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp_out, format='GIF', append_images=imgs, save_all=True, duration=200, loop=0)