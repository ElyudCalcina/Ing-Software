# Laboratorio 04: xUnit y cobertura de código

Implementación de Bubble Sort con paradigma orientado a objetos, pruebas automatizadas con pytest y cobertura con Coverage.py.

## Requisitos

- Python 3.10 o superior
- Instalar dependencias: `python -m pip install -r requirements.txt`

## Ejecutar las pruebas

Desde la carpeta del proyecto:

```bash
python -m pytest -v
```

## Generar cobertura

```bash
python -m coverage run -m pytest
python -m coverage report -m
python -m coverage html
```

El reporte navegable se crea en `htmlcov/index.html`.

## Estructura

- `src/bubble_sort.py`: implementación.
- `tests/test_bubble_sort.py`: casos automatizados.
- `evidence/`: reportes de ejecución y cobertura obtenidos al ejecutar el proyecto.

La función devuelve una lista ordenada nueva y conserva intacta la lista recibida.
