from typing import *
# import actor:
from thespian.actors import *
from thespian.troupe import troupe

# import the core cipher engines:
from ENGINE.CORE.CoreCipher.StreamCipher.CipherSymm import SymmEnc as StreamSymmEnc
from ENGINE.CORE.CoreCipher.BlockCipher.CipherSymm import SymmEnc as BlockSymmEnc
from ENGINE.CORE.AlgSelectors.CryptoAlgSelector.SelectSymmAlgorithm import SelectEncAlg


# The child classes:

# The Gen Assym Key Actor
# noinspection PyCompatibility
@troupe(max_count=40, idle_count=4)
class EncryptSymmStreamActor(Actor):
    """This class uses the thespian concurrency library to encrypt files"""

    def receiveMessage(self, msg, sender):
        """ msg: Dict = {
            "selected_enc_alg": choice_stream_alg,
            "secret_key": secret_key,
            "nonce": nonce, # optional, only for XSalsa-Poly
            "enc_box": enc_box # optional, only for XSalsa-Poly
            "to_be_enc_bytes": processing_bytes
        } """

        # start acting on the message received:
        if len(msg) == 5:
            # XSalsa-Poly Stream Enc:
            streamInstance = StreamSymmEnc(
                secret_key=msg["secret_key"],
                cipher_alg=msg["selected_enc_alg"],
                sym_box=msg["enc_box"],
                nonce=msg["nonce"]
            )
            enc_data = streamInstance.encrypt_symm_salsa(msg["to_be_enc_bytes"])
            self.send(sender, enc_data)
        elif len(msg) == 3:
            # Chacha-Poly Stream Enc:
            streamInstance = StreamSymmEnc(
                secret_key=msg["secret_key"],
                cipher_alg=msg["selected_enc_alg"],
            )
            enc_data = streamInstance.encrypt_symm_chacha(msg["to_be_enc_bytes"])
            self.send(sender, enc_data)


@troupe(max_count=40, idle_count=4)
class EncryptSymmBlockActor(Actor):

    def receiveMessage(self, msg, sender):
        """msg: Dict = {
            # "selected_enc_alg": choice_stream_alg,
            "secret_key": secret_key,
            "to_be_enc_bytes": processing_bytes
        } """
        # first select random block enc algorithm:
        choiceAlg = SelectEncAlg.select_choice_block_enc_alg()
        # for AES encryption:
        blockInstance = BlockSymmEnc(
            cipher_alg=choiceAlg
        )
        enc_data: Dict = blockInstance.encrypt_symm(
            secret_key=msg["secret_key"],
            raw_data=msg["to_be_enc_bytes"]
        )
        self.send(sender, enc_data)
