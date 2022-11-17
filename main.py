from cast import Cast
from player1 import Player1
from script import Script
from move_actors_action import MoveActorsAction
from draw_actors_action import DrawActorsAction
from director import Director
from OutputService import OutputService

def main():

    cast = Cast()
    cast.add_actor("players", Player1())
    #add more actors here

    output_service = OutputService()
    #add other service here

    script = Script()
    script.add_action("update", MoveActorsAction())
    script.add_action("output", DrawActorsAction(output_service))
    #add more scripts here, like collisions

    director = Director(output_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()