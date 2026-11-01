# Data Card: Financial Ledger Transaction Stream

## Dataset Overview
- **Name**: Simulated Financial Ledger Stream
- **Purpose**: Benchmarking Exactly-Once processing semantics under failure conditions.
- **Fields**:
  - `transaction_id` (UUID): Unique global identifier.
  - `sequence_num` (Monotonic Long): Strictly increasing integer for gap detection.
  - `account_from` (String): Source account ID.
  - `account_to` (String): Destination account ID.
  - `amount` (Decimal): Transfer value in USD.
  - `timestamp` (Timestamp): Ingestion event time.

## Integrity Assertions
- Zero duplicate `transaction_id` values allowed.
- Zero gap in `sequence_num` range.