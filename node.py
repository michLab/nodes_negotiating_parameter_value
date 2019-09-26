import queue
from time import time, sleep

class Node:
    """ A simple node class"""
    
    def __init__(self, name='Anonymous Node', queue_in=None, queue_out=None):
        # Initialize the class members
        self.name = name
        if queue_in is None:
            self.queue_in = queue.Queue()
        else:
            self.queue_in = queue_in
        if queue_out is None:
            self.queue_out = queue.Queue()
        else:
            self.queue_out = queue_out
        self.negotiated_parameter = 0
        self.allowed_parameter_values = range(0, 100)
        self.free_parameter_list = []
        self.nodes_list = []
        self.watchdog_timeout = 5  # After that time the msg will be removed [Seconds]

    def add_new_node(self):
        """Processes received message"""
        while not self.queue_in.empty():
            msg = self.queue_in.get_nowait()
            time = self.get_time()
            new_node = {
                "time": time,
                "name": msg[0],
                "parameter": msg[1]
            }
            # Check if node is already on the list:
            node_is_on_the_list = False
            for node in self.nodes_list:
                print node
                if node["name"] is new_node["name"]:
                    node_is_on_the_list = True
            if not node_is_on_the_list:
                self.nodes_list.append(new_node)

    def get_time(self):
        """Returns time in [s] sinde 01.01.1970 00:00:00"""
        return time()

    def show_nodes_list(self):
        """Shows all nodes stored in nodes_list"""
        print("[Node: " + str(self.name) + "]: nodes_list members: ")
        for node in self.nodes_list:
            print(node)
    
    def introduce(self):
        """Introduce yourself to the World!"""
        print("[Node " + str(self.name) + "]: Hi, I am node " + str(self.name))

    def watchdog(self):
        current_time = self.get_time()
        self.nodes_list[:] = [x for x in self.nodes_list if not (current_time-x["time"] > self.watchdog_timeout)]
        
    def loop(self):
        """A loop, where node sends and receives messages"""
        while True:
            self.add_new_node()
            self.watchdog()
            self.show_nodes_list()
            sleep(1)
            
        



        
