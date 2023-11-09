from Funciones_RegEx import * 
import random
test_strings = [
    "UELLO",    
    "Hello",    
    "",         
    "uORLD123", 
    "   ",
    "Educacion",      
    "ABCDEF",
    "UBCDE ABCD",
    "ABECE abvcd",
    "asdf ACVB",
    "hola",
    "hola mundo",
    "1234",
    "U123 123",
    "Hola como estas MUNDO?",
    "123.123",
    "3,123",
    "45..56",
    "0,465",
    "0001",
    "1010",
    "10100010u",
    "tres",
    "un.a",
    "cancion",

]
palabra_aleatoria = random.choice(test_strings)

texto = """La tecnología de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización de procesos han permitido 
la optimización de los recursos y la mejora en la eficiencia de los sistemas. La cibernética, la robótica y la inteligencia artificial son algunas de las áreas 
de la informática que se han desarrollado en las últimas décadas y han transformado la forma en que vivimos y trabajamos. La interconexión de dispositivos y la 
transmisión de datos en tiempo real han permitido la creación de nuevas industrias y modelos de negocio que antes eran impensables. La educación, la salud, 
el transporte y la logística son algunos de los sectores que han sido beneficiados por la innovación tecnológica. En conclusión, la tecnología ha generado una 
revolución en nuestra sociedad que ha llevado a la transformación y evolución de la misma."""

texto_dos = """La vida es hermosa. A veces, nos enfrentamos a desafíos inesperados. Pero no debemos rendirnos ante ellos. Debemos luchar por nuestros sueños y metas.
La perseverancia nos lleva lejos. ¡Nunca subestimes tu propia fuerza! ¿Estás listo para enfrentar el mundo? ¡Adelante, sé valiente y conquista tus miedos!"""
"""
re.search(): esta función se utiliza para buscar un patrón de expresión regular en una cadena de texto. Devuelve un objeto Match si encuentra una coincidencia, 
o None si no encuentra ninguna.

re.match(): esta función es similar a re.search(), pero sólo busca coincidencias al principio de la cadena de texto. Si no hay coincidencias al 
principio de la cadena, devuelve None.

re.findall(): esta función busca todas las coincidencias de un patrón de expresión regular en una cadena de texto y devuelve una lista con todas las 
coincidencias encontradas.

re.sub(): esta función se utiliza para buscar un patrón de expresión regular en una cadena de texto y reemplazarlo por otra cadena. Devuelve una nueva cadena de 
texto con todas las coincidencias reemplazadas.

re.split(): esta función se utiliza para dividir una cadena de texto en una lista de subcadenas, utilizando un patrón de expresión regular como delimitador.

GUIA EJERCICIOS BASICOS CON EXPRESIONES REGULARES

1)Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de que  todas las letras sean mayúsculas o False en el caso contrario
"""
# print(palabra_aleatoria,es_mayuscula(palabra_aleatoria))

"PARA LA FUNCION CON DESEMPAQUETADO"
# print(es_mayuscula(texto_1="HELLO",
#                     texto_2="Hello",
#                     texto_3="",
#                     texto_4="WORLD123",
#                     texto_5="   ",
#                     texto_6="ABCDEF",
#                     texto_7="ABCDE ABCD",
#                     texto_8="ABECE abvcd",
#                     texto_9="asdf ACVB"))

"""
2)Crear una función llamada es_minuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario
"""
# print(palabra_aleatoria,es_minuscula(palabra_aleatoria))

"""
3)Crear una función llamada es_entero que reciba un string y devuelva True en caso de que se trate de un número entero y False en caso contrario.
"""
# print(palabra_aleatoria,es_entero(palabra_aleatoria))

