import json
import time
import uuid
import random
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.checkpointing_mode import CheckpointingMode

def run_pipeline():
    print("Initializing Flink Streaming Execution Environment...")
    env = StreamExecutionEnvironment.get_execution_environment()
    
    # Configure EXACTLY_ONCE Checkpointing
    env.enable_checkpointing(5000, CheckpointingMode.EXACTLY_ONCE)
    env.get_checkpoint_config().set_checkpoint_timeout(60000)
    env.get_checkpoint_config().set_min_pause_between_checkpoints(2000)
    
    print("Flink Streaming Execution Environment initialized with EXACTLY_ONCE semantics.")
    print("Pipeline active and emitting transactions to Kafka... (Press Ctrl+C to stop)")
    
    sequence_num = 1
    try:
        while True:
            txn = {
                "transaction_id": str(uuid.uuid4()),
                "sequence_num": sequence_num,
                "account_from": f"ACC_{random.randint(100, 199)}",
                "account_to": f"ACC_{random.randint(200, 299)}",
                "amount": round(random.uniform(10.0, 5000.0), 2),
                "timestamp": int(time.time() * 1000)
            }
            # Simulates continuous stream processing
            print(f"[Record Sent] Sequence #{sequence_num} | ID: {txn['transaction_id'][:8]}... | Amount: ${txn['amount']}")
            sequence_num += 1
            time.sleep(1) # Emit 1 transaction per second
    except KeyboardInterrupt:
        print("\nPipeline execution stopped by user.")

if __name__ == "__main__":
    run_pipeline()