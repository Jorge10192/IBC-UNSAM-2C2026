"""
Práctica 1.1: Argumentos causales alternativos e incertidumbre.
============================================
"""

import warnings
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore")

# ------------------------------------------------------------
# 1. Definición del espacio de hipótesis
# ------------------------------------------------------------

# H representa las 3 cajas posibles {0, 1, 2}
H = np.arange(3)


# ------------------------------------------------------------
# 2. Priors
# ------------------------------------------------------------

# Justificacion p_r: Se define la probabilidad de elegir en regalo dentro de una de las cajas
# Si esta fuera de las cajas (Domino H) no deberia haber ningun regalo

def p_r(r: int) -> float:
    """
    P(R = r).
    Prior sobre la ubicación del regalo.
    r ∈ {0, 1, 2}
    """
    if r in H:
        return 1/3
    else:
        return 0

# Verificacion:
print(' Justificacion p_r: Se define la probabilidad de elegir en regalo dentro de una de las cajas ' \
'Si esta fuera de las cajas (Domino H) no deberia haber ningun regalo')
print('Verificacion1: Todos los valores de p_r debe sumar 1(Probabilidad de eleccion del regalo):', p_r(r=0)+p_r(r=1)+p_r(r=2) == 1)
print('Verificacion2: p_r(5) debe ser 0:', p_r(5) == 0)

# Jusitificacion p_c: Similar a p_r pero ahora es eleccion de una caja.
# En principio se puede eelgir cualquier caja, sin restriccion alguna, pero no un valor de afuera. 

def p_c(c: int) -> float:
    """
    P(C = c).
    Prior sobre la caja elegida por el participante
    c ∈ {0, 1, 2}
    """
    if c in H:
        return 1 / 3
    else:
        return 0


# ------------------------------------------------------------
# 3. Modelos del presentador
# ------------------------------------------------------------

# Justificacion p_s_rM0: Hay solo una condicion, el presentador no puede abrir la caja donde esta el regalo.
def p_s_rM0(s: int, r: int) -> float:
    """
    P(S = s | R= r, M = 0).
    Modelo 0 (No Monty Hall):
    El presentador abre cualquier caja que no tenga el regalo.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    """
    if r not in H or s not in H:
        return 0
    elif s == r:
        return 0
    else:
        return 1/2


def p_s_rcM1(s: int, r: int, c: int):
    """
    P(S = s | R= r, C= c, M = 1).
    Modelo 1 (Monty Hall):
    El presentador abre una caja que no tenga el regalo
    ni haya sido seleccionada.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    """
    # Check valores estén dentro del dominio
    if s not in H or r not in H or c not in H:
        return 0

    # Cajas que Monty puede elegir
    opciones = [x for x in H if x != r and x != c]

    # Si s no es una caja permitida, su probabilidad es 0
    if s not in opciones:
        return 0

    # Máxima incertidumbre entre las opciones disponibles
    return 1 / len(opciones)


print(
    "Verificación M1 - r=0, c=0:",
    p_s_rcM1(0, 0, 0),
    p_s_rcM1(1, 0, 0),
    p_s_rcM1(2, 0, 0)
)


# ------------------------------------------------------------
# 4. Distribución conjunta P(r, c, s | M)
# ------------------------------------------------------------

#m = 0 -> Modelo Base
#m = 1 -> Modelo Monty Hall

def p_rcs_M(r: int, c: int, s: int, m: int) -> float:
    """
    P(r, c, s | M) = P(r | M)P(c | M)P(s | r, c, M)
    Distribución conjunta del modelo m.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    m ∈ {0, 1}
    """
    if m == 0:
        return p_r(r) * p_c(c) * p_s_rM0(s, r)

    elif m == 1:
        return p_r(r) * p_c(c) * p_s_rcM1(s, r, c)

    else:
        return 0


# ------------------------------------------------------------
# 5. Simulación de datos (asumiendo Monty Hall verdadero)
# ------------------------------------------------------------

np.random.seed(0)


def simular(T=16) -> List[Tuple[int, int, int]]:
    """
    Función para simular datos según el modelo Monty Hall verdadero.
    T: número de datos a generar.

    Cada tirada es documentada de la forma ti=(ci,si,ri)
    """
    datos = []

    for t in range(T):

        # 1. Simular ubicación del regalo
        prob_r = [p_r(r) for r in H]
        r = np.random.choice(H, p=prob_r)

        # 2. Simular elección del participante
        prob_c = [p_c(c) for c in H]
        c = np.random.choice(H, p=prob_c)

        # 3. Simular la pista usando el modelo Monty Hall
        prob_s = [p_s_rcM1(s, r, c) for s in H]
        s = np.random.choice(H, p=prob_s)

        # 4. Guardar episodio en el orden pedido: (c, s, r)
        datos.append((c, s, r))

    return datos


