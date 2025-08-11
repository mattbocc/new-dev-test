import pandas as pd
import numpy as np

# Extract
rnaseq_tpm = pd.read_csv('data/CCLE_RNAseq_rsem_genes_tpm_20180929.txt', sep='\t')
rnaseq_metadata = pd.read_csv('data/Cell_lines_annotations_20181226.txt', sep='\t')

# Transform
# Drop columns with >700 missing values in metadata
missing_counts = rnaseq_metadata.isnull().sum() + (rnaseq_metadata == '').sum()
cols_to_drop = missing_counts[missing_counts > 700].index.tolist()
if cols_to_drop:
    rnaseq_metadata = rnaseq_metadata.drop(columns=cols_to_drop)

# Drop transcript_ids and apply log2 transformation
rnaseq_tpm = rnaseq_tpm.drop(columns=['transcript_ids'])
numeric_cols = rnaseq_tpm.columns[1:]
for col in numeric_cols:
    rnaseq_tpm[col] = np.log2(pd.to_numeric(rnaseq_tpm[col]) + 0.001)

# Find common cell lines and subset data
rnaseq_cell_lines = set(rnaseq_tpm.columns[1:])
metadata_cell_lines = set(rnaseq_metadata['CCLE_ID'])
common_cell_lines = rnaseq_cell_lines.intersection(metadata_cell_lines)

rnaseq_metadata = rnaseq_metadata[rnaseq_metadata['CCLE_ID'].isin(common_cell_lines)]
common_cols = ['gene_id'] + [col for col in rnaseq_tpm.columns[1:] if col in common_cell_lines]
rnaseq_tpm = rnaseq_tpm[common_cols]

# Reorder metadata to match RNA-seq column order
rnaseq_order = rnaseq_tpm.columns[1:]
order_map = {cell_line: i for i, cell_line in enumerate(rnaseq_order)}
rnaseq_metadata['order'] = rnaseq_metadata['CCLE_ID'].map(order_map)
rnaseq_metadata = rnaseq_metadata.sort_values('order').drop(columns=['order'])

# Load
rnaseq_tpm.to_csv('output/rnaseq_tpm_transformed.csv', index=False)
rnaseq_metadata.to_csv('output/rnaseq_metadata_transformed.csv', index=False)

print(f"RNA-seq shape: {rnaseq_tpm.shape}")
print(f"Metadata shape: {rnaseq_metadata.shape}")
print(f"Common cell lines: {len(common_cell_lines)}")