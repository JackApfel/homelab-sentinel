import os
import psutil
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=dotenv_path)

def get_env_int(name: str) -> int:
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"{name} fehlt in {dotenv_path}")
    return int(value)

CPU_THRESHOLD_WARNING = get_env_int("CPU_THRESHOLD_WARNING")
CPU_THRESHOLD_CRITICAL = get_env_int("CPU_THRESHOLD_CRITICAL")

MEMORY_THRESHOLD_WARNING = get_env_int("MEMORY_THRESHOLD_WARNING")
MEMORY_THRESHOLD_CRITICAL = get_env_int("MEMORY_THRESHOLD_CRITICAL")

STORAGE_THRESHOLD_WARNING = get_env_int("STORAGE_THRESHOLD_WARNING")
STORAGE_THRESHOLD_CRITICAL = get_env_int("STORAGE_THRESHOLD_CRITICAL")

GPU_THRESHOLD_WARNING = get_env_int("GPU_THRESHOLD_WARNING")
GPU_THRESHOLD_CRITICAL = get_env_int("GPU_THRESHOLD_CRITICAL")


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory()

def get_disk_usage(path='/'):
    return psutil.disk_usage(path)


def check_threshold(value, warning, critical):
    if warning is None or critical is None:
        raise ValueError("Warning and critical thresholds must be provided")

    if warning >= critical:
        raise ValueError("Warning threshold must be lower than critical threshold")

    if value < warning:
        return "OK"

    if value < critical:
        return "WARNING"

    return "CRITICAL"

def get_status():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    storage = get_disk_usage()

    status = {
        "cpu": {
            "usage": cpu,
            "state": check_threshold(cpu, CPU_THRESHOLD_WARNING, CPU_THRESHOLD_CRITICAL),
        },
        "memory": {
            "usage": memory.percent,
            "state": check_threshold(
                memory.percent,
                MEMORY_THRESHOLD_WARNING,
                MEMORY_THRESHOLD_CRITICAL,
            ),
        },
        "storage": {
            "usage": storage.percent,
            "state": check_threshold(
                storage.percent,
                STORAGE_THRESHOLD_WARNING,
                STORAGE_THRESHOLD_CRITICAL,
            ),
        },
    }

    return status
