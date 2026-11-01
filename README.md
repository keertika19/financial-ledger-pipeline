# Exactly-Once Financial Ledger Pipeline (Kafka -> Flink -> Iceberg)

## Architecture Overview

[ Ledger Producer ] -> [ Kafka Topic: financial-txns ]
| (Transactional Reading)
[ Apache Flink ] (Two-Phase Commit Sink)
|
[ Apache Iceberg Table ]

## Setup & Execution Steps
1. **Start Infrastructure**:
   ```bash
   docker-compose up -d