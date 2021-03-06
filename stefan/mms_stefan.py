from firedrake import *
from datetime import datetime

snes_atol = 1.0e-9
snes_rtol = 1.0e-9

mg_cycle = {
            "levels_ksp_type": "richardson",
            "levels_ksp_max_it": 1,
            "levels_pc_type": "python",
            "levels_pc_python_type": "firedrake.PatchPC",
            "levels_patch_pc_patch_partition_of_unity": True,
            "levels_patch_pc_patch_construct_type": "vanka",
            "levels_patch_pc_patch_construct_codim": 0,
            "levels_patch_pc_patch_sub_mat_type": "seqdense",
            "levels_patch_pc_patch_local_type": "additive",
            "levels_patch_pc_patch_symmetrise_sweep": False,
            "levels_patch_pc_patch_precompute_element_tensors": True,
            "levels_patch_pc_patch_dense_inverse": True,
            "levels_patch_sub_ksp_type": "preonly",
            "levels_patch_sub_pc_type": "lu",
            "coarse_ksp_type": "preonly",
            "coarse_pc_type": "python",
            "coarse_pc_python_type": "firedrake.AssembledPC",
            "coarse_assembled_mat_type": "aij",
            "coarse_assembled_pc_type": "lu",
            "coarse_assembled_pc_factor_mat_solver_type": "mumps",}

newtonmg =  {"snes_type": "newtonls",
                 "snes_linesearch_type": "l2",
                 "snes_max_it": 100,
                 #"snes_linesearch_monitor": None,
                 "snes_linesearch_maxstep": 1,
                 #"snes_monitor": None,
                 "snes_atol": snes_atol,
                 "snes_rtol": snes_rtol,
                 "snes_converged_reason": None, 
                 "ksp_type":"fgmres", 
                 #"ksp_monitor": None,
                 #"ksp_converged_reason": None,
                 "pc_type": "mg"}

newtonbasicmg =  {"snes_type": "newtonls",
                 "snes_linesearch_type": "basic",
                 "snes_linesearch_damping": 0.75,
                 #"snes_monitor": None,
                 "snes_atol": snes_atol,
                 "snes_rtol": snes_rtol,
                 "snes_converged_reason": None, 
                 "ksp_type":"fgmres", 
                 #"ksp_monitor": None,
                 #"ksp_converged_reason": None,
                 "pc_type": "mg"}

newtonmgmatfree = {
       "mat_type": "matfree",
       "snes_type": "newtonls",
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_monitor": None,
       "snes_converged_reason": None,
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "ksp_type": "fgmres",
       #"ksp_monitor": None,
       #"ksp_converged_reason": None,
       "pc_type": "mg",
       "pc_mg_type": "kaskade",
       "mg_coarse_pc_type": "python",
       "mg_coarse_pc_python_type": "firedrake.AssembledPC",
       "mg_coarse_assembled_ksp_type": "preonly",
       "mg_coarse_assembled_ksp_converged_reason": None,
       "mg_coarse_assembled_pc_type": "lu",
       "mg_coarse_assembled_pc_factor_mat_solver_type": "mumps",
       "mg_levels_pc_type": "jacobi",
         }

newtonlu =  {"snes_type": "newtonls",
                 "snes_linesearch_type": "l2",
                 #"snes_linesearch_monitor": None,
                 "snes_linesearch_maxstep": 1,
                 "snes_atol": snes_atol,
                 "snes_rtol": snes_rtol,
                 #"snes_monitor": None,
                 "snes_converged_reason": None, 
                 "ksp_type":"preonly", 
                 "pc_type": "lu"}
                    
