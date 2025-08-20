from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def inicio(request):
    """Vista básica de prueba"""
    return JsonResponse({
        'mensaje': '¡Hola Mundo! Gateway de Tareas Django funcionando',
        'timestamp': '2025-08-19T20:00:00Z',
        'puerto': 8000
    })

def salud(request):
    """Endpoint de salud del servicio"""
    return JsonResponse({
        'estado': 'ok',
        'servicio': 'Gateway Tareas Django',
        'version': '1.0.0'
    })

# TODO: Implementar las siguientes vistas usando gRPC:

@csrf_exempt
def listar_tareas(request):
    """GET /tareas - Listar tareas con paginación"""
    # TODO: Conectar a gRPC y llamar ListarTareas
    return JsonResponse({'error': 'No implementado aún'}, status=501)

@csrf_exempt
def obtener_tarea(request, tarea_id):
    """GET /tareas/{id} - Obtener tarea por ID"""
    # TODO: Conectar a gRPC y llamar ObtenerTarea
    return JsonResponse({'error': 'No implementado aún'}, status=501)

@csrf_exempt
def crear_tarea(request):
    """POST /tareas - Crear nueva tarea"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    # TODO: Validar datos y conectar a gRPC
    # data = json.loads(request.body)
    # titulo = data.get('titulo')
    # if not titulo:
    #     return JsonResponse({'error': 'titulo_requerido'}, status=400)
    
    return JsonResponse({'error': 'No implementado aún'}, status=501)

@csrf_exempt
def actualizar_tarea(request, tarea_id):
    """PUT /tareas/{id} - Actualizar tarea completa"""
    if request.method != 'PUT':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    # TODO: Conectar a gRPC y llamar ActualizarTarea
    return JsonResponse({'error': 'No implementado aún'}, status=501)

@csrf_exempt
def modificar_tarea(request, tarea_id):
    """PATCH /tareas/{id} - Actualizar tarea parcial"""
    if request.method != 'PATCH':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    # TODO: Conectar a gRPC y llamar ModificarTarea
    return JsonResponse({'error': 'No implementado aún'}, status=501)

@csrf_exempt
def eliminar_tarea(request, tarea_id):
    """DELETE /tareas/{id} - Eliminar tarea"""
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    # TODO: Conectar a gRPC y llamar EliminarTarea
    return JsonResponse({'error': 'No implementado aún'}, status=501)