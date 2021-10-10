"""
for different systems
"""

import platform

class SYSTEM:

    """
    provides different aspects for different systems
    """
    SYSTEM = ""

    systemcode = {

    "Windows": {

    "divsign": "\\",
    "copy": "copy",

    },

    "Linux": {

    "divsign": "/",
    "copy": "cp",

    },

    }

    @staticmethod
    def setSYSTEM():

        s = platform.platform()
        if s.startswith("Windows"):

            SYSTEM.SYSTEM = "Windows"
        else:
            SYSTEM.SYSTEM = "Linux"

    @staticmethod
    def getSYSTEMcalls():

        if not SYSTEM.SYSTEM:

            return {}
        else:

            return SYSTEM.systemcode[SYSTEM.SYSTEM]
