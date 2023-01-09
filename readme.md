# Pasos

Instalar python

Instalar dependencias de python que se encuentran en el archivo requirements.txt

# Running Streamlit
Ejecutar el archivo visual.py con stremlit
```
>cd system
```
Luego de situarnos en la carpeta ejecutamos el archivo visual.py utilizando streamlit
```
$python -m streamlit run visual.py
```
is equivalent to:
```
$ streamlit run visual.py
```

Si pyke da algun conflicto modificar el archivo main.py asignando la ruta de esta carpeta en your_path en la siguiente linea que estara comentada
```
#sys.path.append('your_path')
```