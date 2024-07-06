class Repositorio:
    
    def select(self, db_connection:any) -> None:
        connection = db_connection.conectar()
        print(f"Conectei ao {connection}.")
        print("Fazendo SELECT * FROM...")
        db_connection.desconectar()
        
    def insert(self, db_connection:any) -> None:
        connection = db_connection.conectar()
        print(f"Conectei ao {connection}.")
        print("Fazendo INSERT VALUES...")
        db_connection.desconectar()