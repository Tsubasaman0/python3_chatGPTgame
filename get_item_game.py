import random

# プレイヤーやモンスターなどのキャラクターのクラス
class Character:
    # キャラクター名、ヒットポイント
    def __init__(self, name, hp, x, y):
        self.name = name
        self.hp = hp
        self.x = x
        self.y  = y
    
    # キャラクターを移動させるための関数
    def move(self, direction):
        direction_name = ["上", "下", "右", "左"]
        
        if direction == 1:
            self.y += 1
            
        elif direction == 2:
            self.y -= 1
            
        elif direction == 3:
            self.x += 1
            
        elif direction == 4:
            self.x -= 1
    
        print(f"{self.name}は{direction_name[direction-1]}に進みました")

# プレイヤーの初期位置とHP
player_x = 0
player_y = 0
player_hp = 10

# アイテムの初期位置
item_x = 4
item_y = 5

# モンスターの初期位置とHP
monster_x = 3
monster_y = 3
monster_hp = 8

# 現在の座標を表示する関数
def show_position(x, y, character="プレイヤー"):
    print(f"{character}の現在地はx = {x}, y = {y}です")
    
# テスト用HP確認の関数
def show_hp(player_hp, monster_hp):
    print(f"現在のプレイヤーのHP {player_hp}, モンスターのHP {monster_hp}")

# プレイヤーが選択した方向、もしくはモンスターがランダムの方向に進む関数
def move_character(x, y, character="プレイヤー"):
    
    # 方向の名称の変数
    directions = ["上", "下", "右", "左"]

    # 誰がどっちに進んだかを表示させる関数 
    def display_move_massage(direction):
        print(f"{character}は{direction}に進みました")
  
    # プレイヤーかモンスター、処理の分岐
    if character == "プレイヤー":
        while True:
            try:
                num = int(input("移動方向を選択してください 1: 上 2: 下 3: 右 4: 左 "))

                if 1 <= num <= 4:
                    
                    if num == 1:
                        y += 1
        
                    elif num == 2:
                        y -= 1
                
                    elif num == 3:
                        x += 1

                    elif num == 4:
                        x -= 1
                        
                    display_move_massage(directions[num-1])    
                    return x, y
        
                else:
                    print("誤った数値が入力されました、1-4で入力してください")
                    
            except ValueError:
                print("無効な値が入力されました")
                
    elif character == "モンスター":

        num = random.randint(1, 4)
        
        if num == 1:
            y += 1
            
        elif num == 2:
            y -= 1
        
        elif num == 3:
            x += 1
        
        elif num == 4:
            x -= 1
        
        display_move_massage(directions[num-1])
        return x, y

# アイテムの宝箱の暗号解読の関数
def code_input():
    code_list = ["apple", "banana", "cherry"]
    hint_message = ("ヒント：有名な果物")
        
    while True:
        print("このアイテムは宝箱に入っており、暗号を解かないと開きません")
        user_input = input("暗号を入力してください")
        print(hint_message)
        if user_input in code_list:
            break
        else:
            print("暗号が間違っています")
            
            

# プレイヤーとモンスター,またはアイテムと座標どうかを判別する関数
def check_encounter(player_x, player_y, target_x, target_y):
    return player_x == target_x and player_y == target_y

# プレイヤーとモンスターが遭遇したときのバトルの関数
def battle(player_hp, monster_hp):
    print("モンスターと遭遇した、襲い掛かってきた")
    
    # プレイヤーとモンスターの残りHPを表示する関数
    def show_player_hp_and_monster_hp():
        print(f"プレイヤー残りHP{player_hp} モンスター残りHP{monster_hp}")
        
    # HPが０を下回った売場合にHPを０にする関数
    def normalize_hp(hp):
        return max(hp, 0)
    
    # バトルの流れ                
    while True:
        print("プレイヤーの攻撃")
        input()
        damage = random.randint(1,4)
        monster_hp = normalize_hp(monster_hp - damage)    
        print(f"プレイヤーはモンスターに {damage} ダメージ与えた")
        show_player_hp_and_monster_hp()
        if monster_hp == 0:
            return True
        
        print("モンスターの攻撃")
        input()
        damage = random.randint(1,4)
        player_hp = normalize_hp(player_hp - damage)
        print(f"モンスターはプレイヤーに {damage} ダメージ与えた")
        show_player_hp_and_monster_hp()
        if player_hp == 0:
            return False

# モンスターが逃げた場合の座標変更の関数
def escape_distance(x,y):
    direction = random.randint(1, 4)
    distance = random.randint(2, 3)
    
    if direction == 1:
        return x + distance, y
    elif direction == 2:
        return x, y + distance
    elif direction == 3:
        return x - distance, y
    elif direction == 4:
        return x, y - distance

    

# ゲーム開始
# ルール説明
print("ダンジョン内を移動して、アイテムをゲットしたらクリアです。")
print(f"アイテムはx = {item_x}、y = {item_y}にあります。")
print("ただし、ダンジョン内にはモンスターが徘徊しており、遭遇するとゲームオーバーです。")

while True:
    show_position(player_x, player_y)
    show_position(monster_x, monster_y, "モンスター")
    player_x, player_y = move_character(player_x, player_y)
    monster_x, monster_y = move_character(monster_x, monster_y, "モンスター")
    if check_encounter(player_x, player_y, monster_x, monster_y):
         if battle(player_hp, monster_hp):
             monster_x, monster_y = escape_distance(monster_x, monster_y)
             print("モンスターに勝利、モンスターはどこかに逃げて行った")
             # show_hp(player_hp, monster_hp)
             continue
         else:
            print("モンスターにやられてしまった、ゲームオーバー")
         break
    if check_encounter(player_x, player_y, item_x, item_y):
         code_input()
         print("アイテムゲット！ゲームクリア")
         break
