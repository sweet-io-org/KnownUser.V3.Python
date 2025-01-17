import hmac
import hashlib
import time
from urllib.parse import urlparse, unquote, quote
from datetime import datetime, timedelta


class QueueitHelpers:
    @staticmethod
    def hmacSha256Encode(value: str, key: str):
        digest = hmac.new(key.encode(), msg=value.encode(), digestmod=hashlib.sha256).hexdigest()
        return digest

    @staticmethod
    def getCurrentTime() -> int:
        return int(time.time())

    @staticmethod
    def urlEncode(v):
        return quote(v, safe='~')

    @staticmethod
    def urlDecode(v):
        return unquote(v)

    @staticmethod
    def urlParse(url_string):
        return urlparse(url_string)

    @staticmethod
    def getCookieExpirationDate():
        return datetime.utcnow() + timedelta(days=1)

    @staticmethod
    def getCurrentTimeAsIso8601Str():
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def convertToInt(value):
        try:
            converted = int(value)
        except:
            converted = 0
        return converted