newtonmgvanka = {
       "mat_type": "aij",
       "snes_type": "newtonls",
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_monitor": None,
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "ksp_type": "fgmres",
       #"ksp_monitor": None,
       "pc_type": "mg",
       "mg_coarse_ksp_type": "preonly",
       "mg_coarse_pc_type": "lu",
       "mg_coarse_pc_factor_mat_solver_type": "mumps",
       "mg_levels_ksp_type": "richardson",
       "mg_levels_ksp_max_it": 1,
       "mg_levels_pc_type": "python",
       "mg_levels_pc_python_type": "firedrake.PatchPC",
       "mg_levels_patch_pc_patch_partition_of_unity": True,
       "mg_levels_patch_pc_patch_construct_type": "vanka",
       "mg_levels_patch_pc_patch_construct_codim": 0,
       "mg_levels_patch_pc_patch_sub_mat_type": "seqdense",
       "mg_levels_patch_pc_patch_local_type": "additive",
       "mg_levels_patch_pc_patch_symmetrise_sweep": False,
       "mg_levels_patch_pc_patch_precompute_element_tensors": True,
       "mg_levels_patch_pc_patch_dense_inverse": True,
       "mg_levels_patch_sub_ksp_type": "preonly",
       "mg_levels_patch_sub_pc_type": "lu",
         }

ngmresfasstar  = {
       "mat_type": "matfree",
       "snes_type": "ngmres",
       #"snes_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "python",
       "npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_snes_max_it": 1,
       "npc_fas_levels_snes_convergence_test": "skip",
       #"npc_fas_levels_snes_converged_reason": None,
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_linesearch_type": "basic",
       "npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_fas_levels_patch_snes_patch_construct_type": "star",
       "npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_fas_levels_patch_sub_snes_atol": 1.0e-11,
       "npc_fas_levels_patch_sub_snes_rtol": 1.0e-11,
       #"npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type": "python",
       "npc_fas_coarse_pc_python_type": "firedrake.AssembledPC",
       "npc_fas_coarse_assembled_mat_type": "aij",
       "npc_fas_coarse_assembled_pc_type": "lu",
       "npc_fas_coarse_assembled_pc_factor_mat_solver_type": "mumps",
      }

ngmresfaspardecomp  = {
       "mat_type": "matfree",
       "snes_type": "ngmres",
       #"snes_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "python",
       "npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_snes_max_it": 1,
       "npc_fas_levels_snes_convergence_test": "skip",
       #"npc_fas_levels_snes_converged_reason": None,
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_linesearch_type": "basic",
       "npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_fas_levels_patch_snes_patch_construct_type": "pardecomp",
       "npc_fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_fas_levels_patch_sub_snes_atol": 1.0e-11,
       "npc_fas_levels_patch_sub_snes_rtol": 1.0e-11,
       "npc_fas_levels_patch_sub_snes_stol": 0.0,
       #"npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_fas_levels_patch_sub_pc_factor_mat_solver_type": "mumps",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type": "python",
       "npc_fas_coarse_pc_python_type": "firedrake.AssembledPC",
       "npc_fas_coarse_assembled_mat_type": "aij",
       "npc_fas_coarse_assembled_pc_type": "lu",
       "npc_fas_coarse_assembled_pc_factor_mat_solver_type": "mumps",
      }

ngmresaijfaspardecomp  = {
       "mat_type": "aij",
       "snes_type": "ngmres",
       #"snes_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "python",
       "npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_snes_max_it": 1,
       "npc_fas_levels_snes_convergence_test": "skip",
       #"npc_fas_levels_snes_converged_reason": None,
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_linesearch_type": "basic",
       "npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_fas_levels_patch_snes_patch_construct_type": "pardecomp",
       "npc_fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_fas_levels_patch_sub_snes_atol": 1.0e-11,
       "npc_fas_levels_patch_sub_snes_rtol": 1.0e-11,
       "npc_fas_levels_patch_sub_snes_stol": 0.0,
       #"npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_fas_levels_patch_sub_pc_factor_mat_solver_type": "mumps",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type":"lu",
       "npc_fas_coarse_pc_factor_mat_solver_type": "mumps",
      }

