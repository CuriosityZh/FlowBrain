from fastapi import APIRouter
from core.flow_manager import FlowManager

router = APIRouter()
manager = FlowManager()


@router.post("/run")
async def run_flow(input_data: dict):
    """Trigger reasoning flow execution."""
    results = await manager.run(input_data)
    return {"status": "completed", "results": results}


@router.get("/graph")
async def get_graph():
    """Return task graph for visualization."""
    return {
        "tasks": [
            {"id": t.id, "depends_on": t.depends_on, "done": t.done}
            for t in manager.task_graph.nodes.values()
        ]
    }


@router.post("/add_task")
async def add_task(task: dict):
    """Add a new task to the reasoning graph."""
    task_id = task.get("id")
    depends_on = task.get("depends_on", [])
    meta = task.get("metadata", {})
    manager.task_graph.add_task(task_id, depends_on, meta)
    return {"added": task_id, "depends_on": depends_on}
