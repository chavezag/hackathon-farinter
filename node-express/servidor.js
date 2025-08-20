import express from 'express';

const aplicacion = express();
const PUERTO = process.env.PORT || 3000;

// Middleware para parsear JSON
aplicacion.use(express.json());

// Ruta de prueba básica
aplicacion.get('/', (peticion, respuesta) => {
  respuesta.json({ 
    mensaje: '¡Hola Mundo! Gateway de Tareas funcionando',
    timestamp: new Date().toISOString(),
    puerto: PUERTO
  });
});

aplicacion.get('/', (peticion, respuesta) => {
  respuesta.json({ 
    estado: 'ok',
    servicio: 'Gateway Tareas Express',
    version: '1.0.0'
  });
});

// TODO: Aquí deben implementar las rutas para tareas:
// GET /tareas - Listar tareas
// GET /tareas/:id - Obtener tarea por ID
// POST /tareas - Crear nueva tarea
// PUT /tareas/:id - Actualizar tarea completa
// PATCH /tareas/:id - Actualizar tarea parcial
// DELETE /tareas/:id - Eliminar tarea

aplicacion.listen(PUERTO, () => {
  console.log(`🚀 Servidor Express iniciado en puerto ${PUERTO}`);
  console.log(`📝 Visita http://localhost:${PUERTO} para verificar`);
  console.log(`💡 Implementa las rutas de tareas usando gRPC!`);
});