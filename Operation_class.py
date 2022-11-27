import sys
import threading
import msvcrt
import numpy as np
import time
import sys, os
import datetime
import inspect
import ctypes
import random
from ctypes import *
from MvImport import *

sys.path.append("../MvImport")
from CameraParams_header import *
from MvCameraControl_class import *

def Async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)