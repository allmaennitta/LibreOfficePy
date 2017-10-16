class Page:
    def __init__(self, uno_page, index: int):
        self._uno_page = uno_page
        self._index = index

    @property
    def uno_page(self):
        return self._uno_page