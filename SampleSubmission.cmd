#!/bin/csh -f
#  CuCunrec.cmd
#
#  SGE job for  built Mon Apr 16 23:28:48 PDT 2012
#
#  The following items pertain to this script
#  Use current working directory
#$ -cwd
#  input           = /dev/null
#  output          = /u/home/a/an5989/Documents/VASP/CuCunrec/vasp.output.$JOB_ID
#$ -o /u/home/a/an5989/Documents/VASP/CuCunrec/vasp.output.$JOB_ID
#  error           = Merged with output
#$ -j y
#  The following items pertain to the user program
#  program    = /u/home/a/an5989/Documents/vasp5.2.12build/vasp.5.2/vasp
#  arguments       =
#  program input   = Specified by user
#  program output  = Specified by user
#  Parallelism:  8-way parallel
#  Resources requested
## -pe 8threads* 8
#$ -pe dc_* 8
#$ -l h_data=4G,h_rt=23:00:00
#
#
#  Name of application for log
#$ -v QQAPP=espresso
#  Email address to notify
#$ -M an5989@g.ucla.edu
#  Notify at beginning and end of job
#$ -m ea
#  Job is not rerunable
#$ -r n
#
# Initialization for  parallel execution
#

setenv NBO_VASP yes

  unalias *
  set qqversion =
  set qqapp     = "espresso parallel"
  set qqptasks  = 8
  set qqptasksshm8  = 8
  set qqidir    = /u/home/a/an5989/Documents/VASP/CuCunrec/
  set qqjob     =
  set qqexedir  = /u/home/a/an5989/Documents/vasp5.2.12build/vasp.5.2/
  set qqespresso = vasp
   set qqodir    = /u/home/a/an5989/Documents/VASP/CuCunrec/
  cd  /u/home/a/an5989/Documents/VASP/CuCunrec/
  source /u/home/z/zhangjin/bin/qr.runtime
  if ($status != 0) exit (1)
#
  echo "SGE job for  built Mon Apr 16 23:28:48 PDT 2012"
  echo ""
  echo "   directory:"
  echo "    "/u/home/a/an5989/Documents/VASP/CuCunrec/
  echo "  Submitted to SGE:"
  echo "    "$qqsubmit
  echo "  'scratch' directory (on each node):"
  echo "    $qqscratch"
  echo "   8-way parallel job configuration:"
  echo "    $qqconfig" | tr "\\" "\n"
#
  echo ""
  echo "CuCunrec.cmd started on:   "` hostname -s `
  echo "CuCunrec.cmd started at:   "` date `
  echo ""
#
# Run the user program
#

  source /u/local/Modules/default/init/modules.csh
  module load intel/11.1 openmpi/1.4 lapack/3.4.0 fftw/3.2 ATS python/3.1
  echo " "
  module list
  echo " "
  which mpiexec
  echo " "

  rm /u/scratch/a/an5989/VASP/_$JOB_ID -rf
  mkdir /u/scratch/a/an5989/VASP/_$JOB_ID
  cp /u/home/a/an5989/Documents/VASP/CuCunrec/* /u/scratch/a/an5989/VASP/_$JOB_ID/
  touch /u/home/a/an5989/Documents/VASP/CuCunrec/OUTCAR.$JOB_ID
  cd /u/scratch/a/an5989/VASP/_$JOB_ID

# SCF
  time mpiexec -n  8  -machinefile $QQ_NODEFILE /u/home/a/an5989/Documents/vasp5.2.12build/vasp.5.2/vasp 

  cp /u/scratch/a/an5989/VASP/CuCunrec_$JOB_ID/* /u/home/a/an5989/Documents/VASP/CuCunrec/
  cd /u/home/a/an5989/Documents/VASP/CuCunrec/
  mv OUTCAR OUTCAR.$JOB_ID
  
  echo "CuCunrec.cmd finished at:  "` date `
#
# Cleanup after mpi parallel execution
#
  source /u/home/z/zhangjin/bin/qr.runtime
#
  echo "-------- /u/home/a/an5989/VASP/vasp.output.$JOB_ID --------" >> /u/local/apps/queue.logs/espresso.log.parallel
 if (`wc -l /u/home/a/an5989/Documents/VASP/CuCunrec/vasp.output.$JOB_ID  | awk '{print $1}'` >= 1000) then
        head -50 /u/home/a/an5989/Documents/VASP/CuCunrec/vasp.output.$JOB_ID >> /u/local/apps/queue.logs/espresso.log.parallel
        echo " "  >> /u/local/apps/queue.logs/espresso.log.parallel
        tail -10 /u/home/a/an5989/Documents/VASP/CuCunrec/vasp.output.$JOB_ID >> /u/local/apps/queue.logs/espresso.log.parallel
  else
        cat /u/home/a/an5989/Documents/VASP/CuCunrec/vasp.output.$JOB_ID >> /u/local/apps/queue.logs/espresso.log.parallel
  endif
#    cat            /u/home/a/an5989/Documents/VASP/CuCunrec/vasp.output.$JOB_ID  >> /u/local/apps/queue.logs/espresso.log.parallel
  exit (0)
                                                                                      109,1         Bot


                                                                                      93,0-1        74%

                                                                                      1,1           Top
