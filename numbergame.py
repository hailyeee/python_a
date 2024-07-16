import random

# 1부터 100 사이의 랜덤한 숫자 선택
target_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    try:
        guess = int(input("숫자를 입력하세요: "))

        if guess > 100:
            print("100이하의 숫자만 입력해주세요")
            continue
        
        attempts += 1

        if guess < target_number:
            print(f"[{attempts}번째] 당신이 입력하신 {guess}는 정답보다 작은 숫자입니다")
        elif guess > target_number:
            print(f"[{attempts}번째] 당신이 입력하신 {guess}는 정답보다 큰 숫자입니다")
            
        else:
            print(f"정답입니다! {attempts}번 만에 숫자를 맞추셨습니다.")
            break
    except ValueError:
        print("유효한 숫자를 입력해주세요!!")
