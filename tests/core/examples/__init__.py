"""
This __init__.py file initializes and imports the setups defined in this sub-folder.

Attributes:
    CONFIG_FILE (str)
    LAYOUT_FILE (str)
    REGISTRY_FILE (str)
    
## Functions:
    setup: Load setup from files and return as NamedTuple or Platform
"""
from dataclasses import dataclass
from pathlib import Path
from controllably.core.factory import get_setup         # pip install control-lab-ly
__all__ = ['CONFIG_FILE', 'LAYOUT_FILE', 'REGISTRY_FILE', 'setup']
__setup__ = None

HERE = Path(__file__).parent.absolute()
CONFIGS = Path(__file__).parent.parent.absolute()
CONFIG_FILE = HERE/"config.yaml"
LAYOUT_FILE = HERE/"layout.json"
REGISTRY_FILE = CONFIGS/"registry.yaml"

# ========== Optional (for typing) ========== #
from .mock_module import TestClass, TestCompoundClass, TestCombinedClass

@dataclass
class Platform:
    Device01: TestClass
    Device02: TestCompoundClass
    Device04: TestCombinedClass
    shortcut1: TestClass
    shortcut2: TestClass
    
# ========================================== #

def setup() -> tuple|Platform:
    global __setup__
    if __setup__ is not None:
        print(f"Setup already loaded from {CONFIG_FILE}")
        return __setup__
    __setup__ = get_setup(CONFIG_FILE, REGISTRY_FILE, Platform)
    return __setup__
