"""HWB class."""
from ...spaces import Space, Cylindrical
from ...cat import WHITES
from ...gamut.bounds import GamutBound, FLG_ANGLE, FLG_PERCENT
from ... import util
from ...util import MutableVector
from typing import Tuple


def hwb_to_hsv(hwb: MutableVector) -> MutableVector:
    """HWB to HSV."""

    h, w, b = hwb

    wb = w + b
    if (wb >= 1):
        gray = w / wb
        return [util.NaN, 0.0, gray]

    v = 1 - b
    s = 0 if v == 0 else 1 - w / v
    return [h, s, v]


def hsv_to_hwb(hsv: MutableVector) -> MutableVector:
    """HSV to HWB."""

    h, s, v = hsv
    w = v * (1 - s)
    b = 1 - v
    if w + b >= 1:
        h = util.NaN
    return [h, w, b]


class HWB(Cylindrical, Space):
    """HWB class."""

    BASE = "hsv"
    NAME = "hwb"
    SERIALIZE = ("--hwb",)
    CHANNEL_NAMES = ("h", "w", "b")
    CHANNEL_ALIASES = {
        "hue": "h",
        "whiteness": "w",
        "blackness": "b"
    }
    GAMUT_CHECK = "srgb"
    WHITE = WHITES['2deg']['D65']

    BOUNDS = (
        GamutBound(0.0, 360.0, FLG_ANGLE),
        GamutBound(0.0, 1.0, FLG_PERCENT),
        GamutBound(0.0, 1.0, FLG_PERCENT)
    )

    @property
    def h(self) -> float:
        """Hue channel."""

        return self._coords[0]

    @h.setter
    def h(self, value: float) -> None:
        """Shift the hue."""

        self._coords[0] = value

    @property
    def w(self) -> float:
        """Whiteness channel."""

        return self._coords[1]

    @w.setter
    def w(self, value: float) -> None:
        """Set whiteness channel."""

        self._coords[1] = value

    @property
    def b(self) -> float:
        """Blackness channel."""

        return self._coords[2]

    @b.setter
    def b(self, value: float) -> None:
        """Set blackness channel."""

        self._coords[2] = value

    @classmethod
    def null_adjust(cls, coords: MutableVector, alpha: float) -> Tuple[MutableVector, float]:
        """On color update."""

        coords = util.no_nans(coords)
        if coords[1] + coords[2] >= 1:
            coords[0] = util.NaN
        return coords, util.no_nan(alpha)

    @classmethod
    def to_base(cls, coords: MutableVector) -> MutableVector:
        """To HSV from HWB."""

        return hwb_to_hsv(coords)

    @classmethod
    def from_base(cls, coords: MutableVector) -> MutableVector:
        """From HSV to HWB."""

        return hsv_to_hwb(coords)
