#-------------- SELECT PROBLEM--------------------#
# import plan_problem_drone_1 as solver_output # problem_1
import plan_problem_drone_2 as solver_output # problem_2
#-------------------------------------------------------#
import pygame
import time
from queue import PriorityQueue
import random

WIDTH = 800
WIN  = pygame.display.set_mode((WIDTH,WIDTH))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE= (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
DARK_GREY = (150,150,150)
ORANGE_2 = (255, 165, 50)


class Spot:
    def __init__(self,row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = [] 
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK
    
    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def make_waypoint(self):
        self.color = ORANGE_2 
    
    def make_battery(self):
        self.color = (30, 255, 30)
    
    def make_drone_path(self):
        self.color = DARK_GREY
    
    def make_drone(self):
        self.color = BLUE
    
    def make_in_process(self):
        self.color = (255, 255, 20)

    def make_recharge(self):
        self.color = (10, 255, 10)
    
    def make_get_data(self):
        self.color = (127,26,204)
    
    def make_communicate(self):
        self.color = (128,17, 128)

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x, self.y, self.width, self.width))
    
    def update_neigbours(self,grid):
        self.neighbors = []

        if self.row < self.total_rows -1 and not grid[self.row+1][self.col].is_barrier(): #down
            self.neighbors.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row-1][self.col].is_barrier(): #up
            self.neighbors.append(grid[self.row-1][self.col])

        if self.col < self.total_rows -1 and not grid[self.row][self.col+1].is_barrier(): #right
            self.neighbors.append(grid[self.row][self.col+1])

        if self.col > 0  and not grid[self.row][self.col-1].is_barrier(): # right
            self.neighbors.append(grid[self.row][self.col-1])


def h(p1,p2):
    x1, y1 = p1
    x2 , y2 = p2
    return abs(x1-x2)+abs(y1-y2)


