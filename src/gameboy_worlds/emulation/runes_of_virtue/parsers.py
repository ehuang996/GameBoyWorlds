"""
Runes of Virtue specific game state parser implementations.

Visual screen-region matching is used (mirroring the Pokemon module's design) so that
adding additional Runes of Virtue variants only requires per-variant capture data and
optional region overrides, not a fork of the parser logic.

CORE DESIGN PRINCIPLE: Never branch the parser subclasses for a given variant. The inheritance tree for a parser after the game variant parser should always be a tree with only one child per layer.
This is to ensure that we don't double effort, any capability added to a parser will always be valid for that game variant.
If this principle is followed, any state tracker can always use the STRONGEST (lowest level) parser for a given variant without concern for missing functionality.
"""

import os
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Tuple

import numpy as np
from pyboy import PyBoy

from gameboy_worlds.emulation.parser import (
    NamedScreenRegion,
    StateParser,
    _get_proper_regions,
)
from gameboy_worlds.utils import log_error, verify_parameters


class AgentState(Enum):
    """
    0. FREE_ROAM: The agent is freely roaming the game world.
    1. IN_MENU: The agent is in the inventory/status menu.
    """

    FREE_ROAM = 0
    IN_MENU = 1


class RunesOfVirtueStateParser(StateParser, ABC):
    """
    Base class for Runes of Virtue game state parsers. Uses visual screen regions to parse game state.
    Defines common named screen regions and methods for determining game states such as being in a menu.

    Can be used to determine the exact AgentState.
    """

    COMMON_REGIONS: List[Tuple[str, int, int, int, int]] = []
    """ List of common named screen regions for Runes of Virtue games. Subclasses extend this with variant-specific regions via override_regions. """

    COMMON_MULTI_TARGET_REGIONS: List[Tuple[str, int, int, int, int]] = []
    """ List of common multi-target named screen regions for Runes of Virtue games. """

    COMMON_MULTI_TARGETS: Dict[str, List[str]] = {}
    """ Common multi-targets for the common multi-target named screen regions. """

    def __init__(
        self,
        variant: str,
        pyboy: PyBoy,
        parameters: dict,
        additional_named_screen_region_details: List[
            Tuple[str, int, int, int, int]
        ] = [],
        additional_multi_target_named_screen_region_details: List[
            Tuple[str, int, int, int, int]
        ] = [],
        override_multi_targets: Dict[str, List[str]] = {},
    ):
        """
        Initializes the RunesOfVirtueStateParser.
        Args:
            variant (str): The variant of the Runes of Virtue game.
            pyboy (PyBoy): The PyBoy emulator instance.
            parameters (dict): Configuration parameters for the emulator.
            additional_named_screen_region_details: Additional named screen region tuples to register.
            additional_multi_target_named_screen_region_details: Additional multi-target named screen region tuples to register.
            override_multi_targets: Dictionary mapping region names to lists of target names for multi-target regions.
        """
        verify_parameters(parameters)
        regions = _get_proper_regions(
            override_regions=additional_named_screen_region_details,
            base_regions=self.COMMON_REGIONS,
        )
        self.variant = variant
        if f"{variant}_rom_data_path" not in parameters:
            log_error(
                f"ROM data path not found for variant: {variant}. Add {variant}_rom_data_path to the config files. See configs/rom_data_path_vars.yaml for an example",
                parameters,
            )
        self.rom_data_path = parameters[f"{variant}_rom_data_path"]
        """ Path to the ROM data directory for the specific Runes of Virtue variant."""
        captures_dir = os.path.join(self.rom_data_path, "captures")
        named_screen_regions = []
        for region_name, x, y, w, h in regions:
            region = NamedScreenRegion(
                region_name,
                x,
                y,
                w,
                h,
                parameters=parameters,
                target_path=os.path.join(captures_dir, region_name),
            )
            named_screen_regions.append(region)
        multi_target_regions = _get_proper_regions(
            override_regions=additional_multi_target_named_screen_region_details,
            base_regions=self.COMMON_MULTI_TARGET_REGIONS,
        )
        multi_target_region_names = [region[0] for region in multi_target_regions]
        multi_targets = {k: list(v) for k, v in self.COMMON_MULTI_TARGETS.items()}
        for key in override_multi_targets:
            if key in multi_targets:
                multi_targets[key].extend(override_multi_targets[key])
            else:
                multi_targets[key] = list(override_multi_targets[key])
        if not set(multi_targets.keys()).issubset(set(multi_target_region_names)):
            log_error(
                f"Multi-target regions provided in multi_targets do not match the defined multi-target regions. Provided: {list(multi_targets.keys())}, Defined: {multi_target_region_names}",
                parameters,
            )
        for region_name, x, y, w, h in multi_target_regions:
            region_target_paths = {}
            subdir = os.path.join(captures_dir, region_name)
            for target_name in multi_targets.get(region_name, []):
                region_target_paths[target_name] = os.path.join(subdir, target_name)
            region = NamedScreenRegion(
                region_name,
                x,
                y,
                w,
                h,
                parameters=parameters,
                multi_target_paths=region_target_paths,
            )
            named_screen_regions.append(region)
        super().__init__(pyboy, parameters, named_screen_regions)

    @abstractmethod
    def is_in_menu(self, current_screen: np.ndarray) -> bool:
        """
        Determines if the inventory/status menu is currently open.

        Args:
            current_screen (np.ndarray): The current screen frame from the emulator.
        Returns:
            bool: True if the menu is open, False otherwise.
        """
        raise NotImplementedError

    def get_agent_state(self, current_screen: np.ndarray) -> AgentState:
        """
        Determines the current agent state based on the screen.

        Args:
            current_screen (np.ndarray): The current screen frame from the emulator.

        Returns:
            AgentState: The current agent state.
        """
        if self.is_in_menu(current_screen):
            return AgentState.IN_MENU
        return AgentState.FREE_ROAM

    def __repr__(self) -> str:
        return f"<RunesOfVirtueParser(variant={self.variant})>"


