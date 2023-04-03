from tkinter import*
import random 
random.seed()

ch_II=0
ch_Gamer=0
ISK_CH=random.randrange(1,4)
a=0

    
def clicked():
    Game =Tk()
    Game.configure(background='#3165de')
    Game.title ('Угадай число')
    Game.geometry('750x300')

    #----------------------------------------------------------------FUNCK
    def rasch():
        
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 1:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                ch_Gamer=ch_Gamer+10
                but_v1.config(background='#05f505')#GREEN
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 1:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v1.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 1:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v1.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 1:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                but_v1.config(background='#f5051d')#RED
                ch_II=ch_II+10
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
           
   
    def bat1 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 1:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                ch_Gamer=ch_Gamer+10
                but_v1.config(background='#05f505')#GREEN
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 1:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v1.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 1:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v1.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 1:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                but_v1.config(background='#f5051d')#RED
                ch_II=ch_II+10
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
        
    def bat2 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 2:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                ch_Gamer=ch_Gamer+10
                but_v2.config(background='#05f505')#GREEN
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 2:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v2.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 2:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v2.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 2:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                but_v2.config(background='#f5051d')#RED
                ch_II=ch_II+10
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
        
    def bat3 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 3:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                but_v3.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+10
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 3:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v3.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 3:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v3.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 3:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                ch_II=ch_II+10
                but_v3.config(background='#f5051d')#RED
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
        
    def bat4 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 4:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                but_v4.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+10
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 4:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v4.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 4:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v4.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 4:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                ch_II=ch_II+10
                but_v4.config(background='#f5051d')#RED
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
    def bat5 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 5:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                but_v5.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+10
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 5:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v5.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 5:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v5.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 5:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                ch_II=ch_II+10
                but_v5.config(background='#f5051d')#RED
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
    def bat6 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 6:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                but_v6.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+10
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 6:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v6.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 6:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v6.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 6:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                ch_II=ch_II+10
                but_v6.config(background='#f5051d')#RED
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
    def bat7 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 7:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                but_v7.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+10
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 7:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v7.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 7:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v7.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 7:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                ch_II=ch_II+10
                but_v7.config(background='#f5051d')#RED
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
    def bat8 ():
        global ch_Gamer
        global ch_II
        global a
        a=a+1
        
        if a<=1:
            
            if ISK_CH == 8:
                lab1.config(text='Поздравляю, ты угадал с первого раз!!!! Вот твои 10Б')
                but_v8.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+10
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
            elif ISK_CH != 8:
                lab1.config(text='Не угaдал, вторая попытка.')
                but_v8.config(background='#f5051d')#RED
                
        elif a ==2:
            
            if ISK_CH == 8:
                lab1.config(text='Поздравляю, ты угадал со второго раза 5Б')
                but_v8.config(background='#05f505')#GREEN
                ch_Gamer=ch_Gamer+5
                lab5.config(text=ch_Gamer)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
                
                
            elif ISK_CH != 8:
                lab1.config(text='второй раз не угaдал, мне 10Б.')
                ch_II=ch_II+10
                but_v8.config(background='#f5051d')#RED
                lab6.config(text=ch_II)
                but_v1.config(state=DISABLED)
                but_v2.config(state=DISABLED)
                but_v3.config(state=DISABLED)
                but_v4.config(state=DISABLED)
                but_v5.config(state=DISABLED)
                but_v6.config(state=DISABLED)
                but_v7.config(state=DISABLED)
                but_v8.config(state=DISABLED)
        


    def nov():
        global a
        but_v1.config(state=NORMAL)
        but_v2.config(state=NORMAL)
        but_v3.config(state=NORMAL)
        but_v4.config(state=NORMAL)
        but_v5.config(state=NORMAL)
        but_v6.config(state=NORMAL)
        but_v7.config(state=NORMAL)
        but_v8.config(state=NORMAL)

        but_v1.config(background='#edd8da')#NORM
        but_v2.config(background='#edd8da')#NORM
        but_v3.config(background='#edd8da')#NORM
        but_v4.config(background='#edd8da')#NORM
        but_v5.config(background='#edd8da')#NORM
        but_v6.config(background='#edd8da')#NORM
        but_v7.config(background='#edd8da')#NORM
        but_v8.config(background='#edd8da')#NORM
        
        global ISK_CH
        ISK_CH=random.randrange(1,9)
        lab1.config(text='Загадал!!!')
        a=0
        print(ISK_CH)
       
    #-------------------

    
