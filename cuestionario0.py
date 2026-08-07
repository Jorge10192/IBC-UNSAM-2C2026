# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: global
#     language: python
#     name: python3
# ---

# %%
import math
import random
import inspect
import warnings

respuestas = {}

# %% [markdown]
# # 1 - Preguntas sobre fundamentos
#
# Este notebook contiene una lista de preguntas junto con una lista exhaustiva de respuestas mutuamente contradictorias. 
# A diferencia de los enunciados de tipo "multiple choise" en los que se pide seleccionar una única opción, aquí se pide que distribuyan creencias entre las diferentes opciones, asegurándose que el valor asignado sea positivo y la suma sea 1.
# La evaluación será el producto de las creencias asiganadas a las respuestas correctas. 
# En caso de que la respuesta sea una variable aleatoria, se considerará la predicción típica a largo plazo, es decir, su media geométrica.
# Notar que un único cero en la secuencia anula todo el producto.
# Por ello, en caso de duda, no conviene que concentren toda su creencia en una sola opción, sino distribuir algo de creencia en todas las opciones que consideran posibles.
# Notar también que conviene asignar más a la opción en la que más creen, porque distribuir creencias en partes iguales entre todas las opciones no es mucho mejor que el azar (baseline).

# %% [markdown]
# ### Moneda
#
# ¿Cuál será el resultado del lanzamiento de una moneda?
#
# 0. Anverso (Cara)
# 0. Reverso (Sello)
# 0. Canto (Borde)

# %%
respuestas["Moneda"] = [
1/3, # 0. Anverso (Cara)
1/3, # 1. Reverso (Sello)
1/3, # 2. Canto (Borde)
"""
Justifique:
Los tres resultados posibles considerados son Cara, Sello y Borde, por lo que al ser todos los eventos posibles
la suma de sus probabilidades deben sumar 1:

P(Cara) + P(Sello) + P(Borde) = 1.

Como no se proporciona información adicional que permita distinguir o
privilegiar alguno de los tres resultados, aplicamos el principio de máxima
incertidumbre dada la información disponible. Esto se logra distribuyendo la
creencia en partes iguales (prior uniforme):

P(Cara) = P(Sello) = P(Borde) = 1/3.
""",
]

# %% [markdown]
# ### 1.1 Cajas
#
# Hay tres cajas idénticas. Sabemos que detrás de una de ellas hay un regalo. El resto están vacías. ¿Dónde está el regalo?
#
# 0. Caja 0
# 1. Caja 1
# 2. Caja 2
# 3. Otro lugar

# %%
respuestas["Cajas"] = [
1/3, # 0. Caja 0
1/3, # 1. Caja 1
1/3, # 2. Caja 2
0, # 3. Otro lugar
"""
Justifique:
El enunciado afirma que hay 3 cajas y detras de ellas 
hay un regalo, por lo tanto Ω={Caja 0,Caja 1,Caja 2}.

i) Luego {regalo en otro lugar}=∅ y P(∅)=0
ii) Como las tres cajas son idénticas y no se proporciona información que permita
distinguir o privilegiar alguna de ellas, aplicamos el principio de máxima
incertidumbre dada la información disponible, distribuyendo la creencia en
partes iguales. P(Caja 0) = P(Caja 1) = P(Caja 2) = 1/3
""",
]

# %% [markdown]
# ### Mentir
#
# ¿Cuál de todas las opciones se considera una definición matemática del principio de no mentir?
#
# 0. Máxima incertidumbre (o entropía)
# 0. Mínima incertidumbre (o entropía)
# 0. Máxima incertidumbre (o entropía) dada la información disponible (restricciones)
# 0. Mínima incertidumbre (o entropía) dada la información disponible (restricciones)
# 0. Ninguna de las anteriores

