import pandas as pd
import numpy as np

from argparse import ArgumentParser

def is_close(value1, value2, tolerance):

    return all(abs(value1 - value2) <= tolerance)
    
    
def main():
    args = parse_arguments()

    df1 = pd.read_csv(args.binette_report_A, delimiter='\t')
    df2 = pd.read_csv(args.binette_report_B, delimiter='\t')


    # Compare columns that require exact matching
    exact_columns = ["origin", "size", "N50", "contig_count"]
    exact_match = (df1[exact_columns] == df2[exact_columns]).all(axis=1)

    # Compare columns with tolerance

    tolerance_columns = ['completeness', 'contamination', "score"]
    tolerance_col_to_isclose = {}
    for col in tolerance_columns:
        tolerance_col_to_isclose[col] = is_close(df1[col], df2[col], args.tolerance)
    tolerance_cols_ok = all(tolerance_col_to_isclose.values())

    # Check if both exact and tolerance comparisons are satisfied
    if exact_match.all() and  tolerance_cols_ok:
        print("Binette quality reports are identical within the specified tolerance.")
        exit(0)
    else:
        
        print("Binette quality reports files differ in some columns.")
        if not tolerance_cols_ok:
            problematic_cols = [c for c, v in tolerance_col_to_isclose.items() if not v]
            print(f'Columns that display such different values: {problematic_cols}' )
            
        exit(1)

def parse_arguments():
    """Parse script arguments."""

    parser = ArgumentParser()

    parser.add_argument("binette_report_A",  help="A final_bins_quality_reports.tsv output from binette to compare.")
    parser.add_argument("binette_report_B",  help="Another final_bins_quality_reports.tsv output from binette to compare.")
    
    parser.add_argument("--tolerance",  required=False, type=float, default=1., help="Tolerance in completeness and contamination variariton form checkm2.")

    args = parser.parse_args()
    return args


# If this script is run from the command line then call the main function.
if __name__ == "__main__":
    main()
    