from typing import Optional

from gameboy_worlds.emulation.harvest_moon.parsers import HarvestMoonStateParser, BaseHarvestMoonStateParser
from gameboy_worlds.emulation.tracker import (
    RegionMatchTerminationOnlyMetric,
    TerminationMetric,
    RegionMatchTerminationMetric,
    RegionMatchSubGoal,
    AnyRegionMatchSubGoal,
)

class ChickenCoopTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom"
    _TERMINATION_TARGET_NAME = "chicken_coop_entrance"

class OutsideChickenCoopSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_chicken_coop"
    _NAMED_REGIONS = [
        "screen_middle",
        "screen_middle",
        "screen_middle",
    ]
    _TARGET_NAMES = [
        "outside_chicken_coop_left",
        "outside_chicken_coop_right",
        "outside_chicken_coop_up",
    ]
    
class CowBarnTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom"
    _TERMINATION_TARGET_NAME = "cow_barn_entrance"

class OutsideCowBarnSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_cow_barn"
    _NAMED_REGIONS = [
        "screen_middle",
        "screen_middle",
        "screen_middle",
    ]
    _TARGET_NAMES = [
        "outside_cow_barn_left",
        "outside_cow_barn_right",
        "outside_cow_barn_up",
    ]
    
class PickupWaterCanTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_top"
    _TERMINATION_TARGET_NAME = "pick_up_watercan"

class NextToWaterCanSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_water_can"
    _NAMED_REGIONS = [
        "item_watercan_above",
        "item_watercan_right",
        "item_watercan_below",
    ]
    _TARGET_NAMES = [
        "pickup_watercan_down",
        "pickup_watercan_left",
        "pickup_watercan_up",
    ]
    
class GoToSleepTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "item_bed"
    _TERMINATION_TARGET_NAME = "sleep_in_bed"
    
class SleepOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "sleep_option"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "choose_yes_for_sleep",
    ]
    
class FeedSpiritTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "fed_spirit"

class NextToSpiritSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_spirit"
    _NAMED_REGIONS = [
        "item_spirit_left",
        "item_spirit_below",
        "item_spirit_above",       
    ]
    _TARGET_NAMES = [
        "feed_spirit_right",
        "feed_spirit_up",
        "feed_spirit_down",
    ]

class WaterTurnipTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "turnip_center"
    _TERMINATION_TARGET_NAME = "finish_watering"

class NextToTurnipSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_turnip"
    _NAMED_REGIONS = [
        "turnip_top",
    ]
    _TARGET_NAMES = [
        "ready_to_water",
    ]
    
class BuyPotatoSeedsTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_potato_seeds"
    
class ShopForSeedsSubgoal(AnyRegionMatchSubGoal):
    NAME = "shop_for_seeds"
    _NAMED_REGIONS = [
        "center_sign",
    ]
    _TARGET_NAMES = [
        "outside_flower_shop",
    ]

class SelectPotatoSeedsSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_potato_seeds"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_potato_seeds",
    ]
    
class SelectPotatoSeedsOnePortionSubgoal(AnyRegionMatchSubGoal):
    NAME = "select_potato_seeds_one_portion"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_potato_seeds_portion",
    ]
    
class BuyTurnipSeedsTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_turnip_seeds"
    
class SelectTurnipSeedsSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_turnip_seeds"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_turnip_seeds",
    ]
    
class SelectTurnipSeedsOnePortionSubgoal(AnyRegionMatchSubGoal):
    NAME = "select_turnip_seeds_two_portion"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_turnip_seeds_portion",
    ]