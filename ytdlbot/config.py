#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - config.py
# 8/28/21 15:01
#

__author__ = "Benny <benny.think@gmail.com>"

import os

from blinker import signal

# general settings
WORKERS: int = int(os.getenv("WORKERS", 10))
PYRO_WORKERS: int = int(os.getenv("PYRO_WORKERS", 100))
APP_ID: int = int(os.getenv("APP_ID", 21894814))
APP_HASH = os.getenv("APP_HASH", "4366bdf6ed33089c363df8e4d7b9a1b5")
TOKEN = os.getenv("TOKEN", "6613657830:AAFJDcqAvKBV7d_-llNVIij_I6uoXmOxgZo")

REDIS = os.getenv("REDIS", False)

ENABLE_VIP = os.getenv("VIP", False)
OWNER = os.getenv("OWNER", "Bimbo69")

# limitation settings
AUTHORIZED_USER: str = os.getenv("AUTHORIZED_USER", "5071005351")
# membership requires: the format could be username(without @ sign)/chat_id of channel or group.
# You need to add the bot to this group/channel as admin
REQUIRED_MEMBERSHIP: str = os.getenv("REQUIRED_MEMBERSHIP", "-1002334928020")

# celery related
ENABLE_CELERY = os.getenv("ENABLE_CELERY", True)
BROKER = os.getenv("BROKER", f"redis://{REDIS}:6379/1")

MYSQL_HOST = os.getenv("MYSQL_HOST", False)
MYSQL_USER = os.getenv("MYSQL_USER", False)
MYSQL_PASS = os.getenv("MYSQL_PASS", False)

ARCHIVE_ID = os.getenv("ARCHIVE_ID", -1002367641884)

ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", True)
AUDIO_FORMAT = os.getenv("AUDIO_FORMAT", True)

PLAYLIST_SUPPORT = os.getenv("PLAYLIST_SUPPORT", True)
M3U8_SUPPORT = os.getenv("M3U8_SUPPORT", True)
ENABLE_ARIA2 = os.getenv("ENABLE_ARIA2", True)

RCLONE_PATH = os.getenv("RCLONE")

# payment settings
AFD_LINK = os.getenv("AFD_LINK", "https://afdian.net/@Bimbo69")
COFFEE_LINK = os.getenv("COFFEE_LINK", "https://www.buymeacoffee.com/Bimbo69")
COFFEE_TOKEN = os.getenv("COFFEE_TOKEN")
AFD_TOKEN = os.getenv("AFD_TOKEN")
AFD_USER_ID = os.getenv("AFD_USER_ID")
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN") or "1234"
FREE_DOWNLOAD = os.getenv("FREE_DOWNLOAD", 10)
EXPIRE = 24 * 3600
TOKEN_PRICE = os.getenv("BUY_UNIT", 20)  # one USD=20 credits
TRONGRID_KEY = os.getenv("TRONGRID_KEY", "").split(",")
# the default mnemonic is for nile testnet
TRON_MNEMONIC = os.getenv("TRON_MNEMONIC", "cram floor today legend service drill pitch leaf car govern harvest soda")
TRX_SIGNAL = signal("trx_received")

PREMIUM_USER = int(os.getenv("PREMIUM_USER", "5071005351"))

# For advance users
# Please do not change, if you don't know what these are.
TG_PREMIUM_MAX_SIZE = 4000 * 1024 * 1024
TG_NORMAL_MAX_SIZE = 2000 * 1024 * 1024
CAPTION_URL_LENGTH_LIMIT = 150
IPv6 = os.getenv("IPv6", False)
RATE_LIMIT = os.getenv("RATE_LIMIT", 120)
# This will set the value for the tmpfile path(download path). If not, will return None and use system’s default path.
# Please ensure that the directory exists and you have necessary permissions to write to it.
TMPFILE_PATH = os.getenv("TMPFILE_PATH")


class FileTooBig(Exception):
    pass
