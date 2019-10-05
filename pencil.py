class Pencil:

    def __init__(self, point_durability=40000, length=40):
        self._point_durability = point_durability
        self._length = length
        self._initial_durability = point_durability

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def point_durability(self):
        return self._point_durability

    @point_durability.setter
    def point_durability(self, point_durability):
        self._point_durability = point_durability

    def write(self, text, paper):
        for char in text:
            self.write_char(char, paper)

    def calculate_write_cost(self, char):
        if char.isupper() or char.isnumeric():
            return 2
        elif char.islower():
            return 1
        else:
            return 0

    def write_char(self, char, paper):
        if self.calculate_write_cost(char) > self.point_durability:
            paper.text += ' '
        else:
            self.point_durability -= self.calculate_write_cost(char)
            paper.text += char

    def sharpen(self):
        if self.length>0:
            self.point_durability=self._initial_durability
            self.length-=1
