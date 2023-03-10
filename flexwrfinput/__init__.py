from pathlib import Path

from donfig import Config

default_config = Config(
    "flexwrfinput", paths=[Path(__file__).parent / ".default_flexwrfinput_config.yaml"]
)


from .flexwrfinput import FlexwrfInput, read_input
