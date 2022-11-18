import constants
from player1 import Player1
from player2 import player2
from action import Action
from point import Point

class handle_collision_actions(Action):


    def __init__(self):
        self._game_over = False

    def execute(self, script, collision_cast):

        if not self._game_over:
            self._handle_segment_collision(collision_cast)
            self._handle_game_over(collision_cast)

    def _handle_segment_collision(self, collision_cast):

        bike = collision_cast
        head = bike.get_segments()[0]
        segments = bike.get_segments()[1]
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._game_over = True


    def _handle_game_over(self, collision_cast):

        if self._game_over:
            bike = collision_cast("bike")
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x,y)

            message = Player1()
            message = player2()
            message.set_text("The Game is Over!")
            message.set_postition(position)