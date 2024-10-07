You are tasked with building a Python-based queue system to manage video dubbing jobs processed by a third-party API. The system should efficiently handle job initialization, status checking, and optimize for scalability by avoiding blocking operations.

1. Building the Queue: Use existing Python libraries to create a basic queue.
2. Implementing the Worker: Complete the process_message method in the worker class.


# Context
**TODO:** You are working as a backend engineer for a company that provides video content services. Your team is developing a new feature that allows users to have their videos translated into multiple target languages using a third-party dubbing API. This service needs to handle multiple dubbing jobs efficiently, ensuring that users receive their dubbed videos in a timely manner

# Task & Objectives
**TODO:** Your task is to design and implement a queue system in Python to manage the video translation jobs using the third-party API. The system should handle job initialization, status checking, and retries, ensuring efficient processing.

You will start by building a basic queue using Python's standard libraries. Then, you will implement a worker that processes messages from the queue. 

### 1. Set Objectives 
**TODO:** 

1. Implement the Queue System:

Use Python's standard libraries (e.g., queue.Queue) to build a basic queue that can add and retrieve messages.
Ensure the queue can handle messages representing dubbing jobs.
Complete the Worker Implementation:

2. Implement the process_message method in the provided worker class.
The worker should:
Initialize new dubbing jobs using the initialize_dubbing function if the message lacks a dubbing_id.
Check the status of existing dubbing jobs using the check_dubbing_status function if the message includes a dubbing_id.
Handle job statuses appropriately, including handling of "COMPLETED", "IN_PROGRESS", and "FAILED" statuses.



# Guidance
**TODO:** For the initial implementation, it is acceptable for the worker to wait (block) while checking job statuses. We will discuss optimization following the initial implementation. 

Following  Questions:

What happens if there are multiple messages in the queue?
How can we modify the system to avoid blocking and improve scalability?
Is there a feature or mechanism we can introduce to manage message processing more efficiently?




