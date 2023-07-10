from typing import *
from thespian.actors import Actor
from thespian.troupe import troupe

# import children actor factories:
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentCipherAssymFactory import EncryptAssymActor
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentCipherAssymFactory import DecryptAssymActor


# Generate:
@troupe(max_count=10, idle_count=2)
class CipherAsymmEncCoord(Actor):
    """This class uses the thespian concurrency library to coordinate assymmetric encryption"""

    def receiveMessage(self, msg, sender):
        # Instantiate Symm Cipher actor factory and send the message,
        factory_actor_instance = self.createActor(EncryptAssymActor)
        enc_data = self.send(factory_actor_instance, msg)
        # report back to the Master
        self.send(sender, enc_data)


# Generate:
@troupe(max_count=10, idle_count=2)
class CipherAsymmDecCoord(Actor):
    """This class uses the thespian concurrency library to coordinate assymetric decryption"""

    def receiveMessage(self, msg, sender):
        # Instantiate Symm Cipher actor factory and send the message,
        factory_actor_instance = self.createActor(DecryptAssymActor)
        enc_data = self.send(factory_actor_instance, msg)
        # report back to the Master
        self.send(sender, enc_data)

    
