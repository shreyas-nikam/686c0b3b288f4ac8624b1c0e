
import pytest
import pandas as pd
from <your_module> import create_pairwise_registration_data

def test_dataframe_core_structure():
    """
    Test Case 1: Verify the basic structure of the returned object.
    It should be a non-empty Pandas DataFrame with the exact required column names.
    """
    df = create_pairwise_registration_data()
    
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame."
    assert not df.empty, "The DataFrame should not be empty."
    
    expected_columns = ['Dataset', 'Method', 'RE', 'TE', 'Recall@5°', 'Recall@1cm']
    assert list(df.columns) == expected_columns, \
        f"DataFrame columns mismatch. Expected: {expected_columns}, Got: {list(df.columns)}"

def test_dataframe_content_datasets_and_methods():
    """
    Test Case 2: Verify the presence of expected datasets and methods within the DataFrame.
    This ensures the simulation covers the specified data points from the RPF document.
    """
    df = create_pairwise_registration_data()
    
    # Check for specific datasets mentioned in the specification
    expected_datasets = ['TUD-L', 'ModelNet 40']
    assert set(expected_datasets).issubset(df['Dataset'].unique()), \
        f"Expected datasets {expected_datasets} not found in DataFrame. Found: {df['Dataset'].unique().tolist()}"
    
    # Check for a representative set of methods mentioned in the specification (Pairwise Registration section)
    # The spec lists: DCPNet, RPMNet, GeoTransformer, GARF, Diff-RPMNet, plus RPF (Single) and RPF (Joint)
    expected_methods_subset = [
        'RPF (Single)', 'RPF (Joint)', 'DCPNet', 'RPMNet', 
        'GeoTransformer', 'GARF', 'Diff-RPMNet'
    ]
    actual_methods = df['Method'].unique().tolist()
    assert all(method in actual_methods for method in expected_methods_subset), \
        f"Some expected methods {expected_methods_subset} not found in DataFrame. Found: {actual_methods}"

def test_numerical_columns_data_types_and_ranges():
    """
    Test Case 3: Verify that numerical columns have appropriate data types and plausible value ranges.
    RE and TE should be non-negative. Recall metrics should be between 0 and 100.
    """
    df = create_pairwise_registration_data()
    
    numerical_cols = ['RE', 'TE', 'Recall@5°', 'Recall@1cm']
    for col in numerical_cols:
        # Check if the column is numeric (integer or float)
        assert pd.api.types.is_numeric_dtype(df[col]), f"Column '{col}' should have a numeric data type."
        
        # Check for non-negativity for Rotation Error (RE) and Translation Error (TE)
        if col in ['RE', 'TE']:
            assert (df[col] >= 0).all(), f"All values in column '{col}' should be non-negative."
        
        # Check for Recall metrics to be within the 0 to 100 range (percentages)
        if col in ['Recall@5°', 'Recall@1cm']:
            assert (df[col] >= 0).all() and (df[col] <= 100).all(), \
                f"All values in column '{col}' should be between 0 and 100 (inclusive)."

def test_dataframe_data_completeness_and_uniqueness():
    """
    Test Case 4: Verify data completeness based on expected unique values and row count.
    Ensures that the DataFrame contains data for all specified datasets and methods,
    and has a reasonable number of rows indicating a full simulation.
    Also checks for uniqueness of (Dataset, Method) pairs.
    """
    df = create_pairwise_registration_data()
    
    expected_datasets_count = 2 # TUD-L, ModelNet 40
    # Minimum methods from the list provided in the spec's Pairwise Registration section
    expected_methods_min_count = 7 
    
    actual_datasets_count = df['Dataset'].nunique()
    actual_methods_count = df['Method'].nunique()
    
    assert actual_datasets_count == expected_datasets_count, \
        f"Expected {expected_datasets_count} unique datasets, but found {actual_datasets_count}."
    assert actual_methods_count >= expected_methods_min_count, \
        f"Expected at least {expected_methods_min_count} unique methods, but found {actual_methods_count}."
    
    # Check if the number of rows is at least the product of unique datasets and minimum expected methods
    min_expected_rows = expected_datasets_count * expected_methods_min_count
    assert df.shape[0] >= min_expected_rows, \
        f"DataFrame should contain at least {min_expected_rows} rows (2 datasets * min 7 methods), but found {df.shape[0]}."
    
    # Check for uniqueness of (Dataset, Method) pairs, as typical for tables of results
    assert df.duplicated(['Dataset', 'Method']).sum() == 0, \
        "DataFrame should not contain any duplicate (Dataset, Method) entries."

def test_no_null_values_in_dataframe():
    """
    Test Case 5: Verify that there are no NaN or null values in the DataFrame.
    Since the data is supposed to be 'pre-populated' and simulated internally,
    it should not contain any missing entries.
    """
    df = create_pairwise_registration_data()
    
    # Check for any null values across the entire DataFrame
    assert not df.isnull().values.any(), "DataFrame should not contain any null (NaN) values."
