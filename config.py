import os


def get_env(name, default=None, is_raise=True):
    value = os.getenv(name, default)
    if is_raise and not value:
        raise
    return value


VOICE_API = get_env("VOICE_API")
VOICE_TOKEN = get_env("VOICE_TOKEN")
VOICE_ADMIN_ID = get_env("VOICE_ADMIN_ID")
REBOT_API = get_env("REBOT_API")
REBOT_TOKEN = get_env("REBOT_TOKEN")
SAY_HELLO = "您好, 我叫 Mirror, 是一个图灵机器人, 如果有什么问题, 欢迎留言 :)"
SAY_HELLO = get_env("SAY_HELLO", SAY_HELLO)
