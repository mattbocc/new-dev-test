#!/bin/bash
#SBATCH --job-name=test
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=1:00:00
#SBATCH --mem=5G
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=john.doe@uhn.com
module load snakemake
snakemake --cores 4 -s pipeline.smk
