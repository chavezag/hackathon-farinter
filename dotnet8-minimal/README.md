# Gateway de Tareas - .NET 8 Minimal API

Template básico para implementar un gateway HTTP que consuma el servicio gRPC de tareas usando .NET 8 Minimal APIs.

## 🎯 Objetivo del Hackathon

Implementar un gateway HTTP completo que:
1. Se conecte al servidor gRPC de tareas (puerto 50051)
2. Exponga endpoints REST para todas las operaciones CRUD
3. Maneje validaciones y errores apropiadamente
4. Use GitHub Copilot para acelerar el desarrollo

## 🚀 Cómo empezar

### 1. Restaurar paquetes
```bash
dotnet restore
```

### 2. Compilar y ejecutar
```bash
dotnet run
```

### 3. Verificar que funciona
Visita: http://localhost:5000

Deberías ver:
```json
{
  "mensaje": "¡Hola Mundo! Gateway de Tareas .NET funcionando",
  "timestamp": "2025-08-19T20:00:00.000Z",
  "puerto": 5000
}
```

## 📋 Tareas a implementar

### Paso 1: Configurar gRPC
1. **Descomenta y configura** la referencia al proto en `GatewayTareas.csproj`:
   ```xml
   <ItemGroup>
     <Protobuf Include="..\..\proto\tareas.proto" GrpcServices="Client" Link="Protos\tareas.proto" />
   </ItemGroup>
   ```

2. **Registra el cliente gRPC** en `Program.cs`:
   ```csharp
   builder.Services.AddGrpcClient<ServicioTareas.ServicioTareasClient>(options =>
   {
       options.Address = new Uri("http://172.16.2.231:50051"); // ✅ YA DESPLEGADO
   });
   ```

### Paso 2: Implementar endpoints REST

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/tareas` | Listar tareas (con query params: `limite` y `desplazamiento`) |
| GET | `/tareas/{id}` | Obtener tarea por ID |
| POST | `/tareas` | Crear nueva tarea |
| PUT | `/tareas/{id}` | Actualizar tarea completa |
| PATCH | `/tareas/{id}` | Actualizar tarea parcial |
| DELETE | `/tareas/{id}` | Eliminar tarea |

### Paso 3: Definir modelos
Descomenta y ajusta los modelos en `Program.cs`:
```csharp
public record CrearTareaRequest(string Titulo, string? Descripcion, int Prioridad, bool Completada);
public record ActualizarTareaRequest(string Titulo, string? Descripcion, int Prioridad, bool Completada);
public record ModificarTareaRequest(string? Titulo, string? Descripcion, int? Prioridad, bool? Completada);
```

### Paso 4: Validaciones requeridas
- **Título**: Requerido, no vacío
- **Prioridad**: Número entre 1 y 5
- **Descripción**: Opcional
- **Completada**: Boolean, por defecto false

### Paso 5: Manejo de errores
```csharp
// Mapear errores gRPC a HTTP status codes
catch (RpcException ex) when (ex.StatusCode == StatusCode.NotFound)
{
    return Results.NotFound(new { error = "tarea_no_encontrada" });
}
catch (RpcException ex) when (ex.StatusCode == StatusCode.InvalidArgument)
{
    return Results.BadRequest(new { error = ex.Status.Detail });
}
```

## 🔧 Estructura del proyecto sugerida

```
dotnet8-minimal/
├── GatewayTareas.csproj  ← Configuración del proyecto
├── Program.cs            ← Servidor principal (¡YA EXISTE!)
├── Servicios/
│   └── TareasService.cs  ← Lógica de negocio (CREAR)
├── Modelos/
│   ├── Requests.cs       ← Modelos de petición (CREAR)
│   └── Responses.cs      ← Modelos de respuesta (CREAR)
└── Utils/
    ├── Validaciones.cs   ← Validaciones (CREAR)
    └── ErrorMapper.cs    ← Mapeo de errores (CREAR)
```

## 💡 Tips para usar GitHub Copilot

1. **Comenta tu intención** antes de escribir código:
   ```csharp
   // Configurar cliente gRPC para conectar a servidor de tareas en puerto 50051
   ```

2. **Usa nombres descriptivos** en español:
   ```csharp
   app.MapGet("/tareas", async (ServicioTareas.ServicioTareasClient cliente) => {
   ```

3. **Define firmas de métodos primero**:
   ```csharp
   // POST /tareas - crear nueva tarea con validación de título y prioridad
   app.MapPost("/tareas", async (CrearTareaRequest request, ServicioTareas.ServicioTareasClient cliente) => {
   ```

## ✅ Criterios de evaluación

- ✅ Servidor levanta correctamente en puerto 5000
- ✅ Endpoints REST funcionan y llaman a gRPC  
- ✅ Validaciones implementadas correctamente
- ✅ Manejo de errores apropiado (RpcException → HTTP Status)
- ✅ Código limpio y bien estructurado
- ✅ Uso efectivo de GitHub Copilot

## 🔧 Comandos útiles

```bash
# Restaurar dependencias
dotnet restore

# Compilar
dotnet build

# Ejecutar en modo desarrollo
dotnet run

# Ejecutar con hot reload
dotnet watch run

# Ver información del proyecto
dotnet list package
```

## 🆘 ¿Necesitas ayuda?

1. Verifica que el servidor gRPC esté corriendo: `netstat -an | findstr 50051`
2. Revisa los ejemplos completos en la carpeta `ejemplos-completos/`
3. Usa la colección de Insomnia para probar: `tests/insomnia-tareas-collection.json`
4. Si hay errores de proto, ejecuta: `dotnet build` para regenerar las clases

¡Buena suerte! 🚀