# %%
respuestas["Mentir"] = [
0, # 0. Máxima incertidumbre (entropía)
0, # 1. Mínima incertidumbre (entropía)
0.99, # 2. Máxima incertidumbre (entropía) dada la información disponible (restricciones)
0, # 3. Mínima incertidumbre (entropía) dada la información disponible (restricciones)
0.01, # 4. Ninguna de las anteriores
"""
Justifique:
i) La opcion 0 es una definicion incorrecta (o incompleta) porque ignora la restriccion de la informacion disponible.
ii) Las opciones 1 y 3 son incorrectas porque contradicen la definicion de maximizar la incertidumbre.
iii) La opcion 2 se ajusta bien a la definicion, estaba en duda si es o no una definicion matematica por lo cual,
busque en internet si la definicion dada en el ejercicio se puede considerar, o no, una definicion matematica. 
Esto se debe a que la definicon no esta expresada simbolicamente como por ejemplo P* = argmax_P H(P) mas ajustado a lo que
se conoce como definicion matematica.

La respuesta de google a mi pregunta, es que la opcion 2 si se considera una definicion matemtica, por lo tanto tengo alta certeza
acerca de la opcion 2, pero no certeza completa.
Asigno alta probabilidad a la opcion 2 y un poco a la opcion 4.
(Y no asigno probabilidad a la opcion 0, debido a que el enunciado pregunta por "cual" y no "cuales", asique debe elegirse 1 respuesta y la opcion 2
encaja mejor que la opcion 0 en la definicion)
""",
]

# %% [markdown]
# ### Universos
#
# En contextos de incertidumbre los posibles universos se bifurcan.
# Supongamos que hay tres cajas idénticas y detrás de una de ellas hay un regalo (el resto van a quedar vacías).
# Supongamos que nos permiten reservar una caja y luego, una persona nos muestra que en una de las otras cajas no está el regalo.
# En el contexto en el que reservamos la caja 1: ¿Cuál de todos los universos mutuamente contradictorios va a ocurrir?
# ¿El regalo está en la caja 1 y nos muestran la caja 1? ¿El regalo está en la caja 1 y nos muestran la caja 2?
# ... ¿El regalo está en la caja 3 y nos muestran la caja 2? ¿El regalo está en la caja 3 y nos muestran la caja 3?
#
# 0. Regalo = 1, Abren = 1
# 1. Regalo = 1, Abren = 2
# 2. Regalo = 1, Abren = 3
# 3. Regalo = 2, Abren = 1
# 4. Regalo = 2, Abren = 2
# 5. Regalo = 2, Abren = 3
# 6. Regalo = 3, Abren = 1
# 7. Regalo = 3, Abren = 2
# 8. Regalo = 3, Abren = 3
#

# %%
respuestas["Universos"] = [
0, # 0. Regalo = 1, Abren = 1
1/6, # 1. Regalo = 1, Abren = 2
1/6, # 2. Regalo = 1, Abren = 3
0, # 3. Regalo = 2, Abren = 1
0, # 4. Regalo = 2, Abren = 2
1/3, # 5. Regalo = 2, Abren = 3
0, # 6. Regalo = 3, Abren = 1
1/3, # 7. Regalo = 3, Abren = 2
0, # 8. Regalo = 3, Abren = 3
"""
Justifique:
i) Asigno probabilidad 0 a los eventos que no son posibles porque contradicen las hipotesis iniciales del enunciado:
Caso 1- Se abre la caja uno (Abren = 1), porque es la caja elegida por el participante y esa debe quedar en juego tenga o no el regalo dentro.
(Descarto opciones 0, 3 y 6)
Caso 2- Se abre la caja que tiene el regalo (Regalo = Abren), porque el presentador debe abrir una caja que no contenga el regalo.
(Descarto opciones 4 y 8)

ii) Luego asigno probabilidades a los distintos eventos siguiendo el concepto del juego Monty Hall.
(Regalo: r y Pista:s). Donde la primera seleccion de caja tiene igual probabilidad 1/3 cada una.
Caso 1- (Regalo = 1). En ese caso las opciones de eleccion de la caja correcta tienen
probabilidad 1/6 ya que el presentador puede elegir cualquiera de las otras dos cajas. 
Caso 2- (Regalo = 2 o Regalo = 3) las opciones donde se selecciona la caja incorrecta tienen probabilidad 1/3.
(El presentador solo tiene un unico camino posible para seleccionar la otra caja incorrecta)
""",
]


