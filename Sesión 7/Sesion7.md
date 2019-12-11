Sesión 7: CT aplicado a Humanidades (Digital):  Funciones, Separar Strings

Las Strings son muy útiles para modelar datos textuales o generar nuevos datos, e indexarlos en y rebanarlas es sólo el principio. Empezaremos esta sección con una breve prosa
párrafo, el Artículo 1 de la Declaración Universal de Derechos Humanos, el texto en inglés. El
El texto de este documento se puede encontrar (y seleccionar y copiar) en línea en:
http://www.un.org/en/documents/udhr/

Una pregunta sencilla es: ¿cuántos caracteres tiene esta String? Nosotros puede resolver esto simplemente comprobando la longitud de la String, usando la función len(). Adivina y luego inténtalo:

Dividir un texto en palabras (primer intento)
La clase string tiene un método muy útil para este caso. Este método, split(), divide una String en una lista de Strings, rompiéndola cada vez que la String especificada (la String uno dado como argumento). Prueba esto y verás:

El resultado es nuestra String, pero dividida en una lista de palabras. La puntuación que está al lado de una palabra se queda con él. Vuelva a escribir el texto para ver que este método devuelve una lista con la String dividida como elementos, pero no cambia el valor del texto en sí mismo, o el valor de la String que sea invocada el.

Podemos comprobar la longitud de la String dividida, text.split(' '), como una forma de determinar cuántas palabras hay en el texto:

El resultado tiene cierto sentido, pero es un poco inusual, y probablemente no lo es.
lo que queremos para contar palabras. La String se divide en "hola", la String nula,
la String nula de nuevo, y finalmente 'mundo'. Los tres espacios del centro se utilizaron para
dividir esta String en cuatro partes.

La línea de arriba produce exactamente el mismo resultado que las dos líneas anteriores - intente que sea seguro. La única diferencia es que en las dos líneas anteriores, la String 'hola ....' recibe un valor de o, equivalente, asignado a una variable, hi. Eso significa que más tarde, es posible referirse a "hola" en lugar de escribir "hola...". Y, si transformamos lo que hemos etiquetado hi de alguna manera -asignando un nuevo valor a esa variable- esa variable se referirá a la variable transformación.

Note que esta línea está haciendo uso de la conveniencia que nos proporciona la variable hi. Nosotros no es necesario escribir (o copiar y pegar) 'hola ....' otra vez; simplemente podemos escribir estas dos cosas caracteres. Esa no es, por supuesto, la única razón para usar variables, pero es una.
