#  2020-2 Grupo 5: Chefcitos 
Repositorio del diseño de una plataforma para buscar y compartir recetas de cocina.


# Antes de empezar
Estas son las instrucciones para comenzar a usar a usar el repositorio `2020-2-grupo5`.


Es recomendable preparar un ambiente virtual usando anaconda o [virtualenv](https://docs.python.org/3/library/venv.html) para manejar las librerías de python.


## Clonar el repositorio  y configurar el entorno virtual
Cree una carpeta donde quiera guardar los archivos del proyecto.
Después se puede clonar el repositorio o descargar el archivo zip.

**Para clonar el repositorio**

Se recominda usar SSH para clonar al contrario de HTPPS.
Desde el terminal, o el terminal de git **Git Bash** si es que está ocupando Windows, escriba:

```
git clone git@github.com:DCC-CC4401/2020-2-grupo5.git
```

**Configurar un ambiente virtual**

Para **Windows**, En la ventana del terminal, navege a la carpeta donde tenga los archivos descomprimidos o clonados.
Asegurese de tener instalado python3 en su sistema operativo.
Para instalar virtualenv, desde el terminal ejecute:
```
pip install virtualenv
```

Actualize las librerías:
```
py -m pip install --upgrade pip
```

Cree un ambiente virtual en la carpeta donde quiera almacenarlo escribiendo:
```
python3 -m venv 'nombre-entorno'
```

Para virtualenv y anaconda, en el terminal active su ambiente virtual y ejecute el siguiente comando:

```
pip install -r requirements.txt
```



(Revisar para anaconda y para distribuciones de Linux)


## Montar el sitio web localmente

Para visualizar el sitio web y montarlo en la computadora, en el terminal dirigase a la carpeta chefcito donde se encuentra el archivo manage.py, y ejectue:

```
python3 manage.py runserver
```
