from __future__ import annotations


class Distance:
    def __init__(self, km: int | float):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: int | float) -> Distance:
        return self.add(other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: int | float) -> Distance:
        return self.mul(other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        val = other.km if isinstance(other, Distance) else other
        return self.km < val

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        val = other.km if isinstance(other, Distance) else other
        return self.km > val

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        val = other.km if isinstance(other, Distance) else other
        return self.km == val

    def __le__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        val = other.km if isinstance(other, Distance) else other
        return self.km <= val

    def __ge__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        val = other.km if isinstance(other, Distance) else other
        return self.km >= val
