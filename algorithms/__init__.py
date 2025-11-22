# algorithms/__init__.py
# This file marks the folder as a package
from .sorting .insertionsort import insertion_sort
from .sorting .quicksort import quick_sort
from .sorting .bubblesort import bubble_sort
from .sorting .mergesort import merge_sort
from .sorting .selectionsort import selection_sort
from .graphs .bfs import bfs
from .graphs .dfs import dfs
from .graphs .dijkstra import dijkstra
from .graphs .unionfind import unionfind

__all__ = ["bubble_sort", "merge_sort", "selection_sort", "insertion_sort", "quick_sort", "bfs", "dfs", "dijkstra", "unionfind"]
