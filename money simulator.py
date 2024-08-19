#Тут просто база - импорты, создание окошек, и так далее
import customtkinter as ctk 
from time import sleep

root = ctk.CTk()
root.title('Auth')
root.geometry('300x350')
root.resizable(height=False, width=False)

ctk.set_appearance_mode('system')

money = 0
money_alltime = 0
appending_amount = 1
price_click_upgrade = 200
experience_level = 0
xp_amount = 0
player_level = 0
player_rank = 'Homeless'

users = [
    {'username': 'admin', 'password': 'admin'},
    {'username': '123123', 'password': '123123'},
    {'username': 'user1', 'password': 'user1'},
]

#Функции для перекрашивания цветов кнопок, свитчей и так далее
def button_theme(widget):
    widget.configure(fg_color='#519686', hover_color='#2b5249')

def switch_theme(widget):
    widget.configure(fg_color='#63b886')

#Проверяет если в entry логина и пароля совпадает с теми, что есть в переменной users
def auth_check(username, password):
    global users
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

#Копирует значение из поле ввода окна логина, и отправляет данные в функцию auth_check, дальше она отправит True если пароль и логин правильный, и False если нет, и вход не произведется
def mainauth():
    global money
    global users
    global player_level
    global xp_amount
    global money_alltime
    global player_rank
    
    username = entry_login.get()
    password = entry_password.get()
    if auth_check(username, password):
        if username == 'admin':
            money = 999999999
            xp_amount = 999999
            player_level = 999
            money_alltime = 999999999
            player_rank = 'Touch some grass'
        if username == 'user1':
            money = 100
            xp_amount = 100
            player_level = 1
            money_alltime = 100
        sleep(0.3)
        new_window()
    else:
        label_login_failed = ctk.CTkLabel(master=frame_login, text='Wrong login or password', font=('lemon milk light', 10), text_color='red')
        label_login_failed.pack()

