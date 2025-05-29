# Parqueadero
El parqueadero está hecho en lenguaje de Python, es un parqueadero como se puede ver en cualquier centro comercial están por colores las entradas, las salidas, los sitios disponibles, las Paredes, la zona discapacitados y la zonas ocupadas. 
Las entradas y las salidas están de color amarillo, las zonas libres están de color verde y la zonas ocupadas de color rojo. Hay Paredes y se ubican por los lados y están de color gris, hay sitios de discapacitados que es de color azul y si ya está ocupado el sitio de discapacitados es de color púrpura, también hay conos de color naranja, donde no se pueden parquear, para ingresar uno ingresa la placa, despues qué tipo de parqueadero necesita si normal o de discapacitados y se pueden escoger el sitio donde quiera parquear. Para retirar el vehículo, sólo necesitas la placa y se retira el vehiculo que parqueo
La libreria que utilice para los colores en la terminal es la libreria de colorama y usando la pateta de colorama pude marca cada espcaio un color para indicar mejro cada espacio


#Pokemon
El juego inspirado enel famoso juego de Pokemon esta en lenguaje de C++, esta con todas las bases de el juego, y los terminos que se utilizaron son muy basicos en nivel de progrogramacion, en este se puede ver la vida de un pokemos en especifico, su energia, que esta sirve para poder hacer ataques mas potentes, y un menu interactivo para que se pueda escoger que ataque que va hacer el pokemon y se muestra el daño que hace el mismo ataque, el codigo tiene algunas librerias adicionales a las convencionales ya que esta ayuda a hacer numeros aleatorios, en este caso el numero del daño no simpre es el mismo, puede ser critico o muy debil.

 Turno del oponente
     cout << "\nTurno del oponente...\n";
     int eleccion = rand() % 3; // 0 = especial, 1 = ataque, 2 = esperar

En esta parte del codigo nos tuvimos que apoyar por una inteligencia artificial, ya que estabamos estancados y no sabiamos como avanzar, este bloque hace que el oponente tambien tiene variedad de ataques y claramnete tambien el numero del daño cambia al pasar del tiempo, nos avisa que es turno del oponente y no podemos atacar.

#include <cstdlib>
#include <ctime>

Estas son las librerias que nos ayudan para que que el daño de los ataques cambien y no siempre sean lo mismo.

Ya cuando la batalla termina, nos mandan un aviso de que somos ganadores o perdedores.
Este es el codigo en general, muy sencillo pero cumple con los parametros propuestos.
