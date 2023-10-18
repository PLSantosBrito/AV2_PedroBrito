import mysql.connector

# Alterar baseado na conexão 
mydb = mysql.connector.connect(
    host="localhost",
    user="ProgFunc",
    password="q4Ped",
)

cursor = mydb.cursor()

execSQLcmd = lambda cmd: cursor.execute(cmd)
printLista = lambda l : [print(x) for x in l]

createTable = lambda table, attrs : execSQLcmd("CREATE TABLE IF NOT EXISTS " + table + " (" + attrs + ");\n")
createDB = lambda dbname : execSQLcmd("CREATE DATABASE IF NOT EXISTS " + dbname + ";\n")
useDB = lambda dbname : execSQLcmd("USE " + dbname + ";\n")
dropDB = lambda dbname : execSQLcmd("DROP DATABASE " + dbname + ";\n")
dropTable = lambda dbname : execSQLcmd("DROP TABLE " + dbname + ";\n")
select = lambda attrs, table, wherecond : execSQLcmd("SELECT " + attrs + " FROM " + table + " WHERE " + wherecond + ";\n")
delete = lambda table, columnName, value : execSQLcmd("DELETE FROM " + table + " WHERE " + columnName + " = " + value + " OR " + columnName + " IS NULL;\n")
insert = lambda table, attrs, values : execSQLcmd("INSERT INTO " + table + " (" + attrs + ")" + " VALUES (" + values + ");\n")
update = lambda table, columnName, newValue, id : execSQLcmd("UPDATE " + table + "\n" + "SET " + columnName + " = " + newValue + "\n" + "WHERE id = " + str(id))

createDB("mydb")
useDB("mydb")

createTable("usuarios", "id INT , name VARCHAR (255) , console VARCHAR (45)")
createTable("jogos", "id INT , name VARCHAR (255), lancamento DATE")


#Usuario
insert("usuarios", "id, name, console", "1, 'PedroLucas' , 'PlayStation'")

insert("usuarios", "id, name, console", "2, 'IgorSantos' , 'Switch'")

insert("usuarios", "id, name, console", "2, 'Gilberto' , 'Xbox'")

#Jogos
insert("jogos", "id, name, lancamento", "1, 'Dave The Diver', '2022-10-27'")

insert("jogos", "id, name, lancamento", "2, 'Minecraft', '2011-11-18'")

insert("jogos", "id, name, lancamento", "3, 'Horizon: Zero Dawn', '2011-02-28'")

insert("jogos", "id, name, lancamento", "4, 'The Legend of Zelda: Ocarina of Time', '1998-11-21'")

#delete("usuarios", "name", "'IgorSantos'")
#delete("jogos", "name", "'Minecraft'")

#update("usuarios", "console", "'Nintendo Switch'", 2)
#update("jogos", "id", "10", 2)

select("*", "usuarios", "TRUE")
listaDB = cursor.fetchall()
print("\n\nTabela de Usuarios: ")
printLista(listaDB)

select("*", "jogos", "TRUE")
listaDB = cursor.fetchall()
print("\n\nTabela de Jogos:")
printLista(listaDB)

dropTable("usuarios")
dropDB("mydb")