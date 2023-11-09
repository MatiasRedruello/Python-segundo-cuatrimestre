import sqlite3
PATH = f"./SEMANA 10/Practica sqlite/"
# Creo la tabla 
def crear_base_datos_sql(path:str,nombre_archivo:str,categorias:list[str])->None:
    """
    Parametros: Path-> Ruta del archivo.
                Nombre del archivo -> Como voy a llamr al archivo.
                Categorias -> lista que contiene los nombres de las categorias
    Funcion: Crea una base de datos.
    Retorna: None
    """
    
    with  sqlite3.connect(f"{path}{nombre_archivo}") as conexion:
        
        try:
            # Se puede pasar los datos de la tabla y armar distintas?
            # Se pasa como diccionarios de str?
            # Video pasaron los datos con el tipo de dato. En que cabia si los paso o no?
            sentencia = f""" create table personajes
                            {categorias[0],
                             categorias[1],
                             categorias[2],
                             categorias[3],
                             categorias[4],
                             categorias[5],
                             categorias[6]}
                            """  
            conexion.execute(sentencia)
            print("Se creo la tabla")
        except:
            print("La tabla ya existe")

# inserto datos
def insertar_tabla_sql(path:str,nombre_archivo:str)->None:
    """
    Parametros: Path-> Ruta del archivo.
                Nombre del archivo -> Como voy a llamr al archivo.
    Funcion: Inserta una tabla
    Retorna: None
    """
    with sqlite3.connect(f"{path}{nombre_archivo}") as conexion:
        try:
            # Se puede pasar por parametros datos nuevos?
            # Se pasan como  listas? tuplas? diccionarios? Se puede pasar directamente?
            conexion.execute("""insert into personajes(nombre,apellido,direccion,altura,cp)
                            values(?,?,?,?,?)""",("Matias","Redruello","Fonrouge","100","1234"))
            conexion.execute("""insert into personajes(nombre,apellido,direccion,altura,cp)
                             values(?,?,?,?,?)""",("Pedro","Perez","chile","1239","1425"))      
            print("Se agregaron datos")         
        except:
            print("Error")

def recuperar_filas_tabla_sql(path:str,nombre_archivo:str)->iter:
    """
    Parametros: Path-> Ruta del archivo.
                Nombre del archivo -> Como voy a llamr al archivo.
    Funcion: Recupera las filas de la tabla.
    Retorna: Iterable
    """    
    with sqlite3.connect(f"{path}{nombre_archivo}")as conexion:
        # cursor que devuelve? un iterable?
        cursor = conexion.execute("SELECT * FROM personajes")
    return cursor

def recuperar_filas_tabla_sql_id(path:str,nombre_archivo:str,id:int)->iter:
    """
    Parametros: Path-> Ruta del archivo.
                Nombre del archivo -> Como voy a llamr al archivo.
                Id -> identificacion unica de la fila
    Funcion: Recupera las filas de la tabla usando id.
    Retorna: Iterable
    """    
    with sqlite3.connect(f"{path}{nombre_archivo}") as conexion:
        # cursor que devuelve? un iterable?
        sentencia = "SELECT * FROM personajes WHERE id=?"
        cursor = conexion.execute(sentencia,(id,))
    return cursor

def actualizar_fila_tabla_sql(path:str,nombre_archivo:str,id:int)->iter:
    """
    Parametros: Path-> Ruta del archivo.
                Nombre del archivo -> Como voy a llamr al archivo.
                Id -> identificacion unica de la fila
    Funcion: Recupera las filas de la tabla usando id.
    Retorna: Iterable
    """  
    # Se podra actualizar varios datos?
    with sqlite3.connect(f"{path}{nombre_archivo}") as conexion:
        sentencia = "UPDATE personajes SET nombre = 'Thor' WHERE id=?"
        cursor = conexion.execute(sentencia,(id,))
        filas = cursor.fetchall() # mirar esto
    return filas

def borrar_fila_tabla_sql(path:str,nombre_archivo:str,id:int)->None:
    """
    Parametros: Path-> Ruta del archivo.
                Nombre del archivo -> Como voy a llamr al archivo.
                Id -> identificacion unica de la fila
    Funcion: Borra la  filas de la tabla usando id.
    Retorna: Iterable
    """    
    with sqlite3.connect(f"{path}{nombre_archivo}") as conexion:
        sentencia = "DELETE FROM personajes WHERE id=?"
        cursor = conexion.execute(sentencia,(id,))

if __name__=="__main__":
    #crear_base_datos_sql(PATH,"practica_sqlite.db")

    #insertar_tabla_sql(PATH,"practica_sqlite.db")

    #filas_tabla = recuperar_filas_tabla_sql(PATH,"practica_sqlite.db")

    #filas_tabla_id = recuperar_filas_tabla_sql_id(PATH,"practica_sqlite.db","2")
    #for fila in filas_tabla_id:
        #print(fila)# fila es del tipo tupla

    #actualizar_fila_tabla_sql(PATH,"practica_sqlite.db",1)

    #borrar_fila_tabla_sql(PATH,"practica_sqlite.db",4)
    
    # probando crear base de datos pasando una lista
    lista_practica_base = ("id integer primary key autoincrement",
                           "nombre",
                           "apellido",
                           "direccion",
                           "altura",
                           "cp",
                           "personas")
    crear_base_datos_sql(PATH,"practica_sqlite_dos.db",lista_practica_base)