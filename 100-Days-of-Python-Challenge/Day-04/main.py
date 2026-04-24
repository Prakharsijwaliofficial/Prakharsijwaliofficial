import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list1 = [ rock , paper, scissors]
rand_no= int(input("what did you choose? Type 0 for rock, 1 for paper or 2 for scissors"))
user_inp = list1[rand_no]
rob_inp = random.choice(list1)

print(user_inp)
print("Computer choose\n" +rob_inp  )

if user_inp == rob_inp:
    print("Its a draw")
elif user_inp == rock and rob_inp == scissors :
    print("You win!!!")
elif user_inp == scissors and rob_inp == rock:
    print("you loose")
elif user_inp == paper and rob_inp == scissors:
    print("You loose")
elif user_inp == paper and rob_inp == rock:
    print("You win!!!")
elif user_inp == scissors and rob_inp == paper:
    print("YOu win!!!!")
elif user_inp == rock and rob_inp == paper:
    print("You loose")
