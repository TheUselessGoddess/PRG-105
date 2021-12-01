import tkinter
import tkinter.messagebox
import random
import pickle
from functools import partial
#Max Heals

class Game:
    def __init__(self, master):
        self.repeat = 0
        self.current_enemy = 'Normal'
        self.current_player = ''
        try:
            file = open('customer_file.dat', 'rb')
            pb = pickle.load(file)
            data = pb
        except:
            self.data = {'Player 1': {'Strength': 1, 'Vitality': 1, 'Agility': 1, 'HP': 20, 'Max HP': 20, 'Boss Kills': 0, 'Basic Kills': 0, 'Level': 1, 'Weapon': 'Basic Sword'}}
        #Window Related Stuff
        self.master = master
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)
        self.prompt_label = tkinter.Label(self.top_frame, text = 'Have you played before? If yes then please enter the name you used. If not, then please enter your desired name.')
        self.name_entry = tkinter.Entry(self.top_frame, width = 10)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.master.destroy)
        self.continue_button = tkinter.Button(self.bottom_frame, text = 'Continue', command = self.character_setup)

        self.name_entry.pack(side = 'bottom')
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.continue_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')
        self.prompt_label.pack(side = 'top')



    def stat_explanation(self):
        value = ''
        if value == 'Strength':
            print('Strength is your raw power. The higher your strength the more damage you deal and the higher block chance you get.')
        elif value == 'Vitality':
            print('Vitality is your overall health. The higher your vitality the greater your overall hp.')
        elif value == 'Agility':
            print('Agility is your physical speed. The higher your agility the greater your dodge chance.')

    def save(self, data):
        output_file = open('characters.dat', 'wb')
        pickle.dump(data, output_file)
        output_file.close()

    def character_setup(self):
        name = str(self.name_entry.get())
        if name in self.data.keys():
            self.current_player = name
            _ = Fight(self.master, self.current_player, self.data, self.current_enemy)
        else:
            self.current_player = name
            self.data[name] = self.data['Player 1']
            _ = Fight(self.master, self.current_player, self.data, self.current_enemy)

