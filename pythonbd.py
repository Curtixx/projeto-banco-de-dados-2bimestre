import mysql.connector
from mysql.connector import Error
cont = int()
try:
    connection = mysql.connector.connect(host='localhost',
                                            database='Greenpeace',
                                            user='root',
                                            password='')
    while True:
        if cont == 2:
            break
        desejo = input('deseja iniciar o programa: (S/N)\n').strip().upper()
        while desejo != 'S' and desejo != 'N':
            desejo = input('digite apenas S/N: \n').strip().upper()
        if desejo == 'N':
            print('programa finalizado!!!')
            break
        else:
            nome = input('digite seu nome: \n').strip()
            while nome.isalpha() == False:
                nome = input('digite um nome valido: \n').strip()
            ano = int(input('digite o ano: \n'))
            while ano >=2021:
                ano = int(input('digite um ano valido: \n'))
            mes = int(input('digite o mes: \n'))
            while mes >12:
                mes = int(input('digite um mes valido: \n'))
            dia = int(input('digite o dia: \n'))
            while dia >31:
                dia = int(input('digite um dia valido'))
            derretimento = input('digite o derretimento semestral de toneladas: \n').strip()
            while derretimento.isnumeric() == False:
                derretimento = input('digite um valor valido: \n').strip()
            nivelmar = input('digite a elevação do nivel do mar (use milímetros): \n').strip()
            while nivelmar.isnumeric() == False:
                nivelmar = input('digite um valor valido: \n').strip()

            inset = f"""INSERT INTO Usuario
                        VALUES ('{nome}','{ano}/{mes}/{dia}','{derretimento}','{nivelmar}')"""

            cursor = connection.cursor()
            cursor.execute(inset)
            connection.commit()
            print(cursor.rowcount, "Inserido com sucesso")
            cursor.close()
            cont +=1

except Error as e:
    print("Erro na conexão", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexão fechada")