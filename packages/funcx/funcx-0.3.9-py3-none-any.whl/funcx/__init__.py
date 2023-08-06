""" funcX : Fast function serving for clouds, clusters and supercomputers.

"""
from funcx.sdk.version import VERSION

__author__ = "The funcX team"
__version__ = VERSION

from funcx.sdk.client import FuncXClient
from funcx.sdk.errors import FuncxAPIError
from funcx.sdk.executor import FuncXExecutor

__all__ = ("FuncXExecutor", "FuncXClient", "FuncxAPIError")
