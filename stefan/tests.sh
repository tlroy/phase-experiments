#!/bin/bash
#for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
#  for dt in 0.5 0.25 0.1 0.01; do
#    echo $SOLVER dt=$dt initial=step p=3;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 3 --tstep $dt --baseNy 8 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee stepp3$SOLVER.log
#done
#
#for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
#  for dt in 0.5 0.25 0.1 0.01; do
#    echo $SOLVER dt=$dt initial=tanh p=3;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 3 --tstep $dt --init-cond tanh --baseNy 8 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee tanhp3$SOLVER.log
#done
#
#for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
#  for dt in 0.5 0.25 0.1 0.01; do
#    echo $SOLVER dt=$dt initial=tanh p=4;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 4 --tstep $dt --init-cond tanh --baseNy 6 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee tanhp4$SOLVER.log
#done
#
#
#for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
#  for dt in 0.5 0.25 0.1 0.01; do
#    echo $SOLVER dt=$dt initial=step p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 2 --tstep $dt --init-cond step --baseNy 12 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee stepp2$SOLVER.log
#done

# for SOLVER in newtonaijfaspardecomp newtonaijngmresfaspardecomp newtonaijfasstar faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg newtonaijfasstar; do
#   for dt in 0.5 0.25 0.1 0.01; do
#     echo $SOLVER dt=$dt initial=tanh p=2;
#     for i in 1 2 3 4; do 
#       mpiexec -n 16 python stefan.py --p 2 --tstep $dt --init-cond tanh --baseNy 12 --tstepping euler --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#     done
#     echo "----------------------"
#   done 2>&1 | tee eulertanhp2$SOLVER.log
# done

#for SOLVER in newtonaijfaspardecomp newtonaijngmresfaspardecomp newtonaijfasstar faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
#  for dt in 0.02 0.01 0.005 0.001; do
#    echo $SOLVER dt=$dt initial=step p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 2 --tstep $dt --init-cond step --baseNy 12 --tstepping euler --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee stepp2euler$SOLVER.log
#done
#
#for SOLVER in newtonaijfaspardecomp newtonaijngmresfaspardecomp newtonaijfasstar faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
#  for dt in 0.02 0.01 0.005 0.001; do
#    echo $SOLVER dt=$dt initial=step p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 2 --tstep $dt --init-cond step --baseNy 12 --tstepping cranknicolson --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee stepp2CN$SOLVER.log
#done

#for SOLVER in newtonaijfaspardecomp newtonaijngmresfaspardecomp newtonmg newtonaijfasstar; do
#  for steep in 3 5 6 7; do
#    echo $SOLVER init-cond=$steep p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 2 --tstep 0.25 --init-cond $steep --baseNy 12 --tstepping euler --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee eulertanhp2$SOLVER.log
#done

#for SOLVER in newtonaijfaspardecomp newtonaijngmresfaspardecomp newtonmg newtonbasicmg newtonaijfasstar; do
#  for steep in 2 3 4 5 6 7 8; do
#    echo $SOLVER init-cond=$steep p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 2 --tstep 0.25 --num-tsteps 1 --init-cond $steep --baseNy 12 --tstepping euler --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
#    done
#    echo "----------------------"
#  done 2>&1 | tee eulertanhp2$SOLVER.log
#done


