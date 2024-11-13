from abc import ABC, abstractmethod
from datetime import datetime
import json


class LogHandler(ABC):
    @abstractmethod
    def write(self, message):
        pass


class ConsoleLogHandler(LogHandler):
    def write(self, message):
        print(f"{datetime.now()} - {message}")


class FileLogHandler(LogHandler):
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"{datetime.now()} - {message}\n")


class JSONLogHandler(LogHandler):
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message
        }
        with open(self.filename, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")