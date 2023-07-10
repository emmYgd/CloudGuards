from typing import *
from thespian.actors import ActorSystem


# thespian actor Systems
class ConcSystem(object):
    """This class implement the actor-based concurrency system:"""

    def __init__(self, actor_system_type: AnyStr):
        self.actor_system_type = actor_system_type

    # Run Actor System file:
    def run_actor_system(self) -> ActorSystem:
        myActorSystem = ActorSystem(self.actor_system_type)
        return myActorSystem
