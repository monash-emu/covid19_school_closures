import os
import json
import pandas as pd

def load_timeseries(path: str):
    assert path.endswith(".json"), "Timeseries can only load JSON files (.json)"

    msg = MISSING_MESSAGE.format(path=path)
    assert os.path.exists(path), msg

    # Load the JSON
    with open(path, "r") as f:
        data = json.load(f)

    out_dict = {}

    for k, v in data.items():
        out_dict[k] = pd.Series(
            data=v["values"], index=v["times"], name=v["output_key"], dtype=float
        )

    return out_dict


MISSING_MESSAGE = """

    A timeseries file is missing at {path}

"""


