import turtle
import pandas

# Set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load and display the map image
image = "day_25img.gif"  # Ensure this file is in the same directory
screen.addshape(image)
turtle.shape(image)

# Load state data
data = pandas.read_csv("50_states.csv")  # Ensure this file is in the same directory
all_states = data.state.to_list()
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Exit the game if user types "Exit"
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the answer is correct and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        # Locate the coordinates of the guessed state
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

turtle.mainloop()











