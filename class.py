import random

def rand(start, goal):
    return random.randint(start, goal)

def error_message():
    print("入力値が間違っています、再入力してください")

# プレイヤーやモンスターなどのキャラクターのクラス
class Character:
    # キャラクター名、ヒットポイント
    def __init__(self, name, hp, x, y, item_bag=[]):
        self.name = name
        self.BASE_HP = hp
        self.hp = hp
        self.x = x
        self.y  = y
        self.item_bag = []
    
    # テスト用ステータスを閲覧する関数
    def show_status(self):
        print(f'''Name: {self.name}
HP: {self.hp} / {self.BASE_HP}
x: {self.x}
y: {self.y}
Item_bag: {self.item_bag}''')
        
    # 現在の座標を表示する関数
    def show_position(self):
        print(f"{self.name}の現在地はx = {self.x}, y = {self.y}")
        
    #  キャラクターが対象と同じ位置にあるか判定する関数
    def check_encounter(self, target):
        return self.x == target.x and self.y == target.y
    
    # 選択方向を決める関数
    def choice_direction(self):
        
        while True:
            try:
                user_input = int(input("進む方向を選ぶ 1:上  2:下  3:右  4:左"))
                
                if 1 <= user_input <= 4:
                    return user_input
                
                else:
                    error_message()
                    continue
                
            except ValueError:
                error_message()
    
    
    # キャラクターを移動させるための関数
    def move(self, direction, move_distance=1):
        direction_name = ["上", "下", "右", "左"]
        
        if direction == 1:
            self.y += move_distance
            
        elif direction == 2:
            self.y -= move_distance
            
        elif direction == 3:
            self.x += move_distance
            
        elif direction == 4:
            self.x -= move_distance
    
        print(f"{self.name}は{direction_name[direction-1]}に進んだ")
    
    # 対象のHPが指定した数値以下が判定する関数
    def is_hp_low(self, hp_threshold=0):
        return max(self.hp, hp_threshold)
    
    # 対象に攻撃して、攻撃された側のHPを減らす関数
    def attack(self, target):
        damage = rand(1, 4)
        target.hp -= damage
        print(f"{self.name}の攻撃  {target.name}に{damage}ダメージ")
        if target.hp <= 0:
            target.hp = 0
        print(f"{self.name}: HP {self.hp} / {self.BASE_HP}   {target.name}: HP {target.hp} / {target.BASE_HP}")
        

    # 対象に攻撃されたときに防御したときの関数    
    def defence(self, target):
        block_chance = rand(1, 100)
                            
        if block_chance > 50:
            print("防御成功！ノーダメージ")
            return True                  
        else:
            print("防御失敗")
            return False
        
    # 対象のHPがゼロか確認する関数
    def is_dead(self):
        if self.hp <= 0:
            print(f"{self.name}はやられてしまった")
            return True 
         
    # プレイヤーとモンスターとの戦闘の関数
    def battle(self, target):
        print(f"{target.name}に遭遇、襲い掛かってきた")
        runaway_hp = 3
        
        # お互いのHPを表示する関数
        def show_hp_message():
            print(f"{self.name}: HP {self.hp} / {self.BASE_HP}   {target.name}: HP {target.hp} / {target.BASE_HP}")
        
        while True:
            show_hp_message()
            print(f"{self.name}のターン")
            while True:
                try:
                    user_input = int(input("1: 攻撃   2: 防御"))
                    
                    if 1 <= user_input <= 2:
                        
                        if user_input == 1:
                            self.attack(target)
                                
                            if target.hp < runaway_hp:
                                print(f"{target.name}は痛みに耐えきれず逃げ出した")
                                print(f"逃げながら自分に回復魔法をかけているようだ")
                                target.hp = target.BASE_HP
                                self.show_status()
                                target.move(rand(1, 4), 2)
                                return True
                            
                            target.attack(self)
                            
                            if self.is_dead():
                                return False
                                
                        elif user_input == 2:
                            if not self.defence(target):
                                target.attack(self)
                                
                            if self.is_dead():
                                return False

                        else:
                            error_message()    
                    else:
                        error_message()        
                except ValueError:
                    error_message()
            break
                    
# アイテムのクラス
class Item:
    # アイテム名とその位置
    def __init__(self, name, x, y, value=0, effect=None, effect_points=0):
        self.name = name
        self.x = x
        self.y = y
        self.value = value
        self.effect = effect
    
    # アイテムの座標を表示する関数    
    def show_position(self):
        print(f"{self.name}の現在地はx = {self.x}, y = {self.y}")

    # テスト用ステータスを閲覧する関数
    def show_status(self):
        print(
f'''Name: {self.name}
x: {self.x}
y: {self.y}
value: {self.value}
effect: {self.effect}'''
)
        
    # アイテムエフェクトのひとつ
    def recovery(self, character, recovery_points):
        character.hp += recovery_points
        if character.hp > character.BASH_HP:
            character.hp = character.BASH_HP
            print(f"{character.name}は{self.name}を使った、HPが全回復した")
        else:
            print(f"{character.name}は{self.name}を使った。HPが{recovery_points}回復した")
    
    # 暗号を解読する関数
    def code_input(self, code_list, code_hint_massage="特になし"):
        print("このアイテムは施錠されていて、暗号を解読しないと手に入らない")

        while True:
            print(f"ヒント: {code_hint_massage}")
            user_input = input("暗号を入力してください")
            if user_input in code_list:
                print(f"暗号をの解読に成功！{self.name}を手に入れた")
                return True
            
            else:
                print("暗号が間違っている")

# ゲームのメイン
    
player = Character("ゆうしゃ", 10, 0, 0)
monster = Character("ドラゴン", 8, 1, 1)
chest = Item("伝説の宝", 5, 5, 10000)
potion = Item("ポーション",-1, -1, 500, "recovery", 5)

print(f'''ゲームの説明
ダンジョン内にある{chest.name}を手に入れることが出来ればゲームクリア
{chest.name}の座標はわかっているので確認しながらその場所を目指せ
ただし、ダンジョン内には{monster.name}がいるので、遭遇したら攻撃して追い払え
{monster.name}はHPが一定以下になると逃げる
もし{monster.name}にやられてしまった場合はゲームーオーバー
ゲームスタート
''')

while True:
    player.show_status()
    chest.show_position()
    player.show_position()
    monster.show_position()
    player.move(player.choice_direction())
    monster.move(rand(1,4))
    if player.check_encounter(monster):
        if player.battle(monster):
            if player.check_encounter(chest):
                if chest.code_input(["apple", "banana", "berry"], "有名な果物"):                    
                    print("ゲームクリア！おめでとう！！！")
                    break
        else:
            print("ゲームオーバー")
            break
    elif player.check_encounter(chest):
        if chest.code_input(["apple", "banana", "berry"], "有名な果物"):
            print("ゲームクリア！おめでとう！！！")
            break