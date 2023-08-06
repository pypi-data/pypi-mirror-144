# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from ...BASE import ColorClass
from ...Functions.ColorConversion import (
    rgb_to_hexadecimal,
    rgb_to_hsl,
    rgb_to_cmyk,
    rgb_to_hsv
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def boundary(value:int|float) -> int|float:
    if 0 <= value <= 255:
        return value
    elif value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        ValueError("Value out of range")

class rgb(ColorClass):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,r:int|float,g:int|float,b:int|float):
        if isinstance(r, (int,float)) and isinstance(g, (int,float)) and isinstance(b, (int,float)):
            self.r = r
            self.g = g
            self.b = b
        else:
            raise ValueError("no int or float were given on rgb creation")

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def r(self):
        return self._r
    @r.setter
    def r(self, value:int|float):
        self._r = int(round(boundary(value)))

    @property
    def g(self):
        return self._g
    @g.setter
    def g(self, value: int | float):
        self._g = int(round(boundary(value)))

    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, value: int | float):
        self._b = int(round(boundary(value)))

    # ------------------------------------------------------------------------------------------------------------------
    # Special Methods
    # ------------------------------------------------------------------------------------------------------------------
    def decrease(self, value:float):
        if 0 > value or value > 1:
            raise ValueError("Value decreased can not be larger than 1 or smaller than 0")
        self.r -= self.r * value
        self.g -= self.g * value
        self.b -= self.b * value

    def increase(self, value:float):
        if 0 > value or value > 1:
            raise ValueError("Value increased can not be larger than 1 or smaller than 0")
        self.r += self.r * value
        self.g += self.g * value
        self.b += self.b * value

    # ------------------------------------------------------------------------------------------------------------------
    # Conversion Methods
    # ------------------------------------------------------------------------------------------------------------------
    def to_hexadecimal(self) -> str:
        return rgb_to_hexadecimal(
            r=self.r,
            g=self.g,
            b=self.b
        )
    def to_cmyk(self) -> tuple[float,float,float,float]:
        return rgb_to_cmyk(
            r=self.r,
            g=self.g,
            b=self.b
        )
    def to_hsl(self) -> tuple[float,float,float]:
        return rgb_to_hsl(
            r=self.r,
            g=self.g,
            b=self.b
        )
    def to_hsv(self) -> tuple[float,float,float]:
        return rgb_to_hsv(
            r=self.r,
            g=self.g,
            b=self.b
        )

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.r};{self.g};{self.b}"

    def __repr__(self) -> str:
        return f"rgb(r={self.r},g={self.g},b={self.b})"

    # Comparison operators
    # >
    def __gt__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) > (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) > (other + other + other)
        else:
            return NotImplemented

    # <
    def __lt__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) < (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) < (other + other + other)
        else:
            return NotImplemented

    # ==
    def __eq__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return all(((self.r == other.r), (self.g == other.g), (self.b == other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) == (other + other + other)
        else:
            return NotImplemented
    # !=
    def __ne__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return all(((self.r != other.r), (self.g != other.g), (self.b != other.b)))
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) != (other + other + other)
        else:
            return NotImplemented
    # <=
    def __le__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) > (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) > (other + other + other)
        else:
            return NotImplemented
    # >=
    def __ge__(self, other:rgb|int|float) -> bool:
        if isinstance(other, rgb):
            return (self.r + self.g + self.b) >= (other.r + other.g + other.b)
        elif isinstance(other, (int, float)):
            return (self.r + self.g + self.b) >= (other + other + other)
        else:
            return NotImplemented

    # math operators
    # +
    def __add__(self, other:rgb|int|float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r + other.r
            self.g = self.g + other.g
            self.b = self.b + other.b
            return self
        elif isinstance(other, (int,float)):
            self.r = self.r + other
            self.g = self.g + other
            self.b = self.b + other
            return self
        else:
            return NotImplemented
    # -
    def __sub__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r - other.r
            self.g = self.g - other.g
            self.b = self.b - other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r - other
            self.g = self.g - other
            self.b = self.b - other
            return self
        else:
            return NotImplemented
    # *
    def __mul__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r * other.r
            self.g = self.g * other.g
            self.b = self.b * other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r * other
            self.g = self.g * other
            self.b = self.b * other
            return self
        else:
            return NotImplemented
    # //
    def __floordiv__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r // other.r
            self.g = self.g // other.g
            self.b = self.b // other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r // other
            self.g = self.g // other
            self.b = self.b // other
            return self
        else:
            return NotImplemented
    # /
    def __truediv__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r / other.r
            self.g = self.g / other.g
            self.b = self.b / other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r / other
            self.g = self.g / other
            self.b = self.b / other
            return self
        else:
            return NotImplemented

    # %
    def __mod__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r % other.r
            self.g = self.g % other.g
            self.b = self.b % other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r % other
            self.g = self.g % other
            self.b = self.b % other
            return self
        else:
            return NotImplemented

    # **
    def __pow__(self, other: rgb | int | float) -> rgb:
        if isinstance(other, rgb):
            self.r = self.r ** other.r
            self.g = self.g ** other.g
            self.b = self.b ** other.b
            return self
        elif isinstance(other, (int, float)):
            self.r = self.r ** other
            self.g = self.g ** other
            self.b = self.b ** other
            return self
        else:
            return NotImplemented