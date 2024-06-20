from dataclasses import dataclass
from pybit.exceptions import (
    InvalidChannelTypeError,
    TopicMismatchError,
    UnauthorizedExceptionError,
)
from ._v5_market import MarketHTTP


WSS_NAME = "Unified V5"
PRIVATE_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.com/v5/private"
PUBLIC_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.com/v5/public/{CHANNEL_TYPE}"
AVAILABLE_CHANNEL_TYPES = [
    "inverse",
    "linear",
    "spot",
    "option",
    "private",
]


@dataclass
class HTTP(
    MarketHTTP
):
    def __init__(self, **args):
        super().__init__(**args)