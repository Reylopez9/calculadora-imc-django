# Calculadora de IMC

**Asignatura:** Programación en Python  
**Estudiante:** Angel Reynaldo Lopez Lopez
**Universidad:** Universidad Tecnológica de Honduras  

---

## Descripción

Aplicación web desarrollada con **Python y Django** que calcula el Índice de Masa Corporal (IMC) de una persona y lo clasifica según rangos de peso saludable.

## Funcionalidades

- Ingreso de peso en kilogramos y altura en metros
- Cálculo del IMC con fórmula implementada manualmente
- Clasificación del resultado en 4 categorías
- Validación de entradas (valores no numéricos o negativos)
- Botón para limpiar los campos

## Clasificación del IMC

| Rango | Categoría |
|-------|-----------|
| Menor a 18.5 | Bajo peso |
| 18.5 – 24.9 | Peso normal |
| 25 – 29.9 | Sobrepeso |
| 30 o más | Obesidad |

## Tecnologías utilizadas

- Python 3
- Django 6
- HTML / CSS

## Instrucciones para ejecutar

```bash
pip install django
python manage.py runserver
```

Luego abrir en el navegador: `http://127.0.0.1:8000/`
