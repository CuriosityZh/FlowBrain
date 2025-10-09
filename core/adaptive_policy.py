from typing import Dict, Any


class AdaptivePolicy:
    """Chooses strategies dynamically based on task context and feedback."""

    def __init__(self):
        self.history: Dict[str, str] = {}

    def select_strategy(self, task) -> str:
        """Adaptive strategy selection logic."""
        task_meta = task.metadata.get("type", "generic")

        if task_meta == "planning":
            strategy = "reasoning_tree"
        elif task_meta == "analysis":
            strategy = "embedding_search"
        else:
            strategy = "default_agent"

        self.history[task.id] = strategy
        return strategy

    def feedback(self, task_id: str, success: bool):
        """Update internal state based on previous performance."""
        if success:
            print(f"[AdaptivePolicy] Strategy for {task_id} worked well.")
        else:
            print(f"[AdaptivePolicy] Adjusting policy for {task_id} after failure.")
