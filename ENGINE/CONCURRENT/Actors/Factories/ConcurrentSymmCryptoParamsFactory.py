from typing import *
# import actor:
from thespian.actors import *
from thespian.troupe import troupe

# import the core serial engines:
from ENGINE.CORE.AlgSelectors.CryptoAlgSelector.SelectSymmAlgorithm import SelectEncAlg
from ENGINE.CORE.CoreCrypto.StreamCrypto.GenSymm import Symm as StreamSymm
from ENGINE.CORE.CoreCrypto.BlockCrypto.GenSymm import Symm as BlockSymm


# The child classes:

# The Gen Symm Key Actor
# noinspection PyCompatibility
@troupe(max_count=10, idle_count=2)
class GenSymmKeyNonceBoxActor(Actor):

    def receiveMessage(self, msg, sender):
        # random choose algorithm:
        choice_stream_alg: str = SelectEncAlg.select_choice_stream_enc_alg()
        if choice_stream_alg == "XSalsa-Poly":
            # start enc params computation:
            secret_key: bytes = StreamSymm.gen_secret()
            nonce: bytes = StreamSymm.gen_symm_nonce()
            enc_box = StreamSymm.gen_symm_box(secret_key)
            reply: Dict = {
                "selected_enc_alg": choice_stream_alg,
                "secret_key": secret_key,
                "nonce": nonce,
                "enc_box": enc_box
            }
            # send reply to sender:
            self.send(sender, reply)
        elif choice_stream_alg == "ChaCha-Poly":
            secret_key: bytes = BlockSymm.gen_secret_deterministic()
            reply = {
                "selected_enc_alg": choice_stream_alg,
                "secret_key": secret_key
            }
            # send reply to sender:
            self.send(sender, reply)
