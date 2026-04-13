from typing import Optional

import numpy as np

from gameboy_worlds.emulation.runes_of_virtue_1.parsers import RunesOfVirtue1Parser
from gameboy_worlds.emulation.tracker import TerminationMetric


class OpenMenuTerminateMetric(TerminationMetric):
    """Terminates the episode when the player opens the inventory menu."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_menu = self.state_parser.named_region_matches_target(
                frame, "menu_indicator"
            )
            if in_menu:
                return True
        return False


class KingDialogTerminateMetric(TerminationMetric):
    """Terminates the episode when the king's dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_king_dialog = self.state_parser.named_region_matches_target(
                frame, "king_dialog_indicator"
            )
            if in_king_dialog:
                return True
        return False


class ChucklesDialogTerminateMetric(TerminationMetric):
    """Terminates the episode when Chuckles's dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_chuckles_dialog = self.state_parser.named_region_matches_target(
                frame, "chuckles_dialog_indicator"
            )
            if in_chuckles_dialog:
                return True
        return False


class GnuGnu1DialogTerminateMetric(TerminationMetric):
    """Terminates the episode when Gnu Gnu's 1st store dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_gnu_gnu_1_dialog = self.state_parser.named_region_matches_target(
                frame, "gnu_gnu_1_dialog_indicator"
            )
            if in_gnu_gnu_1_dialog:
                return True
        return False


class GnuGnu2DialogTerminateMetric(TerminationMetric):
    """Terminates the episode when Gnu Gnu's 2nd store dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_gnu_gnu_2_dialog = self.state_parser.named_region_matches_target(
                frame, "gnu_gnu_2_dialog_indicator"
            )
            if in_gnu_gnu_2_dialog:
                return True
        return False


class DeathScreenTerminateMetric(TerminationMetric):
    """Terminates the episode when the death / game over screen is on screen."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_death_screen = self.state_parser.named_region_matches_target(
                frame, "death_screen_indicator"
            )
            if in_death_screen:
                return True
        return False


class CaveOfDeceitTerminateMetric(TerminationMetric):
    """Terminates the episode when the player is inside the Cave of Deceit."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_cave_of_deceit = self.state_parser.named_region_matches_target(
                frame, "cave_of_deceit_indicator"
            )
            if in_cave_of_deceit:
                return True
        return False


class TelescopeViewTerminateMetric(TerminationMetric):
    """Terminates the episode when the telescope view is on screen."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_telescope_view = self.state_parser.named_region_matches_target(
                frame, "telescope_view_indicator"
            )
            if in_telescope_view:
                return True
        return False


class SherryDialogTerminateMetric(TerminationMetric):
    """Terminates the episode when Sherry's dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtue1Parser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtue1Parser
            in_sherry_dialog = self.state_parser.named_region_matches_target(
                frame, "sherry_dialog_indicator"
            )
            if in_sherry_dialog:
                return True
        return False
