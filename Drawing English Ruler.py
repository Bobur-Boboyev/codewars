class Ruler:
    def __init__(self, t: int, n: int):
        """
        Args:
            t: major tick length (>= 2)
            n: number of inches (>= 1)
        """
        if t < 2:
            raise ValueError("t must be >= 2")
        if n < 1:
            raise ValueError("n must be >= 1")
        self.t = t
        self.n = n

    def draw(self) -> str:
        
        def draw_interval(length):
            if length == 0:
                return []
            return draw_interval(length-1) + ['-'*length] + draw_interval(length-1)

        lines = []
        for i in range(self.n + 1):
            lines.append('-'*self.t + f" {i}")
            if i != self.n:
                lines += draw_interval(self.t-1)
        return '\n'.join(lines)