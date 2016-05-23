
from datetime import datetime


class TimeFmt(object):

    def update(self, timestr):
        if not timestr:
            self.datetime = datetime.now()
        elif not isinstance(timestr, str) and len(timestr) != 8:
            raise TypeError("arg must be a string")
        else:
            self.datetime = datetime.strptime(timestr, "%Y%m%d")

    def display(self, timeformat):
        formats = {"MDY": "%m/%d/%y", "MDYY": "%m/%d/%Y", "DMY": "%d/%m/%y",
                   "DMYY": "%d/%m/%Y", "MODYY": "%a %d, %Y"}
        if timeformat not in formats:
            raise ValueError("format string must be one of the %s" % formats.keys())
        print self.datetime.strftime(formats.get(timeformat))
