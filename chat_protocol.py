# Defined commands for protocol
SEPARATOR = "|"

JOIN = "JOIN"
MSG = "MSG"
DM = "DM"
LIST = "LIST"
QUIT = "QUIT"

OK = "OK"
ERROR = "ERROR"
SERVER = "SERVER"
FROM = "FROM"
PRIVATE = "PRIVATE"
USERLIST = "USERLIST"


def build_message(command, *parts):
    """
    Builds a protocol message like:
    MSG|Hello everyone
    DM|Bob|Hello
    """
    return SEPARATOR.join([command, *parts])


def parse_message(raw_message):
    """
    Converts a raw protocol message into:
    command, parts
    """
    raw_message = raw_message.strip()

    if not raw_message:
        return "", []

    pieces = raw_message.split(SEPARATOR)
    command = pieces[0]
    parts = [part.strip() for part in pieces[1:]]

    return command, parts