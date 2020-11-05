import PIL

from .raster import Raster
from ..utils.frange import frange
from ..utils.format_point import format_point
from ..utils.prelude import reset_position

def open_image(image_path):
    return PIL.Image.open(image_path).convert('L')

def get_coordinate(x, y, image, scale):
    return image.getpixel((x//scale, y//scale))/255

class Image(Raster):
    def make_cut(self, image_path, scale):
        image = open_image(image_path)
        def function(x, y):
            return get_coordinate(x, y, image, scale)
        super().make_cut(function, (scale*image.size[0]-1, scale*image.size[1]-1))
