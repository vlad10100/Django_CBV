


import forex_journal

i = 'Yy'
while i in 'Yy':
    print('___________________________________')
    print('[A] ADD TRADE')
    print('[B] VIEW TRADES')
    print('[C] EDIT TRADES')
    print('[D] BALANCE')
    print('[E] DEPOSIT')
    print('[F] WITHDRAW')
    print('[X] CLOSE\n')

    select = input('[A][B][C][D][E][X]:  ')
    print('')
    trade = forex_journal.Forex(select)
    print(trade.selection())
    trade.add_trade()
    trade.edit_trades()
    trade.view_trades()
    trade.deposit()
    trade.balance()
    trade.withdraw()
 

    

