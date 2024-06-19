import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

turtle.shape(image)
state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()
new_list = []

# x_coord = state_data["x"].to_list()
# y_coord = state_data["y"].to_list()
# coord = []
# for a, b in zip(x_coord, y_coord):
#     coord.append((a, b))

is_True = True
number_state = 0
while is_True:
    answer_state = screen.textinput(title=f"{number_state}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        is_True = False
    if answer_state in state_list and answer_state not in new_list:
        coord = state_data[state_data["state"] == answer_state]
        x_cor = int(coord.x)
        y_cor = int(coord.y)
        tim.goto(x_cor, y_cor)
        tim.write(answer_state, align="center")
        number_state += 1
        new_list.append(answer_state)
    if number_state == 50:
        is_True = False
    print(new_list)

Failed_list = [x for x in state_list if x not in new_list]


# States to learn csv
To_df = pandas.DataFrame(Failed_list)
To_df.to_csv("States to learn.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

# screen.exitonclick()
