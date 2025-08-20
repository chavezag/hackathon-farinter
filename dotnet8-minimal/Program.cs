var builder = WebApplication.CreateBuilder(args);

// TODO: Configurar cliente gRPC aquí
// builder.Services.AddGrpcClient<...>

var app = builder.Build();

// Endpoint básico de prueba
app.MapGet("/", () => new
{
    Mensaje = "¡Hola Mundo! Gateway de Tareas .NET funcionando",
    Timestamp = DateTime.UtcNow,
    Puerto = app.Environment.IsDevelopment() ? 5000 : 80
});

// Endpoint de salud
app.MapGet("/salud", () => new
{
    Estado = "ok",
    Servicio = "Gateway Tareas .NET 8",
    Version = "1.0.0"
});

// TODO: Implementar endpoints para tareas:
// app.MapGet("/tareas", async () => { /* Listar tareas */ });
// app.MapGet("/tareas/{id}", async (string id) => { /* Obtener tarea */ });
// app.MapPost("/tareas", async (CrearTareaRequest request) => { /* Crear tarea */ });
// app.MapPut("/tareas/{id}", async (string id, ActualizarTareaRequest request) => { /* Actualizar tarea */ });
// app.MapPatch("/tareas/{id}", async (string id, ModificarTareaRequest request) => { /* Modificar tarea */ });
// app.MapDelete("/tareas/{id}", async (string id) => { /* Eliminar tarea */ });

app.Run();

// TODO: Definir modelos de request/response aquí
/*
public record CrearTareaRequest(string Titulo, string? Descripcion, int Prioridad, bool Completada);
public record ActualizarTareaRequest(string Titulo, string? Descripcion, int Prioridad, bool Completada);
public record ModificarTareaRequest(string? Titulo, string? Descripcion, int? Prioridad, bool? Completada);
*/