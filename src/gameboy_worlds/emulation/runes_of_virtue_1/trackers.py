from gameboy_worlds.emulation.runes_of_virtue_1.base_metrics import CoreRunesOfVirtue1Metrics
from gameboy_worlds.emulation.runes_of_virtue_1.test_metrics import (
    CaveOfDeceitTerminateMetric,
    ChucklesDialogTerminateMetric,
    DeathScreenTerminateMetric,
    GnuGnu1DialogTerminateMetric,
    GnuGnu2DialogTerminateMetric,
    KingDialogTerminateMetric,
    OpenMenuTerminateMetric,
    SherryDialogTerminateMetric,
    TelescopeViewTerminateMetric,
)
from gameboy_worlds.emulation.tracker import StateTracker, TestTrackerMixin, DummySubGoalMetric


class CoreRunesOfVirtue1Tracker(StateTracker):
    """
    StateTracker for Ultima: Runes of Virtue.

    Tracks agent_state (in_menu vs free_roam) via CoreRunesOfVirtue1Metrics.
    """

    def start(self):
        super().start()
        self.metric_classes.extend([CoreRunesOfVirtue1Metrics])


class RunesOfVirtue1TestTracker(TestTrackerMixin, CoreRunesOfVirtue1Tracker):
    """
    Base test tracker for Runes of Virtue 1.
    Inherit and set TERMINATION_TRUNCATION_METRIC for specific tasks.
    """

    TERMINATION_TRUNCATION_METRIC = OpenMenuTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1OpenMenuTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player opens the inventory menu.
    """

    TERMINATION_TRUNCATION_METRIC = OpenMenuTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1KingDialogTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player is in dialog with the king.
    """

    TERMINATION_TRUNCATION_METRIC = KingDialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1ChucklesDialogTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player is in dialog with Chuckles.
    """

    TERMINATION_TRUNCATION_METRIC = ChucklesDialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1GnuGnu1DialogTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player is in dialog with Gnu Gnu at his 1st store.
    """

    TERMINATION_TRUNCATION_METRIC = GnuGnu1DialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1GnuGnu2DialogTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player is in dialog with Gnu Gnu at his 2nd store.
    """

    TERMINATION_TRUNCATION_METRIC = GnuGnu2DialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1DeathScreenTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the death / game over screen is shown.
    """

    TERMINATION_TRUNCATION_METRIC = DeathScreenTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1CaveOfDeceitTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player has entered the Cave of Deceit.
    """

    TERMINATION_TRUNCATION_METRIC = CaveOfDeceitTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1TelescopeViewTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player is looking through the telescope.
    """

    TERMINATION_TRUNCATION_METRIC = TelescopeViewTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1SherryDialogTestTracker(RunesOfVirtue1TestTracker):
    """
    Test tracker that ends an episode when the player is in dialog with Sherry.
    """

    TERMINATION_TRUNCATION_METRIC = SherryDialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric
