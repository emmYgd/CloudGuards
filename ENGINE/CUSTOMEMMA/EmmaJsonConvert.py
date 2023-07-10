from typing import *
import json

class Convert(object):
    """Convert from json to emma and back again"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def json_to_dot_emma(json_content: Union[str, bytes]):
        return json.loads(json_content)

    @staticmethod
    def dot_emma_to_json(obj_content: Any) -> str:
        return json.dumps(obj_content)




