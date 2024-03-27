# massive-bg-remover
Proyecto para eliminar de forma masiva imagenes de un directorio con formatos `.png`, `.jpg`, `.jpeg` o `.gif`

Este programa ejecuta un modelo de **IA** llamado u2net, que en su primera ejecución guardará en `%UserProfile%\.u2net\u2net.onnx`; y cada vez que se ejecute, accederá a este fichero para interpretar que parte de la imagen tendrá que eliminar. En caso de que se elimine, se volverá a descargar cuando se ejecute.

## Comandos
Crea el entorno de virtual de Python
```py -m venv venv```

Activa el entorno creado

```venv\Scripts\activate```

Instalar paquetes necesarios

```pip install -r .\requeriments.txt```

Crea el ejecutable

```pyinstaller --onefile --icon=favicon.ico remover.py```

>run.exe se ha generado en .\DIST Ejecución del programa

## EJECUCIÓN
```remover.exe -i .\input -o .\output```
