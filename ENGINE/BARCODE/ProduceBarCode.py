from typing import *
from typing import Union
# barcode imports:
import barcode
from barcode.writer import ImageWriter
# from barcode.errors import *
# qrcode imports:
import qrcode
from qrcode.image.pil import PilImage


class BarCode(object):
    """Compute uuid:"""

    def __init__(self, barcode_or_qrcode: AnyStr = "QR-CODE",
                 barcode_alg: Optional[AnyStr] = None,
                 barcode_output_format: str = "PNG"
                 ) -> None:
        self.barcode_or_qrcode = barcode_or_qrcode
        self.barcode_alg = barcode_alg
        self.barcode_output_format = barcode_output_format

    def produce(self, input_elem_consider: str, filename: str):
        if self.barcode_or_qrcode == "QR-CODE":
            self.produce_qrcode(input_elem_consider, filename)
        elif self.barcode_or_qrcode == "BARCODE":
            self.produce_bar_code(input_elem_consider, filename)

    def produce_bar_code(self, elem: str, filename: str) -> bool:
        barcode_class = barcode.get_barcode_class(self.barcode_alg)
        if self.barcode_output_format == "PNG":
            bar_code_instance = barcode_class(elem, writer=ImageWriter())
            bar_code_instance.save(filename)
            if True:
                return True
        elif self.barcode_output_format == "SVG":
            bar_code_instance = barcode_class(elem)
            bar_code_instance.save(filename)
            if True:
                return True

    @classmethod
    def produce_qrcode(cls, input_byte_str: str, filename: str) -> bool:
        img_instance: PilImage = qrcode.make(input_byte_str)
        img_instance.save(filename)
        if True:
            return True

