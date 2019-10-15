from firedrake import *
N = 4
nref = 1
distribution_parameters={"partition": True, "overlap_type": (DistributedMeshOverlapType.VERTEX, 2)}
base = SquareMesh(N, N, 2.0, 1.0,distribution_parameters=distribution_parameters)
mh = MeshHierarchy(base, nref, distribution_parameters=distribution_parameters)
mesh = mh[-1]

V = FunctionSpace(mesh, "CG", 1)

T = Function(V)
T_ = Function(V)
s = TestFunction(V)





x, y = SpatialCoordinate(mesh)  

# Physical parameters
rho_l = 1.0
rho_s = 1.0
c_s = 1.0
c_l = 1.0
L = 70.26 # Latent heat fusion
K_s = 1.08
K_l = 1.08
T_l = -45.
T_r = -0.15
T0 = 0.

r = 0.01

f_s = Constant(0)
f_l = Constant(0)

phi = Function(V).interpolate(0.5*(1 + tanh(T-T_r/r)))

alpha = rho_s*c_s + phi*(rho_l*c_l - rho_s*c_s)
kappa = K_s + phi*(K_l - K_s)
f = f_s + phi*(f_l-f_s)

alpha = Constant(1)


dt = Constant(0.1)

phi_ = Function(V).assign(phi)

a_time = alpha*(T - T_)/dt*s*dx
a_phase =  rho_l*L*(phi - phi_)/dt*s*dx
a_diff = inner(kappa*grad(T), grad(s))*dx
F = a_time + a_phase + a_diff - f*s*dx

#ic = Function(V).interpolate(conditional(gt(x,0.5),T_l,))
ic = Constant(T0)

T.assign(ic)
T_.assign(ic)


bcs = DirichletBC(V, Constant(T_l), 1)
solver_params = {}

nvproblem = NonlinearVariationalProblem(F, T, bcs=bcs)
solver = NonlinearVariationalSolver(nvproblem, solver_parameters=solver_params)

outfile = File("results/temperature.pvd")

outfile.write(T)
t = 0.0
T_final = 1.0
while(t<T_final):
    solver.solve()
    T_.assign(T)
    phi_.assign(phi)
    outfile.write(T) 
    t += dt.values()[0]
    #from IPython import embed; embed()
    
    



