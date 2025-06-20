import os
import pygame
import json
from datetime import datetime

def asset(asset):
    if asset == "title":
        return "assets/images/main/title.png"
    elif asset == "default_font":
        return 'assets/font/Pixeltype.ttf'
    
def asset_frames(prefix, count, ext="png", folder="menu_bg"):
    frames = []
    for i in range(1, count + 1):
        path = os.path.join("assets", "images", "main",folder, f"{prefix}_{i}.{ext}")
        surf = pygame.image.load(path).convert_alpha()
        frames.append(surf)
    return frames

def log_system_state_transitions(from_state,to_state,state_type):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "type": state_type,
        "from": str(from_state),
        "to": str(to_state)
    }
    with open("logs/Main_State_Logs/app_state_transitions.log", "a") as f:
        f.write(json.dumps(log_data) + "\n")

def log_entity_state_transitions(from_state,to_state,state_type):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "type": state_type,
        "from": str(from_state),
        "to": str(to_state)
    }
    with open("logs/Entities_State_Logs/entity_state_transitions.log", "a") as f:
        f.write(json.dumps(log_data) + "\n")

def log_app_mode_transitions(from_mode,to_mode):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "type": "APPMODE",
        "from": str(from_mode),
        "to": str(to_mode)
    }
    with open("logs/Mode_Logs/mode_transitions.log", "a") as f:
        f.write(json.dumps(log_data) + "\n")