# %% [markdown]
# ### Historia
#
# En los últimos siglos hubieron muchos avances científicos.
# En los últimos años, en particular, se han producido enormes avances en el área de la inteligencia artificial.
# ¿Cuándo ocurrió el primer uso conocido del actual sistema de razonamiento para contextos de incertidumbre?
#
# 0. Siglo 21
# 1. Siglo 20
# 2. Siglo 19
# 3. Siglo 18
# 4. Siglo 17
# 5. Antes

# %%
respuestas["Historia"] = [
0, # 0. Siglo 21
0, # 1. Siglo 20
0, # 2. Siglo 19
0.5, # 3. Siglo 18
0.4, # 4. Siglo 17
0.1, # 5. Antes
"""
Justifique:
Interpreto la expresión "actual sistema de razonamiento para contextos de
incertidumbre" como una referencia al sistema basado en las reglas de la
probabilidad.

Respuestas posibles:
i) Según las diapositivas de la clase, en el siglo XVIII "nace la
probabilidad (soluciones analíticas)", por lo que asigno alta creencia
a esta opción.

ii) Sin embargo, históricamente existe evidencia importante a favor del
siglo XVII. La correspondencia entre Blaise Pascal y Pierre de Fermat de 1654 suele
considerarse uno de los orígenes de la teoría matemática de la probabilidad.
Posteriormente, Christiaan Huygens publica en 1657 uno de los primeros
tratados sistemáticos sobre probabilidad. Por este motivo asigno también
una creencia alta al siglo XVII.

iii) Existen otros intentos anteriores de registros de sistemas de razonamiento de incertidumbre anteriores
al siglo 17 como por ejemplo:
(a) El poema "De Vetula" (Siglo XIII): Un poema en latín de autor desconocido que incluye la primera 
enumeración exacta de todas las formas posibles en que pueden caer tres dados (las 216 combinaciones posibles)
(b) Fra Luca Pacioli (1494): contabilidad Summa de arithmetica..., propuso por escrito una versión temprana 
del problema de los puntos (cómo repartir las apuestas si un juego se interrumpe)
Pero estos antecedentes no son necesariamente usos del "sistema actual de razonamiento" probabilistico.
por lo que asigno una creencia menor.
""",
]


# %% [markdown]
# ### Conjunta
#
# La distribución de creencias conjunta sobre varias variables se puede descomponer como el producto de la probabilidad marginal de cualquiera de las variables, multiplicado por la probabilidad condicional del resto de las variables dada la primera variable (usada en la marginal).
#
# 1. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Conjunta"] = [
1, # 0. Siempre
0, # 1. A veces
0, # 2. Nunca
"""
Justifique:
Por la regla del producto, una distribución conjunta puede descomponerse
tomando como marginal cualquiera de sus variables y multiplicándola por
la distribución condicional del resto de las variables.
""",
]


# %% [markdown]
# ### Independencia (REVISAR ENUNCIADO CONDICINAL)
#
# Si A es independiente de B sabemos que P(A|B) = P(B). ¿Pero es cierta la siguiente igualdad: P(A)P(B|A) = P(A)P(B)?
#
# 0. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Independencia"] = [
1, # 0. Siempre
0, # 1. A veces
0, # 2. Nunca
"""
Justifique:
Por propiedad de independencia P(B|A) = P(B). 
Luego se multiplica en ambos lados por P(A) y se forma la igualdad P(A)P(B|A) = P(A)P(B).
""",
]


# %% [markdown]
# ### Descomposiciones
#
# Sabemos que siempre existe alguna forma de descomponer la distribución conjunta como el producto de distribuciones condicionales unidimensionales.
# ¿Si hay N variables, cuántas descomposiciones en total existen?
#
# 0. 1
# 1. N - 1
# 2. N
# 3. N * (N - 1)
# 4. N * N
# 5. N! - 1
# 6. N!
# 7. N ^ N - 1
# 8. N ^ N

# %%
respuestas["Descomposiciones"] = [
0, # 0. 1
0, # 1. N - 1
0, # 2. N
0, # 3. N * (N - 1)
0, # 4. N * N
0, # 5. N! - 1
1, # 6. N!
0, # 7. N ^ N - 1
0, # 8. N ^ N
"""
Justifique:
Contar las descomposiciones es exactamente contar las permutaciones de las N variables.
Si hay N variables, hay N! órdenes posibles y cada orden forma una descomposición distinta.
""",
]