#----------------------------------------------------------------Счёт
    lab5=Label(Game, font=("Arial", 15), background='#3165de',text='Name')
    lab5.place(x=430,y=120)
    
    lab5.config(text=ent.get())

    lab3=Label(Game, font=("Arial", 15), background='#3165de',text='Счёт:  ')
    lab3.place(x=510,y=60)

    lab4=Label(Game, font=("Arial", 15), background='#3165de',text='Компьютер  ')
    lab4.place(x=430,y=90)

    lab5=Label(Game, font=("Arial", 15), background='#3165de',text=ch_Gamer)
    lab5.place(x=560,y=120)

    lab6=Label(Game, font=("Arial", 15), background='#3165de',text=ch_II)
    lab6.place(x=560,y=90)
#-------------------------

    
    btn2=Button (Game, text='Ещё разок?', font=('Aria', 11), background='#61b536',command=nov)
    btn2.place(x=560, y=170)

    
    lab=Label(Game, borderwidth=2, font=("Arial", 12), background='#b4f593' ,relief= 'raised' ,text='Привет. Я загадаю цифру от 1 до 8, если угадаешь с 1-го раза, получишь 10Б, со 2-го 5Б')
    lab.place(x=5, y=10)
    lab=Label(Game, borderwidth=2, font=("Arial", 12), background='#b4f593' ,relief= 'raised' ,text='Если ты не угадываешь с двух раз, то я получаю 10Б')
    lab.place(x=5, y=35)

    lab1=Label(Game, borderwidth=3, font=("Arial", 13), background='#eff2bf' ,relief= 'raised' ,text='Поздравляю, ты выиграл с певого раза!!! Вот твои заслуженные 10Б')
    lab1.place(x=5, y=245)

    
    
#----------------------------------------------------------------------------------------- кнопки
    but_v1=Button(Game, text='1', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat1)
    but_v1.place(x=5, y=90)

    but_v2=Button(Game, text='2', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat2)
    but_v2.place(x=5, y=160)

    but_v3=Button(Game, text='3', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat3)
    but_v3.place(x=70, y=90)

    but_v4=Button(Game, text='4', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat4)
    but_v4.place(x=70, y=160)

    but_v5=Button(Game, text='5', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat5)
    but_v5.place(x=135, y=90)

    but_v6=Button(Game, text='6', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat6)
    but_v6.place(x=135, y=160)

    but_v7=Button(Game, text='7', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat7)
    but_v7.place(x=200, y=90)

    but_v8=Button(Game, text='8', font=('Aria', 14), background='#edd8da',height=1, width=4, command=bat8)
    but_v8.place(x=200, y=160)
#---------------
    

    
Game =Tk()
Game.configure(background='#3165de')
Game.title ('Угадай число')
Game.geometry('250x80')


lab2=Label(Game, borderwidth=2, font=("Arial", 11), background='#dff7e2' ,relief= 'raised' ,text='Введите ваше имя:  ')
lab2.place(x=5, y=10)
ent=Entry(Game, borderwidth=2, background='#dff7e2' ,relief= 'raised',width=23)
ent.place (x=5, y=35)

btn=Button (Game, borderwidth=3, font=("Arial", 17), background='#dff7e2' ,relief= 'raised' ,text='Ввод', command=clicked)
btn.place(x=160, y=10)


Game.mainloop()