#Функция с самой игрой
def new_window():
    #Убирает окно с логином, и создает новое
    global money
    global money_alltime
    global appending_amount
    global label_money_counter
    global money_per_click_stat_label
    global experience_level
    global progressbar_level
    global xp_label
    global xp_amount
    global player_level
    global player_rank
    global rank_label
    
    root.destroy()
    newapp = ctk.CTk()
    newapp.title('Money making simulator')
    newapp.resizable(height=False, width=False)
    
    #Функция которая добавляет деньги в банк, и счетчик денег за всё время, и так же обновляет надпись с текущим счетом игрока 
    def add_money():
        global appending_amount
        global money
        global money_alltime
        global label_money_counter
        global money_per_click_stat_label
        global experience_level
        global progressbar_level
        global xp_label
        global xp_amount
        global player_level
        global player_rank
        global rank_label
        
        money += appending_amount
        money_alltime += appending_amount
        experience_level += 0.01
        xp_amount += 1
        progressbar_level.set(experience_level)
        
        if player_level >= 1:
            player_rank = 'Silver Homeless'
            rank_label.configure(text=f'Rank: {player_rank}')
            
        if player_level >= 5:
            player_rank = 'Gold Homeless'
            rank_label.configure(text=f'Rank: {player_rank}')
            
        if player_level >= 10:
            player_rank = 'Middle'
            rank_label.configure(text=f'Rank: {player_rank}')
            
        if player_level >= 15:
            player_rank = 'Silver Middle'
            rank_label.configure(text=f'Rank: {player_rank}')
        
        if player_level >= 20:
            player_rank = 'Gold Middle'
            rank_label.configure(text=f'Rank: {player_rank}')
        
        if player_level >= 25:
            player_rank = 'Rich'
            rank_label.configure(text=f'Rank: {player_rank}')    
        
        if player_level >= 30:
            player_rank = 'Silver Rich'
            rank_label.configure(text=f'Rank: {player_rank}')
            
        if player_level >= 35:
            player_rank = 'Gold Rich'
            rank_label.configure(text=f'Rank: {player_rank}')
        
        if player_level >= 40:
            player_rank = 'Diamond'
            rank_label.configure(text=f'Rank: {player_rank}')

        if player_level >= 50:
            player_rank = 'S Tier'
            rank_label.configure(text=f'Rank: {player_rank}')
            
        if player_level >= 100:
            player_rank = 'Touch Some Grass'
            rank_label.configure(text=f'Rank: {player_rank}')
            
        if player_level >= 150:
            player_rank = 'Pls Stop'
            rank_label.configure(text=f'Rank: {player_rank}')
        
        if experience_level >= 1:
            experience_level = 0
            player_level += 1
            level_label.configure(text=f'LVL: {player_level}')
            
        xp_label.configure(text=f'XP: {xp_amount}')
        label_money_counter.configure(text=f'{money}$')
        money_of_all_time_label.configure(text=f'Money made for all time: {money_alltime}$')
    
    #Фрейм с кнопкой сделать деньги
    frame_clicker = ctk.CTkFrame(master=newapp, corner_radius=30)
    frame_clicker.grid(row=2, column=1, pady=50, padx=50)
    
    rank_label = ctk.CTkLabel(master=frame_clicker, text=f'Rank: {player_rank}', font=('lemon milk light', 20))
    rank_label.pack(padx=20, pady=20)
    
    #Надпись с текущим счетом игрока
    label_money_counter = ctk.CTkLabel(master=frame_clicker, text=f'{money}$', font=('Lemon milk light', 40))
    label_money_counter.pack(pady=20)

    #Кнопка чтобы сделать деньги
    clicker_button = ctk.CTkButton(master=frame_clicker, text='Click here to make money', font=('Lemon milk light', 20), command=add_money, corner_radius=30, height=50)
    clicker_button.pack(anchor=ctk.CENTER, padx=20)
    button_theme(clicker_button)
    
    #Опыт игркоа (Или просто сколько раз игрок кликнул на кнопку)
    xp_label = ctk.CTkLabel(master=frame_clicker, text=f'XP: {xp_amount}', font=('lemon milk light', 20))
    xp_label.pack(pady=10, padx=30, anchor='w')
    
    #Прогрессбар до улучшения уровня игрока
    progressbar_level = ctk.CTkProgressBar(master=frame_clicker, progress_color='#519686')
    progressbar_level.pack(anchor='w', padx=30)
    progressbar_level.set(experience_level)

    #Отаброжение уровня игрока
    level_label = ctk.CTkLabel(master=frame_clicker, text=f'LVL: {player_level}', font=('lemon milk light', 20))
    level_label.pack(pady=10, padx=30, anchor='w')

    #Создание фрейма с статистикой игрока
    stats_frame = ctk.CTkFrame(master=newapp, corner_radius=30)
    stats_frame.grid(row=2, column=2, pady=50, padx=50)
    
    #Кнопка магазина
    shop_button = ctk.CTkButton(master=stats_frame, text='Upgrades Store', corner_radius=30, font=('Lemon milk light', 30), command=upgrade_store)
    shop_button.pack(pady=20)
    button_theme(shop_button)
    
    #Надпись "Stats:"
    stats_title_label = ctk.CTkLabel(master=stats_frame, text='Stats:', font=('Lemon milk light', 30))
    stats_title_label.pack(pady=20)
    
    #Сколько денег делается за один клик на кнопку
    money_per_click_stat_label = ctk.CTkLabel(master=stats_frame, text=f'Money per click: {appending_amount}$', font=('Lemon milk light', 20))
    money_per_click_stat_label.pack(padx=20, anchor='w')
    
    #Сколько денег было сделано за всё время не считая затраты
    money_of_all_time_label = ctk.CTkLabel(master=stats_frame, text=f'Money made for all time: {money_alltime}$', font=('Lemon milk light', 20))
    money_of_all_time_label.pack(anchor='w', pady=20, padx=20)
    
    newapp.mainloop()

