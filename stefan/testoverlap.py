from firedrake import *
import pardecompoverlap

mesh = UnitSquareMesh(2, 2)

overlap = pardecompoverlap.PardecompOverlap()

class PC(object):
    def getDM(self):
        return mesh._plex
    def getOptionsPrefix(self):
        return ""
pc = PC()

out = overlap(pc)
