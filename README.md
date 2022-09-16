# intelimetricaCRUD
Dentro de esta carpeta se ha creado un ambiente virtual con los requerimientos necesarios para que la APIREST funcione.
Se incluye el archivo requeriments.txt el cual contiene las librerias con las que se trabaja, se puede instalar en caso de
requerirlo con 'pip install -r requeriments.txt'.
La base de datos que se utilizo es MySQL

Se ha creado un super usuario para gestionar el modulo Admin del proyecto 'restaurantCRUD'
superuser = adminRest
password = root

Al acceder puede ver la informacion contenida en la BD dentro de la app que se creo a la cual le puse por nombre 'app_CRUD'
Se crearon 2 modelos para guardar la información, el primer modelo se llama 'Restaurant' y contiene la informacion obtenida en el archivo CSV
El segundo modelo se llama RestaurantStatistics, la cual es una tabla auxiliar que almacena los datos de la url con parametros latitude, longitude,radius.
Esta segunda tabla solo almacena una fila y es la informacion que se muestra en el segundo formato JSON con los campos 'count','avg','std'
El formato de la URL con parametros es la siguiente:
127.0.0.1:8000/restaurants/statistics/latitude=NUMBER&longitude=NUMBER&radius=NUMBER

Cabe mencionar que al ingresar esta url se redirecciona al siguiente enlace:
http://127.0.0.1:8000/api/statistics/
Este enlace contiene el formato JSON que se pide en la tarea 2:
ejemplo para la url (http://127.0.0.1:8000/restaurants/statistics/latitude=17.048461376336846&longitude=-96.69138479711978&radius=1000000):
[
    {
        "count": 100,
        "avg": 1.72,
        "std": 1.44968962195361
    }
]
En este ejemplo la equivalencia del radio es en Metros.
Para importar los datos del archivo CSV nos auxiliamos del siguiente enlace
http://127.0.0.1:8000/import/

Se utilizo la libreria geopy para obtener las distancias entre la latitud y longitud dadas en la URL y cada uno de los registros almacenados
La información que se obtiene se guarda en una nueva lista y solose guardan aquellos registros que sean menores o iguales al radio proporcionado en la URL.
Esto significa que esos registros almacenados o restaurantes estan dentro del radio proporcionado