# %% [markdown]
# ### Teorema de Bayes.
#
# El teorema de Bayes nos permite actualizar las creencias de las hipótesis internas a los modelos causales dado los datos.
# El denominador del teorema de Bayes es constante para las diferentes hipótesis.
#
# 0. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Teorema de Bayes"] = [
0.95, # 0. Siempre
0.05, # 1. A veces
0, # 2. Nunca
"""
Justifique:
i) Para hipótesis internas a un mismo modelo, el teorema de Bayes puede
escribirse como:

P(H_i|D,M) = P(D|H_i,M)P(H_i|M) / P(D|M).

Al considerar las diferentes hipótesis H_i, el denominador P(D|M) no
depende de H_i. Por lo tanto, es constante respecto de las diferentes
hipótesis.

ii) Asigno una pequeña creencia a "A veces" debido a una posible ambigüedad en
la palabra "constante". P(D|M) no es una constante absoluta: si cambian los
datos D o el modelo M, el valor de la evidencia también puede cambiar. 

""",
]



# %% [markdown]
# ### Predicciones
#
# La predicción que una hipótesis H hace de un conjunto de datos, P(Datos = {d1, ..., d_n} | H), puede calcularse como el producto de las predicciones que la hipótesis hace de cada dato individual dado los datos ya vistos, P(d1|H)P(d2|d1,H)...
# Para que el cálculo sea correcto es importante que se respete el orden en el cual los datos fueron observados en los hechos, es decir, que no ocurra P(d2|H)P(d1|d2,H)..
#
# 0. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Predicciones"] = [
0, # 0. Siempre
0, # 1. A veces
1, # 2. Nunca
"""
Justifique:
Por la regla del producto, la probabilidad conjunta de los datos puede
descomponerse siguiendo cualquier orden, siempre que las probabilidades
condicionales se modifiquen consistentemente con el orden elegido.
""",
]


# %% [markdown]
# ### Valor de verdad
#
# Si una hipótesis predice con 0 uno de los datos observados, la hipótesis se hace falsa.
#
# 0. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Valor de verdad"] = [
1, # 0. Siempre
0, # 1. A veces
0, # 2. Nunca
"""
Justifique:
Por la regla del producto, la predicción del conjunto de datos puede
escribirse como:
P(D|H) = P(d1|H)P(d2|d1,H)...P(dn|d1,...,d_{n-1},H).

Si cualquiera de estos factores es 0, entonces todo el producto es 0:

Por lo que, aplicando regla de bayes, P(H|D) tambien es cero. Es decir, si la hipótesis asignaba probabilidad
cero a un dato que efectivamente fue observado, pierde toda su creencia posterior y queda falseada.
""",
]


# %% [markdown]
# ### Teorías causales
#
# Históricamente todas las ciencias con datos, desde la física hasta las ciencias sociales, explicaron el mundo a través de teorías causales.
# Los recientes avances en el área de aprendizaje automático e inteligencia artificial, sin embargo, se produjeron por el desarrollo de algoritmos altamente predictivos sin ninguna interpretación causal.
# ¿Qué relación hay entre los modelos causal y los complejos algoritmos de AI/ML?
#
# 0. El modelo causal que se corresponde con la realidad causal subyacente nunca puede ser mejor prediciendo que los complejos algoritmos de AI/ML.
# 1. El modelo causal que se corresponde con la realidad causal subyacente a veces puede ser mejor, y a veces peor, que los complejos algoritmos de AI/ML.
# 2. El modelo causal que se corresponde con la realidad causal subyacente nunca puede ser peor prediciendo que los complejos algoritmos de AI/ML.
# 3. No son comparables porque los modelos causales solo explican, no predicen.
# 4. Ninguna de las anteriores

