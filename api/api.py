from flask import Blueprint

from api.utils import logger


base_bp = Blueprint("base", __name__)


@base_bp.route("/api/v1.0/health")
def health():
    logger.info("Service in good health!")
    return "I'am doing great!"
