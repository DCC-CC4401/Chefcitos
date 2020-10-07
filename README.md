#  2020-2 Grupo 5: Chefcitos 
Repositorio del diseño de una plataforma para buscar y compartir recetas de cocina.


# Antes de empezar
Estas son las instrucciones para comenzar a usar a usar el repositorio `2020-2-grupo5`.


Es recomendable preparar un ambiente virtual usando [anaconda](https://docs.anaconda.com/anaconda/install/windows/) o [virtualenv](https://docs.python.org/3/library/venv.html) para manejar las librerías de python.


## Clonar el repositorio  y configurar el entorno virtual
Cree una carpeta donde quiera guardar los archivos del proyecto.
Después se puede clonar el repositorio o descargar el archivo zip.

**Para clonar el repositorio**

Se recominda usar SSH para clonar al contrario de HTPPS.
Desde el terminal, o el terminal de git **Git Bash** en Windows, escriba:

```
git clone git@github.com:DCC-CC4401/2020-2-grupo5.git
```

**Configurar un ambiente virtual**

Para instalar **virtualenv** en **Windows**, desde la ventana del terminal navege a la carpeta donde tenga los archivos descomprimidos o clonados. Asegurese de tener instalado python3 en su sistema operativo.
Para instalar virtualenv, desde el terminal ejecute:
```
python3 -m pip install --user virtualenv
```
o
```
pip install virtualenv
```

Cree un ambiente virtual en la carpeta donde quiera almacenarlo, es recomendable en la carpeta del proyecto, escribiendo:
```
python3 -m venv 'nombre-entorno'
```
Para activar y desactivar el ambiente respectivamente, ejecute en el directorio donde este almacenado:

```
.\"nombre-entorno"\Scripts\activate
deactivate
```

Para instalar [**anaconda**](https://docs.anaconda.com/anaconda/install/windows/) siga las instrucciones del link.
Para crear un entorno virtual desde el terminal de anaconda, **Anaconda Prompt**, ejecute:

```
conda create --name myenv
```

Para activar y desactivar el ambiente respectivamente, ejecute:
```
conda activate myenv
conda deactivate
```


Para **virtualenv** y **anaconda** actualize las librerías:
```
python3 -m pip install --upgrade pip
```

Por último, se deben instalar las librerías necesarias para correr el proyecto. Active su ambiente virtual y ejecute el siguiente comando en la carpeta donde este almacenado su proyecto:

```
pip install -r requirements.txt
```


## Montar el sitio web localmente

Para visualizar el sitio web y montarlo en la computadora, desde el terminal dirigase a la carpeta chefcito donde se encuentra el archivo manage.py, y ejectue:

```
python manage.py runserver
```
