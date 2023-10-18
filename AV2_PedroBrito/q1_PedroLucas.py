Logins = {"Pedro":["senha1",50],"Saulo":["senha2",60]}

updateBalance = lambda amm,log,pas : Logins[log][1] if not Logins.update({log:[pas,Logins[log][1]+amm]}) else print("DEU RUIM")

deposit = lambda amm,log,pas : updateBalance(amm,log,pas)

withdraw = lambda amm,log,pas : updateBalance(-amm,log,pas) if amm <= Logins[log][1] else "Sem saldo"

escolha = lambda esc,log,pas: lambda amm: withdraw(amm,log,pas) if esc == "Withdraw" else deposit(amm,log,pas) if esc == "Deposit" else print("ERROR")

banco = lambda log,pas: lambda esc:escolha(esc,log,pas) if log in Logins.keys() and pas == Logins[log][0] else print("Login Failed")

banco("Pedro","senha1")("Deposit")(20)
banco("Pedro","senha1")("Withdraw")(50)
print(banco("Pedro","senha1")("Deposit")(33))



