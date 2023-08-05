from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Dict, List, overload

import matplotlib.axes
import matplotlib.figure
import numpy as np

if TYPE_CHECKING:
    from pysimgame.types import AttributeName, RegionName


@dataclass
class PlotLine:
    """A line that will be plotted using the matplotlib plot function.

    Any kwargs that should be passed to plt.plot
    can be done using  kwargs ={}.
    """

    region: str
    attribute: str | List[str]
    kwargs: dict = field(default_factory=dict)
    share_y: bool = True
    y_lims: list = None


def plot(
    figure: matplotlib.figure.Figure,
    ax: matplotlib.axes.Axes,
    data: Dict[RegionName, Dict[AttributeName, np.ndarray]],
    *plot_lines: PlotLine,
):
    for line in plot_lines:
        ax.plot(data[line.region][line.attribute])


class Plot:
    name: str
    plot_lines: List[PlotLine]
    plot_method: Callable

    # @overload
    # def __init__(self, *args: PlotLine) -> None:
    #     ...

    # @overload
    # def __init__(
    #     self,
    #     regions: RegionName | List[RegionName],
    #     attributes: AttributeName | List[AttributeName],
    #     *args: PlotLine,
    # ) -> None:
    #     ...

    def __init__(
        self,
        name: str,
        *args: PlotLine,
        regions: RegionName | List[RegionName] = None,
        attributes: AttributeName | List[AttributeName] = None,
    ) -> None:
        """Create a plot object."""
        if not isinstance(name, str):
            logging.getLogger(__name__).error("Plot name must be str.")
        self.name = name
        from .manager import _PLOT_MANAGER

        game = _PLOT_MANAGER.GAME
        if regions is None:
            # None means all regions
            regions = (
                list(game.REGIONS_DICT.keys())
                if not args or attributes is not None
                else []
            )
        if attributes is None:
            attributes = (
                _PLOT_MANAGER.MODEL_MANAGER.capture_attributes
                if not args
                else []
            )
        if isinstance(regions, str):
            regions = [regions]
        if isinstance(attributes, str):
            attributes = [attributes]
        # Adds the lines specified by the user

        self.plot_lines = list(args) + [
            PlotLine(reg, attributes) for reg in regions
        ]

        _PLOT_MANAGER.add_plot(name, self)
