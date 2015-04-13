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
        self.date_groups = None
        try:
            # make it thread-safe
            if threading.activeCount() > 1:
                if jpype.isThreadAttachedToJVM() is not 1:
                    jpype.attachThreadToJVM()
            lock.acquire()

            self.date_groups = NattyParser.parseDateIntoGroups(date_string)
        finally:
            lock.release()

    def parse(self, d):
        return parser.parse(d)

    def result(self):
        if self.date_groups is not None and len(self.date_groups):
            return [self.parse(d.toString()) for d in [
                dg for dg in self.date_groups][0].dates]
        return None