# ------------------------------------------------------------
# 6. Probabilidad de los datos dado un modelo
# ------------------------------------------------------------



def pDatos_M(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    P(Datos | M) = prod([ P(c,s,r|M) for c, s, r in Datos ])
    Probabilidad de ver los datos dados el modelo considerado.
    m ∈ {0, 1}
    """
    probabilidad = 1

    for c, s, r in datos:
        probabilidad *= p_rcs_M(r, c, s, m)

    return probabilidad


# ------------------------------------------------------------
# 7. Probabilidad total de ver los datos
# ------------------------------------------------------------


def pM(m: int) -> float:
    """
    P(M)
    Prior sobre los modelos.
    m ∈ {0, 1}
    """
    if m == 0 or m == 1:
        return 1 / 2
    else:
        return 0


def pDatos(datos: List[Tuple[int, int, int]]) -> float:
    """
    P(Datos)
    Probabilidad total de ver los datos usando la contribución
    de todos los modelos.

    P(Datos)=∑​P(Datos∣M)*P(M)
    """
    probabilidad = 0

    for m in [0, 1]:
        probabilidad += pDatos_M(datos, m) * pM(m)

    return probabilidad


# ------------------------------------------------------------
# 8. Actualización de creencias sobre los modelos
# ------------------------------------------------------------


def pM_Datos(m: int, datos: List[Tuple[int, int, int]]) -> float:
    """
    P(M | Datos)
    Actualización de la creencia sobre el modelo M dado los datos
    (distribución a posteriori).
    """
    return (pDatos_M(datos, m) * pM(m)) / pDatos(datos)


def evolucion_posterior(m: int, datos: List[Tuple[int, int, int]]) -> List[float]:
    """
    Evolución del posterior de los modelos según se observa información.
    """
    posteriores = []

    for t in range(len(datos) + 1):
        posteriores.append(
            pM_Datos(m, datos[:t])
        )

    return posteriores



# ------------------------------------------------------------
# 9. Cálculo del bayes factor
# (diferencia en órdenes de magnitud en escala logarítmica)
# ------------------------------------------------------------

#Idea: Transformar producto en sumatoria a escala logaritmica

def log_pDatos_M(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    log(P(Datos | M))
    Logaritmo de la probabilidad de ver los datos dados el modelo considerado.
    """
    log_probabilidad = 0

    for c, s, r in datos:

        prob_episodio = p_rcs_M(r, c, s, m)

        if prob_episodio == 0:
            return -np.inf

        log_probabilidad += np.log10(prob_episodio)

    return log_probabilidad


def log_bayes_factor(datos: List[Tuple[int, int, int]], m_i: int, m_j: int) -> float:
    """
    log(Datos | Mi / Datos | Mj) = log_10P(Datos | Mi) - log_10P(Datos | Mj)
    Bayes factor en escala logarítmica para comparar dos modelos.
    m_i, m_j ∈ {0, 1}
    """
    return (log_pDatos_M(datos, m_i) - log_pDatos_M(datos, m_j))


# ------------------------------------------------------------
# 10. Predicción típica que realizan los modelos sobre los datos
# ------------------------------------------------------------

def prediccion_tipica(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    log(Media Geométrica)
    Logaritmo de la media geométrica de los datos dados el modelo considerado.
    m ∈ {0, 1}
    """
    N = len(datos)

    return log_pDatos_M(datos, m) / N

# La predicción típica en escala original es P(Datos | M) ** (1/N)

# ------------------------------------------------------------
# 11. Ejecución principal
# ------------------------------------------------------------

if __name__ == "__main__":
    # Simulación
    print("Simulacion para T=16:")
    datos = simular(T=16)

    # Print de funciones
    print("log_bayes_factor (M1 contra M0):", log_bayes_factor(datos, 1, 0))

    print("Las predicciones estan en factor logaritmico log10 entonces pueden dar negativo")
    print("prediccion_tipica (M0):", prediccion_tipica(datos, 0))
    print("prediccion_tipica (M1):", prediccion_tipica(datos, 1))

    # Posteriores
    post_M0 = evolucion_posterior(0, datos)
    post_M1 = evolucion_posterior(1, datos)

    # Gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(post_M0, label="M0: Base")
    plt.plot(post_M1, label="M1: Monty Hall")
    plt.xlabel("Número de episodios")
    plt.ylabel("P(Modelo | Datos)")
    plt.title("Evolución del posterior de los modelos")
    plt.legend()
    plt.tight_layout()
    plt.show()
