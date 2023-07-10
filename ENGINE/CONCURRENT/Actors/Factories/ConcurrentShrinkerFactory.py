from typing import *
# import actor:
from thespian.actors import *
from thespian.troupe import troupe

# import comp algorithm:
from ENGINE.CORE.AlgSelectors.ShrinkerAlgSelector.SelectShrinker import SelectEncAlg

from zlib import DEFLATED

# import the core cipher engines:
from ENGINE.CORE.CoreShrinker.CoreZipCompress import Compressor as ZipCompressor
from ENGINE.CORE.CoreShrinker.CoreLzmaCompress import Compressor as LzmaCompressor
from ENGINE.CORE.CoreShrinker.CoreBz2Compress import Compressor as Bz2Compressor


# The child classes:

# The Gen Assym Key Actor
@troupe(max_count=40, idle_count=4)
class CompressActor(Actor):
    """This class uses the thespian concurrency library to encrypt files"""

    def receiveMessage(self, msg, sender):
        """ msg: Dict = {
            "asset_bytes": asset_bytes
        } """

        global asset_nature
        global comp_alg_choice
        global comp_asset

        # start acting on the message received:
        if len(msg) == 1:
            asset_bytes: bytes = msg["asset_bytes"]
            # select comp alg:
            comp_alg_choice = SelectEncAlg.select_choice_shrinker()

            if comp_alg_choice == "ZIP":
                # now check for big or small files:
                if len(asset_bytes) <= 524288000:
                    asset_nature = "small"
                    # instantiate zip object:
                    zip_obj = ZipCompressor(level=-1, method=DEFLATED, wbits=0, mem_level=10, bufsize=10000000)
                    # small file:
                    comp_asset = zip_obj.compress_small_file_at_once(asset_bytes)
                if len(asset_bytes) > 524288000:
                    asset_nature = "big"
                    # instantiate zip object:
                    zip_obj = ZipCompressor(level=-1, method=DEFLATED, wbits=0, mem_level=10, bufsize=100000000)
                    # big file:
                    comp_obj = zip_obj.big_file_compress_object()
                    comp_asset = zip_obj.compress_big_files(comp_obj, asset_bytes)

            if comp_alg_choice == "LZMA":
                # now check for big or small files:
                if len(asset_bytes) <= 524288000:
                    asset_nature = "small"
                    # small file:
                    comp_asset = LzmaCompressor.compress_small_file(asset_bytes)
                if len(asset_bytes) > 524288000:
                    asset_nature = "big"
                    # big file:
                    comp_asset = LzmaCompressor.compress_big_file(asset_bytes)

            if comp_alg_choice == "BZ2":
                # now check for big or small files:
                if len(asset_bytes) <= 524288000:
                    asset_nature = "small"
                    # small file:
                    comp_asset = Bz2Compressor.compress_small_file(asset_bytes)
                if len(asset_bytes) > 524288000:
                    asset_nature = "big"
                    # big file
                    comp_asset = Bz2Compressor.compress_big_file(asset_bytes)

        reply = {
            "nature": asset_nature,
            "comp_alg_choice": comp_alg_choice,
            "comp_asset_bytes": comp_asset
        }
        # send back to the coordinator:
        self.send(sender, reply)


@troupe(max_count=40, idle_count=4)
class DecompressActor(Actor):

    def receiveMessage(self, msg, sender):
        """ msg: Dict = {
                "nature": asset_nature,
                "comp_alg_choice": comp_alg_choice,
                "comp_asset_bytes": comp_asset
        } """

        global asset_bytes

        # start acting on the message received:
        if len(msg) == 1:
            comp_asset_bytes: bytes = msg["comp_asset_bytes"]

            if msg["comp_alg_choice"] == "ZIP":
                # now check for big or small files:
                if msg["nature"] == "small":
                    # instantiate zip object:
                    zip_obj = ZipCompressor(level=-1, method=DEFLATED, wbits=0, mem_level=10, bufsize=10000000)
                    # small file:
                    asset_bytes = zip_obj.decompress_small_file_at_once(comp_asset_bytes)
                if msg["nature"] == "big":
                    # instantiate zip object:
                    zip_obj = ZipCompressor(level=-1, method=DEFLATED, wbits=0, mem_level=10, bufsize=100000000)
                    # big file:
                    decomp_obj = zip_obj.big_file_decompress_object()
                    asset_bytes = zip_obj.decompress_big_files(decomp_obj, comp_asset_bytes)

            if msg["comp_alg_choice"] == "LZMA":
                # now check for big or small files:
                if msg["nature"] == "small":
                    # small file:
                    asset_bytes = LzmaCompressor.decompress_small_file(comp_asset_bytes)
                if msg["nature"] == "big":
                    # big file:
                    asset_bytes = LzmaCompressor.decompress_big_file(comp_asset_bytes)

            if msg["comp_alg_choice"] == "BZ2":
                # now check for big or small files:
                # now check for big or small files:
                if msg["nature"] == "small":
                    # small file:
                    asset_bytes = Bz2Compressor.decompress_small_file(comp_asset_bytes)
                if msg["nature"] == "big":
                    # big file:
                    asset_bytes = Bz2Compressor.decompress_big_file(comp_asset_bytes)
        reply = {
            "asset_bytes": asset_bytes
        }
        # send back to the coordinator:
        self.send(sender, reply)
