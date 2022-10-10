from typing import Optional

from .models import Utils as Utils


class RedirectionParam:
    # This is discussed in section 5.3.5.4 of the Technical Integration document, version 5.1.3.
    QUEUE = "Queue"  # The user is being redirected from the queue
    SAFETY_NET = "SafetyNet"  # The target URL is only peak-protected, and the protection is not currently active
    AFTER_EVENT = "AfterEvent"  # The waiting room is dead
    DISABLED = "Disabled"
    DIRECT_LINK = "DirectLink"  # The user has not been through the waiting room
    IDLE = "Idle"  # The waiting room was idle


class QueueUrlParams:
    KEY_VALUE_SEPARATOR_GROUP_CHAR = '~'
    KEY_VALUE_SEPARATOR_CHAR = '_'
    TIMESTAMP_KEY = "ts"
    COOKIE_VALIDITY_MINUTES_KEY = "cv"
    EVENT_ID_KEY = "e"  # The waiting room's lifetime is an "event".
    EXTENDABLE_COOKIE_KEY = "ce"
    HASH_KEY = "h"
    QUEUE_ID_KEY = "q"  # A unique identifier for a specific user in a specific queue / "event". See 5.3.5.1.
    REDIRECT_TYPE_KEY = "rt"  # Redirection parameter

    def __init__(self):
        self.timeStamp = 0
        self.eventId = ""
        self.hashCode = ""
        self.extendableCookie = False
        self.cookieValidityMinutes = None
        self.queueITToken = ""
        self.queueITTokenWithoutHash = ""
        self.queueId = ""
        self.redirectType = None  # See RedirectionParam

    @staticmethod
    def extractQueueParams(queueit_token) -> Optional["QueueUrlParams"]:
        result = QueueUrlParams()
        if Utils.isNilOrEmpty(queueit_token):
            return None
        result.queueITToken = queueit_token
        params_name_value_list = result.queueITToken.split(QueueUrlParams.KEY_VALUE_SEPARATOR_GROUP_CHAR)
        for pNameValue in params_name_value_list:
            param_name_value_arr = pNameValue.split(QueueUrlParams.KEY_VALUE_SEPARATOR_CHAR)
            if len(param_name_value_arr) != 2:
                continue
            param_name = param_name_value_arr[0]
            param_value = param_name_value_arr[1]

            if param_name == QueueUrlParams.HASH_KEY:
                result.hashCode = param_value
            elif param_name == QueueUrlParams.TIMESTAMP_KEY:
                if not param_value.isdigit():
                    continue
                result.timeStamp = int(param_value)
            elif param_name == QueueUrlParams.COOKIE_VALIDITY_MINUTES_KEY:
                if not param_value.isdigit():
                    continue
                result.cookieValidityMinutes = int(param_value)
            elif param_name == QueueUrlParams.EVENT_ID_KEY:
                result.eventId = param_value
            elif param_name == QueueUrlParams.EXTENDABLE_COOKIE_KEY:
                if param_value.upper() == 'TRUE':
                    result.extendableCookie = True
            elif param_name == QueueUrlParams.QUEUE_ID_KEY:
                result.queueId = param_value
            elif param_name == QueueUrlParams.REDIRECT_TYPE_KEY:
                result.redirectType = param_value

        hash_value = QueueUrlParams.KEY_VALUE_SEPARATOR_GROUP_CHAR + QueueUrlParams.HASH_KEY \
                     + QueueUrlParams.KEY_VALUE_SEPARATOR_CHAR \
                     + result.hashCode
        result.queueITTokenWithoutHash = result.queueITToken.replace(hash_value, "")
        return result
