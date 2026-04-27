from typing import Dict, Type

from gameboy_worlds.interface.controller import Controller
from gameboy_worlds.interface.environment import DummyEnvironment, Environment
from gameboy_worlds.interface.runes_of_virtue.environments import (
    RunesOfVirtueEnvironment,
    RunesOfVirtueTestEnvironment,
    RunesOfVirtueTrainEnvironment,
)


AVAILABLE_ENVIRONMENTS: Dict[str, Dict[str, Type[Environment]]] = {
    "runes_of_virtue_1": {
        "dummy": DummyEnvironment,
        "default": RunesOfVirtueEnvironment,
        "basic": RunesOfVirtueEnvironment,
        "train": RunesOfVirtueTrainEnvironment,
        "test": RunesOfVirtueTestEnvironment,
    },
}


AVAILABLE_CONTROLLERS: Dict[str, Dict[str, Type[Controller]]] = {}