# %%
respuestas["Teorías causales"] = [
0, # 0. El modelo causal que se corresponde con la realidad causal subyacente nunca puede ser mejor prediciendo que los complejos algoritmos de AI/ML.
0.99, # 1. El modelo causal que se corresponde con la realidad causal subyacente a veces puede ser mejor, y a veces peor, que los complejos algoritmos de AI/ML.
0.01, # 2. El modelo causal que se corresponde con la realidad causal subyacente nunca puede ser peor prediciendo que los complejos algoritmos de AI/ML.
0, # 3. No son comparables porque los modelos causales solo explican, no predicen.
0, # 4. Ninguna de las anteriores
"""
Justifique:
i) La opcion 4 se descarta porque las opciones 0, 1 y 2 0, 1 y 2 cubren todo el espacio de posibilidades de comparación entre
un modelo causal y un modelo algoritmico de IA/ML

ii) La opcion 3 tambien se le puede asignar probabilidad 0, porque los modelos causales se caractizan por su capacidad
de asignar probabilidad a los datos. Ademas si el modelo se corresponde con el verdadero proceso
causal generador, induce la distribución probabilística correcta de los datos. 
(Si son comparables ambos modelos incluso dando valores erroneos)

iii) Al comparar el rendimiento predictivo sobre datos observacionales, un modelo causal no tiene por qué ser siempre 
mejor ni siempre peor que un algoritmo de AI/ML. El rendimiento puede depender de la información disponible, 
de las variables utilizadas, de la especificación del modelo y de cómo fueron estimados sus parámetros.
""",
]


# %% [markdown]
# ### Predicción e información
#
# Cuanto mejor se predice más información (de Shannon) se obtiene.
#
# 0. Siempre
# 1. A veces
# 2. Nunca


# %%
respuestas["Predicción e información"] = [
0, # 0. Siempre
0, # 1. A veces
1, # 2. Nunca
"""
Justifique:
La entropía de Shannon puede interpretarse como una medida de nuestra incertidumbre acerca del valor de X.
Mejor Prediccion o Mayor Probabilidad <-> Menor Sorpresa o Informacion de Shanon

Si sabemos que X siempre va a ocurrir P(X) = 1 entonces no hay sorpresa de Shanon, 
pero si X es un resultado poco probable, entonces el aprendizaje es mas alto con los datos observados.

La funcion es estrictamente decreciente: I(x)=−logP(x)
""",
]


# %% [markdown]
# ### Modelos e información
#
# Al evaluar modelos causales, preferimos el que acumula más información (de Shannon).
#
# 0. Siempre
# 1. A veces
# 2. Nunca


# %%
respuestas["Modelos e información"] = [
0, # 0. Siempre
0.01, # 1. A veces
0.99, # 2. Nunca
"""
Justifique
i) En general se comparan modelos bajo mismo conjunto de Datos (No esta especificado).
La información de Shannon acumulada por un modelo se define como
I(Datos|Modelo) = -log P(Datos|Modelo),

Cuanto mejor predice un modelo los datos observados, mayor es
P(Datos|Modelo) y, por lo tanto, menor es -log P(Datos|Modelo

ii) Si un modelo tiene mas Datos que otro, puede tener mayor informacion de Shannon acumulada e igualmente
ser mejor modelo prediciendo.
""",
]

# %% [markdown]
# ### Evaluación de modelos
#
# Podemos identificar el modelo causal correcto si observamos suficientes datos.
#
# 0. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Evaluación de modelos"] = [
0, # 0. Siempre
1, # 1. A veces
0, # 2. Nunca
"""
Justifique
Segun Koller con datos observacionales solamente, en general no se puede determinar una estructura 
causal única ni siquiera con infinitos datos; como máximo puede identificarse una clase de equivalencia.
Eso tampoco quita que a veces si pueda lograrse.
Al ser todas opciones excluyentes se elige solo la opcion 1.
""",
]

# %% [markdown]
# ### Contrafactuales
#
# Cuando conocemos los mecasnimos causales probabilísticos de cada variable podemos usar la información factual para predecir cuál hubiera sido un resultado contrafactual.
#
# 0. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Contrafactuales"] = [
0, # 0. Siempre
1, # 1. A veces
0, # 2. Nunca
"""
Justifique
i) Siempre no pasa porque hay contrafactuales que no quedan determinados por la información factual
y los mecanismos probabilísticos disponibles.

ii) Nunca tampoco porque en ciertos modelos la información factual sí restringe suficientemente el mecanismo 
y permite calcular una distribución contrafactual.
""",
]



