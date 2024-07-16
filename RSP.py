import random

def get_user_choice():
    while True:
        choice = input("S, R, P 중 하나를 선택하세요: ")
        if choice in ["S", "R", "P"]:
            return choice
        print("잘못된 입력입니다. 다시 선택해주세요.")

def get_computer_choice():
    return random.choice(["S", "R", "P"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (
        (user_choice == "S" and computer_choice == "P") or
        (user_choice == "R" and computer_choice == "S") or
        (user_choice == "P" and computer_choice == "R")
        ):
        return "사용자 승리"
    else:
        return "컴퓨터 승리"

def play_game():
    print("가위바위보 게임을 시작합니다!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"사용자 선택: {user_choice}")
        print(f"컴퓨터 선택: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(f"결과: {result}")
        
        play_again = input("다시 플레이하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            break
    
    print("게임을 종료합니다. 감사합니다!")

if __name__ == "__main__":
    play_game()