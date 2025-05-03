#03/05/25
import pgzrun,time

TITLE = 'Mothers Day!'

HEIGHT = 600
WIDTH = 700


q_file = 'questions.txt'
q_append = []

score = 0 
current_que = 0 
question_count = 0
scroll_msg = ''
t_time = 10
g_over = False

scroller_box = Rect(0,0,700,100)

quiz_box = Rect(25,145,550,100)


ans1 = ((200,100),75)
ans2 = ((500,100),75)
ans3 = ((200,450),75)
ans4 = ((500,450),75)

time_box = Rect(600,145,150,100)

ans = [ans1,ans2,ans3,ans4]
def draw():

    screen.clear()
    screen.fill('sky blue')

    screen.draw.filled_circle(ans1[0],ans1[1],'pink')
    '''screen.draw.filled_circle(ans2,'pink')
    screen.draw.filled_circle(ans3,'pastel pink')
    screen.draw.filled_circle(ans4,'pastel pink')
'''
    scroll_msg = f'Welcome to the quiz, you are on Q:{current_que} of {question_count}'
    screen.draw.textbox(scroll_msg, scroller_box, color='black')
    screen.draw.textbox(str(t_time), time_box, color = 'dark blue')

pgzrun.go()