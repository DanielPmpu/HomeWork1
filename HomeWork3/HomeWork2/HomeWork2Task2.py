from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date_period in self.dates:
            n = 0
            while date_period[0] + timedelta(days=n) <= date_period[1]:
                yield date_period[0] + timedelta(days=n)
                n += 1


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

if __name__ == '__main__':
    for d in m.schedule():
        print(d)
