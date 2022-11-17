def is_close(self, x, otherx):
        is_close = False
        precision = 25
        lower_limit = otherx - precision
        upper_limit = otherx + precision
        
        if self.is_close(int(collision_p.x), int(player_p.x)) and self.is_close(int(collision_p.y), int(player_p.y)):
            if lower_limit <= x <= upper_limit:
                is_close = True
            return is_close