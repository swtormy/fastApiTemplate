from typing import Union

from fastapi import FastAPI

import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/data/year={year}&entity={entity}")
def read_item(year: int, entity: str):
    if entity.lower() in ['russia', 'west', 'east', 'center', 'moscow', 'south'] \
    and len(str(year))==4 and year in [2020,2021,2022]:
        k = 1 if entity.lower() == 'russia' else 0.2
        return {
            "year": year,
            "entity": entity,
            "type": {
                "forecast":
                    [{"Jan": random.randint(1200000*k, 1400000*k)},
                     {"Feb": random.randint(1100000*k, 1300000*k)},
                     {"Mar": random.randint(1000000*k, 1100000*k)},
                     {"Apr": random.randint(900000*k, 1000000*k)},
                     {"May": random.randint(800000*k, 900000*k)},
                     {"Jun": random.randint(800000*k, 900000*k)},
                     {"Jul": random.randint(800000*k, 900000*k)},
                     {"Aug": random.randint(800000*k, 900000*k)},
                     {"Sep": random.randint(800000*k, 900000*k)},
                     {"Oct": random.randint(800000*k, 900000*k)},
                     {"Nov": random.randint(800000*k, 900000*k)},
                     {"Dec": random.randint(800000*k, 900000*k)}, ],
                "actual":
                    [{"Jan": random.randint(1200000*k, 1400000*k)},
                     {"Feb": random.randint(1100000*k, 1300000*k)},
                     {"Mar": random.randint(1000000*k, 1100000*k)},
                     {"Apr": random.randint(900000*k, 1000000*k)},
                     {"May": random.randint(800000*k, 900000*k)},
                     {"Jun": random.randint(800000*k, 900000*k)},
                     {"Jul": random.randint(800000*k, 900000*k)},
                     {"Aug": random.randint(800000*k, 900000*k)},
                     {"Sep": random.randint(800000*k, 900000*k)},
                     {"Oct": random.randint(800000*k, 900000*k)},
                     {"Nov": random.randint(800000*k, 900000*k)},
                     {"Dec": random.randint(800000*k, 900000*k)}, ],
                "budget":
                    [{"Jan": random.randint(1200000*k, 1400000*k)},
                     {"Feb": random.randint(1100000*k, 1300000*k)},
                     {"Mar": random.randint(1000000*k, 1100000*k)},
                     {"Apr": random.randint(900000*k, 1000000*k)},
                     {"May": random.randint(800000*k, 900000*k)},
                     {"Jun": random.randint(800000*k, 900000*k)},
                     {"Jul": random.randint(800000*k, 900000*k)},
                     {"Aug": random.randint(800000*k, 900000*k)},
                     {"Sep": random.randint(800000*k, 900000*k)},
                     {"Oct": random.randint(800000*k, 900000*k)},
                     {"Nov": random.randint(800000*k, 900000*k)},
                     {"Dec": random.randint(800000*k, 900000*k)}, ],
            },
        }

    else:
        return {
            'message': 'incorrect data'
        }
