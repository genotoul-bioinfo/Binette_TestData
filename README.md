# Test data for Binette

**Binette is a binning refinement tool that constructs high-quality MAGs from the output of multiple binning tools.**

This repository contains test data and instructions for running Binette and comparing the results with expected outcomes.

## Test locally

1. **Install Binette**:

   Make sure you have Binette installed on your system. You can refer to the [Binette](https://github.com/genotoul-bioinfo/Binette) repository for installation instructions.


2. **Clone This Repository**:

   Clone this repository to your local machine using Git:

```bash

git clone https://github.com/genotoul-bioinfo/Binette_TestData.git

cd Binette_TestData

```

2. **Run Binette**:

   Execute Binette on the test data using the following command:

```bash
binette -b binning_results/* --contigs all_contigs.fna --checkm2_db checkm2_tiny_db/checkm2_tiny_db.dmnd  -v -o test_results

```

This command should complete in just a few seconds.

4. **Compare Results**: 

After running Binette, you can compare the generated `final_bins_quality_reports.tsv` with the expected results. Some variation in the completeness, contamination, and score columns is expected due to Checkm2's slight variability.

You can perform the comparison manually by using the head command:

```bash
head  expected_results/final_bins_quality_reports.tsv test_results/final_bins_quality_reports.tsv

```

Alternatively, you can use the provided Python script for automated comparison:  [compare_results.py](scripts/compare_results.py) 

```bash

python scripts/compare_results.py expected_results/final_bins_quality_reports.tsv test_results/final_bins_quality_reports.tsv

```