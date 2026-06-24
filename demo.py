from us_visa.logger import logging
from us_visa.exception import USvisaExecption
import sys

try:
    r = 4/0
    print(r)
except Exception as e:
    raise USvisaExecption(e,sys)


