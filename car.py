# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:12:50 2023

@author: angel
"""

import pygame
import random

def fn_fight():
    
    #파이썬 기본 설정
    pygame.init()
    
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # 파이썬 이미지 불러오기
    back = pygame.image.load("back.png")
    car = pygame.image.load("car.png")
    x,y = -200,-200
    c = False
    flag = pygame.image.load("flag.png")
    flag_x,flag_y = -200,-200
    f = False
    
    save_list = []
    
    running = True
    while running:
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                
            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    c = True
                    x_p, y_p = pygame.mouse.get_pos()    
                
                # 상단
                    if x_p >= 0 and x_p <= 200 and y_p >= 0 and y_p <= 200:
                        x = 0
                        y = 0
                    if x_p >= 200 and x_p <= 400 and y_p >= 0 and y_p <= 200:
                        x = 200
                        y = 0
                    if x_p >= 400 and x_p <= 600 and y_p >= 0 and y_p <= 200:
                        x = 400
                        y = 0
                        
                # 중단
                    if x_p >= 0 and x_p <= 200 and y_p >= 200 and y_p <= 400:
                        x = 0
                        y = 200
                    if x_p >= 200 and x_p <= 400 and y_p >= 200 and y_p <= 400:
                        x = 200
                        y = 200
                    if x_p >= 400 and x_p <= 600 and y_p >= 200 and y_p <= 400:
                        x = 400
                        y = 200
                        
                   # 하단 
                    if x_p >= 0 and x_p <= 200 and y_p >= 400 and y_p <= 600:
                        x = 0
                        y = 400
                    if x_p >= 200 and x_p <= 400 and y_p >= 400 and y_p <= 600:
                        x = 200
                        y = 400
                    if x_p >= 400 and x_p <= 600 and y_p >= 400 and y_p <= 600:
                        x = 400
                        y = 400
                        
                if event.button == 3:  # 마우스 오른쪽 클릭시
                    f = True
                    x_p, y_p = pygame.mouse.get_pos()    
                
                # 상단
                    if x_p >= 0 and x_p <= 200 and y_p >= 0 and y_p <= 200:
                        flag_x = 0
                        flag_y = 0
                    if x_p >= 200 and x_p <= 400 and y_p >= 0 and y_p <= 200:
                        flag_x = 200
                        flag_y = 0
                    if x_p >= 400 and x_p <= 600 and y_p >= 0 and y_p <= 200:
                        flag_x = 400
                        flag_y = 0
                        
                # 중단
                    if x_p >= 0 and x_p <= 200 and y_p >= 200 and y_p <= 400:
                        flag_x = 0
                        flag_y = 200
                    if x_p >= 200 and x_p <= 400 and y_p >= 200 and y_p <= 400:
                        flag_x = 200
                        flag_y = 200
                    if x_p >= 400 and x_p <= 600 and y_p >= 200 and y_p <= 400:
                        flag_x = 400
                        flag_y = 200
                        
                   # 하단 
                    if x_p >= 0 and x_p <= 200 and y_p >= 400 and y_p <= 600:
                        flag_x = 0
                        flag_y = 400
                    if x_p >= 200 and x_p <= 400 and y_p >= 400 and y_p <= 600:
                        flag_x = 200
                        flag_y = 400
                    if x_p >= 400 and x_p <= 600 and y_p >= 400 and y_p <= 600:
                        flag_x = 400
                        flag_y = 400
                        
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            
        screen.blit(back,(0,0))
        if f == True and c == True:
            
            if x == flag_x and y == flag_y :
                f = False
                print(save_list)
                return save_list
                running = False
                
                save_list.clear()
        if f == True :
            screen.blit(flag,(flag_x,flag_y)) 
            
        pygame.time.delay(300)
        if f == True :     
                
            pygame.time.delay(200)
            
            if flag_x > x :
                x += 200
                save_list.append("➝")
                screen.blit(car,(x,y))     
            elif flag_x < x :
                x -= 200
                save_list.append("←")
                screen.blit(car,(x,y))     
            elif flag_y > y :
                y += 200
                save_list.append("↓")
                screen.blit(car,(x,y))     
            elif flag_y < y :
                y -= 200
                save_list.append("↑")
                screen.blit(car,(x,y))     
            print(x,y)
        screen.blit(car,(x,y))     
    
        pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":       
    a = fn_fight()
    print(a)
