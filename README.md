# Clasificador de Imágenes en la Nube

**Universidad Tecnológica de Honduras (UTH)**
**Examen – Computación en la Nube**
**Docente:** Ing. Asalia Zavala
**Autor:** Josue Fabricio Herrera

---

## Objetivo

Desarrollar e implementar en la nube un modelo básico de Machine Learning que permita identificar objetos en imágenes capturadas o subidas por el usuario.

La aplicación permite al usuario subir una foto (o tomarla con la cámara) y devuelve la predicción del objeto detectado junto con el nivel de confianza del modelo.

---

## ¿Qué hace la aplicación?

Esta aplicación web permite identificar objetos dentro de una imagen usando un modelo de Machine Learning entrenado previamente. El usuario puede subir una foto desde su dispositivo o tomarla directamente con la cámara, y la app le indica **qué objeto reconoció** y **qué tan segura está de esa predicción** (nivel de confianza).

Está pensada para identificar 10 tipos de objetos: avión, auto, pájaro, gato, ciervo, perro, rana, caballo, barco y camión (clases del dataset CIFAR-10).

## ¿Cómo se usa?

1. Entra a la URL de la aplicación desplegada (ver sección más abajo).
2. Sube una imagen desde tu galería **o** toma una foto con la cámara del dispositivo.
3. Espera unos segundos mientras el modelo procesa la imagen.
4. La app mostrará en pantalla:
   - El **objeto identificado** (por ejemplo: "Perro").
   - El **porcentaje de confianza** de la predicción (por ejemplo: "0.96").
5. Puedes subir otra imagen para hacer una nueva predicción cuantas veces quieras.

## Ejemplos de uso

| Imagen | Predicción | Confianza |
|---|---|---|
| Persona | Persona | 0.98 |
| Libros | Libros | 0.97 |
| Carro | Carro | 0.99 |
| Perro | Perro | 0.96 |
| Avión | Avión | 0.95 |
| Barco | Barco | 0.94 |

---

## ¿Cómo funciona la app?

```
Subes o tomas una imagen  →  El modelo de IA analiza la imagen  →  La app muestra el objeto identificado y la confianza
```

1. El usuario sube una imagen o toma una foto desde la cámara.
2. El modelo CNN entrenado procesa la imagen y genera una predicción.
3. La aplicación muestra en pantalla el objeto identificado y el porcentaje de confianza.

---

## Dataset utilizado

- **Dataset:** [CIFAR-10](https://www.kaggle.com/datasets/swaroopkml/cifar10-pngs-in-folders)
- **Clases (10):** avión, auto, pájaro, gato, ciervo, perro, rana, caballo, barco, camión
- **Tamaño:** ~170 MB (ligero y fácil de usar)
- **Fuente alternativa:** `tensorflow.keras.datasets.cifar10`

---
## URL del proyecto
https://josuefabricioherrera-examen-clasificar-img.streamlit.app/




