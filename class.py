import random

def rand(start, goal):
    return random.randint(start, goal)

def error_message():
    print("入力値が間違っています、再入力してください")

# プレイヤーやモンスターなどのキャラクターのクラス
class Character:
    # キャラクター名、ヒットポイント
    def __init__(self, name, base_hp, hp, attack_power, defense_power, x, y, exp=0, level=1, exp_to_next_level=0, level_up_table=2, item_bag=None):
        self.name = name
        self.base_hp = base_hp
        self.hp = hp
        self.attack_power = attack_power
        self.defence_power = defense_power
        self.x = x
        self.y  = y
        self.exp = exp
        self.level = level
        self.exp_to_next_level = exp_to_next_level
        self.level_up_table = level_up_table
        if item_bag is None:
            self.item_bag = []
        
    # 経験値を取得する関数
    def add_exp(self, exp_gained):
        self.exp += exp_gained
        
    # 次回レベルアップまでの経験値を計算、self.exp_to_next_levelに代入する関数
    def get_next_level_exp(self):
        level_up_table_exp_sum = 0
        temp_level = 0
        while True:
            temp_level += 1
            level_up_table_exp_sum += self.level_up_table ** temp_level
            if self.exp < level_up_table_exp_sum:
                self.exp_to_next_level = self.exp - level_up_table_exp_sum
                break
        
    # キャラクターがレベルアップする経験値に達しているかを返す関数
    def check_level_up(self):
        return self.exp_to_next_level <= 0
        
    # いくつレベルアップしたか確認する関数
    def calculate_level_ups(self):
        temp_level = self.level   # この関数がおかしい
        level_up_count = 0
        
        while True:
            if  self.exp_to_next_level <= 0:
                level_up_count += 1
                temp_level +=1
                # 次回レベルアップまでの経験値を計算した値を、self.exp_to_next_levelに代入することもセットで処理
                initial_exp_needed = self.level_up_table ** temp_level
                self.exp_to_next_level = initial_exp_needed + self.exp_to_next_level 
            else:
                return level_up_count
    
    # キャラクターがレベルアップしたときの処理関数
    def level_ups(self, level_up_ponints):
        
        for _ in range(level_up_ponints):
            hp_points = rand(7, 12)
            attack_power_points = rand(1,3)
            defense_power_points = rand(1,2)
            print(f'''
{self.name}のレベルがあがった
レベル: {self.level} + 1 ↑
HP: {self.base_hp} + {hp_points} ↑
攻撃力: {self.attack_power} + {attack_power_points} ↑
防御力: {self.defence_power} + {defense_power_points} ↑
''')
            self.level += 1
            self.base_hp += hp_points                    
            self.attack_power += attack_power_points
            self.defence_power += defense_power_points

    
    # ステータスを閲覧する関数
    def show_status(self):
        item_names = "\n".join(f"・{item.name}" for item in self.item_bag if self.item_bag)
        
        print(f'''
名前: {self.name}
レベル: {self.level}
HP: {self.hp} / {self.base_hp}
攻撃力: {self.attack_power}
防御力: {self.defence_power}
次のレベルアップまでの経験値: {self.exp_to_next_level} 
x: {self.x}
y: {self.y}
アイテムバッグ:
{item_names}
''')
        
    # 現在の座標を表示する関数
    def show_position(self):
        print(f"{self.name}の現在地はx = {self.x}, y = {self.y}")
        
    # Item_bagを開いた時の動作の関数
    def open_item_bag(self):
        if len(self.item_bag) == 0:
            print("アイテムを持っていません")
            
        else:
            select_item_index = self.select_index(len(self.item_bag), self.item_bag, True, "アイテムを選んでください", True)
            action_item_index = self.select_index(3, ["使う", "捨てる", "閉じる"])
            
            if action_item_index == 1: # 使う
                self.use_item(self.item_bag[select_item_index-1], action_item_index-1)
            
            elif action_item_index == 2: # 捨てる
                print(f"{self.item_bag[select_item_index-1].name}を捨てた")
                self.item_bag.pop(select_item_index-1)
                 
            elif action_item_index == 3: # 閉じる   
                return # 処理終了
            
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

    # 行動や方向を選択するための関数、choice_directionとselect_actionをまとめたもの
    def select_index(
            self, index, options_list, is_message_selected=True, select_message="選んでください", has_name=False):
        
        # options_listをfor分でprintする、そのあとにinputで選択したindexを返す
        
        while True:
            try:
                if is_message_selected == True:
                    print(select_message)
                
                for i in range(len(options_list)):
                    option = options_list[i]
                    
                    if has_name:
                        print(f"{i+1}:  {option.name}")
                    else:
                        print(f"{i+1}:  {option}")
                
                user_input = int(input())
                
                if 1 <= user_input <= index:
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
        return self.hp <= hp_threshold
    
    # 対象に攻撃して、攻撃された側のHPを減らす関数
    def attack(self, target):
        damage = rand(1, 4)
        target.hp -= damage
        print(f"{self.name}の攻撃  {target.name}に{damage}ダメージ")
        if target.hp <= 0:
            target.hp = 0
        print(f"{self.name}: HP {self.hp} / {self.base_hp}   {target.name}: HP {target.hp} / {target.base_hp}")
        

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
            print(f"{self.name}: HP {self.hp} / {self.base_hp}   {target.name}: HP {target.hp} / {target.base_hp}")
        
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
                                target.hp = target.base_hp
                                target.move(rand(1, 4), 2)
                                self.handle_battle_end(target.exp_points)
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
        
    # バトル終了後の経験値付与、レベルアップなどの処理関数
    def handle_battle_end(self, exp_gained):
        print(f"""
戦いに勝った
経験値を{exp_gained}手に入れた
""")
        self.add_exp(exp_gained)
        
        if self.check_level_up:
            level_up_points =  self.calculate_level_ups()
            self.level_ups(level_up_points)
            
    # キャラクターがアイテムを使う関数 Character.use_item(item) 
    def use_item(self, item, popped_index):
        item.use(self)
        self.item_bag.pop(popped_index)
    
    # キャラクターがアイテムを手に入れたときの関数
    def get_item(self, item):
        self.item_bag.append(item)
        item.x, item.y = None, None
        print(f"{self.name}は{item.name}を手に入れた")
        
