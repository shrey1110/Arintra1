import pandas as pd
import pytest


def validate_sheets(expected_sheet, actual_sheet, expected_column):
    expected = pd.read_csv(expected_sheet)
    actual = pd.read_csv(actual_sheet)

    merged_data = pd.merge(expected,actual,on="id",suffixes=("_expected","_actual"))

    for i, row in merged_data.iterrows():
        expected_col = row[expected_column].split(',')

        for col in expected_col:
            exp_value = row[f"{col}_expected"]
            actual_value = row[f"{col}_actual"]

            assert exp_value == actual_value, (
                f"Expected: {exp_value}, actual: {actual_value}, row: {i}"
            )



@pytest.mark.parametrize("expected_sheet,actual_sheet,expected_column", [
    ("1.csv", "2.csv","Expected Column"),("5.csv","6.csv", "Expected Column")])
def test_data(expected_sheet, actual_sheet, expected_column):
    validate_sheets(expected_sheet, actual_sheet,expected_column)
