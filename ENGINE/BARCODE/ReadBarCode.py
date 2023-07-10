from typing import *

from pyzbar.pyzbar import decode
from PIL import Image
# use the cv library:
import cv2


class BarCode(object):
    """Read Bar or QR code:"""

    def __init__(self) -> None:
        pass

    @classmethod
    def decode_bar_or_qr_code_1(cls, filename: Union[bytes, AnyStr]) -> Union[List, str]:
        # open as Image(either supplied directly as byte or read from any file with the string name/path provided)
        open_as_image: Image = Image.open(filename)
        decode_object = decode(open_as_image)
        decode_list = [each_decoded_msg.data for each_decoded_msg in decode_object]

        return decode_list

    @classmethod
    def decode_bar_or_qr_code_2(cls, filename: Union[bytes, AnyStr]) -> Union[List, str]:
        # open as Image(either supplied directly as byte or read from any file with the string name/path provided)
        qr_image = cv2.imread(filename)
        # init cv-2 detector:
        detector = cv2.QRCodeDetector()
        # detect and decode
        (data, vertices_array, binary_qrcode) = detector.detectAndDecode(qr_image)
        # if there is a QR code
        if vertices_array is not None:
            return data



