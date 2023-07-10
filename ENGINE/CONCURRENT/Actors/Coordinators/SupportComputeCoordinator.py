from typing import *
from thespian.actors import Actor
from thespian.troupe import troupe

# import children actor factories:
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentSupportComputeFactory import SupportAuthComputeActor
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentSupportComputeFactory import SupportAuthVerifyActor


# Generate:
@troupe(max_count=10, idle_count=2)
class AuthComputeCoord(Actor):
    """This class uses the thespian concurrency library to compute crypto auth params """

    def receiveMessage(self, msg, sender):
        # Instantiate Shrinker actor factory and send the message,
        factory_actor_instance = self.createActor(SupportAuthComputeActor)
        auth_params = self.send(factory_actor_instance, msg)
        # report back to the Master
        self.send(sender, auth_params)


# Generate:
@troupe(max_count=10, idle_count=2)
class AuthVerifyCoord(Actor):
    """This class uses the thespian concurrency library to verify crypto auth params"""

    def receiveMessage(self, msg, sender):
        # Instantiate shrinker actor factory and send the message:
        factory_actor_instance = self.createActor(SupportAuthVerifyActor)
        verify_params = self.send(factory_actor_instance, msg)
        # report back to the Master:
        self.send(sender, verify_params)