class Fight:
    def __init__(self, master, player, data, enemy):
        self.look = tkinter.Toplevel(master)
        self.charge_attack = 0
        self.enemy_hp = 20
        self.data = data
        self.player = player
        self.enemy = enemy
        self.look.title('Combat Menu')
        self.top_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)
        #Labels
        self.player_hp_label = tkinter.Label(self.top_frame, text = 'Player HP: ' + str(data[player]['HP']))
        self.enemy_hp_label = tkinter.Label(self.top_frame, text = '')
        if enemy == 'Normal':
            self.enemy_hp_label.config(text = 'Enemy HP: ' + str(data[player]['Level'] * 1.5 + 10))
            self.enemy_hp = data[player]['Level'] * 1.5 + 10
        elif enemy == 'Boss':
            self.enemy_hp_label.config(text = 'Enemy HP: ' + str(data[player]['Level'] * 2 + 15))
        #Buttons
        self.attack_button = tkinter.Button(self.bottom_frame, text = 'Attack', command = partial(self.turn_outputs, enemy, player, 2, data, master))
        self.heal_button = tkinter.Button(self.bottom_frame, text = 'Heal', command = partial(self.turn_outputs, enemy, player, 1, data, master))
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.look.destroy)
        self.show_stats = tkinter.Button(self.bottom_frame, text = 'Show Stats', command = partial(self.stats_function, master, data, player))

        self.attack_button.pack(side = 'left')
        self.heal_button.pack(side = 'right')
        self.show_stats.pack()
        self.quit_button.pack(side = 'bottom')
        self.bottom_frame.pack()
        self.top_frame.pack()
        self.enemy_hp_label.pack()
        self.player_hp_label.pack()

    def turn_outputs(self, enemy, player, selection, data, master):
        choice = 0
        response = ''
        damage = ''
        enemy_damage = 0
        check = [0, 0]
        response2 = ''
        if enemy == 'Normal':
            choice = random.randint(1, 5)
        elif enemy == 'Boss' and self.charge_attack != 1:
            choice = random.randint(1, 6)
        if 0 < choice < 4:
            enemy_damage = 2
            response2 = 'normal attack for 2 damage.'
        elif 3 < choice < 6:
            enemy_damage = 5
            response2 = 'strong attack for 5 damage.'
        elif choice == 6 and self.charge_attack == 1:
            enemy_damage = 10
        if selection == 1:
            response = 'healed.'
            data[player]['HP'] = data[player]['Max HP']
            damage = 0
            if check[0] != 1 and check[1] != 1:
                if choice != 7:
                    tkinter.messagebox.showinfo('Response', 'You ' + response + ' damage.' + ' \nThe enemy did a ' + response2)
                else:
                    tkinter.messagebox.showinfo('Response', 'You ' + response + ' \nThe enemy is charging up a big attack.')
                data[player]['HP'] -= enemy_damage
                self.player_hp_label.config(text = 'Player HP: ' + str(data[player]['HP']))
        else:
            if data[player]['Weapon'] == 'Basic Sword':
                damage = data[player]['Strength'] + 2
            elif data[player]['Weapon'] == 'Apprentice Sword':
                damage = data[player]['Strength'] + 4
            elif data[player]['Weapon'] == 'Intermediate Sword':
                damage = data[player]['Strength'] + 6
            elif data[player]['Weapon'] == 'Advanced Sword':
                damage = data[player]['Strength'] + 8
            elif data[player]['Weapon'] == 'Master Sword':
                damage = data[player]['Strength'] + 10
            response = 'attacked and did ' + str(damage)
            data[player]['HP'] -= enemy_damage
            if data[player]['HP'] <= 0:
                check[0] = 1
            if int(self.enemy_hp - damage) <= 0:
                check[1] = 1
            if check[0] != 1 and check[1] != 1:
                if choice != 7:
                    tkinter.messagebox.showinfo('Response', 'You ' + response + ' \nThe enemy did a ' + response2)
                else:
                    tkinter.messagebox.showinfo('Response', 'You ' + response + ' \nThe enemy is charging up a big attack.')
                self.enemy_hp -= damage
                self.player_hp_label.config(text = 'Player HP: ' + str(data[player]['HP']))
                self.enemy_hp_label.config(text = 'Enemy HP: ' + str(self.enemy_hp))

            elif check[0] == 1:
                enemyResults = ''
                if self.enemy == 1:
                    if choice == 1:
                        enemyResults = 'normal enemy with a basic attack.'
                    else:
                        enemyResults = 'normal enemy with a strong attack.'
                else:
                    tkinter.messagebox.showinfo('Response', 'You have died. You were killed by a ' + enemyResults)
                    data[player]['HP'] = data[player]['Max HP']
                    self.enemy_hp = data[player]['Level'] * 2 + 15
                    self.look.destroy()
            elif check [1] == 1:
                if self.enemy == 'Normal':
                    data[player]['Basic Kills'] += 1
                    self.level_up(data, player, master)
                    tkinter.messagebox.showinfo('Response', 'You killed a normal enemy.\nCurrent Total Kills: ' + str(data[player]['Basic Kills']))
                    data[player]['HP'] = data[player]['Max HP']
                    self.enemy_hp = data[player]['Level'] * 1.5 + 10
                    self.look.destroy()
                else:
                    data[player]['Boss Kills'] += 1
                    self.level_up(data, player, master)
                    tkinter.messagebox.showinfo('Response', 'You killed a boss enemy.')
                    data[player]['HP'] = data[player]['Max HP']
                    self.enemy_hp = data[player]['Level'] * 2 + 15
                    self.look.destroy()
        self.save(data)

    def level_up(self, data, player, master):
        count = 0
        while count == 0:
            if data[player]['Basic Kills'] > 2.5 * data[player]['Level'] or data[player]['Boss Kills'] > 1.2 * data[player]['Level']:
                data[player]['Level'] += 1
            else:
                count = 1
        if data[player]['Level'] == 5:
            data[player]['Weapon'] = 'Apprentice Sword'
        elif data[player]['Level'] == 10:
            data[player]['Weapon'] = 'Intermediate Sword'
        elif data[player]['Level'] == 15:
            data[player]['Weapon'] = 'Advanced Sword'
        elif data[player]['Level'] == 20:
            data[player]['Weapon'] = 'Master Sword'
        if count == 1:
            self.level = tkinter.Toplevel(master)
            self.top_frame2 = tkinter.Frame(self.level)
            self.bottom_frame2 = tkinter.Frame(self.level)
            self.stat_label = tkinter.Label('Enter the stat you would like to increase: Vitality, Strength, or Dexterity')
            self.stat_entry = tkinter.Entry(width = 10)
            self.stat_button = tkinter.Button(self.bottom_frame2, text = 'Confirm Stat', command = partial(self.choose_stat, data, player))
        
            self.stat_label.pack()
            self.top_frame2.pack()
            self.bottom_frame2.pack()
            self.stat_entry.pack()
        self.save(data)

    def choose_stat(self, data, player):
        choice = str(self.stat_entry.get())
        if choice.lower() == 'strength':
            data[player]['Strength'] += 1
        elif choice.lower() == 'vitality':
            data[player]['Vitality'] += 1
            data[player]['Max HP'] += 3
        elif choice.lower() == 'dexterity':
            data[player]["Dexterity"] += 1

    def save(self, data):
        output_file = open('characters.dat', 'wb')
        pickle.dump(data, output_file)
        output_file.close()

    def stats_function(self, master, data, player):
        self.stats = tkinter.Toplevel(master)
        self.kills_label = tkinter.Label(self.stats, text = 'You have killed: ' + str(data[player]['Basic Kills']) + ' normal enemies, and ' + str(data[player]['Boss Kills']) + ' boss enemies.')
        self.quit_button2 = tkinter.Button(self.stats, text = 'Quit', command = self.stats.destroy)
        self.kills_label.pack()
        self.quit_button2.pack()
def main():
    root = tkinter.Tk()
    _ = Game(root)
    root.mainloop()

main()
