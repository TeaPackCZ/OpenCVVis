import cv2
import numpy as np
from matplotlib import pyplot as plt

class OpenCVVis:
    def __init__(self, x=480, y=640):
        self.size_X = x
        self.size_Y = y
        self.map = np.zeros((x,y,3),np.uint8)
        self.rob_position = [x/2,y/2]
        self.rob_heading = 0.0
        self.rob_trajectory = [self.rob_position]
        self.boundaries = []
        self.obstacles = []
        self.active_obstacle = []
        
    def update_robot(self,new_pos, new_heading=0):
        cv2.circle(self.map,(self.rob_position[0],self.rob_position[1]),5,(63,63,63),-1)
        # Last argument: -1 = fill with color, 1 = only circle
        self.rob_position = new_pos
        self.rob_heading = new_heading
        self.rob_trajectory.append(self.rob_position)
        cv2.circle(self.map,(self.rob_position[0],self.rob_position[1]),5,(255,0,0),-1)
    
    def show_preview(self):
        plt.imshow(self.map, origin='lower')
        plt.show()
        
    def show_trajectory(self):
        pts = np.asarray(self.rob_trajectory, np.int32)
        cv2.polylines(self.map,[pts],False,(0,255,255))
        
    def show_heading(self, length=20):
        start = self.rob_position
        end = [start[0]+np.cos(self.rob_heading/180.0*np.pi)*length, start[1]+np.sin(self.rob_heading/180.0*np.pi)*length]
        pts = np.asarray([start,end],np.int32)
        cv2.polylines(self.map,[pts],False,(255,0,255))
        
    def set_boundaries(self,boundaries):
        self.boundaries = np.asarray(boundaries, np.int32)
        cv2.polylines(self.map, [self.boundaries], True, (255,255,255),3)
        
    def set_obstacle(self,pts):
        self.obstacles.append(pts)
        self.obstacles_np = np.asarray(self.obstacles, np.int32)
        self.active_obstacle.append(len(self.obstacles) -1)
                
    def remove_obstacle(self,obstacle):
        self.active_obstacle.remove(self.obstacles.index(obstacle))
        
    def print_obstacles(self, active=True):
        if(active):
            cv2.polylines(self.map, self.obstacles_np[self.active_obstacle], True, (0,255,0),3)
            print self.obstacles_np[self.active_obstacle]
        else:
            cv2.polylines(self.map, self.obstacles_np, True, (0,255,0),3)
            print self.obstacles_np[self.active_obstacle]
        
    def deinit(self):
        pass

