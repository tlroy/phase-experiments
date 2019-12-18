from firedrake import *

mesh = UnitSquareMesh(2,2)
V = FunctionSpace(mesh, "DG", 0)

print(mesh.comm.rank)

u = Function(V)

u.dat.data[...] = float(mesh.comm.rank)

print(u.vector()[:])

