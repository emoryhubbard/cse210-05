import constants
from color import Color
from point import Point

class player2:



    def __init__(self):

        self._text = ""
        self._font_size = 15
        self._color = Color(300,300,300)
        self._position = Point(0,0)
        self._velocity = Point(0,0)
    
    def get_color(self):

        return self._color

    def get_font_size(self):

        return self._font_size

    def get_postion(self):

        return self._position

    def get_velocity(self):

        return self._velocity

    def move_next(self):

        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_X

    def set_color(self,color):

        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self,font_size):

        self._font_size = font_size

    def set_velocity(self, velocity):

        self._velocity = velocity

    def set_text(self, text):

        self._text = text