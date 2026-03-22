def estimate_cost(task_type: str, model_id: str = "default"):
    """
    Simulates the cost of an API call.
    In a real app, you would count tokens. Here, we use flat rates.
    """
    prices = {
        "embedding": 0.0001,  # Cost per HF embedding call
        "llm_small": 0.0005,   # Cost per small LLM inference (e.g., Groq)
        "llm_large": 0.01,     # Cost per large LLM inference
    }
    
    if "sentence-transformers" in model_id or "embedding" in task_type:
        return prices["embedding"]
    return prices["llm_small"]