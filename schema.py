"""
Defines schema for JSON output
"""

from typing import List, Dict

class TruthWeaverResult:
    def __init__(self, shadow_id: str, revealed_truth: Dict, deception_patterns: List[Dict]):
        self.shadow_id = shadow_id
        self.revealed_truth = revealed_truth
        self.deception_patterns = deception_patterns

    def to_dict(self):
        return {
            "shadow_id": self.shadow_id,
            "revealed_truth": self.revealed_truth,
            "deception_patterns": self.deception_patterns
        }

