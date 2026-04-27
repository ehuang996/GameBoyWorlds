from typing import Optional

import numpy as np

from gameboy_worlds.emulation.runes_of_virtue.parsers import (
    RunesOfVirtueStateParser,
)
from gameboy_worlds.emulation.tracker import TerminationMetric


class RunesOfVirtue1OpenMenuTerminateMetric(TerminationMetric):
    """Terminates the episode when the player opens the inventory menu in Runes of Virtue 1."""

    REQUIRED_PARSER = RunesOfVirtueStateParser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtueStateParser
            if self.state_parser.is_in_menu(frame):
                return True
        return False


class _RegionMatchTerminateMetric(TerminationMetric):
    """Base class: terminates the episode when a named region matches its captured target."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    REGION_NAME: str = ""

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtueStateParser
            if self.state_parser.named_region_matches_target(frame, self.REGION_NAME):
                return True
        return False


class RunesOfVirtue1KingDialogTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when the king's dialog is on screen."""
    REGION_NAME = "king_dialog_indicator"


class RunesOfVirtue1ChucklesDialogTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when Chuckles's dialog is on screen."""
    REGION_NAME = "chuckles_dialog_indicator"


class RunesOfVirtue1GnuGnu1DialogTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when Gnu Gnu's 1st store dialog is on screen."""
    REGION_NAME = "gnu_gnu_1_dialog_indicator"


class RunesOfVirtue1GnuGnu2DialogTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when Gnu Gnu's 2nd store dialog is on screen."""
    REGION_NAME = "gnu_gnu_2_dialog_indicator"


class RunesOfVirtue1SherryDialogTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when Sherry's dialog is on screen."""
    REGION_NAME = "sherry_dialog_indicator"


class RunesOfVirtue1CaveOfDeceitTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when the player is inside the Cave of Deceit."""
    REGION_NAME = "cave_of_deceit_indicator"


class RunesOfVirtue1TelescopeViewTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when the telescope view is on screen."""
    REGION_NAME = "telescope_view_indicator"


class RunesOfVirtue1DeathScreenTerminateMetric(_RegionMatchTerminateMetric):
    """Terminates when the death / game over screen is on screen."""
    REGION_NAME = "death_screen_indicator"
