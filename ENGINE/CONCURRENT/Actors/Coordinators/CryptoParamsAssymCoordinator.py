from typing import *
from thespian.actors import Actor
from thespian.troupe import troupe

# import children actor factories:
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentAssymCryptoParamsFactory import GenAssymKeyNonceBoxActor


# Generate Symmetric Stream Parameters:
@troupe(max_count=10, idle_count=2)
class GenAssymParamsCoord(Actor):
    """This class uses the thespian concurrency library to spun processes that generate secret key, nonce and Box"""

    INSTRUCTION_SYMM = "GEN_ASYMM_PARAMS"

    def receiveMessage(self, msg, sender):
        if msg == self.INSTRUCTION_SYMM:
            # Instantiate Symm Key actor factory and send the message,
            factory_actor_instance = self.createActor(GenAssymKeyNonceBoxActor)
            # create message:
            message = "START_CREATION"
            # send and receive async:
            assym_params_map: Any = self.send(factory_actor_instance, message)
            # report back to the Master
            self.send(sender, assym_params_map)
