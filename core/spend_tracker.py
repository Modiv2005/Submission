import json
import os
from datetime import datetime
from core.logger import get_logger

logger = get_logger("SpendTracker")

class SpendTracker:
    def __init__(self, budget_limit: float = 100.0, log_file: str = "outputs/spend_log.json"):
        self.budget_limit = budget_limit
        self.log_file = log_file
        self.current_spend = 0.0
        self.expenses = []
        self._load_log()

    def _load_log(self):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r") as f:
                    data = json.load(f)
                    self.current_spend = data.get("total_spend", 0.0)
                    self.expenses = data.get("expenses", [])
            except json.JSONDecodeError:
                logger.warning("Could not parse spend log, starting fresh.")
        else:
            self._save_log()

    def _save_log(self):
        with open(self.log_file, "w") as f:
            json.dump({
                "total_spend": self.current_spend,
                "budget_limit": self.budget_limit,
                "expenses": self.expenses
            }, f, indent=4)

    def log_expense(self, service: str, cost: float, description: str):
        if self.current_spend + cost > self.budget_limit:
            logger.error(f"Budget exceeded! Attempted to spend ₹{cost} on {service}, but only ₹{self.budget_limit - self.current_spend} remaining.")
            raise Exception("Budget Cap Exceeded")
            
        self.current_spend += cost
        expense_entry = {
            "timestamp": datetime.now().isoformat(),
            "service": service,
            "cost_inr": cost,
            "description": description
        }
        self.expenses.append(expense_entry)
        self._save_log()
        logger.info(f"Logged expense: ₹{cost} for {service} ({description}). Total Spend: ₹{self.current_spend}")

spend_tracker = SpendTracker()
