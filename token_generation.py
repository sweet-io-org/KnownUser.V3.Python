import uuid

from .queue_url_params import QueueUrlParams
from .queueit_helpers import QueueitHelpers


def generate_safetynet_token(event_id: str, secret_key: str, expired_token: bool = False) -> str:
    time_stamp = QueueitHelpers.getCurrentTime() + (3 * 60)
    queue_id = str(uuid.uuid4())  # The identifier for a user in a queue.
    if expired_token:
        time_stamp = time_stamp - 1000
    token_without_hash = (
                                 QueueUrlParams.EVENT_ID_KEY +
                                 QueueUrlParams.KEY_VALUE_SEPARATOR_CHAR +
                                 event_id) + QueueUrlParams.KEY_VALUE_SEPARATOR_GROUP_CHAR + (
                                 QueueUrlParams.QUEUE_ID_KEY +
                                 QueueUrlParams.KEY_VALUE_SEPARATOR_CHAR +
                                 queue_id) + QueueUrlParams.KEY_VALUE_SEPARATOR_GROUP_CHAR + (
                                 QueueUrlParams.REDIRECT_TYPE_KEY +
                                 QueueUrlParams.KEY_VALUE_SEPARATOR_CHAR +
                                 "safetynet") + QueueUrlParams.KEY_VALUE_SEPARATOR_GROUP_CHAR + (
                                 QueueUrlParams.TIMESTAMP_KEY +
                                 QueueUrlParams.KEY_VALUE_SEPARATOR_CHAR + str(time_stamp))

    hash_value = QueueitHelpers.hmacSha256Encode(token_without_hash, secret_key)
    token = token_without_hash + QueueUrlParams.KEY_VALUE_SEPARATOR_GROUP_CHAR + QueueUrlParams.HASH_KEY + QueueUrlParams.KEY_VALUE_SEPARATOR_CHAR + hash_value
    return token
