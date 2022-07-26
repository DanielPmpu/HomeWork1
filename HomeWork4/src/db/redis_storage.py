from redis import Redis
from src.core.config import REDIS_HOST, REDIS_PORT


blocked_access_tokens = Redis(
    host=REDIS_HOST, port=REDIS_PORT, db=1, decode_responses=True,
)

active_refresh_tokens = Redis(
    host=REDIS_HOST, port=REDIS_PORT, db=2, decode_responses=True,
)


def get_blocked_access_token():
    return blocked_access_tokens


def get_active_refresh_token():
    return active_refresh_tokens