def reconstruct_path(came_from, current,draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def algorithm(draw, grid, start,end):
    count =0
    open_set = PriorityQueue()
    open_set.put((0, count,start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start]= 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end,draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 

            if temp_g_score < g_score[neighbor]:
               came_from[neighbor]  = current
               g_score[neighbor] = temp_g_score
               f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
               if neighbor not in open_set_hash:
                   count +=1
                   open_set.put((f_score[neighbor],count,neighbor))
                   open_set_hash.add(neighbor)
                   neighbor.make_open()
        draw()

        if current != start:
            current.make_closed()
    
    return False



def make_grid(rows,width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot =Spot(i, j, gap,rows)
            grid[i].append(spot)
    
    return grid


def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
      pygame.draw.line(win,GREY,(0,i*gap),(width, i*gap) )  

      for j in range(rows):
        pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width) )  

def draw(win,grid,rows, width,start,goal):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    text(win,start,goal)
    pygame.display.update() 

def draw2(win,grid,rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)


def get_clicked_pos(pos,rows,width):
    gap = width // rows
    y,x = pos

    row = y//gap
    col = x// gap
    return row, col


def draw_barrier(grid):
    #brrier1 loc2
    for col in range(8):
        grid[col+5][15].make_barrier()
    for row in range(10):
        grid[22][18-row].make_barrier()
    #barrirer 2 loc 7
    for col in range(8):
        grid[col+7][30].make_barrier()
    for row in range(3):
        grid[15][30+row].make_barrier()
    # barrier 3 loc 13
    for row in range(7):
        grid[33][43-row].make_barrier()
    for col in range(5):
        grid[33-col][43].make_barrier()
        grid[33-col][38].make_barrier()
        grid[33+col][41].make_barrier()
    for col in range(5):
        grid[31-col][39+col].make_barrier() 
    #barrirer loc 3
    for row in range(6):
        grid[7][28-row].make_barrier()
    for col in range(14):
        grid[col][24].make_barrier()
    #barrier 4 loc 5
    for col in range(10):
        grid[24-col][25].make_barrier()
    for col in range(9):
        grid[29-col][25+col].make_barrier()
    # barrier loc 8

def text(win,start,end):
        green = (0, 255, 0)
        blue = (0, 0, 128)
        red = (255, 0, 0)
        pygame.init()
        pygame.display.set_caption('fire fighting drone- cognitive robots project')
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("START", True, green, blue)
        textRect = text.get_rect()
        textRect.center = (start[0]*16, start[1]*16-8)
        win.blit(text, textRect)
        text = font.render("GOAL", True, green, blue)
        textRect = text.get_rect()
        textRect.center = (end[0]*16, end[1]*16-8)
        win.blit(text, textRect)


class DECODE():
    def __init__(self, stage, win, grid, ROWS, width, drones, waypoints, current_drones,battery):
        
        self.stage = stage
        self.action_name = stage[0]
        self.win = win
        self.grid = grid
        self.ROWS= ROWS
        self.width = width
        self.drones= drones
        self.waypoints = waypoints
        self.current_drones= current_drones
        self.battery = battery
        self.current_drone = current_drones[stage[1]]
        self.drone_col = self.current_drone[0]
        self.drone_row = self.current_drone[1]
        self.text = str(self.stage)

        draw2(self.win, self.grid, self.ROWS, self.width)
        self.show_text()

    def action(self):
        if self.action_name == "take_off":
            self.grid[self.drone_col][self.drone_row].make_in_process()
            t = 2

        elif self.action_name == "navigate":

            target = self.waypoints[self.stage[3]]
            while self.current_drone != target:

                if self.current_drone not in self.waypoints.values():
                    self.grid[self.drone_col][self.drone_row].make_drone_path()
                else :
                    self.grid[self.drone_col][self.drone_row].make_waypoint()

                targer_col, target_row = target[0], target[1]
                if targer_col >  self.drone_col:
                    self.drone_col += 1
                elif targer_col <  self.drone_col:
                    self.drone_col -= 1
                if target_row > self.drone_row:
                    self.drone_row += 1
                elif target_row < self.drone_row:
                    self.drone_row -= 1

                self.grid[self.drone_col][self.drone_row].make_drone()
                self.current_drone = [self.drone_col, self.drone_row]
                self.current_drones[self.stage[1]] = self.current_drone

                
                draw2(self.win, self.grid, self.ROWS, self.width)
                self.show_text()
                t= 0.1
                time.sleep(0.1)
                

        elif self.action_name == "land":
            self.grid[self.drone_col][self.drone_row].make_in_process()
            t = 2
        
        elif self.action_name == "recharge":
            self.grid[self.drone_col][self.drone_row].make_recharge()
            t = 3    

        elif self.action_name == "raise_antenna":
            self.grid[self.drone_col][self.drone_row].make_in_process()
            t = 2

        elif self.action_name == "retract_antenna":
            self.grid[self.drone_col][self.drone_row].make_in_process()
            t = 2

        elif self.action_name == "get_gps_pos":
            self.grid[self.drone_col][self.drone_row].make_get_data()
            t = 2

        elif self.action_name == "communicate_gps_pos":
            self.grid[self.drone_col][self.drone_row].make_communicate()
            t = 2

        elif self.action_name == "focus_camera":
            self.grid[self.drone_col][self.drone_row].make_in_process()
            t = 2

        elif self.action_name == "take_image":
            self.grid[self.drone_col][self.drone_row].make_get_data()
            t = 2

        elif self.action_name == "communicate_image_data":
            self.grid[self.drone_col][self.drone_row].make_communicate()
            t = 2

        draw2(self.win, self.grid, self.ROWS, self.width)   
        self.show_text()
        time.sleep(t)
        return self.current_drones
       
    
    def show_text(self):
        draw_barrier(self.grid)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        red = (255, 0, 0)
        pygame.init()
        pygame.display.set_caption('fire fighting drone- cognitive robots project')
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.text, True, green, blue)
        textRect = text.get_rect()
        textRect.center = (400, 50)
        self.win.blit(text, textRect)

        #draw drones text
        for drone in self.current_drones:
            font = pygame.font.Font('freesansbold.ttf', 14)
            text_waypoint = font.render(drone, True, green, red)
            textRect = text_waypoint.get_rect()
            textRect.center = (self.current_drones[drone][0]*16, self.current_drones[drone][1]*16-5)
            self.win.blit(text_waypoint, textRect)


        # draw waypoints
        waypoints = solver_output.waypoints 
        for waypoint in waypoints:
            font = pygame.font.Font('freesansbold.ttf', 14)
            text_waypoint = font.render(waypoint, True, green, blue)
            textRect = text_waypoint.get_rect()
            textRect.center = (waypoints[waypoint][0]*16, waypoints[waypoint][1]*16+26)
            self.win.blit(text_waypoint, textRect)
        
        #draw battery
        m=1
        for battery in self.battery:
            k=5*(m)+m*2
            delta_k = 5
            j= 35
            delta_j = 12
            for i in range(delta_j):
                self.grid[i+j][k].make_barrier()
                self.grid[i+j][k+delta_k].make_barrier()
            for i in range(delta_k):
                self.grid[j][k+i].make_barrier()
                self.grid[j+delta_j-1][k+i].make_barrier()
            self.grid[j+delta_j][k+2].make_barrier()
            self.grid[j+delta_j][k+3].make_barrier()
            self.grid[j+delta_j+1][k+2].make_barrier()
            self.grid[j+delta_j+1][k+3].make_barrier()

            i = self.battery[battery] // 10
            for row in range(delta_k-1):
                for col in range(i):
                    self.grid[j+1+col][k+1+row].make_battery()
                for col in range(delta_j-2-i):
                    self.grid[j+i+col+1][k+1+row].reset()

            # battery text
            font = pygame.font.Font('freesansbold.ttf', 16)
            text_battery = font.render(battery, True, green, blue)
            textRect = text_battery.get_rect()
            textRect.center = (j*16,k*16+5 )
            self.win.blit(text_battery, textRect)        
            m +=1

        pygame.display.update()
    