ngmresfasstarpardecomp  = {
       "mat_type": "matfree",
       "snes_type": "ngmres",
       #"snes_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "composite",
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_composite_type": "multiplicative",
       "npc_fas_levels_snes_composite_sneses": "python,python",
       "npc_fas_levels_sub_1_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_sub_1_snes_max_it": 1,
       "npc_fas_levels_sub_1_snes_convergence_test": "skip",
       #"npc_fas_levels_sub_1_snes_converged_reason": None,
       #"npc_fas_levels_sub_1_snes_monitor": None,
       "npc_fas_levels_sub_1_snes_linesearch_type": "basic",
       "npc_fas_levels_sub_1_snes_linesearch_damping": 1.0,
       "npc_fas_levels_sub_1_patch_snes_patch_construct_type": "python",
       "npc_fas_levels_sub_1_patch_snes_patch_construct_python_type": "pardecompoverlap.PardecompOverlap",
       "npc_fas_levels_sub_1_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_sub_1_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_fas_levels_sub_1_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_sub_1_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_sub_1_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_sub_0_patch_sub_snes_monitor": None,
       "npc_fas_levels_sub_1_patch_sub_snes_atol": 1.0e-10,
       "npc_fas_levels_sub_1_patch_sub_snes_rtol": 1.0e-10,
       "npc_fas_levels_sub_1_patch_sub_snes_stol": 0.0,
       "npc_fas_levels_sub_1_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_sub_1_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_sub_1_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_sub_1_patch_sub_pc_type": "lu",
       
       "npc_fas_levels_sub_0_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_sub_0_snes_max_it": 1,
       "npc_fas_levels_sub_0_snes_convergence_test": "skip",
       #"npc_fas_levels_sub_0_snes_converged_reason": None,
       #"npc_fas_levels_sub_0_snes_monitor": None,
       "npc_fas_levels_sub_0_snes_linesearch_type": "basic",
       "npc_fas_levels_sub_0_snes_linesearch_damping": 1.0,
       "npc_fas_levels_sub_0_patch_snes_patch_construct_type": "pardecomp",
       "npc_fas_levels_sub_0_patch_snes_patch_pardecomp_overlap": 1,
       "npc_fas_levels_sub_0_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_sub_0_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_fas_levels_sub_0_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_sub_0_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_sub_0_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_sub_0_patch_sub_snes_monitor": None,
       "npc_fas_levels_sub_0_patch_sub_snes_atol": 1.0e-10,
       "npc_fas_levels_sub_0_patch_sub_snes_rtol": 1.0e-10,
       "npc_fas_levels_sub_0_patch_sub_snes_stol": 0.0,
       #"npc_fas_levels_sub_0_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_sub_0_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_sub_0_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_sub_0_patch_sub_pc_type": "lu",
       "npc_fas_levels_sub_0_patch_sub_pc_factor_mat_solver_type": "mumps",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type": "python",
       "npc_fas_coarse_pc_python_type": "firedrake.AssembledPC",
       "npc_fas_coarse_assembled_mat_type": "aij",
       "npc_fas_coarse_assembled_pc_type": "lu",
       "npc_fas_coarse_assembled_pc_factor_mat_solver_type": "mumps",
      }

faspardecomp  = {
       "mat_type": "matfree",
       "snes_type": "fas",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_fas_cycles": 1,
       "snes_fas_type": "kaskade",
       "snes_fas_galerkin": False,
       #"snes_fas_smoothup": 1,
       #"snes_fas_smoothdown": 1,
       "snes_fas_full_downsweep": False,
       #"snes_monitor": None,
       "snes_converged_reason": None,
       "snes_max_it": 100,
       "fas_levels_snes_type": "python",
       "fas_levels_snes_python_type": "firedrake.PatchSNES",
       "fas_levels_snes_max_it": 1,
       "fas_levels_snes_convergence_test": "skip",
       #"fas_levels_snes_converged_reason": None,
       #"fas_levels_snes_monitor": None,
       "fas_levels_snes_linesearch_type": "basic",
       "fas_levels_snes_linesearch_damping": 1.0,
       "fas_levels_patch_sub_snes_atol": 1.0e-10,
       "fas_levels_patch_sub_snes_rtol": 1.0e-10,
       "fas_levels_patch_sub_snes_stol": 0.0,
       "fas_levels_patch_snes_patch_construct_type": "pardecomp",
       "fas_levels_patch_snes_patch_partition_of_unity": True,
       "fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       "fas_levels_patch_snes_patch_local_type": "additive",
       "fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "fas_levels_patch_sub_snes_type": "newtonls",
       #"fas_levels_patch_sub_snes_monitor": None,
       #"fas_levels_patch_sub_snes_converged_reason": None,
       "fas_levels_patch_sub_snes_linesearch_type": "basic",
       "fas_levels_patch_sub_ksp_type": "preonly",
       "fas_levels_patch_sub_pc_type": "lu",
       "fas_coarse_snes_type": "newtonls",
       #"fas_coarse_snes_monitor": None,
       #"fas_coarse_snes_converged_reason": None,
       "fas_coarse_snes_max_it": 100,
       "fas_coarse_snes_atol": 1.0e-14,
       "fas_coarse_snes_rtol": 1.0e-14,
       "fas_coarse_snes_linesearch_type": "l2",
       "fas_coarse_ksp_type": "preonly",
       "fas_coarse_ksp_max_it": 1,
       "fas_coarse_pc_type": "python",
       "fas_coarse_pc_python_type": "firedrake.AssembledPC",
       "fas_coarse_assembled_mat_type": "aij",
       "fas_coarse_assembled_pc_type": "lu",
       "fas_coarse_assembled_pc_factor_mat_solver_type": "mumps",
      }


