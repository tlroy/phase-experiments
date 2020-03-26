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
       "npc_fas_log": None,
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
       "npc_fas_levels_snes_converged_reason": None,
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
       "npc_fas_coarse_snes_converged_reason": None,
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

newtonmgpardecomp =  {"snes_type": "newtonls",
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
                 "ksp_converged_reason": None,
                 "pc_type": "mg",
                 "pc_mg_cycles": 1,
                 "pc_mg_type": "kaskade",
                 "pc_mg_galerkin": False,
                 "pc_mg_full_downsweep": False,
                 #"pc_monitor": None,
                 #"pc_max_it": 1,
                 "mg_levels_pc_type": "python",
                 "mg_levels_pc_python_type": "firedrake.PatchPC",
                 "mg_levels_pc_max_it": 1,
                 "mg_levels_pc_convergence_test": "skip",
                 #"mg_levels_pc_converged_reason": None,
                 #"mg_levels_pc_monitor": None,
                 "mg_levels_patch_pc_patch_construct_type": "pardecomp",
                 "mg_levels_patch_pc_patch_pardecomp_overlap": 1,
                 "mg_levels_patch_pc_patch_partition_of_unity": True,
                 "mg_levels_patch_pc_patch_sub_mat_type": "seqaij",
                 "mg_levels_patch_pc_patch_local_type": "additive",
                 "mg_levels_patch_pc_patch_symmetrise_sweep": False,
                 "mg_levels_patch_sub_ksp_type": "preonly",
                 #"mg_levels_patch_sub_ksp_converged_reason": None,
                 "mg_levels_patch_sub_pc_type": "lu",
                 "mg_levels_patch_sub_pc_factor_mat_solver_type": "mumps",
                 "mg_coarse_ksp_type": "preonly",
                 #"mg_coarse_ksp_converged_reason": None,
                 "mg_coarse_ksp_max_it": 1,
                 "mg_coarse_pc_type": "lu",
                 "mg_coarse_pc_factor_mat_solver_type": "mumps",
                }



solvers = {"newtonlu": newtonlu,
           "newtonmg": newtonmg,
           "newtonbasicmg": newtonbasicmg,
           "newtonmgmatfree": newtonmgmatfree,
           "newtonmgvanka": newtonmgvanka,
           "ngmresfaspardecomp": ngmresfaspardecomp,
           "ngmresfasstar": ngmresfasstar,
           "ngmresfasstarpardecomp": ngmresfasstarpardecomp,
           "faspardecomp": faspardecomp,
           "newtonfaspardecomp": newtonfaspardecomp,
           "newtonaijfaspardecomp": newtonaijfaspardecomp,
           "newtonaijngmresfaspardecomp": newtonaijngmresfaspardecomp,
           "ngmresaijfaspardecomp": ngmresaijfaspardecomp,
           "newtonaijpardecomp": newtonaijpardecomp,
           "newtonaijstarpardecomp": newtonaijstarpardecomp,
           "newtonaijfasstar": newtonaijfasstar,   
           "newtonaijfasvanka": newtonaijfasvanka,
           "newtonmgpardecomp": newtonmgpardecomp,
           }   
           
import argparse
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--solver-type", choices=list(solvers.keys()), required=True)
parser.add_argument("--nref",  type=int, default=4)
parser.add_argument("--baseNy",  type=int, default=12)
parser.add_argument("--p",  type=int, default=2)
parser.add_argument("--tstep",  type=float, default=0.02)
parser.add_argument("--num-tsteps",  type=float, default=1)
parser.add_argument("--tstepping",  type=str, default="euler")
parser.add_argument("--reg",  type=float, default=0.1)
parser.add_argument("--init-cond", type=float, default=0)
parser.add_argument("--case", type=str, default="simplerectangle")
args, _ = parser.parse_known_args()
sp = solvers[args.solver_type]


