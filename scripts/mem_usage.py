import sys
from resource import getrusage, RUSAGE_SELF
import numpy as np

from skimage import data
from skimage.feature import register_translation
from scipy.ndimage import fourier_shift
from skimage.transform import rescale

# Load and resize a sample image included in scikit-image:
image = data.camera()
image = rescale(image, int(sys.argv[1]), anti_aliasing=True)

# Register the image against itself; the answer should
# always be (0, 0), but that's fine, right now we just care
# about memory usage.
shift, error, diffphase = register_translation(image, image)

print("Image size (Kilo pixels):", image.size / 1024)
print("Peak memory (MiB):",
      int(getrusage(RUSAGE_SELF).ru_maxrss / 1024))
