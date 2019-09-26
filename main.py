import queue
import threading

from time import sleep

from node import Node


def node_callback(arg_node_name="", arg_queue_in=None, arg_queue_out=None):
    """A callback function for a node's thread"""
    local_node = Node(name=arg_node_name, queue_in=arg_queue_in,
                      queue_out=arg_queue_out)
    local_node.introduce()
    local_node.loop()

def main():
    """A main function to run rimulation"""
    node_count = 1
    node_list = []
    queue_to_node_list = []
    queue_from_node_list = []
    thread_list = []

    for node_number in range(0, node_count):
        # Create queues and threads for each node:
        print "Creating a node:"
        queue_to_node = queue.Queue()
        queue_to_node_list.append(queue_to_node)
        queue_from_node = queue.Queue()
        queue_from_node_list.append(queue_from_node)
        thread = threading.Thread(target=node_callback, kwargs=dict(arg_node_name=str(node_number),
                                  arg_queue_in=queue_to_node, arg_queue_out=queue_from_node))
        thread.setDaemon(True)
        thread.start()
        thread_list.append(thread)

    loop_number = 0
    while True:
        synthetic_message = (str(loop_number), 1)
        queue_to_node_list[0].put_nowait(synthetic_message)
        print "Put message to node"
        loop_number += 1
        sleep(2)



if __name__ == '__main__':
    main()

