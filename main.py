from typing import Union

from fastapi import FastAPI

import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/data/year={year}&entity={entity}")
def read_item(year: int, entity: str):
    if entity.lower() in ['russia', 'west', 'east', 'center', 'moscow', 'south']:
        return {
            "year": year,
            "entity": entity,
            "type": {
                "forecast":
                    [{"Jan": random.randint(1200000, 1400000)},
                     {"Feb": random.randint(1100000, 1300000)},
                     {"Mar": random.randint(1000000, 1100000)},
                     {"Apr": random.randint(900000, 1000000)},
                     {"May": random.randint(800000, 900000)},
                     {"Jun": random.randint(800000, 900000)},
                     {"Jul": random.randint(800000, 900000)},
                     {"Aug": random.randint(800000, 900000)},
                     {"Sep": random.randint(800000, 900000)},
                     {"Oct": random.randint(800000, 900000)},
                     {"Nov": random.randint(800000, 900000)},
                     {"Dec": random.randint(800000, 900000)}, ],
                "actual":
                    [{"Jan": random.randint(1200000, 1400000)},
                     {"Feb": random.randint(1100000, 1300000)},
                     {"Mar": random.randint(1000000, 1100000)},
                     {"Apr": random.randint(900000, 1000000)},
                     {"May": random.randint(800000, 900000)},
                     {"Jun": random.randint(800000, 900000)},
                     {"Jul": random.randint(800000, 900000)},
                     {"Aug": random.randint(800000, 900000)},
                     {"Sep": random.randint(800000, 900000)},
                     {"Oct": random.randint(800000, 900000)},
                     {"Nov": random.randint(800000, 900000)},
                     {"Dec": random.randint(800000, 900000)}, ],
                "budget":
                    [{"Jan": random.randint(1200000, 1400000)},
                     {"Feb": random.randint(1100000, 1300000)},
                     {"Mar": random.randint(1000000, 1100000)},
                     {"Apr": random.randint(900000, 1000000)},
                     {"May": random.randint(800000, 900000)},
                     {"Jun": random.randint(800000, 900000)},
                     {"Jul": random.randint(800000, 900000)},
                     {"Aug": random.randint(800000, 900000)},
                     {"Sep": random.randint(800000, 900000)},
                     {"Oct": random.randint(800000, 900000)},
                     {"Nov": random.randint(800000, 900000)},
                     {"Dec": random.randint(800000, 900000)}, ],
            },
        }

    else:
        return {
            'message': 'incorrect data'
        }
