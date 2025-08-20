# 📡 Documentación API gRPC - Servicio de Tareas

El servidor gRPC de tareas está desplegado y listo para consumir. Esta documentación te ayudará a entender cómo conectarte y usar el servicio.

## 🌐 Información de Conexión

- **Host**: `172.16.2.236`
- **Puerto**: `50051` 
- **Protocolo**: gRPC (HTTP/2)
- **Estado**: ✅ Desplegado y funcionando

## 📋 Proto Definition

El archivo `tareas.proto` define todos los servicios disponibles:

```protobuf
syntax = "proto3";
package tareas;
import "google/protobuf/wrappers.proto";

message Tarea {
  string id = 1;
  string titulo = 2;
  string descripcion = 3;
  int32 prioridad = 4;
  bool completada = 5;
  string fecha_creacion = 6;
  string fecha_actualizacion = 7;
}

service ServicioTareas {
  rpc ObtenerTarea(ObtenerTareaRequest) returns (Tarea);
  rpc ListarTareas(ListarTareasRequest) returns (ListarTareasResponse);
  rpc CrearTarea(CrearTareaRequest) returns (Tarea);
  rpc ActualizarTarea(ActualizarTareaRequest) returns (Tarea);
  rpc ModificarTarea(ModificarTareaRequest) returns (Tarea);
  rpc EliminarTarea(EliminarTareaRequest) returns (Vacio);
}
```

## 🔧 Métodos Disponibles

### 1. ListarTareas
**Descripción**: Obtiene lista paginada de tareas

**Request**:
```protobuf
message ListarTareasRequest {
  int32 limite = 1;        // Máximo 100, por defecto 10
  int32 desplazamiento = 2; // Offset para paginación
}
```

**Response**:
```protobuf
message ListarTareasResponse {
  repeated Tarea datos = 1;
  int32 total = 2;
}
```

### 2. ObtenerTarea
**Descripción**: Obtiene una tarea específica por ID

**Request**:
```protobuf
message ObtenerTareaRequest {
  string id = 1; // UUID de la tarea
}
```

**Response**: `Tarea` o error `NOT_FOUND`

### 3. CrearTarea
**Descripción**: Crea una nueva tarea

**Request**:
```protobuf
message CrearTareaRequest {
  string titulo = 1;       // Requerido, no vacío
  string descripcion = 2;  // Opcional
  int32 prioridad = 3;     // 1-5, por defecto 1
  bool completada = 4;     // Por defecto false
}
```

**Response**: `Tarea` creada con ID generado

### 4. ActualizarTarea
**Descripción**: Actualiza todos los campos de una tarea

**Request**:
```protobuf
message ActualizarTareaRequest {
  string id = 1;           // UUID de la tarea
  string titulo = 2;       // Requerido
  string descripcion = 3;  // Opcional
  int32 prioridad = 4;     // 1-5
  bool completada = 5;     // Boolean
}
```

### 5. ModificarTarea (PATCH)
**Descripción**: Actualiza campos específicos usando wrappers

**Request**:
```protobuf
message ModificarTareaRequest {
  string id = 1;
  google.protobuf.StringValue titulo = 2;
  google.protobuf.StringValue descripcion = 3;
  google.protobuf.Int32Value prioridad = 4;
  google.protobuf.BoolValue completada = 5;
}
```

### 6. EliminarTarea
**Descripción**: Elimina una tarea

**Request**:
```protobuf
message EliminarTareaRequest {
  string id = 1;
}
```

**Response**: `Vacio` (empty message)

## ⚠️ Validaciones y Errores

### Validaciones
- **Título**: Requerido, no puede estar vacío
- **Prioridad**: Debe estar entre 1 y 5
- **ID**: Debe ser un UUID válido para operaciones de obtener/actualizar/eliminar

### Códigos de Error gRPC
- `INVALID_ARGUMENT` (3): Validación fallida
  - `titulo_requerido`: Falta el título
  - `prioridad_invalida`: Prioridad fuera del rango 1-5
  - `sin_campos_para_actualizar`: PATCH sin campos a modificar
- `NOT_FOUND` (5): Tarea no encontrada
  - `tarea_no_encontrada`: ID no existe
- `INTERNAL` (13): Error interno del servidor

## 📊 Datos de Prueba Disponibles

El servidor tiene estas tareas predefinidas:

1. **Estudiar para examen**
   - Descripción: "Repasar capítulos 1-5 de matemáticas"
   - Prioridad: 5
   - Completada: false

2. **Comprar víveres**
   - Descripción: "Lista: pan, leche, huevos, frutas"
   - Prioridad: 3
   - Completada: false

3. **Llamar al dentista**
   - Descripción: "Agendar cita para limpieza dental"
   - Prioridad: 4
   - Completada: true

## 🔌 Ejemplos de Conexión

### Node.js
```javascript
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

const packageDefinition = protoLoader.loadSync('tareas.proto');
const tareasProto = grpc.loadPackageDefinition(packageDefinition).tareas;

const cliente = new tareasProto.ServicioTareas(
  '172.16.2.231:50051',
  grpc.credentials.createInsecure()
);
```

### .NET
```csharp
using Grpc.Net.Client;

var channel = GrpcChannel.ForAddress("http://172.16.2.231:50051");
var client = new ServicioTareas.ServicioTareasClient(channel);
```

### Python
```python
import grpc
import tareas_pb2_grpc

channel = grpc.insecure_channel('172.16.2.231:50051')
client = tareas_pb2_grpc.ServicioTareasStub(channel)
```

## 🧪 Testing con gRPC

Puedes probar directamente con herramientas como:
- **grpcurl**: Para testing desde línea de comandos
- **BloomRPC**: GUI para testing gRPC
- **Postman**: Soporte nativo para gRPC

### Ejemplo con grpcurl:
```bash
# Listar tareas
grpcurl -plaintext 172.16.2.231:50051 tareas.ServicioTareas/ListarTareas

# Obtener tarea específica
grpcurl -plaintext -d '{"id": "uuid-aquí"}' 172.16.2.231:50051 tareas.ServicioTareas/ObtenerTarea
```

---

**¿Problemas de conexión?**
1. Verifica que puedas hacer ping a `172.16.2.231`
2. Asegúrate que el puerto 50051 esté accesible
3. Revisa que estés usando el proto correcto (`tareas.proto`)