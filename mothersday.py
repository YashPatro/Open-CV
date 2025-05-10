# Mother's Day Quiz - Final Version with Background Image and Pastel Colours
import pgzrun

TITLE = 'Mother’s Day Quiz'
WIDTH = 800
HEIGHT = 600

q_file = 'mothersday_quiz.txt'
q_append = []

score = 0
current_que = 0
question_count = 0
t_time = 10
g_over = False
question = []

# UI Layout
scroller_box = Rect(0, 0, WIDTH, 50)
quiz_box = Rect(100, 60, 600, 80)

# Answer circles
ans1 = ((200, 200), 60)
ans2 = ((600, 200), 60)
ans3 = ((200, 380), 60)
ans4 = ((600, 380), 60)
ans = [ans1, ans2, ans3, ans4]

# Timer in centre
timer_circle_pos = (400, 290)
timer_radius = 40

def read_q():
    global question_count
    with open(q_file, 'r') as f:
        for line in f:
            q_append.append(line)
            question_count += 1

def read_nq():
    global current_que
    current_que += 1
    return q_append.pop(0).split('|')

def draw():
    screen.clear()

    if g_over:
        screen.blit("mothers_day_bg", (0, 0))
        screen.draw.text(
            f"Your score: {score} / {question_count}",
            center=(WIDTH / 2, HEIGHT / 2),
            color="blue"
        )
        return

    screen.fill("#FFF5F7")  # Soft rose background
    screen.draw.filled_rect(scroller_box, "#FADADD")  # Pale pink
    screen.draw.text("💐 Happy Mother’s Day! 💐",
                     center=scroller_box.center,
                     color="dark red")

    screen.draw.filled_rect(quiz_box, "#D6AEDD")  # Lavender
    screen.draw.textbox(question[0].strip(), quiz_box,
                        color="white")

    index = 1
    for (centre, radius) in ans:
        screen.draw.filled_circle(centre, radius, "#A8E6CF")  # Mint green
        screen.draw.text(question[index].strip(),
                         center=centre,
                         color="black")
        index += 1

    screen.draw.filled_circle(timer_circle_pos, timer_radius, "#FFB3BA")  # Coral pink
    screen.draw.text(str(t_time),
                     center=timer_circle_pos,
                     color="white")

def update():
    scroller_box.x -= 2
    if scroller_box.right < 0:
        scroller_box.x = WIDTH

def on_mouse_down(pos):
    global score, question, g_over

    if g_over:
        return

    index = 1
    for (centre, radius) in ans:
        if distance(pos, centre) <= radius:
            if index == int(question[5]):
                score += 1
            if q_append:
                next_q()
            else:
                game_over()
            return
        index += 1

def next_q():
    global question, t_time
    question = read_nq()
    t_time = 10

def game_over():
    global g_over, t_time
    g_over = True
    t_time = 0

def timer():
    global t_time
    if not g_over and t_time > 0:
        t_time -= 1
    elif t_time == 0:
        game_over()

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

read_q()
question = read_nq()
clock.schedule_interval(timer, 1)

pgzrun.go()
