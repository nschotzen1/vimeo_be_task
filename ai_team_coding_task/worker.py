from queue import DubbingQueue
class Worker:
    def __init__(self, queue):
        self.queue = queue

    def process_message(self, message):
        # Candidate to implement
        pass

# Sample message
message = {
    'id': 'job1',
    'file_name': 'video123.mp4',
    'format': 'mp4',
    'input_file_path': '/path/to/video123.mp4',
    'source_lang': 'en',
    'target_language': 'es'
}

queue = DubbingQueue()
worker = Worker(queue)

# Add sample messages to the queue
message1 = {
    'id': 'job1',
    'file_name': 'video123.mp4',
    'format': 'mp4',
    'input_file_path': '/path/to/video123.mp4',
    'source_lang': 'en',
    'target_language': 'es'
}
queue.add_message(message1)

message2 = {
    'id': 'job2',
    'file_name': 'video456.mp4',
    'format': 'mp4',
    'input_file_path': '/path/to/video456.mp4',
    'source_lang': 'en',
    'target_language': 'fr'
}
queue.add_message(message2)
print('asdf')
# Main loop to continuously process messages
while True:
    message = queue.get_message()
    if message:
        worker.process_message(message)
    else:
        print("No messages to process. Waiting...")
        time.sleep(5)
