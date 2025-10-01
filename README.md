# 🐍 Snake Game (with High Score & Special Food)

This is a **classic Snake Game** built using **Python** and **Pygame**.  
The game includes **high score tracking**, **special food mechanics**, and simple controls.  



## 🎮 Features
🐍 Classic snake gameplay
💾 High score saved in `high_score.txt`
🍏 Regular food increases snake length by **1**
🍒 Special food appears every **4 foods eaten**, increases length by **3**
🔄 Restart option after game over
🎨 Simple UI with score & high score display



## 🖥️ Requirements
Make sure you have the following installed:

- Python 3.x  
- Pygame  

Install pygame via pip:
```bash
pip install pygame





## ▶️ How to Play

1. Run the game:

   ```bash
   python snake_game.py
   ```

   *(replace `snake_game.py` with your filename if different)*

2. Use arrow keys to move:

   * ⬅️ Left arrow → Move left
   * ➡️ Right arrow → Move right
   * ⬆️ Up arrow → Move up
   * ⬇️ Down arrow → Move down

3. Eat food to grow your snake.

4. Every 4 foods, a **special red food** appears that gives **extra length**.

5. Don’t crash into walls or yourself!



## 🏆 Scoring

* Normal Food → +1 length
* Special Food (red) → +3 length
* Your highest score is stored in `high_score.txt`

---

## 📂 Project Structure

```
SnakeGame/
│── snake_game.py      # Main game code
│── high_score.txt     # Stores highest score (auto-created)
│── README.md          # Documentation
```



## 🔧 Customization

You can tweak the following in the code:

* `snake_speed` → Adjust difficulty (default `10`)
* `special_food_value` → Change special food growth (default `3`)
* Colors → Modify snake/food colors in the code



## 📸 Screenshot

*(Add a screenshot of your game here for better presentation)*



## 📜 License

This project is for **educational and personal use**.
Feel free to modify and share! 🚀



