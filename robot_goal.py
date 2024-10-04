x = 0
y = 0

print("x=5 y=5 の位置がゴールです")

def goal_confirmation(x,y):

    if x == 5 and y == 5:
        return True
    
def current_location_massage(x,y):

    print(f"現在地はx = {x}, y = {y} です")

def move_select_massage():

    print("どちらに進みますか？")
    print("1: うえ 2: した 3: みぎ 4: ひだり")

def move_select():

    global x
    global y

    while True:
            try:
                num = int(input())

                if num == 1:
                    y += 1
                    break
                if num == 2:
                    y -= 1
                    break
                if num == 3:
                    x += 1
                    break
                if num == 4:
                    x -= 1
                    break
                else:
                    print("無効な数値です、正しく入力してください")
            except ValueError:
                print("半角数値で入力してください")

while True:
    current_location_massage(x,y)
    move_select_massage()
    move_select()
    goal_confirmation(x,y)
    if goal_confirmation(x,y):
        print("ゲームクリアです。おめでとうございます")
        break
