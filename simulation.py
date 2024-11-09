import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


alpha, beta, gamma = 0.03, 0.02, 0.02   
delta, epsilon, zeta = 0.02, 0.03, 0.015 
A0, U0 = 0.6, 0.4 


def modelo(variables, t):
    A, U = variables
    dA_dt = alpha * U + beta * 1.0 - gamma * A
    dU_dt = delta * A + epsilon * 1.0 - zeta * U
    return [dA_dt, dU_dt]


tiempo = np.linspace(0, 100, 200)
resultado = odeint(modelo, [A0, U0], tiempo)


plt.figure(figsize=(10, 6))
plt.plot(tiempo, resultado[:, 0], label="Aceptación de Usuarios (A)", color="blue")
plt.plot(tiempo, resultado[:, 1], label="Aceptación de No Usuarios (U)", color="red")
plt.xlabel("Tiempo")
plt.ylabel("Aceptación")
plt.legend()
plt.title("Simulación de aceptación del metro en Bogotá")
plt.grid(True)
plt.show()
