import asyncio
from typing import Dict, Any


class AgentExecutor:
    """Executes a given task by simulating an agent reasoning process."""

    async def execute(self, task, strategy: str, context: Dict[str, Any]) -> Any:
        await asyncio.sleep(0.5)  # simulate async reasoning delay
        print(f"[AgentExecutor] Executing {task.id} via {strategy}")
        # simulate reasoning process
        output = {
            "task": task.id,
            "strategy": strategy,
            "context_summary": list(context.keys()),
            "result": f"Result of {task.id} with strategy {strategy}"
        }
        return output
