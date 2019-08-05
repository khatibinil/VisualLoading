import time
import sys

def loading_progress(progress):
    """Display loading percentatge of a task."""
    dots = int(round(5*progress))
    msg = "\r{0}% complete. Loading{1}".format(round(progress*100, 2), "."*dots)
    sys.stdout.write(msg)
    sys.stdout.flush()

def main(task_length):
    """Create long running task."""
    for i in range(task_length):
        time.sleep(0.05)
        loading_progress(i/task_length)
    print("\r\nLoading Complete!")

if __name__ == "__main__":
    task_length = 100
    main(task_length)
