from typing import List, Dict, Any
from dataclasses import dataclass, field


@dataclass
class TaskNode:
    id: str
    depends_on: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    done: bool = False
    result: Any = None


class TaskGraph:
    """Dependency graph of reasoning tasks."""

    def __init__(self):
        self.nodes: Dict[str, TaskNode] = {}

    def add_task(self, task_id: str, depends_on: List[str] = None, metadata: Dict[str, Any] = None):
        self.nodes[task_id] = TaskNode(
            id=task_id,
            depends_on=depends_on or [],
            metadata=metadata or {}
        )

    def mark_done(self, task_id: str, result: Any):
        if task_id in self.nodes:
            self.nodes[task_id].done = True
            self.nodes[task_id].result = result

    def get_ready_tasks(self) -> List[TaskNode]:
        """Return tasks that can be executed (no unmet dependencies)."""
        ready = []
        for node in self.nodes.values():
            if not node.done and all(self.nodes[dep].done for dep in node.depends_on):
                ready.append(node)
        return ready

    def visualize(self):
        print("🧠 Task Graph:")
        for task in self.nodes.values():
            deps = ", ".join(task.depends_on) or "None"
            print(f" • {task.id} ← [{deps}]  | Done: {task.done}")