#for SOLVER in newtonaijfas newtonmg; do
#    echo "----------------------"
#    echo oscillatingsource $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 2 --tstep 1 --num-tsteps 12 --baseNy 20 --tstepping euler --reg 0.00025 --nref 4 --solver-type $SOLVER --case oscillatingsource 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee oscillatingsourcep2$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg; do
#    echo "----------------------"
#    echo oscillatingsource $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 1 --tstep 1 --num-tsteps 12 --baseNy 40 --tstepping euler --reg 0.00025 --nref 4 --solver-type $SOLVER --case oscillatingsource 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee oscillatingsourcep1$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg; do
#    echo "----------------------"
#    echo cuspformation $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 2 --tstep .1 --num-tsteps 10 --baseNy 20 --tstepping euler --reg 0.025 --nref 4 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee cuspformationp2$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg; do
#    echo "----------------------"
#    echo cuspformation $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 1 --tstep .1 --num-tsteps 10 --baseNy 40 --tstepping euler --reg 0.025 --nref 4 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee cuspformationp1$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo simplerectangle $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 2 --tstep .25 --num-tsteps 1 --baseNy 12 --tstepping euler --reg 0.1 --nref 4 --solver-type $SOLVER --case simplerectangle --init-cond 7 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee simplerectanglep2$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo simplerectangle $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 1 --tstep .25 --num-tsteps 1 --baseNy 24 --tstepping euler --reg 0.1 --nref 4 --solver-type $SOLVER --case simplerectangle --init-cond 7 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee simplerectanglep1$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo simplerectangle $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 1 --tstep .001 --num-tsteps 1 --baseNy 24 --tstepping euler --reg 0.1 --nref 4 --solver-type $SOLVER --case simplerectangle --init-cond 0 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee simplerectanglestepp1$SOLVER.log
#done

#for SOLVER in newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo oscillatingsource $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 2 --tstep 1 --num-tsteps 12 --baseNy 20 --tstepping euler --reg 0.00025 --nref 4 --solver-type $SOLVER --case oscillatingsource 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee oscillatingsourcefpdp2$SOLVER.log
#done
#
#for SOLVER in newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo oscillatingsource $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 1 --tstep 1 --num-tsteps 12 --baseNy 40 --tstepping euler --reg 0.00025 --nref 4 --solver-type $SOLVER --case oscillatingsource 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee oscillatingsourcefpdp1$SOLVER.log
#done
#

#for SOLVER in newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo cuspformation $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 2 --tstep .1 --num-tsteps 10 --baseNy 20 --tstepping euler --reg 0.025 --nref 4 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee cuspformationfpdp2$SOLVER.log
#done
#
#for SOLVER in newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo cuspformation $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 8 python stefan.py --p 1 --tstep .1 --num-tsteps 10 --baseNy 40 --tstepping euler --reg 0.025 --nref 4 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee cuspformationfpdp1$SOLVER.log
#done

for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
    echo "----------------------"
    echo cuspformation $SOLVER p=2;
    for i in 1 2 3 4; do 
      mpiexec -n 8 python stefan.py --p 2 --tstep .2 --num-tsteps 5 --baseNy 20 --tstepping euler --reg 0.04 --nref 4 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
    done 2>&1 | tee cuspformationp2$SOLVER.log
done

for SOLVER in newtonmg newtonaijfas newtonaijfaspardecomp; do
    echo "----------------------"
    echo cuspformation $SOLVER p=1;
    for i in 1 2 3 4; do 
      mpiexec -n 8 python stefan.py --p 1 --tstep .2 --num-tsteps 5 --baseNy 40 --tstepping euler --reg 0.04 --nref 4 --solver-type $SOLVER --case cuspformation 2>&1; # | grep -E '(^time|due to)';
    done 2>&1 | tee cuspformationp1$SOLVER.log
done

#for SOLVER in newtonaijfas newtonmg newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo simplerectangle $SOLVER p=2;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 2 --tstep .25 --num-tsteps 2 --baseNy 12 --tstepping euler --reg 0.1 --nref 4 --solver-type $SOLVER --case simplerectangle --init-cond 7 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee simplerectangle2dtp2$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo simplerectangle $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 1 --tstep .25 --num-tsteps 2 --baseNy 24 --tstepping euler --reg 0.1 --nref 4 --solver-type $SOLVER --case simplerectangle --init-cond 7 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee simplerectangle2dtp1$SOLVER.log
#done
#
#for SOLVER in newtonaijfas newtonmg newtonaijfaspardecomp; do
#    echo "----------------------"
#    echo simplerectangle $SOLVER p=1;
#    for i in 1 2 3 4; do 
#      mpiexec -n 16 python stefan.py --p 1 --tstep .001 --num-tsteps 2 --baseNy 24 --tstepping euler --reg 0.1 --nref 4 --solver-type $SOLVER --case simplerectangle --init-cond 0 2>&1; # | grep -E '(^time|due to)';
#    done 2>&1 | tee simplerectangle2dtstepp1$SOLVER.log
#done
