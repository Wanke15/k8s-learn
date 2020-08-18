from flask import Blueprint

import socket

import hashlib

from api.utils import logger

base_bp = Blueprint("base", __name__)


@base_bp.route("/api/v1.0/health")
def health():
    logger.info("Service in good health!")
    return "I'am doing great!"


colors = ["black", "blue", "green", "purple", "red", "pink", "orange"]


def ab_bucket(data):
    bucket_int = int(hashlib.md5(data.encode('utf8')).hexdigest(), 16) % len(colors)
    return bucket_int


@base_bp.route('/')
def hello_world():
    host_name = socket.gethostname()
    return 'Hello world! This is served by host: <font color="{}">{}</font>'.format(colors[ab_bucket(host_name)],
                                                                                    host_name)
