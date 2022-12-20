import random

def roll_dice():
  # 1 ve 6 arasında bir sayi uret
  roll = random.randint(1, 6)
  print(roll," attınız.")

while True:
  # Zar atılıp atılmak istenmedigini sor.
  choice = input("Zar atmak istiyor musunuz? (e/h) ")
  
  if choice.lower() == 'e':
    roll_dice()
  elif choice.lower() == 'h':
    break
  else:
    print("Yanlis deger girdiniz. 'e' veya 'h' deneyin.")
