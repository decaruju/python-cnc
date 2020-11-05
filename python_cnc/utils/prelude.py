from .format_point import format_point

def prelude(rpm, feed_rate):
    return [
        'G90',
        f'M03 S{rpm}',
        f'F{feed_rate}'
    ]

def end():
    return [
        *reset_position(),
        'M5',
    ]

def reset_position():
    return [
        format_point(z=3),
        format_point(x=0, y=0),
    ]
