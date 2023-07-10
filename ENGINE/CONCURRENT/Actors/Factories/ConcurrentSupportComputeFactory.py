from typing import *
# import actor:
from thespian.actors import *
from thespian.troupe import troupe

# import comp algorithm:
from ENGINE.CORE.AlgSelectors.SupportAuthComputesAlgSelector.RandomAlgPicker import RandomAlg
from ENGINE.SUPPORTAUTHCOMPUTES.Signature import Signature
from ENGINE.SUPPORTAUTHCOMPUTES.Hashing.Hashing import Hash
from ENGINE.SUPPORTAUTHCOMPUTES.Hashing.XOF import XOF
from ENGINE.SUPPORTAUTHCOMPUTES.MAC import MAC
from ENGINE.SUPPORTAUTHCOMPUTES.CheckSum import CheckSum


# The child classes:

# The Gen Assym Key Actor
@troupe(max_count=40, idle_count=4)
class SupportAuthComputeActor(Actor):
    """This class uses the thespian concurrency library to perform other crypto computations such as
    Signature/Hash/MAC/CheckSum """

    def receiveMessage(self, msg, sender):
        """ msg = {
            "instruction": "START_AUTH_COMPUTE"
            "asset": concerned_asset
        } """

        global hash_alg, mac_param, checksum_param
        support_computes_params = {}

        concerned_asset: bytes = msg["concerned_asset"]
        if len(msg) == 2:
            if msg["instruction"] == "START_AUTH_COMPUTE":
                # random algorithm picker for Hash, Mac and XOF:

                # pick hash or xof:
                choice_hash_or_xof = RandomAlg.pick_hash_or_xof()
                if choice_hash_or_xof == "HASH":
                    # pick random hash:
                    hash_alg: str = RandomAlg.pick_random_hash_alg()
                    hash_param = Hash(hash_alg).gen_hash(concerned_asset)
                    support_computes_params["hash_alg"] = hash_alg
                    support_computes_params["computed_hash_param"] = hash_param
                else:
                    # pick random xof:
                    xof_alg: str = RandomAlg.pick_random_xof_alg()
                    xof_param = XOF(xof_alg).gen_xof(concerned_asset)
                    support_computes_params["xof_alg"] = xof_alg
                    support_computes_params["computed_xof_param"] = xof_param

                # compute signature:
                signature_params: Dict = Signature.compute_signature(concerned_asset)
                support_computes_params["computed_sign_params"] = signature_params

                # pick for mac:
                mac_alg: str = RandomAlg.pick_random_mac_alg()
                if mac_alg == "HMAC":
                    mac_param = MAC.gen_mac_hmac(
                        mac_key=support_computes_params["verify_key"],
                        data=concerned_asset,
                        dig_mod=hash_alg
                    )
                if mac_alg == "Poly":
                    mac_param = MAC.gen_mac_poly(
                        data=concerned_asset,
                        mac_key=support_computes_params["verify_key"]
                    )
                if mac_alg == "KMAC":
                    mac_param = MAC.gen_mac_kmac(
                        data=concerned_asset,
                        mac_key=support_computes_params["verify_key"]
                    )
                # add all mac values:
                support_computes_params["computed_mac_param"] = mac_param

                compute_alg: str = RandomAlg.pick_random_checksum_alg()
                # compute for checksum:
                if compute_alg == "NORMAL":
                    checksum_param = CheckSum.compute_checksum(concerned_asset)
                if compute_alg == "FASTER":
                    checksum_param = CheckSum.compute_faster_checksum(concerned_asset)
                # add all checksum values:
                support_computes_params["computed_checksum_param"] = checksum_param

            reply: Dict = support_computes_params
            # send back to the coordinator:
            self.send(sender, reply)


@troupe(max_count=40, idle_count=4)
class SupportAuthVerifyActor(Actor):

    def receiveMessage(self, msg, sender):
        pass
