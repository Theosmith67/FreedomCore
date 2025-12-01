from core.wise_men.malachi import Malachi

keeper = Malachi()
result = keeper.execute({'type': 'balance_check'})
print(result)
