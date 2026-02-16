from poke_worlds.utils import verify_parameters, log_error
from poke_worlds.emulation.parser import StateParser


class BaseLegendOfZeldaParser(StateParser):
    """
    Minimal state parser for Legend of Zelda GameBoy variants.

    This parser only provides the ROM data path required by the base StateParser.
    No custom screen regions or metrics are defined.
    """

    def __init__(self, variant: str, pyboy, parameters):
        """
        Args:
            variant: Zelda variant string (e.g., legend_of_zelda_links_awakening).
            pyboy: PyBoy emulator instance.
            parameters: Project parameters loaded from configs.
        """
        verify_parameters(parameters)
        if f"{variant}_rom_data_path" not in parameters:
            log_error(
                f"ROM data path not found for variant: {variant}. Add {variant}_rom_data_path to the config files.",
                parameters,
            )
        self.variant = variant
        self.rom_data_path = parameters[f"{variant}_rom_data_path"]
        super().__init__(pyboy, parameters)

    def __repr__(self) -> str:
        return f"<BaseLegendOfZeldaParser(variant={self.variant})>"


class LegendOfZeldaLinksAwakeningParser(BaseLegendOfZeldaParser):
    def __init__(self, pyboy, parameters):
        super().__init__(
            variant="legend_of_zelda_links_awakening",
            pyboy=pyboy,
            parameters=parameters,
        )


class LegendOfZeldaTheOracleOfAgesParser(BaseLegendOfZeldaParser):
    def __init__(self, pyboy, parameters):
        super().__init__(
            variant="legend_of_zelda_the_oracle_of_ages",
            pyboy=pyboy,
            parameters=parameters,
        )


class LegendOfZeldaTheOracleOfSeasonsParser(BaseLegendOfZeldaParser):
    def __init__(self, pyboy, parameters):
        super().__init__(
            variant="legend_of_zelda_the_oracle_of_seasons",
            pyboy=pyboy,
            parameters=parameters,
        )


class LegendOfZeldaParser(LegendOfZeldaLinksAwakeningParser):
    pass