def main(win,width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    drones =  solver_output.drones
    waypoints =  solver_output.waypoints
    current_drones = solver_output.drones.copy()
    initial_battery = solver_output.initial_battery
    costs = solver_output.costs
    target = solver_output.target



    for waypoint in solver_output.waypoints.values():  # draw drones location
        grid[waypoint[0]][waypoint[1]].make_waypoint()
    
    for drone in solver_output.drones.values():
        grid[drone[0]][drone[1]].make_drone()
       
    battery = initial_battery.copy()
    total_cost = 0

    plan =  solver_output.plan
    for stage in plan.values():
        stage = stage.split()
        print(stage)
        if stage[0] == "navigate":
            for cost_loc in costs:
                cost = cost_loc.split()
                if cost == [stage[2], stage[3]]:
                    battery[stage[1]] = battery[stage[1]] - costs[cost_loc]
                    total_cost = total_cost + costs[cost_loc]
        if stage[0] == "recharge":
            battery[stage[1]] = 100
        
        decode1 = DECODE(stage,win, grid, ROWS, width,drones, waypoints, current_drones,battery)
        current_drones = decode1.action()
    print("TOTAL BATTERY COST:", total_cost)


    for drone in drones.keys():  
        # fire = random.choice([True, False])
        fire = True
        if not fire: print("------------- ALL NORAMAL ------------------", drone)
        if fire:
            print("----------------!!!  FIRE  !!! ------------------", drone)
            print("---------- SEND FIRE FIGHTING DRONE -------------", drone)
            grid = make_grid(ROWS,width) 
            start = grid[drones[drone][0]][drones[drone][1]]
            start.make_start()
            end = grid[target[drone][0]][target[drone][1]]
            end.make_end()
            initial = [drones[drone][0],drones[drone][1]]
            goal = [target[drone][0],target[drone][1]]
            draw(win, grid, ROWS, width,initial, goal)
            draw_barrier(grid)
            
            run = True
            show = True
            while show:
                draw(win, grid, ROWS, width,initial, goal) # DRAW GRID
                if run:
                    for row in grid:
                        for spot in row:
                            spot.update_neigbours(grid)
                    
                    algorithm(lambda: draw(win, grid, ROWS, width,initial, goal), grid, start,end)
                    run = False
                    time.sleep(1)
                    show = False  
  

main(WIN, WIDTH)







        


