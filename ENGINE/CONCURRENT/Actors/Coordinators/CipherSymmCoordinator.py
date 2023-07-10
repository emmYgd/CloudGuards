from typing import *
from thespian.actors import Actor
from thespian.troupe import troupe

# import children actor factories:
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentCipherSymmFactory import EncryptSymmStreamActor
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentCipherSymmFactory import EncryptSymmBlockActor


# Generate:
@troupe(max_count=10, idle_count=2)
class CipherSymmStreamCoord(Actor):
    """This class uses the thespian concurrency library to coordinate symmetric stream encryption"""

    def receiveMessage(self, msg, sender):
        # Instantiate Symm Cipher actor factory and send the message,
        factory_actor_instance = self.createActor(EncryptSymmStreamActor)
        enc_data = self.send(factory_actor_instance, msg)
        # report back to the Master
        self.send(sender, enc_data)


# Generate:
@troupe(max_count=10, idle_count=2)
class CipherSymmBlockCoord(Actor):
    """This class uses the thespian concurrency library to coordinate symmetric block encryption"""

    def receiveMessage(self, msg, sender):
        # Instantiate Symm Cipher actor factory and send the message:
        factory_actor_instance = self.createActor(EncryptSymmBlockActor)
        enc_data = self.send(factory_actor_instance, msg)
        # report back to the Master:
        self.send(sender, enc_data)
