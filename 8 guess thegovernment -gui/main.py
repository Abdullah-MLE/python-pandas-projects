from turtle import Turtle, Screen
import pandas

# initialize the score bord
def score_refresh():
    score_t.clear()
    score_t.goto(210, 115)
    score_t.write(arg=f"{score} / 27", align="left", font=("Minecraft", 15, "normal"))
    score_t.goto(210, 77)
    score_t.write(arg=f"10/{typos} : الأخطاء", align="left", font=("Minecraft", 15, "normal"))

# initialize the moving turtle
t = Turtle()
t.penup()
t.hideturtle()

# initialize the score turtle
score_t = Turtle()
score_t.penup()
score_t.hideturtle()

# initialize the screen object
s = Screen()
s.setup(width=675 , height=599)
s.bgpic("bg.png")
s.tracer(0)
s.title("تخمين محافظات مصر")
s.getcanvas().winfo_toplevel().iconbitmap('icon.ico')

# lode data
data = pandas.read_csv("egypt_gov.csv")

# initialize game variables
game_is_on = True
score = 0
typos = 0
score_refresh()
guessed_governments = []

# cheat code
# for gov in data.gov.values:
#     x_answer = int(data.x[data.gov == gov])
#     y_answer = int(data.y[data.gov == gov])
#     t.goto(x_answer, y_answer)
#     t.write(arg=gov, align="center")
#     guessed_governments.append(gov)
#     score += 1
#     score_refresh()

# start game loop
while game_is_on:
    # get the government that the user enter
    answer_government = s.textinput(title=f"guessed {score}/27 correct", prompt="دخل اسم محافظة :")
    if answer_government:
        answer_government = answer_government.strip()

    # if user value matches a government that in the csv file it will apper it's nane and add 1 to the score
    if answer_government in data.gov.values:
        if answer_government in guessed_governments:
            continue
        x_answer = int(data.x[data.gov == answer_government])
        y_answer = int(data.y[data.gov == answer_government])
        t.goto(x_answer, y_answer)
        t.write(arg=answer_government, align="center")
        guessed_governments.append(answer_government)
        score += 1
        score_refresh()

    # if the value is not correct add 1 to typos
    else:
        typos += 1
        score_refresh()

    # if the user click cansel or close the popup window or the typos is more than 10 or get all the correct answers it will do the following
    # 1- close the popup window
    # 2- if the typos > 10, or he hit cansel it will print GAME OVER! and attach a csv for the user includes the missing ones
    # 3- if he gets all the 27 it will print GG!
    if answer_government is None or score == 27 or typos == 10:
        game_is_on = False
        if typos == 10 or answer_government is None:
            remaining_governments = []
            governments = data.gov.values

            for government in governments:
                if government in guessed_governments:
                    continue
                else:
                    remaining_governments.append(government)
            remaining_governments_df = pandas.DataFrame(remaining_governments)
            remaining_governments_df.to_csv("the remaining governmentc.csv")

            t.goto(0, 0)
            t.color("red")
            t.write(arg="GAME OVER!", align="center", move=False, font=("Minecraft", 60, "normal"))

            t.goto(0, -50)
            t.color("black")
            t.write(arg="the remaining governments that you didn't known is in a CSV file.", align="center", move=False, font=("Minecraft", 15, "normal"))
        if score == 27:
            t.goto(0, 0)
            t.color("green")
            t.write(arg="GG!", align="center", move=False, font=("Minecraft", 60, "normal"))
    s.update()








s.mainloop()