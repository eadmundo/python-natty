import os
import imp
import jpype
import socket
import threading
from dateutil import parser

if jpype.isJVMStarted() is not 1:
    jars = []
    for top, dirs, files in os.walk(imp.find_module('natty')[1] + '/data'):
        for nm in files:
            jars.append(os.path.join(top, nm))
    jpype.startJVM(
        jpype.getDefaultJVMPath(),
        "-Djava.class.path=%s" % os.pathsep.join(jars)
    )

socket.setdefaulttimeout(15)
lock = threading.Lock()

NattyParser = jpype.JClass('com.eadmundo.natty.NattyParser')


class DateParser(object):

    def __init__(self, date_string):
        try:
            # make it thread-safe
            if threading.activeCount() > 1:
                if jpype.isThreadAttachedToJVM() is not 1:
                    jpype.attachThreadToJVM()
            lock.acquire()

            self._result = NattyParser.parseDate(date_string)
        finally:
            lock.release()

    def result(self):
        return False if self._result == 'false' else parser.parse(self._result)
