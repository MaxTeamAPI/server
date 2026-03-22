from .main import MainProcessors
from .auth import AuthProcessors
from .search import SearchProcessors

class Processors(MainProcessors, AuthProcessors, SearchProcessors):
    pass