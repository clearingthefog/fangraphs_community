import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches

import pybaseball


def statcast_to_feet(x, y):
    """
    convert statcast locations to feet from homeplate origin

    homeplate center location can be found from:
    ```
        STADIUM_COORDS = pd.read_csv(
            pybaseball.plotting.CUR_PATH / 'data/mlbstadiums.csv', 
            index_col=0,
        )
        coords = STADIUM_COORDS[STADIUM_COORDS.segment == "home_plate"]
        plt.scatter(
            coords.x, coords.y
        )
    ```
    looks like 125.2, 201.5

    sc_to_feet from https://community.fangraphs.com/using-statcast-data-to-estimate-minor-league-home-run-distance/
    """
    sc_to_feet = 2.29
    x = sc_to_feet * (x - 125.2)
    y = sc_to_feet * (201.5 - y)
    return x, y


def plot_stadium_feet(team: str, title=None, width=None,
                 height=None, axis=None):
    """
    adapted from pybaseball
    """
    STADIUM_COORDS = pd.read_csv(
        pybaseball.plotting.CUR_PATH / 'data/mlbstadiums.csv', 
        index_col=0,
    )
    coords = STADIUM_COORDS[STADIUM_COORDS['team'] == team.lower()].copy()

    # convert to feet
    coords["x"], coords["y"] = statcast_to_feet(coords["x"], coords["y"])

    if not axis:
        name = list(coords['name'])[0]

        stadium = plt.figure()
        if width is not None and height is not None:
            stadium.set_size_inches(width / stadium.dpi, height / stadium.dpi)
        else:
            stadium.set_size_inches(5, 5)
        axis = stadium.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)  # Centering

        xlim = max(coords.x.abs()) + 15
        axis.set_xlim(-xlim, xlim)
        axis.set_ylim(coords.y.min() - 15, coords.y.max() + 25)

        # axis.set_xticks([])
        # axis.set_yticks([])

    segments = set(coords['segment'])

    for segment in segments:
        segment_verts = coords[coords['segment'] == segment][['x', 'y']]
        path = matplotlib.path.Path(segment_verts)
        patch = matplotlib.patches.PathPatch(path, facecolor='None', edgecolor='black', lw=0.6)
        axis.add_patch(patch)

    # if title is None:
    #     _title = name
    #     if team == 'generic':
    #         _title = 'Generic Stadium'

    #     plt.title(_title)
    # else:
    #     plt.title(title)

    return axis