class RunesOfVirtue1StateParser(RunesOfVirtueStateParser):
    """
    State parser for Ultima: Runes of Virtue (1991).

    Screen regions:
    - menu_indicator: A region (y=30-50, x=20-60) that is uniformly white when the
      inventory/status menu is open (triggered by START), and contains game world
      content during normal gameplay.
    """

    REGIONS = [
        ("menu_indicator", 20, 30, 40, 20),
        ("king_dialog_indicator", 5, 100, 115, 40),
        ("chuckles_dialog_indicator", 5, 90, 115, 40),
        ("gnu_gnu_1_dialog_indicator", 5, 90, 115, 40),
        ("gnu_gnu_2_dialog_indicator", 5, 90, 115, 40),
        ("sherry_dialog_indicator", 5, 90, 115, 40),
        ("cave_of_deceit_indicator", 0, 0, 100, 70),
        ("telescope_view_indicator", 40, 40, 80, 60),
        ("death_screen_indicator", 60, 100, 30, 30),
    ]
    """ Additional named screen regions specific to Runes of Virtue 1.
    - menu_indicator: A patch above the dialogue box that goes white when the inventory/status menu opens. Open the START menu to capture this.
    """

    def __init__(
        self,
        pyboy: PyBoy,
        parameters: dict,
        override_regions: List[Tuple[str, int, int, int, int]] = [],
        override_multi_target_regions: List[Tuple[str, int, int, int, int]] = [],
        override_multi_targets: Dict[str, List[str]] = {},
    ):
        regions = _get_proper_regions(
            override_regions=override_regions, base_regions=self.REGIONS
        )
        super().__init__(
            variant="runes_of_virtue_1",
            pyboy=pyboy,
            parameters=parameters,
            additional_named_screen_region_details=regions,
            additional_multi_target_named_screen_region_details=override_multi_target_regions,
            override_multi_targets=override_multi_targets,
        )

    def is_in_menu(self, current_screen: np.ndarray) -> bool:
        return self.named_region_matches_target(current_screen, "menu_indicator")