newtonfaspardecomp  = {
       "mat_type": "matfree",
       "snes_type": "newtonls",
       #"snes_monitor": None,
       "snes_linesearch_type": "basic",
       #"snes_view": None,
       "ksp_type": "fgmres",
       "pc_type": "mg",
       "pc_mg_type" : "full",
       "mg": mg_cycle,
       #"ksp_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "python",
       "npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_snes_max_it": 1,
       "npc_fas_levels_snes_convergence_test": "skip",
       #"npc_fas_levels_snes_converged_reason": None,
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_linesearch_type": "basic",
       "npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_fas_levels_patch_snes_patch_construct_type": "pardecomp",
       "npc_fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_fas_levels_patch_sub_snes_atol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_rtol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_stol": 0.0,
       #"npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_fas_levels_patch_sub_pc_factor_mat_solver_type": "mumps",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type": "python",
       "npc_fas_coarse_pc_python_type": "firedrake.AssembledPC",
       "npc_fas_coarse_assembled_mat_type": "aij",
       "npc_fas_coarse_assembled_pc_type": "lu",
       "npc_fas_coarse_assembled_pc_factor_mat_solver_type": "mumps",
      }

newtonaijfaspardecomp  = {
       "mat_type": "aij",
       "snes_type": "newtonls",
       #"snes_monitor": None,
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_view": None,
       "ksp_type": "fgmres",
       "pc_type": "mg",
       "pc_mg_type" : "full",
       #"ksp_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "python",
       "npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_snes_max_it": 1,
       "npc_fas_levels_snes_convergence_test": "skip",
       #"npc_fas_levels_snes_converged_reason": None,
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_linesearch_type": "basic",
       "npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_fas_levels_patch_snes_patch_construct_type": "pardecomp",
       "npc_fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_fas_levels_patch_sub_snes_atol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_rtol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_stol": 0.0,
       #"npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_fas_levels_patch_sub_pc_factor_mat_solver_type": "mumps",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       #"npc_fas_coarse_ksp_converged_reason": None,
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type": "lu",
       "npc_fas_coarse_pc_factor_mat_solver_type": "mumps",
      }