# %% [markdown]
# ### Diversificación
#
# Una casa de apuestas nos paga 3 por Cara y 1.2 por Sello por el lanzamiento de moneda.
# La moneda es normal, con 0.5 de probabilidad de que salga Cara o Sello.
# Supongamos que nos ofrecen jugar 10000 veces, pero apostando absolutamente todos los recursos en cada paso temporal.
# Apostamos todo, nos devuelven actualizado y volvemos a apostar.
# ¿Qué proporción conviene apostar a Cara?
# Notar que el resto se asigna a Sello.
# Notar además que si apostamos todo a Cara y sale Sello perdemos todos los recursos y no podemos volver a jugar (solo nos pagan en el lado donde sale la moneda).
#
# 0. Recursos asignados a Cara: 0.0
# 1. Recursos asignados a Cara: 0.1
# 2. Recursos asignados a Cara: 0.2    
# 3. Recursos asignados a Cara: 0.3
# 4. Recursos asignados a Cara: 0.4
# 5. Recursos asignados a Cara: 0.5
# 6. Recursos asignados a Cara: 0.6
# 7. Recursos asignados a Cara: 0.7
# 8. Recursos asignados a Cara: 0.8
# 9. Recursos asignados a Cara: 0.9
# 10. Recursos asignados a Cara: 1.0

# %%
respuestas["Diversificación"] = [
0, # 0. Recursos asignados a Cara: 0.0
0, # 1. Recursos asignados a Cara: 0.1
0, # 2. Recursos asignados a Cara: 0.2
0, # 3. Recursos asignados a Cara: 0.3
0.02, # 4. Recursos asignados a Cara: 0.4
0.96, # 5. Recursos asignados a Cara: 0.5
0.02, # 6. Recursos asignados a Cara: 0.6
0, # 7. Recursos asignados a Cara: 0.7
0, # 8. Recursos asignados a Cara: 0.8
0, # 9. Recursos asignados a Cara: 0.9
0, # 10. Recursos asignados a Cara: 1.0
"""
Justifique:

Se evaluaron por simulación todas las proporciones posibles entre 0 y 1,
en pasos de 0.1.

Para cada proporción f asignada a Cara, el resto 1-f se asignó a Sello.
En cada tirada el capital se actualizó multiplicándolo por 3*f si salía
Cara y por 1.2*(1-f) si salía Sello.

Se simularon muchas secuencias largas de lanzamientos y se repitió cada
experimento varias veces para reducir el efecto del azar de una única
secuencia.

Al comparar el crecimiento obtenido por las distintas estrategias, la
proporción f = 0.5 produjo sistemáticamente el mejor comportamiento de
largo plazo entre las alternativas consideradas.

Por lo tanto, la simulación sugiere asignar 50% de los recursos a Cara
y 50% a Sello.
""",
]


# %% [markdown]
# ### Apuesta individual
#
# Una casa de apuestas paga 3 por Cara y 1.2 por Sello. La moneda tiene 0.5 de probabilidad de que salga Cara o Sello.
# Nos ofrecen jugar 10000 veces, apostando en cada ocasión todos nuestros recursos, 50% a Cara y 50% a Sello.
# ¿Nos conviene jugar?
# Notar que cuando sale Cara, crecen nuestros recursos 50% (Si teníamos 100, pusimos 50 en Cara y nos pagaron 3*50=150).
# Notar que cuando sale Sello, crecen nuestros recursos -40% (Si teníamos 100, pusimos 50 en Cara y nos pagaron 1.2*50=60).
#
# 0. No
# 1. Sí

# %%
respuestas["Apuesta individual"] = [
1, # 0. No
0, # 1. Sí
"""
Justifique:

Como Cara y Sello tienen ambos probabilidad 0.5, en una cantidad muy
grande de lanzamientos esperamos aproximadamente la misma cantidad de
Caras y Sellos.
Por cada par formado por una Cara y un Sello, los recursos se
multiplican de la siguiente forma: Capital_t2 = Capital_t1*(1.5 * 0.6) = Capital_t1*0.9
En 10000 lanzamientos esperamos aproximadamente 5000 Caras y
5000 Sellos, por lo que el capital final será aproximadamente 
Capita_final = Capital_inicial * (0.9)^5000 -> 0


""",
]


