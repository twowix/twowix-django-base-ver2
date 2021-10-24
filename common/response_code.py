# SUCCESS CODE
STATUS_RSP_SUCCESS = 200

# Internal ERROR CODE

# COMMON_ERROR
STATUS_RSP_SIGNATURE_EXPIRED = 401
STATUS_RSP_INTERNAL_ERROR = 4000
STATUS_RSP_UNAUTHORIZED = 4001
STATUS_RSP_INVALID_PARAM = 4002
STATUS_RSP_MISSING_MANDATORY_PARAM = 4003
STATUS_RSP_PERMISSION_ERROR = 4004
STATUS_RSP_MAX_SIZE_OVER = 4005

# USER ERROR
STATUS_RSP_USER_DOES_NOT_EXISTS = 4500
STATUS_RSP_USER_ALREADY_EXISTS = 4501
STATUS_RSP_USER_NICK_ALREADY_EXISTS = 4502
STATUS_RSP_USER_PASSWORD_NOT_MATCHED = 4503
STATUS_RSP_USER_INVALID_ACCESS_TOKEN = 4504
STATUS_RSP_USER_IS_DROP_OUT = 4505
STATUS_RSP_USER_IS_BLACK = 4506


_code_to_message = {
    # SUCCESS
    STATUS_RSP_SUCCESS: 'success',
    STATUS_RSP_SIGNATURE_EXPIRED: 'Signature has expired.',

    # COMMON ERROR
    STATUS_RSP_INTERNAL_ERROR: 'internal server error',
    STATUS_RSP_UNAUTHORIZED: 'unauthorized',
    STATUS_RSP_INVALID_PARAM: 'invalid parameter',
    STATUS_RSP_MISSING_MANDATORY_PARAM: 'missing mandatory parameter',
    STATUS_RSP_PERMISSION_ERROR: 'permission error',
    STATUS_RSP_MAX_SIZE_OVER: 'max size over',

    # USER ERROR
    STATUS_RSP_USER_DOES_NOT_EXISTS: 'user does not exists',
    STATUS_RSP_USER_ALREADY_EXISTS: 'user already exists',
    STATUS_RSP_USER_NICK_ALREADY_EXISTS: 'user nick already exists',
    STATUS_RSP_USER_PASSWORD_NOT_MATCHED: 'user password not matched',
    STATUS_RSP_USER_INVALID_ACCESS_TOKEN: 'invalid access token',
    STATUS_RSP_USER_IS_DROP_OUT: 'user is drop out',
    STATUS_RSP_USER_IS_BLACK: 'user is black list',
}


def is_code_success(code):
    if code == 200:
        return True
    return False


def code_to_str(code):
    return str(code)


def code_to_message(code):
    return _code_to_message.get(code)
