#!/usr/bin/env python
# coding: utf-8

# In[1]:


#GDS - Geriatric Depression Scale

print ("Are you basically satisfied with your life?")
print (''' [0] Yes [1] No ''')
opt1 = int(input('Choose an option'))
print ("Have you dropped many of your activities and interests?")
print(''' [1] Yes [0] No ''')
opt2 = int(input('Choose an option '))
print ("Do you feel that your life is empty?")
print(''' [1] Yes [0] No ''')
opt3 = int(input('Choose an option '))
print ("Do you often get bored?")
print(''' [1] Yes [0] No ''')
opt4 = int(input('Choose an option'))
print ("Are you in good spirits most of the time?")
print(''' [0] Yes [1] No ''')
opt5 = int(input('Choose an option'))
print ("Are you afraid that something bad is going to happen to you?")
print(''' [1] Yes [0] No ''')
opt6 = int(input('Choose an option ')) 
print ("Do you feel happy most of the time?")
print(''' [0] Yes [1] No ''')
opt7 = int(input('Choose an option '))
print ("Do you feel helpless?")
print('''[1] Yes [0] No ''')
opt8 = int(input('Choose an option')) 
print ("Do you prefer to stay at home, rather than going out and doing new things?")
print(''' [1] Yes [0] No ''')
opt9 = int(input('Choose an option '))
print ("Do you feel you have more problems with your memory than most?")
print(''' [1] Yes [0] No ''')
opt10 = int(input('Choose an option')) 
print ("Do you think it is good to be alive?")
print('''[0] Yes [1] No ''')
opt11 = int(input('Choose an option '))
print ("Do you feel pretty worthless the way you are now?")
print(''' [1] Yes [0] No ''')
opt12 = int(input('Choose an option')) 
print ("Do you feel full of energy?")
print(''' [0] Yes [1] No ''')
opt13 = int(input('Choose an option '))
print ("Do you feel that your situation is hopeless?")
print('''[1] Yes [0] No ''')
opt14 = int(input('Choose an option ')) 
print ("Do you think that most people are better off than you are?")
print('''[1] Yes [0] No ''')
opt15 = int(input('Choose an option '))
score= opt1+opt2+opt3+opt4+opt5+opt6+opt7+opt8+opt9+opt10+opt11+opt12+opt13+opt14+opt15
print("Your score on the Depression Scale is {}".format(score))
if score <=6:
    print ("You don't have any symptoms of depression ")
elif score >=7 and score <=10:
    print ("You have symptoms of light depression")
else:
    print ("You have symptoms of severe depression")


# 
