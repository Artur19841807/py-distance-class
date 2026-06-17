from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: int | float) -> Distance:
        return self.add(other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

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

    def _get_other_km(self, other: Distance | int | float) -> int | float | type(NotImplemented):
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        val = self._get_other_km(other)
        return self.km < val if val is not NotImplemented else NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        val = self._get_other_km(other)
        return self.km > val if val is not NotImplemented else NotImplemented

    def __eq__(self, other: object) -> bool:
        val = self._get_other_km(other)
        return self.km == val if val is not NotImplemented else NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        val = self._get_other_km(other)
        return self.km <= val if val is not NotImplemented else NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        val = self._get_other_km(other)
        return self.km >= val if val is not NotImplemented else NotImplemented
