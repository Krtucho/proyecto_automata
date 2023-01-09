# Pasos

Instalar python

Instalar dependencias de python que se encuentran en el archivo requirements.txt

# Para pruebas comunes
Ejecutar el archivo main.py que se encuentre en system/pyke_utils

>cd system/pye_utils

>python main.py


# Correr streamlit
# Running
Ejecutar el archivo visual.py con stremlit
```
>cd system
```
```
$python -m streamlit run visual.py
```
is equivalent to:
```
$ streamlit run your_script.py
```

Si pyke da algun conflicto modificar el archivo main.py asignando la ruta de esta carpeta en your_path en la siguiente linea que estara comentada
```
># sys.path.append('your_path')
```