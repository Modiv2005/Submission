import pytest
from core.spend_tracker import SpendTracker
from core.memory import Memory

def test_spend_tracker():
    tracker = SpendTracker(budget_limit=100.0, log_file="outputs/test_spend.json")
    tracker.current_spend = 0.0 # reset for test
    tracker.log_expense("Test API", 10.0, "Test")
    assert tracker.current_spend == 10.0
    
    with pytest.raises(Exception):
        tracker.log_expense("Expensive API", 100.0, "Should Fail")

def test_memory():
    mem = Memory(memory_file="outputs/test_memory.json")
    mem.set("test_key", "test_value")
    assert mem.get("test_key") == "test_value"
    
    mem.add_asset("posts", {"id": 1})
    assert len(mem.get("generated_assets")["posts"]) == 1

def test_mock_llm(monkeypatch):
    # Test that BaseAgent falls back to mock if no client
    from agents.base_agent import BaseAgent
    agent = BaseAgent("TestAgent", "Testing")
    agent.client = None # Force mock
    
    response = agent.execute_with_retry("Hello")
    assert response == "Mock response"
