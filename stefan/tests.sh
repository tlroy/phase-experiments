#!/bin/bash
for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
  for dt in 0.5 0.25 0.1 0.01; do
    echo $SOLVER dt=$dt initial=step p=3;
    for i in 1 2 3 4; do 
      mpiexec -n 16 python stefan.py --p 3 --tstep $dt --baseNy 8 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
    done
    echo "----------------------"
  done 2>&1 | tee $SOLVER.log
done

for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
  for dt in 0.5 0.25 0.1 0.01; do
    echo $SOLVER dt=$dt initial=tanh p=3;
    for i in 1 2 3 4; do 
      mpiexec -n 16 python stefan.py --p 3 --tstep $dt --init-cond tanh --baseNy 8 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
    done
    echo "----------------------"
  done 2>&1 | tee $SOLVER.log
done

for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
  for dt in 0.5 0.25 0.1 0.01; do
    echo $SOLVER dt=$dt initial=tanh p=4;
    for i in 1 2 3 4; do 
      mpiexec -n 16 python stefan.py --p 4 --tstep $dt --init-cond tanh --baseNy 6 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
    done
    echo "----------------------"
  done 2>&1 | tee $SOLVER.log
done


for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
  for dt in 0.5 0.25 0.1 0.01; do
    echo $SOLVER dt=$dt initial=step p=2;
    for i in 1 2 3 4; do 
      mpiexec -n 16 python stefan.py --p 2 --tstep $dt --init-cond step --baseNy 12 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
    done
    echo "----------------------"
  done 2>&1 | tee $SOLVER.log
done

for SOLVER in newtonaijfaspardecomp faspardecomp ngmresfaspardecomp newtonmg newtonbasicmg; do
  for dt in 0.5 0.25 0.1 0.01; do
    echo $SOLVER dt=$dt initial=tanh p=2;
    for i in 1 2 3 4; do 
      mpiexec -n 16 python stefan.py --p 2 --tstep $dt --init-cond tanh --baseNy 12 --solver-type $SOLVER 2>&1; # | grep -E '(^time|due to)';
    done
    echo "----------------------"
  done 2>&1 | tee $SOLVER.log
done
