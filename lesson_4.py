from abc import ABC, abstractmethod

#абстракция
class Notification:
    @abstractmethod
    def send(self, message):
        pass

class IgorNotification(Notification):


# simple_notification = Notification()

