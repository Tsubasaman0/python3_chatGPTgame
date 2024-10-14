# 次にレベルアップするまでの経験値を、今まで取得した経験値から計算
def get_next_level_exp(exp, table):
    level = 0
    level_up_table_exp_sum = 0
    
    while True:
        level +=1
        level_up_table_exp_sum += (table ** level)
        print(level_up_table_exp_sum)
        if exp < level_up_table_exp_sum:    
            next_level_exp = level_up_table_exp_sum - exp
            return next_level_exp, level+1

def get_next_level_exp_level_fixd(level, table, exp):
    level_up_table_exp_sum = 0
    for n in range(level):
        level_up_table_exp_sum += table ** n
    get_next_level_exp = exp - level_up_table_exp_sum
    return get_next_level_exp
# 上の関数が正しいかどうかを判断するために別の計算方法から、値が一致するか確認

# 取得経験値がtable**n(1から条件を満たすまで)を超えるまで計算して、超えた分を残り経験値として返す関数
def get_next_level_exp_new(table, exp):
    level_up_table_exp_sum = 0
    temp_level = 0
    while True:
        temp_level += 1
        level_up_table_exp_sum += table ** temp_level
        if exp < level_up_table_exp_sum:
            next_level_exp = abs(exp - level_up_table_exp_sum)
            return next_level_exp, temp_level
        
# 決められたレベル分ループして、レベルごとに必要経験値、残り経験値を表示させる関数
def show_level_exp_table_and_next_level_exp(table, exp, level):
    level_up_table_exp_sum = 0
    print(f"総取得経験値 {exp} の場合")
    for i in range(1, level):
        level_up_table_exp_sum += table ** i
        next_level_exp = exp - level_up_table_exp_sum
        table_message = f'''
Lv {i+1} までに 必要EXP {table ** i} : 合計必要EXP {level_up_table_exp_sum} : 繰り越しEXP {next_level_exp}'''
        if level_up_table_exp_sum > exp:
            print(table_message)
            print("総取得経験値とレベルが合わないので強制終了")
            break
        else:
            print(table_message)
        
    if next_level_exp > 0:
        print(f"経験値が{next_level_exp}余ってます")
        return
    
    print(f'''
{exp} EXPでLv1から Lv {i} レベルまで上がり、次の Lv {i+1} まで {abs(next_level_exp) } EXP 必要です''')    
    
    
print(get_next_level_exp_new(2, 1000))
show_level_exp_table_and_next_level_exp(2, 1000, 20)
    
        


# 1 2
# 2 4
# 3 8
# 4 16  15get - (2+4+8) = 15残り