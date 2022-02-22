open_list = list()
closed_list = list()
balance_list = [0]


class Forex:
    def __init__(self, select):
       self.select = select

    def selection(self):
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'X']:
            if self.select.upper() == 'A':
                return 'ADD TRADE\n'
            elif self.select.upper() == 'B':
                return 'VIEW TRADES\n'
            elif self.select.upper() == 'C':
                return 'EDIT TRADES\n'
            elif self.select.upper() == 'D':
                return 'BALANCE\n'
            elif self.select.upper() == 'E':
                return 'DEPOSIT\n'
            elif self.select.upper() == 'F':
                return 'WITHDRAW\n'
            elif self.select.upper() == 'X':
                return exit()
            else:
                return '*****INVALID INPUT*****'




    def check_input_major(self, check_input):
        check_input = (f"{(check_input)[:6]}")
        list_input = list(check_input)

        count = 0
        for i in list_input:
            count += 1
            if count == len(list_input) and count !=6:
                list_input.append('0')
        

        dot_count = 0
        for i in list_input:
            if i.isdigit() == False and i != '.':
                return False

            elif i == '.':
                dot_count += 1
                if dot_count == 2:
                    return False
        output = ''
        for i in list_input:
            output +=i

        return output

    

        
    def add_trade(self):
        self.selection()
        if self.selection() == 'ADD TRADE\n':
            trade_name = input('Trade Name: ')
            pair = input('Enter Currency Pair: ')
            position = input('LONG or SHORT: ')
            entry = input('Entry Price: ')
            take_profit = input('Take Profit: ')
            stop_loss = input('Stop Loss: ')
            lot_size = input('Lot Size: ')


            
            if 'usd' in pair.lower():
                entry_check = self.check_input_major(entry)
                entry = entry_check
                tp_check = self.check_input_major(take_profit)
                take_profit = tp_check
                sl_check = self.check_input_major(stop_loss)
                stop_loss = sl_check
                if entry_check == False or tp_check == False or sl_check == False:
                    return
                        
            true_buy = bool(float(entry) < float(take_profit))
            true_sell = bool(float(entry) > float(take_profit))
            true_long = bool(float(take_profit) > float(stop_loss))
            true_short = bool(float(take_profit)< float(stop_loss))
  

            if position.upper() == 'LONG':
                if true_buy == False:
                    return False
                elif true_long == False:
                    return False
            else:
                if true_sell == False:
                    return False
                elif true_short == False:
                    return False


            try:
                win = (int((take_profit)[2:6] )- int((entry)[2:6])) * float(lot_size)
                win = round(abs(win * 10), 3)
                loss = (int((entry)[2:6]) - int((stop_loss)[2:6])) * float(lot_size)
                loss = round(abs(loss * 10), 3)
                risk_reward = win/loss
            except:
                return False
                
            print(f"Potential Gain: {win}")
            print(f"Potential Loss: {loss}")
            print(f"Risk Reward Ratio is   1 : {risk_reward}")

            input_list = {'POSITION': position.upper(), 'ENTRY': entry,
            'TAKE PROFIT': take_profit, 'STOP LOSS': stop_loss, 
            'LOT SIZE': lot_size, 'GAIN': win, 'LOSS': loss}
            ledger = {trade_name : input_list}
            open_list.append(ledger)
            


    def view_trades(self):
        self.selection()
        if self.selection() == 'VIEW TRADES\n':
            print('*****************************')
            print('[A] OPEN TRADES')
            print('[B] CLOSED TRADES')
            show_trades = input('Display: ')
            if show_trades in 'Aa':
                print('\n*****************************')
                print('********OPEN TRADES********')
                print(self.open_trades())
            elif show_trades in 'Bb':
                print('\n*****************************')
                print('********CLOSED TRADES********')
                print(self.closed_trades())
            else:
                return
            

    def edit_trades(self):
        self.selection()
        if self.selection() == 'EDIT TRADES\n':
            search = input('Search Trade: ')
            try:
                for item in open_list:
                    search = item[search]
                    pos = open_list.index(item)
                    outcome = input('WIN or LOSS: ')
                    if outcome in 'Ww':
                        print(f"WIN: {search['GAIN']}")
                        balance_list.append(search['GAIN'])
                        closed_list.append(open_list.pop(pos))
                        
                    elif outcome in 'Ll':
                        print(f"LOSS: {search['LOSS']}") 
                        balance_list.append(-(search['LOSS']))
                        closed_list.append(open_list.pop(pos))
                        
                    else:
                        return
            except KeyError:
                print('Not Found')
                return




    def closed_trades(self):
        closed_output = ''
        for item in closed_list:
            for key, value in item.items():
                closed_output += '\n' + key + '\n'
                for k, v in value.items():
                    closed_output += f"{k} \t {v}\n"
        return closed_output





    def open_trades(self):
        open_output = ''
        for item in open_list:
            for key, value in item.items():
                open_output += '\n' + key + '\n'
                for k, v in value.items():
                    open_output += f"{k} \t {v}\n"
        return open_output
        
     

    def balance(self):
        self.selection()
        total = sum(balance_list)
        if self.selection() == 'BALANCE\n':
            print(total)





    def deposit(self):
        self.selection()
        if self.selection() == 'DEPOSIT\n':
            amount = input('Enter AMOUNT: ')
            balance_list.append(int(amount))


    def withdraw(self):
        self.selection()
        if self.selection() == 'WITHDRAW\n':
            amount = input('Enter AMOUNT: ')
            if sum(balance_list) >= int(amount):
                balance_list.append(int(amount)*(-1))
            else:
                print('Cannot Withdraw')
