import logging
from enum import Enum

skyflowLog = logging.getLogger('skyflow')
skyflowLog.setLevel(logging.ERROR)


class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARN = logging.WARN
    ERROR = logging.ERROR
    OFF = logging.CRITICAL


def set_log_level(logLevel: LogLevel):
    '''
    Sets the Log Level for the Skyflow python SDK
    '''
    skyflowLog.setLevel(logLevel.value)


def log_info(message: str, interface: str):
    formattedMessage = '{} {}'.format(interface, message)
    skyflowLog.info(formattedMessage)


# def log_debug(message: str, interface: str):
#     formattedMessage = '{} {}'.format(interface, message)
#     skyflowLog.debug(formattedMessage)


def log_error(message: str, interface: str):
    formattedMessage = '{} {}'.format(interface, message)
    skyflowLog.error(formattedMessage)


class InfoMessages(Enum):
    INITIALIZE_CLIENT = "Initializing skyflow client"
    CLIENT_INITIALIZED = "Initialized skyflow client successfully"
    VALIDATE_INSERT_RECORDS = "Validating insert records"
    VALIDATE_DETOKENIZE_INPUT = "Validating detokenize input"
    VALIDATE_GET_BY_ID_INPUT = "Validating getByID input"
    VALIDATE_CONNECTION_CONFIG = "Validating connection config"
    INSERT_DATA_SUCCESS = "Data has been inserted successfully."
    DETOKENIZE_SUCCESS = "Data has been detokenized successfully."
    GET_BY_ID_SUCCESS = "Data fetched from ID successfully."
    BEARER_TOKEN_RECEIVED = "tokenProvider returned token successfully."
    INSERT_TRIGGERED = "Insert method triggered."
    DETOKENIZE_TRIGGERED = "Detokenize method triggered."
    GET_BY_ID_TRIGGERED = "Get by ID triggered."
    INVOKE_CONNECTION_TRIGGERED = "Invoke connection triggered."
    GENERATE_BEARER_TOKEN_TRIGGERED = "Generate bearer token triggered"
    GENERATE_BEARER_TOKEN_SUCCESS = "Generate bearer token returned successfully"
    IS_TOKEN_VALID_TRIGGERED = "isTokenValid() triggered"
    IS_EXPIRED_TRIGGERED = "is_expired() triggered"
    EMPTY_ACCESS_TOKEN = "Give access token is empty"
    INVALID_TOKEN = "Given token is invalid"


class InterfaceName(Enum):
    CLIENT = "client"
    INSERT = "client.insert"
    DETOKENIZE = "client.detokenize"
    GET_BY_ID = "client.get_by_id"
    INVOKE_CONNECTION = "client.invoke_connection"
    GENERATE_BEARER_TOKEN = "service_account.generate_bearer_token"

    

    IS_TOKEN_VALID = "service_account.isTokenValid"
    IS_EXPIRED = "service_account.is_expired"

