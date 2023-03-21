class Entry:
    def __init__(self, date, close: float):
        self.date = date
        self.close = close
    
    def __get_date(self):
        return self.date
    
    def __get_close(self) -> float:
        return self.close