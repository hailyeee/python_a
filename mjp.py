import random

def get_choice(help_message):
    while True:
        choice = input(f"{help_message}✊(0), ✌️ (1), 🖐 (2) 중 하나를 선택하세요: ")
        if choice in ['0', '1', '2']:
            return int(choice)
        print("잘못된 입력입니다. 다시 선택해주세요.")

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(player, computer):
    if player == computer:
        return "무승부"
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        return "플레이어"
    else:
        return "컴퓨터"

def play_game():
    choices = ["✊", "✌️", "🖐"]
    print("묵찌빠 게임을 시작합니다!")

    # 첫 번째 가위바위보로 공격자 결정
    while True:
        player = get_choice("공격자결정을 위해 ")
        computer = get_computer_choice()
        print(f"플레이어: {choices[player]} , 컴퓨터: {choices[computer]}")
        winner = determine_winner(player, computer)
        if winner != "무승부":
            attacker = winner
            break
        print("무승부입니다. 다시 시도하세요.")

    print(f"{attacker}가 공격자가 되었습니다.")

    # 묵찌빠 진행
    while True:
        player = get_choice("")
        computer = get_computer_choice()
        print(f"플레이어: {choices[player]}, 컴퓨터: {choices[computer]}")

        if player == computer:
            print(f"{attacker}의 승리!")
            break
        else:
            winner = determine_winner(player, computer)
            if winner != attacker:
                print(f"공격권이 {winner}에게 넘어갔습니다.")
                attacker = winner
            else:
                print(f"{attacker}가 계속 공격합니다.")

    print("게임 종료!")

if __name__ == "__main__":
    play_game()