case = args.case
# Physical parameters
if case == "simplerectangle":
    # domain [0,2]X[0,1]
    Lx = 2.0
    left_x = 0.0
    left_y = 0.0
    Ly = 1.0
    rho_l = 1.0
    rho_s = 0.92 #1.0
    #rho_s = 1.0
    c_s = 0.5 #1.0
    #c_s = 1.0
    c_l = 1.0
    L = 70.26 # Latent heat fusion
    K_s = 1.08
    K_l = 0.26 #1.08
    #K_l = 1.08
    T_r = -0.15
elif case == "oscillatingsource":
    # domain [-1,1]X[-1,1]. smallest reg=0.00025. Final time T = 12
    Lx = 2.0
    Ly = 2.0
    left_x = -1.0
    left_y = -1.0
    rho_l = 1.0
    rho_s = 1.0
    c_s = 1.0
    c_l = 1.0
    L = 1.0
    K_s = 1.0
    K_l = 1.0
    T_r = 0.0
elif case == "wedge":
    # domain [-1,1]X[-1,1]. T=0.1. smallest reg for faspardecomp: 0.003. newtonmg: 0.002
    Lx = 1.0
    Ly = 1.0
    left_x = -0.0
    left_y = -0.0
    rho_l = 1.0
    rho_s = 1.0
    c_s = 1.0
    c_l = 1.0
    L = 20.# default: 0.25 
    K_s = 1.0
    K_l = 1.0
    T_r = 0.0
elif case == "cuspformation":
    # domain [-1,1]X[-1,1]. smallest reg: 0.03. Final time T = 1
    Lx = 6.0
    Ly = 5.0
    left_x = -2.0
    left_y = -0.0
    rho_l = 1.0
    rho_s = 1.0
    c_s = 1.0
    c_l = 1.0
    L = 1.0
    K_s = 1.0
    K_l = 1.0
    T_r = 0.0


Ny = args.baseNy
if case == "simplerectangle":
    Nx = 6*Ny
else:
    Nx = Ny
nref = args.nref
distribution_parameters={"partition": True, "overlap_type": (DistributedMeshOverlapType.VERTEX, 2)}
base = RectangleMesh(Nx, Ny, Lx, Ly, distribution_parameters=distribution_parameters)
mh = MeshHierarchy(base, nref, distribution_parameters=distribution_parameters)
mesh = mh[-1]

#Changing coordinates
for msh in mh:
    msh.coordinates.dat.data[:,0] += left_x
    msh.coordinates.dat.data[:,1] += left_y

p = args.p
V = FunctionSpace(mesh, "CG", p)
dim = V.dim()
if mesh.comm.rank == 0: print("V.dim(): %s" % dim)
Vc = FunctionSpace(base, "CG", p)
dimc = Vc.dim()
if mesh.comm.rank == 0: print("Vc.dim(): %s" % dimc)

T = Function(V)
T_ = Function(V, name = "T")
s = TestFunction(V)

t = Constant(args.tstep) #time

x, y = SpatialCoordinate(mesh)

r = args.reg
epsilon = 0.01


# Define source terms, boundary conditions, and initial conditions
if case == "simplerectangle":
    f_s = Constant(0.0)
    f_l = Constant(0.0)
    T_l = -45. #-15.
    bcs = DirichletBC(V, Constant(T_l), 1)
    T0 = 4. # 0.0
    if args.init_cond == 0.0:
        ic = Function(V).assign(Constant(T0))
        bcs.apply(ic)
    else:
        steep = args.init_cond #5.0
        ic = Function(V).interpolate( T0 + (T_l-T0)*(1 + tanh(-steep*x)))
elif case == "oscillatingsource":
    expr1 = (3.125 - 50.*((x+0.2)**2 + (y+0.5)**2))
    expr2 = (3.125 - 50.*((x+0.2)**2 + (y-0.5)**2))
    f_s = cos(t/5.)*conditional(gt(0,expr1), 0, expr1) + sin(t/5.)*conditional(gt(0,expr2), 0, expr2)
    f_l = f_s
    bcs = DirichletBC(V, y/10., [1,2,4])
    ic = Function(V).interpolate(y/10.)
elif case == "wedge":
    f_s = Constant(0.0)
    f_l = Constant(0.0)
    ic = Function(V).interpolate(Constant(0.3))
    bcs = DirichletBC(V, Constant(-1), [1,3])
