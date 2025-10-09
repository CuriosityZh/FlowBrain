from typing import List, Dict, Any
from .task_graph import TaskGraph
from .agent_executor import AgentExecutor
from .adaptive_policy import AdaptivePolicy


class FlowManager:
    """Orchestrates multi-agent workflows using adaptive policies."""

    def __init__(self):
        self.task_graph = TaskGraph()
        self.executor = AgentExecutor()
        self.policy = AdaptivePolicy()

    async def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Executes the workflow according to adaptive policies."""
        print("[FlowManager] Initializing execution flow...")
        ready_tasks = self.task_graph.get_ready_tasks()

        results = {}
        while ready_tasks:
            task = ready_tasks.pop(0)
            strategy = self.policy.select_strategy(task)
            print(f"[FlowManager] Executing task '{task.id}' with strategy '{strategy}'")
            result = await self.executor.execute(task, strategy, input_data)
            results[task.id] = result
            self.task_graph.mark_done(task.id, result)
            ready_tasks = self.task_graph.get_ready_tasks()

        print("[FlowManager] Flow complete.")
        return results

    def visualize(self):
        """Debug-print the current task graph."""
        self.task_graph.visualize()
