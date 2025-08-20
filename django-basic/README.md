# Gateway de Tareas - Django

Template básico para implementar un gateway HTTP que consuma el servicio gRPC de tareas usando Django.

## 🎯 Objetivo del Hackathon

Implementar un gateway HTTP completo que:
1. Se conecte al servidor gRPC de tareas (puerto 50051)
2. Exponga endpoints REST para todas las operaciones CRUD
3. Maneje validaciones y errores apropiadamente
4. Use GitHub Copilot para acelerar el desarrollo

## 🚀 Cómo empezar

### 1. Crear entorno virtual
```bash
python -m venv venv

venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Generar stubs de gRPC
```bash
python -m grpc_tools.protoc -I ../../proto --python_out=. --grpc_python_out=. ../../proto/tareas.proto
```

### 4. Ejecutar servidor
```bash
python manage.py runserver 8000
```

### 5. Verificar que funciona
Visita: http://localhost:8000

Deberías ver:
```json
{
  "mensaje": "¡Hola Mundo! Gateway de Tareas Django funcionando",
  "timestamp": "2025-08-19T20:00:00Z",
  "puerto": 8000
}
```

## 📋 Tareas a implementar

### Paso 1: Generar cliente gRPC
1. Ejecutar comando de generación de stubs (arriba)
2. Crear archivo `cliente_grpc.py` para manejar conexiones
3. Conectar a `172.16.2.231:50051` ✅ **YA DESPLEGADO**
4. Importar en `views.py`

```python
import grpc
import tareas_pb2_grpc

channel = grpc.insecure_channel('172.16.2.231:50051')
cliente = tareas_pb2_grpc.ServicioTareasStub(channel)
```

### Paso 2: Completar vistas en `tareas/views.py`

Las vistas básicas ya están creadas, necesitas:
- Conectar cada vista al cliente gRPC
- Implementar validaciones
- Manejar errores apropiadamente

### Paso 3: Configurar URLs
Actualizar `tareas/urls.py` para manejar todos los métodos HTTP correctamente.

## 🔧 Estructura del proyecto

```
django-basic/
├── requirements.txt
├── manage.py
├── gateway_tareas/
│   ├── settings.py      ← Configuración Django
│   └── urls.py          ← URLs principales
├── tareas/
│   ├── views.py         ← Vistas principales (¡COMPLETAR!)
│   └── urls.py          ← URLs de tareas
└── cliente_grpc.py      ← Cliente gRPC (CREAR)
```

## 💡 Tips para usar GitHub Copilot

1. **Comenta tu intención**:
   ```python
   # Conectar a servidor gRPC de tareas en localhost:50051
   ```

2. **Usa nombres descriptivos**:
   ```python
   def conectar_cliente_tareas():
       # Copilot sugerirá la implementación
   ```

3. **Define estructura primero**:
   ```python
   # POST /tareas - crear nueva tarea con validación
   def crear_tarea(request):
   ```

## ✅ Criterios de evaluación

- ✅ Servidor Django levanta en puerto 8000
- ✅ Endpoints REST funcionan y llaman a gRPC  
- ✅ Validaciones implementadas correctamente
- ✅ Manejo de errores apropiado
- ✅ Código limpio y bien estructurado
- ✅ Uso efectivo de GitHub Copilot

## 🆘 ¿Necesitas ayuda?

1. Verifica que el servidor gRPC esté corriendo: `netstat -an | findstr 50051`
2. Revisa los ejemplos completos en `ejemplos-completos/`
3. Usa la colección de Insomnia: `tests/insomnia-tareas-collection.json`

¡Buena suerte! 🚀