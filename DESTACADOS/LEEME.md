# Destacados de @renuevasmart

Siete destacados, **43 historias** en total, todas a 1080×1920.
Funcionan como un recorrido de venta, no como un escaparate: cada uno responde
una pregunta del prospecto, en este orden.

| # | Destacado | Responde | Historias | De dónde sale el texto |
|---|---|---|---|---|
| 1 | ¿Tu web? | ¿Esto es para mí? | 6 | "Seguro te suena esto" |
| 2 | Servicios | ¿Qué hacen? | 6 | Qué hacemos + Sectores |
| 3 | Proceso | ¿Cómo trabajan? | 7 | Cómo trabajamos (5 pasos) |
| 4 | El caso | ¿Lo hicieron ya? | 6 | Reseñas + capturas reales |
| 5 | Precios | ¿Cuánto cuesta? | 6 | Sin letra chica + FAQ de precio |
| 6 | Preguntas | ¿Qué me frena? | 7 | Preguntas frecuentes |
| 7 | Gratis | ¿Cómo empiezo? | 5 | Muestra gratis |

## Cómo subirlos

1. Subir las historias de una carpeta **en orden de número de archivo**.
2. Crear el destacado y elegir la tapa desde `tapas/tapa-N-nombre.png`.
3. Ponerle de nombre exactamente el de la columna "Destacado". Instagram recorta
   el nombre a unos 15 caracteres, por eso son todos cortos.
4. Mantener el orden de la tabla: el más a la izquierda es el más tocado, y ahí
   tiene que estar el problema, no la presentación de la empresa.

## Reglas del sistema

**El texto sale de renuevasmart.com.** No se redacta de cero. Las dos únicas
adaptaciones permitidas son voseo → tuteo neutro, y "celular" → "teléfono".

**Zona segura.** Instagram tapa unos 230px arriba (barra de progreso, avatar,
nombre) y unos 250px abajo (caja de mensaje). Todo el contenido vive entre
**y=260 y y=1660**. Cada script verifica esto solo antes de exportar y avisa si
algo se sale.

**Las tapas** son de estilo alternado (tinta, naranja, papel rotando), con una
excepción: "Gratis" va siempre en naranja aunque le toque otro color, porque es
la oferta y tiene que destacarse en la fila.

**Nada de nombres genéricos.** Prohibido "Nosotros", "Branding", "Inspiración".
El prospecto tiene que encontrar su problema, no la historia de la empresa.

## Archivos

- `tapas/` — las 7 tapas.
- Una carpeta por destacado con sus historias numeradas.
- Los generadores están en `_fuente/historias_*.py`, uno por destacado, todos
  sobre el mismo `_fuente/_historias.css`. Se edita el texto y se vuelve a correr.