# %% [markdown]
# ### Teoría de utilidad esperada
#
# La teoría de utilidad esperada dice que debemos aceptar una apuesta cuando la utilidad esperada es positiva.
# Supongamos que elegimos una apuesta que nos garantiza crecer 50% cuando sale Cara y caer solo 40% cuando sale Sello (el caso anterior).
# Notar que la esperanza de los recursos es positiva, crece a 5% por paso temporal ((150+60)/2=210/2=105).
# Supongamos que nos ofrecen jugar 10000 veces en un instante, usando absolutamente todos los recursos.
# ¿No conviene jugar?
#
# 0. Siempre
# 1. A veces
# 2. Nunca

# %%
respuestas["Teoría de Utilidad Esperada"] = [
0, # 0. Siempre
1, # 1. A veces
0, # 2. Nunca
"""
Justifique
La probabilidad de Cara y Sello es p = 0.5, pero el enunciado no
especifica la función de utilidad U(w). Por lo tanto, la conveniencia
de aceptar la apuesta depende de cómo el jugador valora su riqueza.

i) Si el jugador es neutral al riesgo, U(w) = w, etonces
E[X] = 0.5*1.5 + 0.5*0.6 = 1.05 > 1 y E[W_10000] = W_0*(1.05)^10000 > W_0.
Si le conviene jugar

ii) Si el jugador tiene utilidad logarítmica, U(w) = ln(w)
E[ln(X)] = 0.5*ln(1.5) + 0.5*ln(0.6) = 0.5*ln(0.9) < 0. 
No le conviene jugar

""",
]


# %% [markdown]
# ### Fondo común
#
# Supongamos que ya estamos jugando una apuesta que nos garantiza crecer 50% cuando sale Cara y caer solo 40% cuando sale Sello.
# ¿Nos conviene juntarnos con alguien, y al final de cada paso temporal poner todos los recursos en un fondo común y dividirlos en partes iguales?
#
#
# 0. No conviene
# 1. Indistinto
# 2. Sí conviene

# %%
respuestas["Fondo común"] = [
0, # 0. No conviene
0.05, # 1. Indistinto
0.95, # 2. Sí conviene
"""
Justifique:
Aca hay dos escenarios posibles
i) Si son en apuestas distintas, rebalancear a partes iguales reduce la varianza. Esto reduce volatilidad y 
permite converger mas rapido en valor esperado.

ii) Si ambos participantes están expuestos exactamente al mismo resultado de la apuesta, el fondo común es indistinto, 
ya que ambos recursos se multiplican por el mismo factor y repartirlos nuevamente no modifica el resultado.

Supongo que el escenario (i) es el planteado para este escenario y el (ii) no es lo pedido por el enunciado
""",
]


# %% [markdown]
# ### Impuestos
#
# Supongamos que ya estamos jugando una apuesta que nos garantiza crecer 50% cuando sale Cara y caer solo 40% cuando sale Sello, y ya estamos hace mucho tiempo jugando con un fondo común de en un grupo de 100 personas.
# ¿Qué pasa con la tasa de crecimiento de nuestros recursos si logramos encontrar la forma de dejar de aportar nuestra cuota al fondo común mientras tenemos garantizado que seguimos recibimos la cuota del fondo en partes iguales?
#
# 0. Disminuye
# 1. No cambia
# 2. Aumenta

# %%
respuestas["Impuestos"] = [
0, # 0. Disminuye
0, # 1. No cambia
1, # 2. Aumenta
"""
Justifique:

Al dejar de aportar al fondo pero seguir recibiendo una parte igual, el jugador conserva el rendimiento
de su propio capital y además recibe una transferencia proveniente de los otros 99 integrantes.

Por lo tanto, si obtenemos Cara nuestros recursos se multiplican
aproximadamente por: 1.5 + 1.0395 = 2.5395

y si obtenemos Sello por: 0.6 + 1.0395 = 1.6395
(donde 1.0395 proviene de (99/100) * 1.05 = 1.0395)

Incluso en el caso desfavorable de Sello, los recursos aumentan
aproximadamente un 64%.
""",
]


