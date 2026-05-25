#!/bin/bash
# The line above this is the "shebang" line.  It must be first line in script
#-----------------------------------------------------
#	SLURM Job Script for Deep Learning Assignment 3
#	Converts and executes Jupyter notebook on GPU
#-----------------------------------------------------
#
# Slurm sbatch parameters section:
#	Request a single task using a single CPU core
#SBATCH -t 30:00
#SBATCH -n 2
#SBATCH --gpus=a100:1
#SBATCH --partition=gpu
#	Do not inherit the environment of the process running the
#	sbatch command.  This requires you to explicitly set up the
#	environment for the job in this script, improving reproducibility
#SBATCH --export=NONE


# This job will convert and run the Assignment 3 Jupyter notebook
# Output will go to local /tmp scratch space on the node we are running
# on, and then will be copied back to our work directory.

# Section to ensure we have the "module" command defined
unalias tap >& /dev/null
if [ -f ~/.bash_profile ]; then
	source ~/.bash_profile
elif [ -f ~/.profile ]; then
	source ~/.profile
fi

# Set SLURM_EXPORT_ENV to ALL.  This prevents the --export=NONE flag
# from being passed to mpirun/srun/etc, which can cause issues.
# We want the environment of the job script to be passed to all 
# tasks/processes of the job
export SLURM_EXPORT_ENV=ALL

# Module load section
# First clear our module list 
module purge
# and reload the standard modules
module load hpcc/deepthought2
# Load Python with CUDA support for TensorFlow/Keras
module load python/gcc/11.3.0/cuda/3.10.10
# Load CUDA toolkit
module load cuda/11.8.0

# Section to make a scratch directory for this job
# For GPU jobs, local /tmp filesystem is a good choice
# We include the SLURM jobid in the directory name to avoid interference if 
# multiple jobs running at same time.
TMPWORKDIR="/tmp/assignment3-job.${SLURM_JOBID}"
mkdir $TMPWORKDIR
cd $TMPWORKDIR

# Copy the notebook to our working directory
cp "${SLURM_SUBMIT_DIR}/Assignment_3,_Code.ipynb" .

# Section to output information identifying the job, etc.
echo "Slurm job ${SLURM_JOBID} running on"
hostname
echo "To run on ${SLURM_NTASKS} CPU cores with ${SLURM_GPUS} GPU(s)"
echo "All nodes: ${SLURM_JOB_NODELIST}"
echo "GPU devices: ${CUDA_VISIBLE_DEVICES}"
date
pwd
echo "Loaded modules are:"
module list
echo "Job will be started out of $TMPWORKDIR"

# Check GPU availability
nvidia-smi

# Set up Python environment and install required packages
echo "Setting up Python environment..."
pip install --user jupyter nbconvert tensorflow keras matplotlib pandas numpy

# Convert notebook to Python script
echo "Converting Jupyter notebook to Python script..."
jupyter nbconvert --to script "Assignment_3,_Code.ipynb" --output assignment3_script

# Run the converted Python script
echo "Running the converted script..."
python assignment3_script.py > assignment3_output.log 2>&1

# Save the exit code from the previous command
ECODE=$?

# Copy results back to submit dir
echo "Copying results back to submit directory..."
cp assignment3_output.log "${SLURM_SUBMIT_DIR}/"
cp assignment3_script.py "${SLURM_SUBMIT_DIR}/"

# Copy any generated plots or output files
cp *.png "${SLURM_SUBMIT_DIR}/" 2>/dev/null || echo "No PNG files to copy"
cp *.pdf "${SLURM_SUBMIT_DIR}/" 2>/dev/null || echo "No PDF files to copy"

echo "Job finished with exit code $ECODE"
date

# Exit with the cached exit code
exit $ECODE