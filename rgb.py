# Convert images

# I'd start by using glob

from PIL import Image
import glob
for filename in glob.glob('/Users/mimireyburn/images/cars/*.jpg'): # assuming gif
    img = Image.open(filename).convert('RGB')
    img.save(filename)
