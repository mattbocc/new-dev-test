FROM condaforge/miniforge3:latest

WORKDIR /app

# copy env file first for better caching
COPY envs/pipeline.yaml /app/envs/

# create conda env
RUN mamba env create -f envs/pipeline.yaml && \
    mamba clean -afy

# make RUN commands use the new env
SHELL ["mamba", "run", "-n", "tcl38-mini", "/bin/bash", "-c"]

# copy the rest of the project
COPY . /app/

# ensure scripts are executable
RUN chmod +x scripts/*.R

# set default command
CMD ["mamba", "run", "-n", "tcl38-mini", "snakemake", "--cores", "1", "outputs/summary.csv"]