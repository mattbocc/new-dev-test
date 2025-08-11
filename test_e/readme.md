# (Bonus problem) ETL Pipeline

## Input Files

- `data/CCLE_RNAseq_rsem_genes_tpm_20180929.txt`
- `data/Cell_lines_annotations_20181226.txt`

## Run

```bash
python3 script.py
```

It will create 2 files in `output` folder:

- `rnaseq_tpm_transformed.csv` - Transformed RNA-seq data
- `rnaseq_metadata_transformed.csv` - Transformed metadata

And successfully will show 1019 cell lines:

```
RNA-seq shape: (57820, 1020)
Metadata shape: (1019, 22)
Common cell lines: 1019
```

## Process

1. Extract: Load both input files
2. Transform:
   - Drop metadata columns with >700 missing values
   - Remove transcript_ids column from RNA-seq data
   - Apply log transformation to numeric values
   - Filter for common cell lines (expected: 1019)
   - Align metadata order with RNA-seq columns
3. Load: Save transformed data as CSV