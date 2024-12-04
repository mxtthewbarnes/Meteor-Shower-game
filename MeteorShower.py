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
    pyg.init()               

    width = 800               
    height = 600              

    red = (255,0,0)           
    yellow = (244,208,63)     
    background = (0,0,156)    

    player_dim = 50           
    player_pos = [width/2, height-2*player_dim]  
                                                 

    met_dim = 20             
    met_list = []             
                              

    screen = pyg.display.set_mode((width, height)) 

    game_over = False         
                              
                             

    score = 0                 

    clock = pyg.time.Clock()  

    my_font = pyg.font.SysFont("monospace", 35) 

    while not game_over:                       
        for event in pyg.event.get():          
            if event.type == pyg.KEYDOWN:     
                x = player_pos[0]             
                y = player_pos[1]              
                if event.key == pyg.K_LEFT:    
                    x -= player_dim            
                elif event.key == pyg.K_RIGHT: 
                    x += player_dim            
                player_pos = [x, y]            
            
        screen.fill(background)                
        drop_meteors(met_list, met_dim, width)
        speed = set_speed(score)               
        score = update_meteor_position(met_list, height, score, speed)
                                               
        text = "Score: " + str(score)              
        label = my_font.render(text, 1, yellow)    
        screen.blit(label, (width-250, height-40)) 
                                                  
                                                   
                                                   
        draw_meteors(met_list, met_dim, screen, yellow) 
                                                        

        pyg.draw.rect(screen, red, (player_pos[0], player_pos[1], player_dim, player_dim))                                       
#draw player
        if collision_check(met_list, player_pos, player_dim, met_dim):
            game_over = True                       
    
        clock.tick(30)                             
                                                   
                                                   

        pyg.display.update()                      
    # Outside while-loop now.
    print('Final score:', score)                   
    pyg.quit()                                    

        
main()

