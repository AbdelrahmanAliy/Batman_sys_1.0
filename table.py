from tabulate import tabulate
import time

print('Welcome Sir hope You are Good!')
print('/>')     # a blank line just for view
print('Lets Go To Work ')
print("/>") 

stuff = [ ["Saturday", "Chemistry","45min:study 30min:solve","Physics","45min:study 30min:solve","Biology","45min:study 30min:solve","Gym"],
        ["Sunday", "Arabic","45min:study 30min:solve","Physics","45min:study 30min:solve","Biology","45min:study 30min:solve","Running"],
        ["Monday", "English","45min:study 30min:solve","Chemistry","45min:study 30min:solve","Arabic","45min:study 30min:solve","Code for hour"],
        ["Tuesday", "Arabic","45min:study 30min:solve","Chemistry","45min:study 30min:solve","German","45min:study 30min:solve","Read 10 pages from book"],
        ["Wednesday", "English","45min:study 30min:solve","Physics","45min:study 30min:solve","English","45min:study 30min:solve","Code new project"],
        ["Thursday", "Arabic","45min:study 30min:solve","Biology","45min:study 30min:solve","Chemistry","45min:study 30min:solve","Pull Ups"],
        ["Friday", "Physics","45min:study 30min:solve","Biology","45min:study 30min:solve","English","45min:study 30min:solve","Repeat"] ]

# i see the best way to study is 45 minutes of studying and 30 minutes of complete solving of what you studied and some revison won't hurt.
headers = ["Day", "Subject", "Duration","Subject", "Duration","Subject", "Duration", "Goal"]
# we are going to study 3 subjects a day for a week so 3 * 7 = 21 
# for 5 main subject and 1 optional (German) so 4 for each week and 1 session for german

print(tabulate(stuff, headers=headers, tablefmt="grid"))

time.sleep(3600)  # time the app stays for ever i mean that!!!

#This is E/Abdelrahman Ali Hassan