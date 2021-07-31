import json
from collections import defaultdict


class BaseHandler:

    def _text_to_dict(self, text: str) -> dict:
        """ Transforma um texto json em um dict python """

        input_dict = defaultdict(lambda: None)
        if text:
            json_string = json.loads(text)
            input_dict.update(json_string)

        return input_dict

