import time
import random
import os
import pygame

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_seconds(t_str):
    h, m = map(int, t_str.split(':'))
    return h * 3600 + m * 60

def defusal_sequence():
    clear_screen()
    print("⚠️  CRITICAL ALERT: PRE-DETONATION SEQUENCE INITIATED ⚠️")
    print("-------------------------------------------------------")
    print("The primary capacitor is leaking. Recalibrate the core!")
    
    for i in range(3):
        a, b = random.randint(10, 99), random.randint(10, 99)
        correct_answer = a + b
        
        user_input = input(f"\n[MODULE {i+1}] Solve to take the long walk: {a} + {b} = ")
        
        if user_input != str(correct_answer):
            print("\n❌ RSP FAILED! VOLTAGE INCREASING!")
            time.sleep(1)
            return False
            
    print("\n✅ DISARMED. You live to suffer another day in the corporate machine.")
    return True

def run_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play(-1) # Loop indefinitely
    
    t_start = get_seconds("05:30")
    t_end = get_seconds("06:00")
    duration = t_end - t_start
    
    disarmed = False
    
    while not disarmed:
        # Get current time in seconds from midnight
        now = time.localtime()
        current_sec = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
        
        if current_sec >= t_start:
            # Calculate volume: 0.0 to 1.0 based on time elapsed
            elapsed = current_sec - t_start
            volume = min(elapsed / duration, 1.0)
            pygame.mixer.music.set_volume(volume)

            clear_screen()
            print("☢️  DEADMAN'S ALARM ACTIVE  ☢️")
            print(f"Current Lethality: {int(volume * 100)}%")
            print("Press 'Enter' to attempt defusal...")
            
            # Simple non-blocking check for user interaction
            # In a full app, this would be a GUI button
            input() 
            if defusal_sequence():
                pygame.mixer.music.stop()
                disarmed = True

        else:
            clear_screen()
            print("...Device unarmed. Sweet dreams, cupcake...")
            time.sleep(30)

if __name__ == "__main__":
    run_alarm()