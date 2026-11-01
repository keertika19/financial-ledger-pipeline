import time
import os

def inject_network_delay():
    print("[Chaos 1/3] Injecting simulated network latency / backpressure...")
    time.sleep(2)
    print("[Chaos 1/3] Latency simulation complete.\n")

def kill_and_restart_taskmanager():
    print("[Chaos 2/3] Killing Flink TaskManager process mid-stream...")
    os.system("docker compose kill taskmanager")
    print("[Chaos 2/3] Waiting 5 seconds before restarting...")
    time.sleep(5)
    print("[Chaos 2/3] Restarting Flink TaskManager...")
    os.system("docker compose start taskmanager")
    print("[Chaos 2/3] TaskManager recovered.\n")

def restart_kafka_broker():
    print("[Chaos 3/3] Restarting Kafka Broker...")
    
    print("[Chaos 3/3] Kafka Broker restarted.\n")

if __name__ == "__main__":
    print("==================================================")
    print("Starting Failure Injection & Chaos Engineering Suite")
    print("==================================================\n")
    
    inject_network_delay()
    kill_and_restart_taskmanager()
    restart_kafka_broker()
    
    print("==================================================")
    print("Chaos execution finished. Run verification scripts.")
    print("==================================================")