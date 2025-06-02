print('''
                                     ^!^
         _._._._._._._._._._._._._._._._._   ^
         | ___   ___    ___    ___   ___ |
     ^!^ ||_|_| |_|_|  |_|_|  |_|_| |_|_||
         |IIIII_IIIII__IIIII__IIIII_IIIII|      ^
         | ___   ___    ___    ___   ___ |
 )o(_    ||_|_| |_|_|  |_|_|  |_|_| |_|_||
/(|)\    |IIIII_IIIII__IIIII__IIIII_IIIII|
  H)o(_  | ___   ___    ___    ___   ___ |
  /(|)\  ||_|_| |_|_|  |_|_|  |_|_| |_|_||
  H H    |IIIII_IIIII__IIIII__IIIII_IIIII|    /)
  H H    | ___   ___   _____   ___   ___ | __/ ),
   ~ ^~^ ||_|_| |_|_|  o~|~o  |_|_| |_|_||  ~^~^
  . ' .'.|IIIII_IIIII__|_|_|__IIIII_IIIII|'^~^'.',
 .,' , .|"""""""""""""/=====\"""""""""""""|.'.'.'.
   `~ ` "^^~ " ^^~'` "'     `",``~^^"" ~^^"   '~'
 .    "        "       ,   '           "    "

  ''')  
print("welcome to investigater.")
print("You wake up in a mysterious laboratory with no memory.")
print("You have 3 ways out: Door A: Blinking keypad.\nDoor B: Requires a fingerprint .\nAir vent: Small but open.\n")
choice=input('type "a" for door A,type "b" for door B,type "c" for Air vent\n').lower()
  
if choice=="a":
    print(" Guess a code (user types it)\nyou escaped with truth.")
    
elif choice == "b":
      choice2=input('Look for a fingerprint (search desk / body / wall),while searching for fingerprint you found a secret door, for enter type "1" else "0" \n')
      if choice2 == "1":
          print("you escaped throug secret door")
      elif choice2 == "0":
          print("you can't find fingurprint and you get cought")
elif choice == "c":
       print("you crwaled through air vent and found an chemical room. ")
       choice4=input('for taking chemical with you type "y" else "n"\n').lower()
       if choice4 == "y":
         print("you escaped with chemical and you got a meddale from government")
       else:
             print("you escaped but no one belived you .")
else:
    print("Invalid choice. You're stuck in the lab forever!")
  