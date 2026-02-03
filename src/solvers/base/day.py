"""Base Day class"""

from abc import ABCMeta, abstractmethod
from solvers.base.types import SolveInfo


# pylint: disable=R0903,C0115
class Day(metaclass=ABCMeta):
    @abstractmethod
    def solve(self) -> SolveInfo:
        pass
