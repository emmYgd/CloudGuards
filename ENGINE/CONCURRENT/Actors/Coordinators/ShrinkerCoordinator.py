from typing import *
from thespian.actors import Actor
from thespian.troupe import troupe

# import children actor factories:
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentShrinkerFactory import CompressActor
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentShrinkerFactory import DecompressActor


# Generate:
@troupe(max_count=10, idle_count=2)
class CompressCoord(Actor):
    """This class uses the thespian concurrency library to coordinate Compression"""

    def receiveMessage(self, msg, sender):
        # Instantiate Shrinker actor factory and send the message,
        factory_actor_instance = self.createActor(CompressActor)
        compress_data = self.send(factory_actor_instance, msg)
        # report back to the Master
        self.send(sender, compress_data)


# Generate:
@troupe(max_count=10, idle_count=2)
class DecompressCoord(Actor):
    """This class uses the thespian concurrency library to coordinate Decompression"""

    def receiveMessage(self, msg, sender):
        # Instantiate Shrinker actor factory and send the message:
        factory_actor_instance = self.createActor(DecompressActor)
        decompress_data = self.send(factory_actor_instance, msg)
        # report back to the Master:
        self.send(sender, decompress_data)
