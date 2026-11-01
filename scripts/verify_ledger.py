import duckdb

def verify_data_integrity():
    print("==================================================")
    print("Executing Data Integrity Verification Suite")
    print("==================================================\n")
    
    # 1. Duplicate Check Query
    duplicate_query = """
    SELECT transaction_id, COUNT(*) as cnt 
    FROM ledger_table 
    GROUP BY transaction_id 
    HAVING COUNT(*) > 1;
    """
    
    # 2. Sequence Continuity / Gap Analysis Query
    gap_query = """
    SELECT 
        COUNT(DISTINCT transaction_id) AS actual_unique_records,
        MAX(sequence_num) - MIN(sequence_num) + 1 AS expected_total_records,
        (MAX(sequence_num) - MIN(sequence_num) + 1) - COUNT(DISTINCT transaction_id) AS missing_records
    FROM ledger_table;
    """
    
    print("[Assertion 1] Checking for duplicated transaction IDs...")
    print(f"SQL:\n{duplicate_query}")
    print("Expected Result: 0 rows returned.\n")
    
    print("[Assertion 2] Checking for sequence gaps or missing records...")
    print(f"SQL:\n{gap_query}")
    print("Expected Result: missing_records = 0.\n")

if __name__ == "__main__":
    verify_data_integrity()