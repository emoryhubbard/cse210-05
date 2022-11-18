from scripting.action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        player1 = cast.get_first_actor("players")

        self._output_service.clear_buffer()
        self._output_service.draw_actor(player1)
        self._output_service.flush_buffer()