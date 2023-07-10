from typing import *
# import actor:
from thespian.actors import *
from thespian.troupe import troupe

# import the core serial engines:
from ENGINE.CORE.AlgSelectors.CryptoAlgSelector.SelectAssymAlgorithm import SelectEncAlg
from ENGINE.CORE.CoreCrypto.StreamCrypto.GenAssym import Assym as ECgenAssym
from ENGINE.CORE.CoreCrypto.BlockCrypto.GenAsymm import Assym as RSAgenAssym


# The child classes:

# The Gen Assym Key Actor
# noinspection PyCompatibility
@troupe(max_count=40, idle_count=4)
class GenAssymKeyNonceBoxActor(Actor):

    def receiveMessage(self, msg, sender):
        # random choose algorithm:
        choice_assym_alg: str = SelectEncAlg.select_choice_enc_alg()

        if choice_assym_alg == "EC":
            # start enc params computation:
            private_key = ECgenAssym.gen_private()
            public_key = ECgenAssym.gen_public(private_key)
            enc_box = ECgenAssym.gen_assym_box(private_key, public_key)
            nonce = ECgenAssym.gen_asymm_nonce(enc_box)
            reply: Dict = {
                "selected_enc_alg": "EC",
                "private_key": private_key,
                "public_key": public_key,
                "enc_box": enc_box,
                "nonce": nonce,
            }
            # send reply to sender:
            self.send(sender, reply)

        if choice_assym_alg == "RSA":
            # start enc params computation:
            key_pair_obj = RSAgenAssym.gen_asymm_keypair()
            private_key = RSAgenAssym.gen_assym_private(key_pair_obj)
            public_key = RSAgenAssym.gen_assym_public(key_pair_obj)  # encoded

            reply = {
                "selected_enc_alg": "RSA",
                "private_key": private_key,
                "public_key": public_key
            }

            # send reply to sender:
            self.send(sender, reply)