"""
4)Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario
"""
# print(palabra_aleatoria,es_solo_texto(palabra_aleatoria))
"""
5)Crear una función llamada es_decimal que reciba dos strings: el primero representa la expresión a evaluar y el segundo el separador decimal (puede ser punto . o coma ,).
Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.
"""
# print(palabra_aleatoria,es_decimal(palabra_aleatoria,"."))
"""
6)Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales) 
"""
# print(palabra_aleatoria,es_alfanumerico(palabra_aleatoria))
"""
7)Crear una función llamada es_binario que devuelva True en caso de un número binario válido (solo ceros y unos) o False en el caso contrario
"""
# print(palabra_aleatoria,es_binario(palabra_aleatoria))
"""
8)Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras  que comienzan con la letra ‘U’
"""
# print(crear_lista_palabras_con_u(test_strings))
"""
9)Crear una función que reciba un texto y devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo
"""
# print(crear_lista_largo_palabra(test_strings))
"""
10)Crear una función que reciba un texto y devuelva una lista de todas las palabras que terminan con ‘ción’. Ejemplo de texto: https://onlinegdb.com/swyremkF6
"""
# print(crear_lista_palabras_terminadas_cion(texto))
"""
11)Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que comienzan con una vocal
"""
# print(crear_lista_palabras_inicia_vocal(texto))
"""
12)Crear una función llamada obtener_oraciones que reciba como parámetro un string y que devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’).
Ejemplo de texto: https://onlinegdb.com/UMdr3hI3G
"""
# print(obtener_oraciones(texto_dos))
"""
13)Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía que no cumplan con la regla ortográfica que indica que antes de V 
se escribe N y que antes de B se escribe M. 
Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura."
La función debería devolver:
“Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar en esta nueva aventura."
"""
# print(corregir_ortografia("Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura."))
"""
14)Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y el segundo el separador de la fecha (puede ser la barra / o el guión -) 
y que devuelva True en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o ‘dd-mm-aaaa’
"""
# print(es_fecha("08-03-1995","-"))
"""
15)Crear la función es_hora que reciba un string y que devuelva True en caso de tratarse de una hora válida y False en el caso contrario. 
El formato admitido es ‘hh:mm:ss’
"""
# print(es_hora("00:14:50"))
"""
16)Crear la función validar_codigo_postal que reciba un string como parámetro y devuelva True en caso de tratarse de código postal válido o False en caso contrario. 
---------------------------------------------------------------------Imagen de ayuda en el archivo-----------------------------------------------------------------
"""
# print(validar_codigo_postal("a4560adv"))
"""
17)
Crear la función validar_patente que reciba un string como parámetro y devuelva True en caso de tratarse de un número de patente válido o False en caso contrario.
Debe poder admitir estos dos tipos:
---------------------------------------------------------------------Imagen de ayuda en el archivo-----------------------------------------------------------------
"""
# print(validar_patente("AS123DF"))
"""
18)Crear una función que se llame obtener_direcciones_email que reciba un texto y devuelva una lista con todas las direcciones de email válidas que 
encuentren en el mismo.Acá dejamos un texto de ejemplo: https://onlinegdb.com/Ln0jhatKeI.
# """
# print(obtener_direcciones_email("""
# <Alberto, Cervantes> acervantes@gmx.com <Ana, Jimenez> ajimenez@hotmail.com
# <Antonio, Castillo> acastillo@gmail.com <Armando, Vega> avega@yahoo.com
# <Arturo, Arredondo> aarredondo@gmail.com <Beatriz, Vargas> bvargas@outlook.com
# <Berenice, Rios> bribos@yahoo.com <Brenda, Gonzalez> bgonzalez@terra.com
# <Brian, Hernandez> bhernandez@outlook.com <Camila, Reyes> creyes@terra.com
# """))
"""
19)Crear una función llamada validar_password que reciba un string y verifique si se trata de una contraseña cumple con los requisitos mínimos de seguridad:

-Al menos 8 caracteres
-Al menos una letra mayúscula y una letra minúscula
-Un número 
-Un carácter especial
	
En caso de no cumplir con alguno de los requisitos, imprimir un mensaje informando cual no se cumplio
"""

# Ejemplo de uso
contrasena1 = "Password123!"
contrasena2 = "pass"
contrasena3 = "Password"

# print("Contraseña 1:")
# validar_password(contrasena1)
# print("\nContraseña 2:")
# validar_password(contrasena2)
# print("\nContraseña 3:")
# validar_password(contrasena3)
"""
20)Crear una función llamada validar_ip que reciba un string como parámetro y verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar True de lo contrario retornar False. 
Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde xxx es un número entero entre 0 y 255

# Ejemplos de uso
print(validar_ip("192.168.0.1"))    # True
print(validar_ip("256.168.0.1"))    # False (fuera de rango)
print(validar_ip("192.168.0.500"))  # False (fuera de rango)
print(validar_ip("192.168.0.1.1"))  # False (formato incorrecto)
"""