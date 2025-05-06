from tkinter import * #creates a window for you, links the keyboard to ur window
import random

#these are constants for our game
GAME_WIDTH=700
GAME_HEIGHT=700
SPEED=100 # THE LESSER THE VALUE THE BETTER
SPACE_SIZE=50 #body parts the snake at begin
BODY_PARTS=3
SNAKE_COLOR="green"
FOOD_COLOR="red"
BACKGROUND_COLOR="black"

class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]
        
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0]) #coordinates of fd and snake both default 0

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
        
class Food:
    
    def __init__(self):
        x=random.randint(0,(GAME_WIDTH//SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,(GAME_HEIGHT//SPACE_SIZE)-1)*SPACE_SIZE
        
        self.coordinates=[x,y]
        
        #to draw the food on canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

class next_turn():
    pass

def next_turn(snake, food): # to make the snake move
    x, y=snake.coordinates[0]  #snakes head
    
    if direction=="up":
        y-=SPACE_SIZE #to make the snake move 1 space up
                        #y bcoz vertical jaa rhe
    elif direction=="down":
        y+=SPACE_SIZE
        
    elif direction=="left":
        x-=SPACE_SIZE   #x bcoz horizontal jaa rhe
        
    elif direction=="right":
        x+=SPACE_SIZE
    
    snake.coordinates.insert(0,(x,y))
    
    square=canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    #updates sq of snake
    snake.squares.insert(0,square)
    
    #snake feeding on the food
    if x== food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food=Food()  #create new food
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]  
    #deletes the peeche ke parts
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)
    
    
def change_direction(new_direction):
    global direction
    
    if new_direction=='left':
        if direction!='right': #prevents the snake to not make 180 turn and colliding in itself
            direction=new_direction
    
    elif new_direction=="right":
        if direction!="left": #prevents the snake to not make 180 turn and colliding in itself
            direction=new_direction
    
    elif new_direction=="up":
        if direction!="down": #prevents the snake to not make 180 turn and colliding in itself
            direction=new_direction
    
    elif new_direction=="down":
        if direction!="up": #prevents the snake to not make 180 turn and colliding in itself
            direction=new_direction

def check_collisions(snake):
    
    #if collides with windows borders
    x, y =snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        print("GAME OVER - touched side")
        return True
    elif y<0 or y>=GAME_HEIGHT:
        print("GAME OVER-touched side")
        return True
    
    #if collides with with its own body
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            print("Game Over- touched body")
            return True
    return False #there are no collisions

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70),text="GAME OVER", fill="red", tag="gameover")

def start_countdown(count):
    if count > 0:
        canvas.delete("countdown")
        canvas.create_text(GAME_WIDTH//2, GAME_HEIGHT//2, 
                           text=str(count), font=('consolas', 60), 
                           fill='white', tag="countdown")
        window.after(1000, start_countdown, count-1)
    elif count == 0:
        canvas.delete("countdown")
        canvas.create_text(GAME_WIDTH//2, GAME_HEIGHT//2, 
                           text="Go!", font=('consolas', 60), 
                           fill='green', tag="countdown")
        window.after(1000, lambda: [canvas.delete("countdown"), next_turn(snake, food)])

#THE window
window=Tk()
window.title("Snake Game")
#window.resizable(False,False)

score=0
direction ='down'
label=Label(window,text="Score;{}".format(score), font=('consolas',40))#the Label widget is used to display text or images in a window
label.pack() #pack() to organize widgets in a Tkinter

#The Canvas widget in Tkinter provides a powerful way to create and manage graphics
canvas=Canvas(window,bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack() #pack() to organize widgets in a Tkinter

#to set its size dynamically based on available screen real estate
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

#to adjust window to centre
x=int((screen_width//2)-(window_width//2))
y=int((screen_height//2)-(window_height//2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#binding keyboard keys to snakes movements 
window.bind('<Left>', lambda event:change_direction('left'))
window.bind('<Right>', lambda event:change_direction('right'))
window.bind('<Up>', lambda event:change_direction('up'))
window.bind('<Down>', lambda event:change_direction('down'))

#creating objects
snake= Snake()
food= Food()

#next_turn(snake, food)
start_countdown(3)

window.mainloop()