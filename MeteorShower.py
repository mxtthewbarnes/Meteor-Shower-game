import random 
import pygame as pyg

#Creates function set_speed
def set_speed(score):      
    if score <= 25: #Determines initial speed of meteors.
        speed = 10/5
    elif score <= 50: #For every 25 score, increase the speed by 1 (5/5)
        speed = 15/5
    elif score <= 75:
        speed = 20/5
    else:
        speed = 25/5 #Maximum speed of meteors, which is in effect for 76+ score onwards
    return speed

#Draws meteors from list
def draw_meteors(met_list, met_dim, screen, red): 
    for i in range(len(met_list)):
        x = met_list[i][0]
        y = met_list[i][1]
        pyg.draw.rect(screen, red, (x, y, met_dim, met_dim))


#Function drops meteors
def drop_meteors(met_list, met_dim, width):
    chance = random.randrange(0, width, met_dim)
    if chance < 75:
        y = 0
        x = random.randrange(0, width - met_dim)
        coords = [x,y]
        met_list.append(coords)
    else:
        pass #Makes it so meteor is not generated when if statement is not satisified to ensure randomized spawning

#Function Updates the location of the meteors
def update_meteor_position(met_list, height, score, speed):
    for i in met_list:
        i[1] += speed
        if i[1] == height: #When meteor passes the player without colliding with them, add to score
            score += 1
            del i
    return score 

#Function detects if meteor has hit player
def detect_collision(met_pos, plyr_pos, plyr_siz, met_siz):
    if int(plyr_pos[0]) <= int(met_pos[0]) + met_siz <= int(plyr_pos[0]) + plyr_siz:
        if int(plyr_pos[1]) <= int(met_pos[1]) + met_siz <= int(plyr_pos[1]) + plyr_siz:
            return True
    else:
        return False
        
#Function calls detect_collision to see if the game stops or not
def collision_check (met_pos, plyr_pos, plyr_siz, met_siz):
    coll = False
    for i in met_pos:
        if i[1] >= plyr_pos[1]:
            coll = detect_collision(i, plyr_pos, plyr_siz, met_siz)
        else:
            return coll



    
def main():
    '''
    Initialize pygame and pygame parameters.  Note that both player and meteors
    are square.  Thus, player_dim and met_dim are the height and width of the
    player and meteors, respectively.  Each line of code is commented.
    '''
    pyg.init()                # initialize pygame

    width = 800               # set width of game screen in pixels
    height = 600              # set height of game screen in pixels

    red = (255,0,0)           # rgb color of player
    yellow = (244,208,63)     # rgb color of meteors
    background = (0,0,156)    # rgb color of sky (midnight blue)

    player_dim = 50           # player size in pixels
    player_pos = [width/2, height-2*player_dim]  # initial location of player
                                                 # at bottom middle; height
                                                 # never changes

    met_dim = 20              # meteor size in pixels
    met_list = []             # initialize list of two-element lists
                              # giving x and y meteor positions

    screen = pyg.display.set_mode((width, height)) # initialize game screen

    game_over = False         # initialize game_over; game played until
                              # game_over is True, i.e., when collision
                              # is detected

    score = 0                 # initialize score

    clock = pyg.time.Clock()  # initialize clock to track time

    my_font = pyg.font.SysFont("monospace", 35) # initialize system font

    while not game_over:                       # play until game_over == True
        for event in pyg.event.get():          # loop through events in queue
            if event.type == pyg.KEYDOWN:      # checks for key press
                x = player_pos[0]              # assign current x position
                y = player_pos[1]              # assign current y position
                if event.key == pyg.K_LEFT:    # checks if left arrow;
                    x -= player_dim            # if true, moves player left
                elif event.key == pyg.K_RIGHT: # checks if right arrow;
                    x += player_dim            # else moves player right
                player_pos = [x, y]            # reset player position
            
        screen.fill(background)                # refresh screen bg color
        drop_meteors(met_list, met_dim, width) # read PA prompt
        speed = set_speed(score)               # read PA prompt
        score = update_meteor_position(met_list, height, score, speed)
                                               # read PA prompt
        text = "Score: " + str(score)              # create score text
        label = my_font.render(text, 1, yellow)    # render text into label
        screen.blit(label, (width-250, height-40)) # blit label to screen at
                                                   # given position; for our 
                                                   # purposes, just thi
                                                   # blit to mean draw
        draw_meteors(met_list, met_dim, screen, yellow) # self-explanatory;
                                                        # read PA prompt

        pyg.draw.rect(screen, red, (player_pos[0], player_pos[1], player_dim, player_dim))                                        # draw player
#draw player
        if collision_check(met_list, player_pos, player_dim, met_dim):
            game_over = True                       # read PA prompt
    
        clock.tick(30)                             # set frame rate to control
                                                   # frames per second (~30); 
                                                   # slows down game

        pyg.display.update()                       # update screen characters
    # Outside while-loop now.
    print('Final score:', score)                   # final score
    pyg.quit()                                     # leave pygame

        
main()
