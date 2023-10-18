path = "C:\\Users\\ogarf\\Desktop\\Faculdade\\AV2_PedroBrito\\q2_PedroLucas\\Logs.txt"

f = open(path,"r")
w = open(path,"a")
divide = lambda line: line.split(",")
dicLog = {divide(line)[0]:divide(line)[1] for line in f}

Login = lambda log,pas: print("SUCESSO") if log in dicLog and pas+"\n" == dicLog[log] else print("FRACASSO")

Register = lambda log,pas: w.write(log+","+pas+"\n")

Register("Samuel","senha4")
Login("Samuel","senha4")


