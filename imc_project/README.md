# Calculadora de IMC — Django

Aplicación web con Django para calcular el Índice de Masa Corporal (IMC).

## Requisitos
- Python 3.8+
- Django 4.x (`pip install django`)

## Instalación y ejecución

```bash
# 1. Clonar / descomprimir el proyecto
cd imc_project

# 2. Instalar dependencia
pip install django

# 3. Ejecutar el servidor
python manage.py runserver

# 4. Abrir en el navegador
http://127.0.0.1:8000/
```

## Estructura del proyecto

```
imc_project/
├── calculadora/
│   ├── templates/calculadora/
│   │   └── index.html       ← Interfaz de usuario
│   ├── views.py             ← Lógica de cálculo y validación
│   └── urls.py              ← Rutas de la app
├── imc_project/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## Fórmula implementada

```
IMC = peso / (altura × altura)
```

Implementada manualmente en `views.py`, sin librerías externas.

## Clasificación

| Rango IMC    | Categoría    |
|--------------|--------------|
| < 18.5       | Bajo peso    |
| 18.5 – 24.9  | Peso normal  |
| 25 – 29.9    | Sobrepeso    |
| ≥ 30         | Obesidad     |

## Validaciones

- Peso y altura deben ser números positivos
- Mensajes de error para valores no numéricos o negativos
