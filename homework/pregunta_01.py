"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import csv
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    ubicacion_zip = "files/input.zip"

    input_direc = "files/input"
    output_direc = "files/output"

    train_csv = os.path.join(output_direc, "train_dataset.csv")
    test_csv = os.path.join(output_direc, "test_dataset.csv")


    os.makedirs(output_direc, exist_ok=True)

    with zipfile.ZipFile(ubicacion_zip, 'r') as zip_ref:
        zip_ref.extractall("files")

    def procesar(folder_path, output_csv):
        rows = []

        for target in os.listdir(folder_path):
            target_path = os.path.join(folder_path, target)
            if os.path.isdir(target_path):
                for file_name in os.listdir(target_path):
                    file_path = os.path.join(target_path, file_name)

                    with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                    rows.append({"phrase": phrase, "target": target})

        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["phrase", "target"])
            writer.writeheader()
            writer.writerows(rows)

    procesar(os.path.join(input_direc, "train"), train_csv)

    procesar(os.path.join(input_direc, "test"), test_csv)


pregunta_01()