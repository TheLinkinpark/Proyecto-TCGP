import time
import random
import os

def draw_wheel(values, selected_index):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen command for Windows and Unix
    print("\n" + "=" * 30)
    for i, value in enumerate(values):
        marker = "<--" if i == selected_index else "   "
        print(f"| {value:^5} | {marker}")
    print("=" * 30 + "\n")

def spin_wheel():
    values = [20, 0, 50, 5, 10, -10, 100, 5]
    selected_index = 0
    
    for _ in range(random.randint(10, 20)):
        selected_index = (selected_index + 1) % len(values)
        draw_wheel(values, selected_index)
        time.sleep(0.2)
    
    print(f"Resultado final: {values[selected_index]}")


spin_wheel()