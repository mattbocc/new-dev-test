# SBATCH Script Fixes

## Changes Made

**Resource Optimization:**
- Reduced nodes from 10 to 1 (small dataset)
- Reduced ntasks from 40 to 5 (better resources)  
- Increased memory from 200M to 4G (sufficient for typical workflows)

**Module & Execution:**
- Changed `module load R` to `module load snakemake`
- Replaced broken R script call with `snakemake --cores 4 -s pipeline.smk`

**Notifications:**
Added email notifications on job completion/failure.
