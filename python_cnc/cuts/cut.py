from ..utils.prelude import prelude, end

class Cut:
    def __init__(self, rpm, feed_rate, depth, depth_per_cut):
        self.output = ''
        self.add_commands(*prelude(rpm, feed_rate))
        self.depth = depth
        self.depth_per_cut = depth_per_cut

    def build(self, *args, **kwargs):
        self.make_cut(*args, **kwargs)
        self.add_commands(*end())
        return self.output

    def add_commands(self, *commands):
        for command in commands:
            self.output += command
            self.output += '\n'

    def make_cut(self):
        pass

