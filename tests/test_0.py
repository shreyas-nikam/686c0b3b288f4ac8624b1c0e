import pytest
import pandas as pd
from definition_548c3e4056504811b544a543d89803a2 import create_pairwise_registration_data

def test_create_pairwise_registration_data():
    """
    Test cases for the create_pairwise_registration_data function.
    Ensures the function returns a properly structured pandas DataFrame
    with expected columns, data types, and content, adhering to the
    notebook specification.
    """
    # Call the function under test
    df = create_pairwise_registration_data()

    # Test Case 1: Verify that the function returns a pandas DataFrame
    assert isinstance(df, pd.DataFrame), \
        "The function should return an instance of pandas.DataFrame."

    # Test Case 2: Verify that the DataFrame is not empty
    assert not df.empty, \
        "The returned DataFrame should not be empty, it must contain data."

    # Test Case 3: Verify the presence of all expected columns
    expected_columns = ['Dataset', 'Method', 'RE', 'TE', 'Recall@5°', 'Recall@1cm']
    assert all(col in df.columns for col in expected_columns), \
        f"DataFrame is missing one or more expected columns. Expected: {expected_columns}, Got: {df.columns.tolist()}"

    # Test Case 4: Verify that the 'Dataset' column contains the specified datasets
    datasets_in_df = df['Dataset'].unique()
    assert 'TUD-L' in datasets_in_df, \
        "The 'Dataset' column must contain data for 'TUD-L' dataset."
    assert 'ModelNet 40' in datasets_in_df, \
        "The 'Dataset' column must contain data for 'ModelNet 40' dataset."

    # Test Case 5: Verify that the 'Method' column contains multiple unique methods
    # This implies that the DataFrame contains comparative data, not just a single entry.
    assert df['Method'].nunique() >= 1, \
        "The 'Method' column should contain at least one unique method."
    # Ensure there are methods associated with both specified datasets
    assert df[df['Dataset'] == 'TUD-L']['Method'].nunique() >= 1, \
        "TUD-L dataset should have at least one associated method."
    assert df[df['Dataset'] == 'ModelNet 40']['Method'].nunique() >= 1, \
        "ModelNet 40 dataset should have at least one associated method."

    # Test Case 6: Verify data types and value ranges for numerical columns
    numerical_cols = ['RE', 'TE', 'Recall@5°', 'Recall@1cm']
    for col in numerical_cols:
        # Check if the column exists (redundant with Test Case 3, but safe)
        assert col in df.columns, f"Numerical column '{col}' is missing."
        # Check if the column's data type is numeric
        assert pd.api.types.is_numeric_dtype(df[col]), \
            f"Column '{col}' should contain numeric data (e.g., int, float)."
        # Check for non-negativity for error and recall metrics
        assert (df[col] >= 0).all(), \
            f"Column '{col}' should contain non-negative values."
        # For 'Recall' metrics, values are typically percentages, so they should not exceed 100.
        if 'Recall' in col:
            assert (df[col] <= 100).all(), \
                f"Recall metric '{col}' values should not exceed 100 (assuming percentage)."

    # Test Case 7: Verify data types and content for string/categorical columns
    string_cols = ['Dataset', 'Method']
    for col in string_cols:
        # Check if the column exists (redundant with Test Case 3, but safe)
        assert col in df.columns, f"String column '{col}' is missing."
        # Check if the column's data type is string/object (typical for text)
        assert pd.api.types.is_string_dtype(df[col]), \
            f"Column '{col}' should contain string/object data."
        # Ensure no NaN values for essential identifiers
        assert df[col].isnull().sum() == 0, \
            f"Column '{col}' should not contain any missing (NaN) values."
        # Ensure no empty strings for essential identifiers
        assert all(isinstance(x, str) and len(x.strip()) > 0 for x in df[col]), \
            f"Column '{col}' should contain non-empty string values."

    # Test Case 8: Verify that specific entries for each dataset are present (implied by content requirements)
    # Ensure there's actual data for TUD-L and ModelNet 40, not just column headers.
    assert not df[df['Dataset'] == 'TUD-L'].empty, \
        "DataFrame should contain actual data rows for the 'TUD-L' dataset."
    assert not df[df['Dataset'] == 'ModelNet 40'].empty, \
        "DataFrame should contain actual data rows for the 'ModelNet 40' dataset."