newtonaijngmresfaspardecomp  = {
       "mat_type": "aij",
       "snes_type": "newtonls",
       #"snes_monitor": None,
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_view": None,
       "ksp_type": "fgmres",
       "pc_type": "mg",
       "pc_mg_type" : "full",
       #"ksp_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       
       "npc_snes_type": "ngmres",
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 3,
       "npc_snes_npc_side": "right",
       "npc_snes_atol": 1e-3,
       "npc_snes_rtol": 1e-3,
       #"npc_snes_converged_reason": None,

       "npc_npc_snes_type": "fas",
       "npc_npc_snes_fas_cycles": 1,
       "npc_npc_snes_fas_type": "kaskade",
       "npc_npc_snes_fas_galerkin": False,
       "npc_npc_snes_fas_full_downsweep": False,
       #"npc_npc_snes_monitor": None,
       "npc_npc_snes_max_it": 1,
       "npc_npc_fas_levels_snes_type": "python",
       "npc_npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_npc_fas_levels_snes_max_it": 1,
       "npc_npc_fas_levels_snes_convergence_test": "skip",
       #"npc_npc_fas_levels_snes_converged_reason": None,
       #"npc_npc_fas_levels_snes_monitor": None,
       "npc_npc_fas_levels_snes_linesearch_type": "basic",
       "npc_npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_npc_fas_levels_patch_snes_patch_construct_type": "pardecomp",
       "npc_npc_fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "npc_npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_npc_fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_npc_fas_levels_patch_sub_snes_atol": 1.0e-10,
       "npc_npc_fas_levels_patch_sub_snes_rtol": 1.0e-10,
       "npc_npc_fas_levels_patch_sub_snes_stol": 0.0,
       #"npc_npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_npc_fas_levels_patch_sub_pc_factor_mat_solver_type": "mumps",
       "npc_npc_fas_coarse_snes_type": "newtonls",
       #"npc_npc_fas_coarse_snes_monitor": None,
       #"npc_npc_fas_coarse_snes_converged_reason": None,
       "npc_npc_fas_coarse_snes_max_it": 100,
       "npc_npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_npc_fas_coarse_ksp_type": "preonly",
       "npc_npc_fas_coarse_ksp_max_it": 1,
       #"npc_npc_fas_coarse_ksp_converged_reason": None,
       "npc_npc_fas_coarse_pc_type": "lu",
       "npc_npc_fas_coarse_pc_factor_mat_solver_type": "mumps",
      }

newtonaijpardecomp  = {
       "mat_type": "aij",
       "snes_type": "newtonls",
       #"snes_monitor": None,
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_view": None,
       "ksp_type": "fgmres",
       "pc_type": "mg",
       "pc_mg_type" : "full",
       #"ksp_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_snes_type": "python",
       "npc_snes_python_type": "firedrake.PatchSNES",
       "npc_snes_convergence_test": "skip",
       #"npc_snes_converged_reason": None,
       "npc_snes_linesearch_type": "basic",
       "npc_snes_linesearch_damping": 1.0,
       "npc_patch_snes_patch_construct_type": "pardecomp",
       "npc_patch_snes_patch_pardecomp_overlap": 1,
       "npc_patch_snes_patch_partition_of_unity": True,
       "npc_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_patch_snes_patch_local_type": "additive",
       "npc_patch_snes_patch_symmetrise_sweep": False,
       "npc_patch_sub_snes_type": "newtonls",
       #"npc_patch_sub_snes_monitor": None,
       "npc_patch_sub_snes_atol": 1.0e-10,
       "npc_patch_sub_snes_rtol": 1.0e-10,
       "npc_patch_sub_snes_stol": 0.0,
       #"npc_patch_sub_snes_converged_reason": None,
       "npc_patch_sub_snes_linesearch_type": "basic",
       "npc_patch_sub_ksp_type": "preonly",
       "npc_patch_sub_pc_type": "lu",
       "npc_patch_sub_pc_factor_mat_solver_type": "mumps",
      }

