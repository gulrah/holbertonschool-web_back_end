#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

from typing import List, Dict
from .1-simple_pagination import Server


class Server(Server):
    """
    Server class to paginate a database of popular baby names.
    """
    
    def __init__(self):
        super().__init__()
        self.__indexed_dataset = None
        
    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset
        
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return deletion-resilient hypermedia pagination."""
        assert index is None or 0 <= index < len(self.dataset()), "Index out of range"
        data = []
        next_index = None
        
        if index is not None:
            data = [self.indexed_dataset()[i] for i in range(index, min(index + page_size, len(self.dataset())))]
            next_index = min(index + page_size, len(self.dataset()))
            
        hyper_dict = {
            "index": index if index is not None else 0,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
        return hyper_dict