#Магазин улучшений
def upgrade_store():
    global money
    global appending_amount
    global label_money_counter
    global money_per_click_stat_label
    
    store = ctk.CTk()
    store.title('store')
    store.resizable(height=False, width=False)
    
    #Проверка есть ли доастаточно денег для покупки улучшения клика, и если есть, то уменьшить её количество, а так же удвоить цену для следующей покупки дабл клика
    def buy_click__upgrade():
        global money
        global appending_amount
        global price_click_upgrade
        global label_money_counter
        global money_per_click_stat_label
        
        if money >= price_click_upgrade:
            money -= price_click_upgrade
            appending_amount *= 2
            price_click_upgrade *= 2
            price_button_click_upgrade.configure(text=f'{price_click_upgrade}$')
            label_money_counter.configure(text=f'{money}$')
            money_per_click_stat_label.configure(text=f'Money per click: {appending_amount}$')
        else:
            desc_label_click_upgrade.configure(text='Not enough money!', text_color='red')
    
    #Создание фрейма под улучшение клика
    frame_click_upgrade = ctk.CTkFrame(master=store, corner_radius=30)
    frame_click_upgrade.grid(row=2, column=1, pady=20, padx=20)
    
    #Название улучшения (Удвоение денег за один клик)
    title_label_click_upgrade = ctk.CTkLabel(master=frame_click_upgrade, text='DOUBLE CLICK!', font=('Lemon milk light', 30))
    title_label_click_upgrade.pack(anchor='n')
    
    #Описание улучшения (Удвоение денег за один клик)
    desc_label_click_upgrade = ctk.CTkLabel(master=frame_click_upgrade, text='Doubles your money income per click', font=('Lemon milk light', 20))
    desc_label_click_upgrade.pack(pady=10)
    
    #Просто надпись 'Buy Now:'
    buynow_label_click_upgrade = ctk.CTkLabel(master=frame_click_upgrade, text='Buy now:', font=('Lemon milk light', 30))
    buynow_label_click_upgrade.pack(padx=50,side='left', pady=10)
    
    #Кнопка для покупки улучшения (Удвоение денег за один клик)
    price_button_click_upgrade = ctk.CTkButton(master=frame_click_upgrade, text=f'{price_click_upgrade}$', corner_radius=30, height=40, font=('Lemon milk light', 20), command=buy_click__upgrade)
    price_button_click_upgrade.pack(side='right',padx=10, pady=10)
    button_theme(price_button_click_upgrade)
    
    store.mainloop()
    
#Создание декоративного фрейма для логина
frame_login = ctk.CTkFrame(root, width=40, height= 30, corner_radius=20)
frame_login.pack(pady=20, padx=30, fill='both')

#Надпись логин
login_label = ctk.CTkLabel(master=frame_login, text='Login', font=('Lemon milk light', 30))
login_label.pack(anchor='n', pady=30, expand=True)

#Поле для ввода логина
entry_login = ctk.CTkEntry(master=frame_login, placeholder_text='Enter your login', font=('lemon milk light', 10),height=20, width=200, )
entry_login.pack(padx=20)

#Поле для ввода пароля
entry_password = ctk.CTkEntry(master=frame_login, placeholder_text='Enter your password', font=('lemon milk light', 10), height=20, width=200, show='*')
entry_password.pack(padx=20, pady=10)

#Чекбокс если пользователь хочет, чтобы система запомнила устройство (Она не зопомнит)
checkbox_remind = ctk.CTkCheckBox(master=frame_login, text='Remember me', font=('lemon milk light', 10))
checkbox_remind.pack(pady=10)
switch_theme(checkbox_remind)

#Кнопка для для продолжения и проверки если пароль и логин верны
button_login = ctk.CTkButton(master=frame_login, text='Continue', height=40, width=150, font=('Lemon milk light', 15), corner_radius=30, command=mainauth)
button_login.pack(pady=20)
button_theme(button_login)

root.mainloop()