# environment.py
import simpy

class GymEnvironment:
    def __init__(self, config):
        self.config = config
        self.env = simpy.Environment()
        self.stations = []  # List of gym stations
        self.queue_manager = None

    def run(self, until):
        self.env.run(until=until)