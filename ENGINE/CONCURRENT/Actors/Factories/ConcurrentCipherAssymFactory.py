from typing import *
# import actor:
from thespian.actors import *
from thespian.troupe import troupe

# import the core cipher engines:
from ENGINE.CORE.CoreCipher.StreamCipher.CipherAssym import AssymEnc as EC_Assym_Cipher
from ENGINE.CORE.CoreCipher.BlockCipher.CipherAssym import AssymEnc as RSA_Assym_Cipher
from ENGINE.CORE.AlgSelectors.CryptoAlgSelector.SelectAssymAlgorithm import SelectEncAlg


# The child classes:

# The Gen Assym Key Actor

@troupe(max_count=40, idle_count=4)
class EncryptAssymActor(Actor):
    """This class uses the thespian concurrency library to encrypt symmetric Keys using assymetric encryption,
    in a hybrid architecture..."""

    def receiveMessage(self, msg, sender):
        """ msg: Dict = {
            'instruction': 'START_ASSM_CIPHER'
            "selected_enc_alg": "EC" or "RSA",
            "private_key": private_key,# majorly for RSA
            # "public_key": public_key, #majorly for RSA
            "enc_box": enc_box,# for EC
            "nonce": nonce, # for EC
            "raw_asset":  byte
        } """

        global enc_params

        # start acting on the message received:
        if msg.instruction == "START_ASSYM_CIPHER":

            # start assymetric encryption
            if msg["selected_enc_alg"] == "EC":
                encrypted_asset = EC_Assym_Cipher.encrypt_assym(
                    msg["raw_asset"],
                    msg["assym_box"],
                    msg["nonce"]
                )
                enc_params["enc_alg"] = "EC"
                enc_params["enc_asset"] = encrypted_asset

            if msg["selected_enc_alg"] == "RSA":
                # select algorithm scheme:
                enc_alg_scheme: str = SelectEncAlg.select_choice_rsa()

                encrypted_message = RSA_Assym_Cipher.encrypt_assym(
                    enc_alg_scheme,
                    msg["raw_asset"],
                    msg["public_key"]
                )
                enc_params["enc_alg"] = "RSA"
                enc_params["enc_data"] = encrypted_message

            reply = enc_params
            '''
            {
                "enc_alg": "EC",
                "enc_asset": encrypted_data
            }
            OR:
            {
            #    "enc_alg": "RSA",
            #    "enc_data": {
            #       "rsa_enc_scheme": enc_alg_scheme,
            #       "enc_asset": encrypted_data
                 }
            }
            '''
            self.send(sender, reply)


@troupe(max_count=40, idle_count=4)
class DecryptAssymActor(Actor):
    """This class uses the thespian concurrency library to encrypt symmetric Keys using assymetric encryption,
    in a hybrid architecture..."""

    def receiveMessage(self, msg, sender):
        """ msg: Dict = {
            'instruction': 'START_ASSM_CIPHER'
            "selected_enc_alg": "EC" or "RSA",
            "private_key": private_key,# majorly for RSA
            #"public_key": public_key,# majorly for RSA
            "enc_box": enc_box,# for EC
            "nonce": nonce, # for EC
            "enc_asset": asset # for EC
        } """

        global dec_params

        # start acting on the message received:
        if msg.instruction == "START_ASSYM_CIPHER":

            # start assymetric encryption
            if msg["selected_enc_alg"] == "EC":
                dec_asset = EC_Assym_Cipher.decrypt_assym(
                    msg["enc_asset"],
                    msg["assym_box"],
                    msg["nonce"]
                )
                dec_params["dec_alg"] = "EC"
                dec_params["dec_asset"] = dec_asset

            if msg["selected_enc_alg"] == "RSA":
                decrypted_asset = RSA_Assym_Cipher.decrypt_assym(
                    msg["enc_alg_scheme"],
                    msg["enc_asset"],
                    msg["private_key"]
                )
                dec_params["dec_alg"] = "RSA"
                dec_params["dec_asset"] = decrypted_asset

        reply = dec_params
        '''
            {
                "dec_alg": "EC",
                "dec_asset": decrypted_data
            }
            OR:
            {
            #    "dec_alg": "RSA",
            #    "raw_asset": raw_data
            }
        '''