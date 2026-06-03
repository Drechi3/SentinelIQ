class GPUScheduler:
    def __init__(self):
        self.nodes = [
            "nosana-node-1",
            "nosana-node-2",
            "nosana-node-3"
        ]

    def allocate(self, workload="inference"):
        return {
            "assigned_node": self.nodes[0],
            "workload": workload
        }