newtonaijstarpardecomp  = {
       "mat_type": "aij",
       "snes_type": "newtonls",
       #"snes_monitor": None,
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_view": None,
       "ksp_type": "fgmres",
       "pc_type": "mg",
       "pc_mg_type" : "full",
       #"ksp_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_snes_type": "composite",
       #"npc_snes_monitor": None,
       "npc_snes_composite_type": "multiplicative",
       "npc_snes_composite_sneses": "nrichardson,nrichardson",
       
       "npc_sub_1_snes_max_it": 1,
       "npc_sub_1_snes_npc_type": "python",
       "npc_sub_1_npc_snes_python_type": "firedrake.PatchSNES",
       "npc_sub_1_npc_snes_convergence_test": "skip",
       #"npc_sub_1_npc_snes_converged_reason": None,
       "npc_sub_1_npc_snes_linesearch_type": "basic",
       "npc_sub_1_npc_snes_linesearch_damping": 1.0,
       "npc_sub_1_npc_patch_snes_patch_construct_type": "star",
       #"npc_sub_1_npc_patch_snes_patch_pardecomp_overlap": 1,
       "npc_sub_1_npc_patch_snes_patch_partition_of_unity": True,
       "npc_sub_1_npc_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_sub_1_npc_patch_snes_patch_local_type": "additive",
       "npc_sub_1_npc_patch_snes_patch_symmetrise_sweep": False,
       "npc_sub_1_npc_patch_sub_snes_type": "newtonls",
       #"npc_sub_1_npc_patch_sub_snes_monitor": None,
       "npc_sub_1_npc_patch_sub_snes_atol": 1.0e-10,
       "npc_sub_1_npc_patch_sub_snes_rtol": 1.0e-10,
       "npc_sub_1_npc_patch_sub_snes_stol": 0.0,
       #"npc_sub_1_npc_patch_sub_snes_converged_reason": None,
       "npc_sub_1_npc_patch_sub_snes_linesearch_type": "basic",
       "npc_sub_1_npc_patch_sub_ksp_type": "preonly",
       "npc_sub_1_npc_patch_sub_pc_type": "lu",
       "npc_sub_1_npc_patch_sub_pc_factor_mat_solver_type": "mumps",
       
       "npc_sub_0_snes_max_it": 1,
       "npc_sub_0_snes_npc_type": "python",       
       "npc_sub_0_npc_snes_python_type": "firedrake.PatchSNES",
       "npc_sub_0_npc_snes_convergence_test": "skip",
       #"npc_sub_0_npc_snes_converged_reason": None,
       "npc_sub_0_npc_snes_linesearch_type": "basic",
       "npc_sub_0_npc_snes_linesearch_damping": 1.0,
       "npc_sub_0_npc_patch_snes_patch_construct_type": "pardecomp",
       "npc_sub_0_npc_patch_snes_patch_pardecomp_overlap": 1,
       "npc_sub_0_npc_patch_snes_patch_partition_of_unity": True,
       "npc_sub_0_npc_patch_snes_patch_sub_mat_type": "seqaij",
       "npc_sub_0_npc_patch_snes_patch_local_type": "additive",
       "npc_sub_0_npc_patch_snes_patch_symmetrise_sweep": False,
       "npc_sub_0_npc_patch_sub_snes_type": "newtonls",
       #"npc_sub_0_npc_patch_sub_snes_monitor": None,
       "npc_sub_0_npc_patch_sub_snes_atol": 1.0e-10,
       "npc_sub_0_npc_patch_sub_snes_rtol": 1.0e-10,
       "npc_sub_0_npc_patch_sub_snes_stol": 0.0,
       #"npc_sub_0_npc_patch_sub_snes_converged_reason": None,
       "npc_sub_0_npc_patch_sub_snes_linesearch_type": "basic",
       "npc_sub_0_npc_patch_sub_ksp_type": "preonly",
       "npc_sub_0_npc_patch_sub_pc_type": "lu",
       "npc_sub_0_npc_patch_sub_pc_factor_mat_solver_type": "mumps",
        }


newtonaijfasstar  = {
       "mat_type": "aij",
       "snes_type": "newtonls",
       #"snes_monitor": None,
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_view": None,
       "ksp_type": "fgmres",
       "pc_type": "mg",
       "pc_mg_type" : "full",
       #"ksp_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "python",
       "npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_snes_max_it": 1,
       "npc_fas_levels_snes_convergence_test": "skip",
       #"npc_fas_levels_snes_converged_reason": None,
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_linesearch_type": "basic",
       "npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_fas_levels_patch_snes_patch_construct_type": "star",
       #"npc_fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_patch_snes_patch_sub_mat_type": "seqaij",
       #"npc_fas_levels_patch_pc_patch_precompute_element_tensors": True,
       #"npc_fas_patch_pc_patch_dense_inverse": True,
       "npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_fas_levels_patch_sub_snes_atol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_rtol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_stol": 0.0,
       #"npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type": "lu",
       "npc_fas_coarse_pc_factor_mat_solver_type": "mumps",
      }

