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


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