elif case == "oscillatingcircle":
    alpha = 0.5 + sin(1.25*t)
    alpha_p = 1.25*cos(1.25*t)
    rr = sqrt(x**2+(y-alpha)**2)
    sinphi = (y-alpha)/rr
    expr1 = 0.75*(rr**2 - 1)
    expr2 = (1.5 - alpha_p*sinphi)*(rr-1)
    T_e = conditional(lt(rr, 1), expr1, expr2)
    print("WARNING: Example not completed") # TODO: find source term
    #f_s = Constant(0.0)
    #f_l = f_s
    bcs = DirichletBC(V, T_e, [2,3,4])
    ic = Function(V).interpolate(T_e)
elif case == "cuspformation":
    rr = sqrt(x**2+(y-2)**2)
    T0 = conditional(lt(rr,1), 1, 0)*conditional(gt(y,2), 0.25*(rr**2-1), 0) \
            + conditional(lt(abs(x),1), 1, 0)*conditional(lt(y,2), 0.25*(x**2-1), 0) \
            + conditional(gt(rr,1), 1, 0)*conditional(gt(y,2), rr-1, 0) \
            + conditional(gt(abs(x), 1), 1, 0)*conditional(lt(y,1), 5*(abs(x)-1), 0) \
            + conditional(gt(abs(x), 1), 1, 0)*conditional(lt(abs(y-1.5),0.5), (abs(x)-1)*(3-2*cos(pi*(y-2))), 0)
    f_s = Constant(0.0)
    f_l = Constant(0.0)
    bcs = DirichletBC(V, T0*(1+t), [1,2,4])
    ic = Function(V).interpolate(T0)


def phi_tanh(T):
    rd = r
    return 0.5*(1 + tanh((T-T_r)/rd))

def phi_interp(T):
    def interp(T):
        return (T-T_r + epsilon)/(2*epsilon)
    return conditional(gt(T, T_r + epsilon), 1.0, conditional(lt(T, T_r - epsilon), 0.0, interp(T)))

def phi_heavi(T):
    return conditional(gt(T,T_r), 1.0, 0.0)

phi_reg = phi_tanh

phi = phi_reg(T)
phi_ = phi_reg(T_)

timestepping = args.tstepping
dt = Constant(args.tstep)

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

alpha = rho_s*c_s + phi_mid*(rho_l*c_l - rho_s*c_s)
f = f_s + phi_mid*(f_l-f_s)

a_time = alpha*(T - T_)/dt*s*dx
a_phase =  rho_l*L*(phi - phi_)/dt*s*dx

F = a_time + a_phase + a_diff - f*s*dx




T.assign(ic)
T_.assign(ic)


nvproblem = NonlinearVariationalProblem(F, T, bcs=bcs)
solver = NonlinearVariationalSolver(nvproblem, solver_parameters=sp)

pphi = Function(V, name = "Phi").assign(phi)



outfile = File("results/solution.pvd")
outfile.write(T_, pphi)
time = 0.0
#t_final = args.num_tsteps*dt.values()[0]
start = datetime.now()
old = start
#while(t<t_final):
KK = 1
k=0

for i in range(0, int(args.num_tsteps)):
    if mesh.comm.rank == 0: print("Initial time: ", time, flush = True)
    solver.solve()
    now = datetime.now()
    if mesh.comm.rank == 0: print("Time taken: %s" % (now-old).total_seconds(), flush = True)
    old = now
    T_.assign(T)
    k += 1
    if k == KK:
        pphi.assign(phi)
        outfile.write(T_, pphi)
        k = 0
    time += dt.values()[0]
    t.assign(time + dt.values()[0])
    
if mesh.comm.rank == 0: 
    print("Total time taken: %s" % (now-start).total_seconds())
dargs = vars(args)                                                                              
if mesh.comm.rank == 0: 
    for x in dargs: 
        print(x, ':', dargs[x]) 


#ranks = Function(V)
#ranks.dat.data[...] = float(mesh.comm.rank)

#outfileranks = File("results/ranks.pvd")
#outfileranks.write(ranks)
