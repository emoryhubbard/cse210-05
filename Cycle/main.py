from casting.cast import Cast
from casting.player1 import Player1
from casting.player2 import player2
from scripting.script import Script
from scripting.move_actors_action import MoveActorsAction
from scripting.draw_actors_action import DrawActorsAction
from scripting.control_actors_action import ControlActorsAction
from Cycle.director import Director
from services.OutputService import OutputService
from services.InputService import InputService

from scripting.handle_collisions_action import handle_collision_actions

def main():

    cast = Cast()
    cast.add_actor("players", Player1())
    cast.add_actor("players", player2())
    #add more actors here

    output_service = OutputService()
    input_service = InputService()

    script = Script()
    script.add_action("input", ControlActorsAction(input_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("output", DrawActorsAction(output_service))
    script.add_action("update", handle_collision_actions())
    #add more scripts here, like collisions

    director = Director(output_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()