newtonaijfasvanka  = {
       "mat_type": "aij",
       "snes_type": "newtonls",
       #"snes_monitor": None,
       "snes_linesearch_type": "l2",
       #"snes_linesearch_monitor": None,
       "snes_linesearch_maxstep": 1,
       #"snes_view": None,
       "ksp_type": "fgmres",
       "pc_type": "mg",
       "pc_mg_type" : "full",
       #"ksp_monitor": None,
       "snes_max_it": 100,
       "snes_npc_side": "right",
       "snes_atol": snes_atol,
       "snes_rtol": snes_rtol,
       "snes_converged_reason": None,
       "npc_snes_type": "fas",
       "npc_snes_fas_cycles": 1,
       "npc_snes_fas_type": "kaskade",
       "npc_snes_fas_galerkin": False,
       "npc_snes_fas_full_downsweep": False,
       #"npc_snes_monitor": None,
       "npc_snes_max_it": 1,
       "npc_fas_levels_snes_type": "python",
       "npc_fas_levels_snes_python_type": "firedrake.PatchSNES",
       "npc_fas_levels_snes_max_it": 1,
       "npc_fas_levels_snes_convergence_test": "skip",
       #"npc_fas_levels_snes_converged_reason": None,
       #"npc_fas_levels_snes_monitor": None,
       "npc_fas_levels_snes_linesearch_type": "basic",
       "npc_fas_levels_snes_linesearch_damping": 1.0,
       "npc_fas_levels_patch_snes_patch_construct_type": "vanka",
       "npc_fas_levels_patch_pc_patch_construct_codim": 0,
       #"npc_fas_levels_patch_snes_patch_pardecomp_overlap": 1,
       "npc_fas_levels_patch_snes_patch_partition_of_unity": True,
       "npc_fas_levels_patch_snes_patch_sub_mat_type": "seqdense",
       "npc_fas_levels_patch_pc_patch_precompute_element_tensors": True,
       #"npc_fas_patch_pc_patch_dense_inverse": True,
       "npc_fas_levels_patch_snes_patch_local_type": "additive",
       "npc_fas_levels_patch_snes_patch_symmetrise_sweep": False,
       "npc_fas_levels_patch_sub_snes_type": "newtonls",
       #"npc_fas_levels_patch_sub_snes_monitor": None,
       "npc_fas_levels_patch_sub_snes_atol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_rtol": 1.0e-10,
       "npc_fas_levels_patch_sub_snes_stol": 0.0,
       #"npc_fas_levels_patch_sub_snes_converged_reason": None,
       "npc_fas_levels_patch_sub_snes_linesearch_type": "basic",
       "npc_fas_levels_patch_sub_ksp_type": "preonly",
       "npc_fas_levels_patch_sub_pc_type": "lu",
       "npc_fas_coarse_snes_type": "newtonls",
       #"npc_fas_coarse_snes_monitor": None,
       #"npc_fas_coarse_snes_converged_reason": None,
       "npc_fas_coarse_snes_max_it": 100,
       "npc_fas_coarse_snes_atol": 1.0e-14,
       "npc_fas_coarse_snes_rtol": 1.0e-14,
       "npc_fas_coarse_snes_linesearch_type": "l2",
       "npc_fas_coarse_ksp_type": "preonly",
       "npc_fas_coarse_ksp_max_it": 1,
       "npc_fas_coarse_pc_type": "lu",
       "npc_fas_coarse_pc_factor_mat_solver_type": "mumps",
      }

import argparse
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--baseNy",  type=int, default=12)
parser.add_argument("--p",  type=int, default=2)
parser.add_argument("--num-tsteps",  type=float, default=2)
parser.add_argument("--tstepping",  type=str, default="euler")
parser.add_argument("--reg",  type=float, default=0.1)
args, _ = parser.parse_known_args()
sp = newtonlu


Ny = args.baseNy
Nx = Ny
mesh = UnitSquareMesh(Nx,Ny)

p = args.p
V = FunctionSpace(mesh, "CG", p)
dim = V.dim()
if mesh.comm.rank == 0: print("V.dim(): %s" % dim)

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
K_s = 1.0
K_l = 1.0
T_l = 0.
T_r = 0.
T_f = 0.


