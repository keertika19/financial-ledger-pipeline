# Technical Report: End-to-End Exactly-Once Data Integrity in Financial Ledgers

## 1. Abstract & System Motivation
In financial ledger accounting, double counting or dropping a transaction is a critical compliance failure. Ensuring end-to-end exactly-once delivery guarantees data consistency across distributed ingestion systems.

## 2. Architecture & Transactional Mechanics
The system utilizes Apache Kafka as an append-only log, Apache Flink for real-time stream processing and checkpoint orchestration, and Apache Iceberg as the immutable ACID table format.

### Two-Phase Commit Protocol (2PC)
- **Pre-Commit Phase**: Flink writes incoming data into temporary Iceberg data files. When a checkpoint is triggered, checkpoint barriers flow through the streaming DAG.
- **Commit Phase**: Upon receiving checkpoint acknowledgments from all tasks, the JobManager commits the transaction manifest to Iceberg, advancing the metadata snapshot atomically.

## 3. Failure Injection & Resilience Analysis
1. **TaskManager Failure**: Flink restores state from the latest successful checkpoint. Uncommitted files created after the checkpoint are ignored by Iceberg's metadata snapshot.
2. **Kafka Broker Restart**: Kafka producer retries prevent data loss while Flink consumer offsets roll back to the last committed checkpoint offset.

## 4. Conclusion & Accountability Standard
Data integrity is an organizational and legal requirement. System auditability relies on deterministic stream processing coupled with ACID table formats.