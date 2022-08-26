import os
import logging

from typing import Any
from typing import Dict


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_radiant() -> Dict[str, Any]:
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "radiant.svg"
        )

    def _radiant_command(port):
        return [
            "/usr/local/bin/R",
            "-e",
            f"options(radiant.jupyter=TRUE); radiant.data::launch(package='radiant', host='0.0.0.0', port={port}, run=FALSE)",
        ]

    return {
        "command": _radiant_command,
        "timeout": 30,
        "new_browser_tab": True,
        "launcher_entry": {"title": "radiant", "icon_path": _get_icon_path()},
    }
