# 🐢 Turtle Race Game

A fun interactive betting game built with Python's Turtle graphics module where you place bets on which colored turtle will win a randomized race.

## 🎮 Overview

This project demonstrates the use of Python's Turtle graphics library to create an entertaining turtle racing simulation with betting mechanics. The program generates six different colored turtles that race across the screen with randomized movements, letting you test your luck by betting on the winner.

## ✨ Features

### 1. Betting System
- Select from six different colored turtles to bet on
- Input validation ensures you choose a valid color
- Real-time race visualization
- Win/loss feedback based on your bet

### 2. Turtle Racing
- Six uniquely colored racing turtles (red, green, purple, black, orange, blue)
- Random movement algorithm creates unpredictable races
- Clear visual indication of the winner
- Race concludes when the first turtle crosses the finish line

### 3. Interactive Graphics
- Clean visual interface with Turtle graphics
- Evenly spaced racers for clear visibility
- Dynamic racing animation
- Proper race termination once a winner is determined

## 🛠️ Requirements

- Python 3.x
- turtle module (standard library)
- random module (standard library)
- time module (standard library)

## 📋 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/turtle-race-game.git
cd turtle-race-game
```

2. No additional packages needed as the game uses only standard Python libraries.

## 🚀 Usage

Run the program with:
```bash
python turtle_race.py
```

The program will:
1. Open a graphics window and prompt you to choose a turtle color
2. Position all turtles at the starting line
3. Begin the race with randomized turtle movements
4. Declare a winner when a turtle reaches the finish line
5. Display whether you won or lost based on your bet

## 🧩 Code Structure

The code is organized into distinct sections:
- **Setup**: Initializes the screen and user input system
- **Input Validation**: Ensures the user selects a valid turtle color
- **Turtle Creation**: Generates and positions the racing turtles
- **Race Logic**: Implements the randomized racing algorithm
- **Winner Determination**: Identifies the first turtle to cross the finish line

## 💡 How It Works

### Turtle Creation
```python
all_turtles = []
turtle_position = -100
for color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, turtle_position)
    turtle_position+=40
    all_turtles.append(new_turtle)
```

### Racing Algorithm
Each turtle moves forward a random distance (0-10 pixels) in each iteration:
```python
while is_game_on:
    for turtle in all_turtles:
        if not is_game_on:  # skip remaining turtles if we already have a winner
            break
        turtle.speed(6)
        move_forward = random.randint(0, 10)
        turtle.forward(move_forward)

        if turtle.xcor() >= 230 and winner is None:
            winner = turtle.pencolor()
            is_game_on = False
```

## 🔍 Customization

You can customize the game by modifying:
- Screen dimensions in the setup section
- The list of turtle colors
- Starting and finishing positions
- Random movement range
- Turtle speed and spacing

## 📝 Future Enhancements

- Add multiple player betting system
- Add visual enhancements (finish line, decorative track)
- Implement race statistics
- Add sound effects for more engaging gameplay

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
