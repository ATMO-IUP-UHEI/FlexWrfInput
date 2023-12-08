# flake8: noqa
from pathlib import Path

from donfig import Config

default_config = Config(
    "flexwrfinput", paths=[Path(__file__).parent / ".default_flexwrfinput_config.yaml"]
)


from .__version__ import __version__
from .flexwrfinput import FlexwrfInput, read_input
