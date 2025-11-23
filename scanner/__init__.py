"""XSS Scanner package"""
from .payload_generator import PayloadGenerator
from .request_handler import RequestHandler
from .scanner import Scanner
from .reporter import Reporter
from .utils import build_argparser

__all__ = [
    "PayloadGenerator",
    "RequestHandler",
    "Scanner",
    "Reporter",
    "build_argparser",
]

__version__ = "1.0.0"
__author__ = "Vivekananda Reddy Andluri"
