from python_cnc.cuts.image import Image
from python_cnc.utils.frange import frange

cut = Image(rpm=1000, feed_rate=300, depth=5, depth_per_cut=1)
print(cut.build(image_path='cage.jpg', scale=0.2))
