from functools import total_ordering


@total_ordering
class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __lt__(self, other):
        return self.top*other.bottom < self.bottom*other.top

    def __eq__(self, other):
        return self.top*other.bottom == self.bottom*other.top
