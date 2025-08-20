# 🧪 Guía de Testing con Insomnia

Esta guía te ayudará a importar y usar la colección de Insomnia para probar tu gateway HTTP durante el hackathon.

## 📥 Importar la Colección

### Paso 1: Abrir Insomnia
Asegúrate de tener Insomnia instalado. Si no lo tienes:
- Descarga desde: https://insomnia.rest/download
- Instala la versión gratuita

### Paso 2: Importar
1. Abre Insomnia
2. Clic en **"Create"** → **"Import From"** → **"File"**
3. Selecciona el archivo: `insomnia-tareas-collection.json`
4. Confirma la importación

### Paso 3: Configurar Entorno
Una vez importada, verás varios entornos disponibles:

- **Gateway Node.js**: `http://localhost:3000`
- **Gateway .NET**: `http://localhost:5000`  
- **Gateway Django**: `http://localhost:8000`

Selecciona el entorno que corresponda a tu implementación.

## 📋 Requests Disponibles

### 🔍 **Operaciones CRUD - Tareas**

#### 1. Listar Tareas
- **Método**: GET
- **URL**: `{{base_url}}/tareas`
- **Query Params**:
  - `limite`: Número de tareas (por defecto 10)
  - `desplazamiento`: Offset para paginación (por defecto 0)

**Respuesta esperada**:
```json
{
  "datos": [
    {
      "id": "uuid-here",
      "titulo": "Estudiar para examen",
      "descripcion": "Repasar capítulos 1-5 de matemáticas",
      "prioridad": 5,
      "completada": false,
      "fecha_creacion": "2025-08-19T20:00:00Z",
      "fecha_actualizacion": "2025-08-19T20:00:00Z"
    }
  ],
  "total": 3
}
```

#### 2. Obtener Tarea por ID
- **Método**: GET
- **URL**: `{{base_url}}/tareas/{{tarea_id}}`

**Variable**: Cambia `{{tarea_id}}` por un ID real de las tareas listadas.

#### 3. Crear Nueva Tarea
- **Método**: POST
- **URL**: `{{base_url}}/tareas`
- **Body** (JSON):
```json
{
  "titulo": "Completar proyecto de hackathon",
  "descripcion": "Implementar gateway HTTP que consuma el servicio gRPC de tareas",
  "prioridad": 5,
  "completada": false
}
```

#### 4. Actualizar Tarea Completa
- **Método**: PUT
- **URL**: `{{base_url}}/tareas/{{tarea_id}}`
- **Body** (JSON):
```json
{
  "titulo": "Proyecto de hackathon actualizado",
  "descripcion": "Implementar y probar gateway HTTP con todos los métodos CRUD",
  "prioridad": 4,
  "completada": true
}
```

#### 5. Modificar Tarea Parcial
- **Método**: PATCH
- **URL**: `{{base_url}}/tareas/{{tarea_id}}`
- **Body** (JSON):
```json
{
  "completada": true,
  "prioridad": 2
}
```

#### 6. Eliminar Tarea
- **Método**: DELETE
- **URL**: `{{base_url}}/tareas/{{tarea_id}}`
- **Respuesta**: 204 No Content

### ⚠️ **Pruebas de Validación**

#### Validación: Título Requerido
- **Request**: POST `/tareas` sin título
- **Respuesta esperada**: 400 Bad Request
```json
{
  "error": "titulo_requerido"
}
```

#### Validación: Prioridad Inválida
- **Request**: POST `/tareas` con prioridad > 5
- **Respuesta esperada**: 400 Bad Request
```json
{
  "error": "prioridad_invalida"
}
```

## 🎯 Flujo de Testing Recomendado

### 1. Verificar Servidor
Primero, asegúrate que tu gateway funciona:
- Ejecuta el request **GET** a la raíz: `{{base_url}}/`
- Debe retornar el mensaje "Hello World"

### 2. Probar Operaciones Básicas
1. **Listar tareas** - Debe mostrar las 3 tareas predefinidas
2. **Obtener tarea** - Copia un ID y prueba obtenerla
3. **Crear tarea** - Crea una nueva con datos válidos

### 3. Probar Actualizaciones
1. **PUT** - Actualiza completamente una tarea
2. **PATCH** - Modifica solo algunos campos

### 4. Probar Validaciones
1. Ejecuta los requests de validación
2. Verifica que retornen errores 400 apropiados

### 5. Probar Eliminación
1. **DELETE** una tarea
2. Verifica que retorne 204
3. Intenta obtenerla de nuevo (debe dar 404)

## 📊 Códigos de Respuesta HTTP

| Código | Significado | Cuándo se usa |
|--------|-------------|---------------|
| 200 | OK | GET, PUT, PATCH exitosos |
| 201 | Created | POST exitoso |
| 204 | No Content | DELETE exitoso |
| 400 | Bad Request | Validaciones fallidas |
| 404 | Not Found | Tarea no encontrada |
| 500 | Internal Server Error | Error del servidor/gRPC |

## 💡 Tips para el Testing

### Variables de Entorno
Puedes modificar las variables del entorno:
- `base_url`: Cambia si usas otro puerto
- `tarea_id`: Actualiza con IDs reales de tus tareas

### Debugging
- Usa la pestaña **Timeline** para ver requests/responses
- Revisa los **Headers** para debugging
- Usa **Console** si necesitas ver logs

### Automatización
- Puedes crear **Tests** en cada request para automatizar validaciones
- Usa **Pre-request Scripts** para setup dinámico

