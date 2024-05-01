#!/usr/bin/env python3
"""
This module provides index_range function
"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """init
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return dataset in a range according to args.
        """
        if not all(isinstance(i, int) for i in [page, page_size]):
            raise AssertionError
        assert all(i > 0 for i in [page, page_size])
        dataset = self.dataset()
        page_num = len(dataset)
        page_range = index_range(page, page_size)
        if page_num < page_range[0]:
            return []
        start_index = page_range[0]
        end_index = page_range[1]
        return dataset[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Create an obj including pagination info and return it.
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        page_range = index_range(page, page_size)
        next_page = page + 1 if len(data) else None
        prev_page = page - 1 if page != 1 else None
        total_pages = math.ceil(len(dataset) / page_size)
        return {
            'page_size': page_size if len(data) else 0,
            'page': page,
            'data': data,
            'next_page': next_page if page < total_pages else None,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
