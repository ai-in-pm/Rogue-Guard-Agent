from pydantic_settings import BaseSettings
from typing import Optional, Dict, Any
import os
from pathlib import Path

class Settings(BaseSettings):
    """RogueGuard Configuration Settings"""
    
    # API Configuration
    OPENAI_API_KEY: Optional[str] = None
    MODEL_ID: str = "gpt-4"
    
    # Analysis Settings
    RISK_THRESHOLD_CRITICAL: float = 0.8
    RISK_THRESHOLD_HIGH: float = 0.6
    RISK_THRESHOLD_MODERATE: float = 0.4
    
    # Storage Settings
    DATA_DIR: Path = Path.home() / ".rogueguard"
    LOG_DIR: Path = DATA_DIR / "logs"
    ANALYSIS_DIR: Path = DATA_DIR / "analysis"
    
    # Monitoring Settings
    ENABLE_LOGGING: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Analysis Parameters
    BEHAVIORAL_WEIGHTS: Dict[str, float] = {
        "deception": 0.25,
        "goal_misalignment": 0.25,
        "autonomy": 0.20,
        "value_drift": 0.15,
        "resource_usage": 0.15
    }
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create necessary directories
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.LOG_DIR.mkdir(parents=True, exist_ok=True)
        self.ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

# Create global settings instance
settings = Settings()