r = args.reg
epsilon = 0.01

def phi_tanh(T):
    rd = r
    return 0.5*(1 + tanh((T-T_f)/rd))

def phi_interp(T):
    def interp(T):
        return (T-T_f + epsilon)/(2*epsilon)
    return conditional(gt(T, T_f + epsilon), 1.0, conditional(lt(T, T_f - epsilon), 0.0, interp(T)))

def phi_heavi(T):
    return conditional(gt(T,T_f), 1.0, 0.0)

def phi_diff(T):
    rd = r
    return 0.5/cosh((T-T_f)/rd)**2/rd

phi_reg = phi_tanh

phi = phi_reg(T)
phi_ = phi_reg(T_)

timestepping = args.tstepping
t_final = 0.1
dt = Constant(t_final/args.num_tsteps)
t = Constant(0.0)


if timestepping == "euler":
    T_mid = T
    phi_mid = phi
elif timestepping == "midpoint":
    T_mid = 0.5*(T + T_)
    phi_mid = phi_reg(T_mid)
elif timestepping == "cranknicolson":
    phi_mid = 0.5*(phi + phi_)

if timestepping in ["euler", "midpoint"]:
    kappa = K_s + phi_mid*(K_l - K_s)
    a_diff = inner(kappa*grad(T_mid), grad(s))*dx
elif timestepping in ["cranknicolson"]:
    kappa = K_s + phi*(K_l - K_s)
    kappa_ = K_s + phi_*(K_l - K_s)
    a_diff = 0.5*inner(kappa*grad(T), grad(s))*dx + 0.5*inner(kappa_*grad(T_), grad(s))*dx

alpha = 1.0

f = rho_l*L*phi_diff(T)*sin(pi*x)*cos(pi*y)*(-2*pi**2)*e**(-2*pi**2*(t+dt))
if timestepping == "cranknicolson":
    f = f/2. + rho_l*L*phi_diff(T_)*sin(pi*x)*cos(pi*y)*(-2*pi**2)*e**(-2*pi**2*(t))/2.

a_time = alpha*(T - T_)/dt*s*dx
a_phase =  rho_l*L*(phi - phi_)/dt*s*dx

F = a_time + a_phase + a_diff - f*s*dx

bcl = DirichletBC(V, Constant(T_l), 1)
bcr = DirichletBC(V, Constant(T_r), 2)
bcs = [bcl,bcr]


ic = Function(V).interpolate(sin(pi*x)*cos(pi*y))



T.assign(ic)
T_.assign(ic)
pphi = Function(V).assign(phi)



#from IPython import embed; embed()    
nvproblem = NonlinearVariationalProblem(F, T, bcs=bcs)
solver = NonlinearVariationalSolver(nvproblem, solver_parameters=sp)


outfileT = File("results/temperature.pvd")
outfilephi = File("results/phi.pvd")

outfileT.write(T_)
outfilephi.write(pphi)

start = datetime.now()
old = start
#while(t<t_final):
for i in range(0, int(args.num_tsteps)):
    if mesh.comm.rank == 0: print("Initial time: ", t.values()[0])
    solver.solve()
    now = datetime.now()
    #if mesh.comm.rank == 0: print("Time taken: %s" % (now-old).total_seconds())
    old = now
    T_.assign(T)
    outfileT.write(T_)
    pphi.assign(phi)
    outfilephi.write(pphi) 
    t.assign(t.values()[0] + dt.values()[0])
if mesh.comm.rank == 0: print("Total time taken: %s" % (now-start).total_seconds())
T_true = Function(V).interpolate(sin(pi*x)*cos(pi*y)*e**(-2*pi**2*t_final))
File("results/T_true.pvd").write(T_true)
print("L2 error: ", errornorm(sin(pi*x)*cos(pi*y)*e**(-2*pi**2*t_final),T, "L2"))

#ranks = Function(V)
#ranks.dat.data[...] = float(mesh.comm.rank)

#outfileranks = File("results/ranks.pvd")
#outfileranks.write(ranks)
