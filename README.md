# 💻 Hackathon Gateway de Tareas con GitHub Copilot

¡Bienvenidos al hackathon de desarrollo utilizando GitHub Copilot! Tu misión es crear un gateway HTTP que consuma un servicio gRPC de gestión de tareas, **usando GitHub Copilot para acelerar tu desarrollo**.

## 🎯 Objetivo

Implementar un **gateway HTTP completo** que:
- Se conecte al servidor gRPC de tareas (ya funcionando)
- Exponga endpoints REST para operaciones CRUD
- Maneje validaciones y errores correctamente
- Demuestre el poder de GitHub Copilot

## 🚀 Integraciones
Crea tu rama `feature/<tu-nombre>` a partir de `main`, para evitar conflictos y mantener un historial limpio.

## ⏱️ Tiempo: 2.5 horas

No pasa nada si no terminas a tiempo, pero trata de avanzar lo más posible.

## 🛠️ Elige tu arma

Selecciona **UNO** de estos templates y conviértelo en una API completa:

### 📁 [Node.js + Express](./node-express/)
- **Puerto**: 3000
- **Lenguaje**: JavaScript/TypeScript

### 📁 [.NET 8 Minimal API](./dotnet8-minimal/)
- **Puerto**: 5000
- **Lenguaje**: C#/.NET

### 📁 [Django](./django-basic/)
- **Puerto**: 8000
- **Lenguaje**: Python


## 📋 API Contract a implementar

Debes implementar estos endpoints que consuman el servidor gRPC:

| Método | Endpoint | Descripción | Respuesta |
|--------|----------|-------------|-----------|
| GET | `/tareas` | Listar tareas (paginado) | `{ datos: [Tarea], total: number }` |
| GET | `/tareas/{id}` | Obtener tarea específica | `Tarea` o 404 |
| POST | `/tareas` | Crear nueva tarea | `Tarea` creada (201) |
| PUT | `/tareas/{id}` | Actualizar tarea completa | `Tarea` actualizada |
| PATCH | `/tareas/{id}` | Actualizar parcial | `Tarea` actualizada |
| DELETE | `/tareas/{id}` | Eliminar tarea | 204 (sin contenido) |

### 📝 Modelo de Tarea

```json
{
  "id": "uuid",
  "titulo": "string (requerido)",
  "descripcion": "string (opcional)",  
  "prioridad": "number (1-5, requerido)",
  "completada": "boolean",
  "fecha_creacion": "ISO date",
  "fecha_actualizacion": "ISO date"
}
```

## ✅ Criterios de evaluación

### Funcionalidad (60%)
- ✅ Servidor levanta correctamente
- ✅ Todos los endpoints implementados
- ✅ Conexión exitosa con gRPC
- ✅ Validaciones funcionando

### Calidad del código (25%)
- ✅ Código limpio y organizado
- ✅ Manejo de errores apropiado
- ✅ Estructura del proyecto coherente

### Uso de GitHub Copilot (15%)
- ✅ Comentarios descriptivos que guíen a Copilot
- ✅ Aprovechamiento de sugerencias
- ✅ Velocidad de desarrollo

## 🚦 Cómo comenzar

### 1. Servidor gRPC ya está desplegado ✅
- **Host**: `172.16.2.231`
- **Puerto**: `50051`

📖 **Documentación completa**: [docs/API-GRPC-DOCUMENTACION.md](./docs/API-GRPC-DOCUMENTACION.md)

### 2. Elegir tu template
```bash
cd hackathon-templates/node-express    # O dotnet8-minimal o django-basic
```

### 3. Leer el README específico
Cada template tiene instrucciones detalladas de setup.

### 4. ¡A programar! 
Usa GitHub Copilot intensivamente. Comenta tu intención antes de escribir código.

## 🧪 Testing

### Usar Insomnia para probar tu API
1. Importar: `insomnia-tareas-collection.json`
2. Cambiar entorno según tu tecnología
3. Probar todos los endpoints

📖 **Guía de testing**: [docs/INSOMNIA-TESTING.md](./docs/INSOMNIA-TESTING.md)

## 🧪 Testing

### Usar Insomnia
1. Importar: `../tests/insomnia-tareas-collection.json`
2. Cambiar entorno según tu tecnología
3. Probar todos los endpoints

### Datos de prueba disponibles
El servidor gRPC ya tiene estas tareas:
- "Estudiar para examen" (prioridad 5, pendiente)
- "Comprar víveres" (prioridad 3, pendiente)  
- "Llamar al dentista" (prioridad 4, completada)

## 💡 Tips para maximizar GitHub Copilot

### ✅ Haz esto:
```javascript
// Crear cliente gRPC para conectar al servidor de tareas en puerto 50051
const clienteTareas = 
```

```csharp
// Endpoint para listar tareas con paginación usando gRPC
app.MapGet("/tareas", async (int? limite, int? desplazamiento) => {
```

```python
# Validar que el título sea requerido y la prioridad esté entre 1-5
def validar_tarea(datos):
```

### ❌ Evita esto:
```javascript
const client = // Sin contexto, Copilot no sabe qué sugerir
```

## 🆘 ¿Problemas?

1. **Servidor gRPC no responde**: Verifica que esté corriendo en puerto 50051
2. **Errores de proto**: Asegúrate de generar los stubs correctamente
3. **CORS/404**: Revisa la configuración de rutas
4. **Ejemplos completos**: Revisa `../ejemplos-completos/` para referencia

## 🏆 ¡Al terminar!

1. Demuestra tu API funcionando
2. Explica cómo usaste GitHub Copilot
3. Comparte lo que aprendiste

---

**¡Que comience el hackathon! 🎉**

*Recuerda: El objetivo no es solo completar la tarea, sino aprender a usar GitHub Copilot efectivamente para acelerar tu desarrollo.*
