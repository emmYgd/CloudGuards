from typing import *
from thespian.actors import Actor
from thespian.troupe import troupe

# import children actor factories:
from ENGINE.CONCURRENT.Actors.Factories.ConcurrentSymmCryptoParamsFactory import GenSymmKeyNonceBoxActor


# Generate Symmetric Stream Parameters:
@troupe(max_count=10, idle_count=2)
class GenSymmParamsCoord(Actor):
    """This class uses the thespian concurrency library to spun processes that generate secret key, nonce and Box"""

    INSTRUCTION_SYMM = "GEN_SYMM_PARAMS"

    def receiveMessage(self, msg, sender):
        if msg == self.INSTRUCTION_SYMM:
            # Instantiate Symm Key actor factory and send the message,
            factory_actor_instance = self.createActor(GenSymmKeyNonceBoxActor)
            # create message:
            message = "START_CREATION"
            # send and receive async:
            symm_params_map: Any = self.send(factory_actor_instance, message)
            # report back to the Master
            self.send(sender, symm_params_map)