# 敵キャラのクラス
class Enemy(Character):
    def __init__(self, name, base_hp, hp, attack_power, defense_power, x, y,
                 # Enemy専用引数
                 exp_points,
                 # ここまで
                 exp=0, level=1, level_up_table=2, item_bag=None,):
        super().__init__(name, base_hp, hp, attack_power, defense_power, x, y, exp, level, level_up_table, item_bag)
        self.exp_points = exp_points
        
                    
# アイテムのクラス
class Item:
    # アイテム名とその位置
    def __init__(self, name, x, y, value=0, effect=None, effect_points=0, effect_summary="特になし"):
        self.name = name
        self.x = x
        self.y = y
        self.value = value
        self.effect = effect
        self.effect_points = effect_points
        self.effect_summary = effect_summary
    
    # アイテムの座標を表示する関数    
    def show_position(self):
        print(f"{self.name}の現在地はx = {self.x}, y = {self.y}")

    # テスト用ステータスを閲覧する関数
    def show_status(self):
        print(
f'''
Name: {self.name}
x: {self.x}
y: {self.y}
value: {self.value}
effect: {self.effect}
effect_points: {self.effect_points}
effect_summary: {self.effect_summary}
''')
        
    # どんなeffectか確認して、そのeffectを作動させる関数
    def use(self, character):
        if self.effect == "recovery":
            self.recovery_by_method(character)
        
    # アイテムエフェクトがrecoveryだった場合の関数
    def recovery_by_method(self, character):
        character.hp += self.effect_points
        if character.hp >= character.BASE_HP:
            character.hp = character.BASE_HP
            print(f"{character.name}は{self.name}を使った、HPが全回復した")
        else:
            print(f"{character.name}は{self.name}を使った。HPが{self.effect_points}回復した")
    
    # 暗号を解読する関数
    def code_input(self, code_list, code_hint_massage="特になし"):
        print("このアイテムは施錠されていて、暗号を解読しないと手に入らない")

        while True:
            print(f"ヒント: {code_hint_massage}")
            user_input = input("暗号を入力してください")
            if user_input in code_list:
                print(f"暗号の解読に成功！{self.name}を手に入れた")
                return True
            
            else:
                print("暗号が間違っている")

# ゲームのメイン

chest = Item("伝説の宝", 5, 5, 10000)
potion = Item("ポーション", 0, -1, 500, "recovery", 5)
hi_potion = Item("ハイポーション", 0,-2, 1000, "recovery", 10)
player = Character("ゆうしゃ", 10, 10, 3, 3, 0, 0, item_bag=[])
monster = Enemy("ドラゴン", 8, 8, 2, 2, 3, 3, 15)

monster_list = [monster]
item_list = [potion, hi_potion, chest]

is_game_over = False

print(f'''ゲームの説明
ダンジョン内にある{chest.name}を手に入れることが出来ればゲームクリア
{chest.name}の座標はわかっているので確認しながらその場所を目指せ
ただし、ダンジョン内には{monster.name}がいるので、遭遇したら攻撃して追い払え
{monster.name}はHPが一定以下になると逃げる
もし{monster.name}にやられてしまった場合はゲームーオーバー
ゲームスタート
''')

while is_game_over is False:
    chest.show_position()
    player.show_position()
    monster.show_position()
    action_index = player.select_index(3, ["移動する", "アイテムバッグを開く", "ステータス確認"])
    if action_index == 1:
        player.move(
            player.select_index(4, ["上", "下", "右", "左"], True, "進む方向を選んでください")
            )
        monster.move(rand(1,4))
        for item in item_list:
            if player.check_encounter(monster):
                if player.battle(monster):
                    if player.check_encounter(item):
                        if item == chest:
                            if chest.code_input(["apple", "banana", "berry"], "有名な果物"):                    
                                print("ゲームクリア！おめでとう！！！")
                                is_game_over = True
                        elif item == potion:
                            player.get_item(potion)
                else:
                    print("ゲームオーバー")
                    is_game_over = True
                break
            elif player.check_encounter(item):
                if item == chest:
                    if chest.code_input(["apple", "banana", "berry"], "有名な果物"):                    
                        print("ゲームクリア！おめでとう！！！")
                        is_game_over = True
                elif item == potion:
                    player.get_item(potion)
    elif action_index == 2:
        player.open_item_bag()
    elif action_index == 3:
        player.show_status()
        