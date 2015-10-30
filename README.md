# Tu_Comunidad

# Primer hito

## Descripción del proyecto
El proyecto consistirá en una plataforma de gestión de comunidades de vecinos que permitirá al presidente llevar un control de todas las cosas a tener en cuenta en una comunidad y a los vecinos acceder a información como facturas, avisos, ... Además se podrán realizar "juntas virtuales" en las que los propietarios podrán debatir y votar sin tener que asistir físicamente a las juntas.

## Servicios necesarios
Para el funcionamiento de la plataforma hará falta:
 - Servidor web
 - Servidor de base de datos
 - Servidor de correo

## Certamen de proyectos libres de la UGR.
![certamen](http://i.imgur.com/wyVy7TZ.png)

# Segundo hito
## Tests e integración continua
Voy a utilizar el sistema de prueba de código que trae Django por defecto como sistema de test para validar todo el código antes de añadirlo al proyecto y Travis-CI para la integración continua.
Para empezar a usarlo basta con enlazar mi cuenta de github al servicio, indicarle que repositorio quiero controlar e indicarle como se compila, que dependencias necesita y como se ejecutan los test en el archivo travis.yml:
```
	language: python
	python:
	 - "3.4.3"
	# command to install dependencies
	install:
	 - python com_app/setup.py install
	# command to run tests
	script:
	 - python com_app/manage.py test

```

A partir de ahora, cada commit que haga se someterá de forma automática a todos los test del archivo test.py (por ahora solo un test de prueba)
![test_superado](http://i.imgur.com/vRVIj8O.png)


