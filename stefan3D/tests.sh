#!/bin/bash

#for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo cuspformation $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan3D.py --p 2 --tstep .1 --num-tsteps 5 --baseNy 6 --tstepping euler --reg 0.04 --nref 3 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee cuspformationp2$SOLVER.log
#done
#
#for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo cuspformation $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan3D.py --p 1 --tstep .1 --num-tsteps 5 --baseNy 12 --tstepping euler --reg 0.04 --nref 3 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee cuspformationp1$SOLVER.log
#done
#
#for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo oscillatingsourceBel3D $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan3D.py --p 2 --tstep .5 --num-tsteps 7 --baseNy 6 --tstepping euler --reg 0.0004 --nref 3 --solver-type $SOLVER --case oscillatingsourceBel3D 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee oscillatingsourceBel3Dp2$SOLVER.log
#done
#
#for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo oscillatingsourceBel3D $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan3D.py --p 1 --tstep .5 --num-tsteps 7 --baseNy 12 --tstepping euler --reg 0.0004 --nref 3 --solver-type $SOLVER --case oscillatingsourceBel3D 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee oscillatingsourceBel3Dp1$SOLVER.log
#done

for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
    echo "----------------------"
    echo oscillatingsource3D $SOLVER p=2;
    for i in 1 2 3 4; do 
      mpiexec -n 32 python stefan3D.py --p 2 --tstep 1 --num-tsteps 12 --baseNy 10 --tstepping euler --reg 0.0004 --nref 3 --solver-type $SOLVER --case oscillatingsource3D 2>&1; # | grep -E '(^time|due to)';
    done 2>&1 | tee oscillatingsource3Dp2$SOLVER.log
done

for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
    echo "----------------------"
    echo oscillatingsource3D $SOLVER p=1;
    for i in 1 2 3 4; do 
      mpiexec -n 32 python stefan3D.py --p 1 --tstep 1 --num-tsteps 12 --baseNy 20 --tstepping euler --reg 0.0004 --nref 3 --solver-type $SOLVER --case oscillatingsource3D 2>&1; # | grep -E '(^time|due to)';
    done 2>&1 | tee oscillatingsource3Dp1$SOLVER.log
done

