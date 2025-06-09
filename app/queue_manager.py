# queue_manager.py
class QueueManager:
    def __init__(self, strategy):
        self.strategy = strategy

    def request_station(self, user):
        # Logic for acquiring a station based on strategy
        pass