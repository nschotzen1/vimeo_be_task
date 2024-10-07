import time
import requests

import time
import random

# Dictionary to store dubbing job information
dubbing_jobs = {}


def initialize_dubbing(file_name, format, input_file_path, source_lang, target_language, num_speakers=0):
    """Initialize a dubbing job and return a dubbing_id and expected_duration."""
    dubbing_id = f"dub-{int(time.time())}"
    expected_duration = 120  # Base expected duration in seconds
    # Store job details
    dubbing_jobs[dubbing_id] = {
        'expected_duration': expected_duration,
        'start_time': time.time()
    }
    return {'dubbing_id': dubbing_id, 'expected_duration': expected_duration}


def check_dubbing_status(dubbing_id):
    """Check the status of a dubbing job and return status, estimated_duration, and result_uri."""
    job = dubbing_jobs.get(dubbing_id)
    if not job:
        return {'status': 'INVALID_ID', 'estimated_duration': None, 'result_uri': None}

    elapsed_time = time.time() - job['start_time']
    # Apply random variation of ±15% to expected duration
    variation = random.uniform(-0.15, 0.15)
    modified_duration = job['expected_duration'] * (1 + variation)

    if elapsed_time >= modified_duration:
        status = 'COMPLETED'
        result_uri = f"https://3rdparty.api.com/results/{dubbing_id}.{format}"
        estimated_duration = 0
    else:
        status = 'IN_PROGRESS'
        result_uri = None
        estimated_duration = modified_duration - elapsed_time

    return {'status': status, 'estimated_duration': estimated_duration, 'result_uri': result_uri}