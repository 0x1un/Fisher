from urllib.request import quote, urlopen
import json



class HTTP:
    @staticmethod
    def get(url, ret_json=True):
        url = quote(url, safe='/:?=&')
        try:
            with urlopen(url) as r:
                result_str = r.read()
                result_str = str(result_str, encoding='utf-8')
            return json.loads(result_str) if ret_json else result_str

        except OSError as e:
            print(e.args)
            return {} if ret_json else None

