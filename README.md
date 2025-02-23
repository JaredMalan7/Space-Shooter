# Space-Shooter Game

# 🚀 Space Shooter Game

## Overview
Space Shooter is an action-packed, arcade-style game developed in **Python** using **Pygame**. Players control a spaceship, navigate through space, and battle against waves of enemy ships and powerful bosses. As the game progresses, the difficulty increases across **three levels**, introducing faster enemies, more challenging bosses, and a dynamic combat system.

The game follows a structured level progression:
1. Level 1: Basic enemies (`ship-1.png`, `ship-2.png`), Boss-1 (`boss-1.png`).
2. Level 2: Faster and stronger enemies (`ship-3.png`, `ship-4.png`), Boss-2 (`boss-2.png`).
3. Level 3: The final challenge, enemies (`ship-5.png`, `ship-6.png`), Boss-3 (`boss-3.png`).

Each boss introduces a more aggressive attack pattern, and enemy ships become increasingly difficult to evade.

---
### [YouTube Video Demo](https://youtu.be/hwoUOThudGM)

---

## 🛠 Installation and Setup
### **Requirements**
- Python **3.x**
- `pygame` library

### Installation Steps
1. Clone the Repository
   ```bash
   git clone https://github.com/JaredMalan7/Space-Shooter.git
   cd space-shooter

2. Install Dependencies
    ```bash
    pip install pygame
   
3. Run the Game
    ```bash
   python main.py
   
## 🎮 Gameplay Mechanics
### Objectives

* Survive waves of enemies
* Defeat 18 enemy ships to trigger the boss battle.
* Advance through three levels, with increasing difficulty.
* Defeat Boss-3 to win the game.

### 🎮 Player Controls
| Action           | Keybinding  |
|-----------------|------------|
| Move Left       | ← (Left Arrow) |
| Move Right      | → (Right Arrow) |
| Move Up         | ↑ (Up Arrow) |
| Move Down       | ↓ (Down Arrow) |
| Shoot           | Spacebar |

---

### 🕹 Game Features
- ✅ **Enemy Waves** – Enemies spawn in structured waves per level.
- ✅ **Boss Battles** – After 18 enemies are defeated, a boss appears.
- ✅ **Increasing Difficulty** – Each level introduces faster enemies and more bullets per attack.
- ✅ **Health System** – The player has a three-stage health bar.
- ✅ **Collision & Damage** – Enemies, asteroids, and bullets can damage the player.

---

### 🏆 Level Progression

Each level follows the **same core mechanics** but increases in difficulty.

| Level | Enemies | Boss | Enemy Bullets | Boss Bullets | Speed Increase |
|--------|------------|-----------|---------------|--------------|--------------|
| **1**  | `ship-1.png`, `ship-2.png` | `boss-1.png` | 1 per shot | 2 per shot | Normal |
| **2**  | `ship-3.png`, `ship-4.png` | `boss-2.png` | 2 per shot | 3 per shot | Faster |
| **3**  | `ship-5.png`, `ship-6.png` | `boss-3.png` | 3 per shot | 4 per shot | Fastest |

After **defeating Boss-3**, the game **ends in victory**.

---

### 🛠 Code Structure

```bash
/space-shooter
│── assets/               # Game assets (sprites, images, sounds)
│── player.py             # Player spaceship class
│── enemy.py              # Enemy AI and behavior
│── boss.py               # Boss AI and attack patterns
│── asteroid.py           # Asteroid mechanics
│── bullet.py             # Player & enemy bullets
│── main.py               # Main game loop and logic
│── README.md             # Project documentation
```

### 📚 Useful Resources

* [Python Documentation](https://docs.python.org/3/tutorial/index.html)
* [Pygame Documentation](https://www.pygame.org/docs/)
* [Game Loop Explained](https://gameprogrammingpatterns.com/game-loop.html)
* [Collision Detection Basics](https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection)
* [Python Game Development](https://realpython.com/pygame-a-primer/)