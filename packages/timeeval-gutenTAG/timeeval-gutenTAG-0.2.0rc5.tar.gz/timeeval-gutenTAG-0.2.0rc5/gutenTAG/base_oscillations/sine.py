from typing import Optional

import numpy as np

from .interface import BaseOscillationInterface
from ..utils.types import BaseOscillationKind


class Sine(BaseOscillationInterface):
    def get_base_oscillation_kind(self) -> BaseOscillationKind:
        return BaseOscillationKind.Sine

    def get_timeseries_periods(self) -> Optional[int]:
        return int((self.length / 100) * self.frequency)

    def generate_only_base(self,
                           length: Optional[int] = None,
                           frequency: Optional[float] = None,
                           amplitude: Optional[float] = None,
                           freq_mod: Optional[float] = None,
                           *args, **kwargs) -> np.ndarray:
        length = length or self.length
        frequency = frequency or self.frequency
        amplitude = amplitude or self.amplitude
        freq_mod = freq_mod or self.freq_mod

        periods = (length / 100) * frequency

        end = 2 * np.pi * periods
        base_ts = np.linspace(0, end, length)

        if freq_mod:
            amplitude = (np.sin(np.linspace(0, end * freq_mod, length)) * amplitude)

        return np.sin(base_ts) * amplitude
