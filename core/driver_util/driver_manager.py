"""
Driver Manager Util:
- Initialize Web Driver for Factory Util
"""
from core.driver_util.driver_util import Driver


class DriverManager:
    def start_driver(self, name="chrome"):
        return Driver().create_driver(name)
