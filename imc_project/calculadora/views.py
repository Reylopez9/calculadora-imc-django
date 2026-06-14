from django.shortcuts import render


def calcular_imc(request):
    context = {}

    if request.method == 'POST':
        peso_raw = request.POST.get('peso', '').strip()
        altura_raw = request.POST.get('altura', '').strip()

        errores = []

        # Validar peso
        try:
            peso = float(peso_raw)
            if peso <= 0:
                errores.append("El peso debe ser un número positivo.")
        except ValueError:
            errores.append("El peso debe ser un valor numérico válido.")
            peso = None

        # Validar altura
        try:
            altura = float(altura_raw)
            if altura <= 0:
                errores.append("La altura debe ser un número positivo.")
        except ValueError:
            errores.append("La altura debe ser un valor numérico válido.")
            altura = None

        if errores:
            context['errores'] = errores
            context['peso'] = peso_raw
            context['altura'] = altura_raw
        else:
            # Cálculo manual del IMC: peso / (altura * altura)
            imc = peso / (altura * altura)
            imc_redondeado = round(imc, 2)

            # Clasificación por condicionales
            if imc < 18.5:
                categoria = "Bajo peso"
                color_clase = "bajo-peso"
            elif imc < 25:
                categoria = "Peso normal"
                color_clase = "peso-normal"
            elif imc < 30:
                categoria = "Sobrepeso"
                color_clase = "sobrepeso"
            else:
                categoria = "Obesidad"
                color_clase = "obesidad"

            context['imc'] = imc_redondeado
            context['categoria'] = categoria
            context['color_clase'] = color_clase
            context['peso'] = peso_raw
            context['altura'] = altura_raw

    return render(request, 'calculadora/index.html', context)
