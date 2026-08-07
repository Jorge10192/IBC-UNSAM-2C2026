# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 07:40:37 2026

@author: Jorge
"""

import numpy as np

# -----------------------------
# PARÁMETROS
# -----------------------------

np.random.seed(42)

n_tiradas = 1000
n_repeticiones = 100

# Proporción apostada a Cara
opciones = np.arange(0, 1.01, 0.1)

# Probabilidades
p_cara = 0.5

# Pagos
pago_cara = 3
pago_sello = 1.2

capital_inicial = 100000


# -----------------------------
# SIMULACIÓN
# -----------------------------

resultados = []

for f in opciones:

    capitales_finales = []
    crecimientos_log = []

    for repeticion in range(n_repeticiones):

        # Generamos 1000 tiradas
        # True = Cara
        # False = Sello
        tiradas = np.random.rand(n_tiradas) < p_cara

        # Caso extremo:
        # si f = 0, una Cara destruye el capital
        # si f = 1, un Sello destruye el capital
        if f == 0 or f == 1:

            capital = capital_inicial

            for cara in tiradas:

                if cara:
                    multiplicador = pago_cara * f
                else:
                    multiplicador = pago_sello * (1 - f)

                capital *= multiplicador

                if capital == 0:
                    break

            capitales_finales.append(capital)

            if capital == 0:
                crecimientos_log.append(-np.inf)

        else:

            # Multiplicador obtenido en cada tirada
            multiplicadores = np.where(
                tiradas,
                pago_cara * f,
                pago_sello * (1 - f)
            )

            # Log del capital final:
            #
            # log(W_final)
            # = log(W_inicial)
            # + sum(log(multiplicadores))
            #
            log_capital_final = (
                np.log(capital_inicial)
                + np.sum(np.log(multiplicadores))
            )

            # Crecimiento logarítmico promedio por tirada
            crecimiento_log_promedio = (
                np.mean(np.log(multiplicadores))
            )

            crecimientos_log.append(
                crecimiento_log_promedio
            )

            # Evitamos overflow si el número es gigantesco
            if log_capital_final < 700:
                capital = np.exp(log_capital_final)
            else:
                capital = np.inf

            capitales_finales.append(capital)

    # -----------------------------
    # RESUMEN PARA ESTA ESTRATEGIA
    # -----------------------------

    capital_promedio = np.mean(capitales_finales)
    capital_mediano = np.median(capitales_finales)

    crecimientos_validos = [
        x for x in crecimientos_log
        if np.isfinite(x)
    ]

    if len(crecimientos_validos) > 0:
        crecimiento_log_medio = np.mean(
            crecimientos_validos
        )
    else:
        crecimiento_log_medio = -np.inf

    resultados.append(
        (
            f,
            capital_promedio,
            capital_mediano,
            crecimiento_log_medio
        )
    )


# -----------------------------
# MOSTRAR RESULTADOS
# -----------------------------

print(
    "f Cara | Capital promedio | "
    "Capital mediano | Crecimiento log medio"
)

print("-" * 75)

for (
    f,
    capital_promedio,
    capital_mediano,
    crecimiento_log_medio
) in resultados:

    print(
        f"{f:5.1f} | "
        f"{capital_promedio:16.5g} | "
        f"{capital_mediano:15.5g} | "
        f"{crecimiento_log_medio:20.6f}"
    )


# -----------------------------
# MEJOR ESTRATEGIA
# según crecimiento logarítmico
# -----------------------------

mejor = max(
    resultados,
    key=lambda x: x[3]
)

print("\nMejor estrategia según crecimiento logarítmico:")

print(
    f"Apostar {mejor[0]:.1f} a Cara "
    f"y {1 - mejor[0]:.1f} a Sello"
)