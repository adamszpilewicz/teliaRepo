import logging
import uuid

logging.basicConfig(
    filename=".logs.log",
    format='%(asctime)s | %(message)s |',
    datefmt='%Y/%m/%d %I:%M:%S %p',
    encoding='utf-8',
    level=logging.INFO
)

# Event class is ABSTRACTION
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False

    def __str__(self):
        return f'Identified event name: {self.__class__.__name__}'


class UnknownEvent(Event):
    """type of event that cannot be identified"""


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
                event_data["before"]["session"] == 0
                and event_data["after"]["session"] == 1
        )


class LogutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
                event_data["before"]["session"] == 1
                and event_data["after"]["session"] == 0
        )


class PanicEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return "panic" in event_data["errors_log"]


class SystemMonitor:
    """identify events that occurred in the system"""

    def __init__(self, event_data: dict) -> Event:
        self.event_data = event_data

    def identify_event(self):
        for event_class in Event.__subclasses__():
            try:
                if event_class.meets_condition(self.event_data):
                    logging.info(f"uuid: {uuid.uuid4()} | class name: {event_class.__name__} | " \
                    f"class data: {self.event_data}")
                    return event_class(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)


if __name__ == "__main__":
    raw_data_1 = {
        "before": {"session": 1},
        "after": {"session": 0},
    }

    raw_data_2 = {
        "errors_log": "panic in the line: 12"
    }

    event_1 = Event(raw_data=raw_data_1)
    event_2 = Event(raw_data=raw_data_2)

    for e in [event_1, event_2]:
        monitor = SystemMonitor(event_data=e.raw_data)
        print(monitor.identify_event())
