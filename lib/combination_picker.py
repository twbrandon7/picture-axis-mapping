from typing import List, Any
from collections import OrderedDict


class CombinationPicker:
    def __init__(self, candidates: "OrderedDict[str, List[Any]]") -> None:
        self._candidates = candidates
        self.__all_combination_counts_cache: int | None = None

    @property
    def all_combination_counts(self) -> int:
        if self.__all_combination_counts_cache is not None:
            return self.__all_combination_counts_cache
        total = 1
        for candidate in self._candidates.values():
            total *= len(candidate)
        self.__all_combination_counts_cache = total
        return total

    def pick_combination(self, index: int) -> OrderedDict[str, Any]:
        if index >= self.all_combination_counts:
            raise ValueError("Index out of range")
        result = OrderedDict()
        for key, candidate in self._candidates.items():
            result[key] = candidate[index % len(candidate)]
            index //= len(candidate)
        return result
