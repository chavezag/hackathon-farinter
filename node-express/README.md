# Gateway de Tareas - Node.js + Express

Template básico para implementar un gateway HTTP que consuma el servicio gRPC de tareas.

## 🎯 Objetivo del Hackathon

Implementar un gateway HTTP completo que:
1. Se conecte al servidor gRPC de tareas (puerto 50051)
2. Exponga endpoints REST para todas las operaciones CRUD
3. Maneje validaciones y errores apropiadamente
4. Use GitHub Copilot para acelerar el desarrollo

## 🚀 Cómo empezar

### 1. Instalar dependencias
```bash
npm install
```

### 2. Iniciar el servidor
```bash
npm start
# o para desarrollo con auto-reload:
npm run dev
```

### 3. Verificar que funciona
Visita: http://localhost:3000

Deberías ver:
```json
{
  "mensaje": "¡Hola Mundo! Gateway de Tareas funcionando",
  "timestamp": "2025-08-19T20:00:00.000Z",
  "puerto": 3000
}
```

## 📋 Tareas a implementar

### Paso 1: Configurar cliente gRPC
- Crear archivo `cliente-grpc.js`
- Cargar el proto `tareas.proto` (disponible en carpeta raíz)
- Conectar al servidor gRPC en `172.16.2.231:50051` ✅ **YA DESPLEGADO**

```javascript
const clienteTareas = new tareasProto.ServicioTareas(
  '172.16.2.231:50051',
  grpc.credentials.createInsecure()
);
```

### Paso 2: Implementar endpoints REST

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/tareas` | Listar tareas (con paginación: `?limite=10&desplazamiento=0`) |
| GET | `/tareas/:id` | Obtener tarea por ID |
| POST | `/tareas` | Crear nueva tarea |
| PUT | `/tareas/:id` | Actualizar tarea completa |
| PATCH | `/tareas/:id` | Actualizar tarea parcial |
| DELETE | `/tareas/:id` | Eliminar tarea |

### Paso 3: Validaciones requeridas
- **Título**: Requerido, no vacío
- **Prioridad**: Número entre 1 y 5
- **Descripción**: Opcional
- **Completada**: Boolean, por defecto false

### Paso 4: Manejo de errores
- 400 Bad Request: Validaciones fallidas
- 404 Not Found: Tarea no encontrada  
- 500 Internal Server Error: Errores del servidor gRPC

## 🔧 Estructura del proyecto sugerida

```
node-express/
├── package.json
├── servidor.js          ← Servidor principal (¡YA EXISTE!)
├── cliente-grpc.js      ← Cliente gRPC (CREAR)
├── rutas/
│   └── tareas.js        ← Rutas de tareas (CREAR)
└── utils/
    ├── validaciones.js  ← Validaciones (CREAR)
    └── errores.js       ← Manejo de errores (CREAR)
```

## 💡 Tips para usar GitHub Copilot

1. **Comenta tu intención** antes de escribir código:
   ```js
   // Configurar cliente gRPC para conectar a servidor de tareas
   ```

2. **Usa nombres descriptivos** en español:
   ```js
   const clienteTareas = // Copilot sugerirá la implementación
   ```

3. **Define interfaces primero**:
   ```js
   // POST /tareas - crear nueva tarea con validación de título y prioridad
   app.post('/tareas', async (req, res) => {
   ```

## ✅ Criterios de evaluación

- ✅ Servidor levanta correctamente en puerto 3000
- ✅ Endpoints REST funcionan y llaman a gRPC  
- ✅ Validaciones implementadas correctamente
- ✅ Manejo de errores apropiado
- ✅ Código limpio y bien estructurado
- ✅ Uso efectivo de GitHub Copilot

## 🆘 ¿Necesitas ayuda?

1. Verifica que el servidor gRPC esté corriendo: `netstat -an | grep 50051`
2. Revisa los ejemplos completos en la carpeta `ejemplos-completos/`
3. Usa la colección de Insomnia para probar: `tests/insomnia-tareas-collection.json`

¡Buena suerte! 🚀