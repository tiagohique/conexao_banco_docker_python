import mysql.connector

# Configurações de conexão com o banco de dados
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost'
}

try:
    # Estabelece a conexão com o banco de dados
    connection = mysql.connector.connect(**config)
    print("Conectado ao banco local do tiago")
    
    # Faça qualquer operação desejada com o banco de dados aqui
    
    # Encerra a conexão
    connection.close()

except mysql.connector.Error as error:
    print("Erro ao conectar ao banco de dados: {}".format(error))
