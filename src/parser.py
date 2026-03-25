from urllib.parse import urlparse

def parse_channel_input(user_input):
    value = user_input.strip()

    if value.startswith("UC"):
        return {"type": "id", "value": value}

    if value.startswith("@"):
        return {"type": "handle", "value": value}

    if value.startswith("http://") or value.startswith("https://"):
        parsed = urlparse(value)
        path = parsed.path.strip("/")

        if path.startswith("channel/"):
            return {"type": "id", "value": path.split("/", 1)[1]}

        if path.startswith("@"):
            return {"type": "handle", "value": path}

        if path.startswith("user/"):
            return {"type": "username", "value": path.split("/", 1)[1]}

    return {"type": "username", "value": value}
