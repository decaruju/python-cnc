from PIL import Image

from .cut import Cut
from ..utils.frange import frange
from ..utils.format_point import format_point
from ..utils.prelude import reset_position


class Raster(Cut):
    def make_cut(self, function, bounds):
        for depth in frange(-1, -self.depth, -self.depth_per_cut):
            self.add_commands(*reset_position())
            for x in frange(0, bounds[0]//10, 0.2):
                for y in frange(0, bounds[1]//10, 0.1):
                    actual_depth = max(depth, function(x, y)*self.depth-self.depth)
                    self.add_commands(format_point(x=x, y=y, z=actual_depth))
                x += 0.1
                for y in frange(bounds[1]//10, 0, -0.1):
                    actual_depth = max(depth, function(x, y)*self.depth-self.depth)
                    self.add_commands(format_point(x=x, y=y, z=actual_depth))
