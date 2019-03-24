""" Abstract base class file. All other classes should derive from Scraper, and must have all methods defined in it. """

# TODO : Put TODOs at the top of files in this format
# TODO : method describing where data goes once it's got?
# TODO : data_dir property

from abc import ABC, abstractmethod
import numpy as np
from pathlib import Path

class ABCScraper(ABC):
    def __init__(self):
        # Initialized on first access
        self._data_dir = None

    @abstractmethod
    def get_data(self, url):
        """Abstract method ~ 
        Return a numpy.ndarray object populated from 
        a known website pointed to by url."""
        pass

    @property
    def data_dir(self):
        """ 
        Top-level directory where data is stored.
        If directory doesn't exist, create it.
        """
        if not self._data_dir:
            p = Path.home() / '.data_dir'
            if not p.is_dir():
                p.mkdir()
                self._data_dir = str(p)
        return self._data_dir

        