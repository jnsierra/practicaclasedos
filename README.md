# Práctica OpenShift - Aplicación Flask con Comunicación Inter-Servicios

## 📋 Descripción del Proyecto

Esta es una aplicación de práctica para un curso de OpenShift que demuestra:

- Despliegue de una aplicación Flask en contenedores
- Comunicación entre servicios dentro del cluster de OpenShift
- Configuración de recursos Kubernetes (Deployment, Service, ConfigMap, Secret, HPA)
- Uso de variables de entorno y secretos

## 🏗️ Arquitectura

La aplicación consiste en:

- **Aplicación principal**: Flask app que expone un endpoint en el puerto 3000
- **Servicio externo**: Comunica con otro servicio en `mi-servicio.nicolas-sierra-dev.svc.cluster.local:4000`
- **ConfigMap**: Para variables de configuración
- **Secret**: Para datos sensibles como contraseñas
- **HPA**: Auto-escalado horizontal basado en CPU

## 📁 Estructura del Proyecto

```
.
├── app.py              # Aplicación Flask principal
├── Dockerfile          # Imagen de contenedor
├── oc.yaml            # Manifiestos de Kubernetes/OpenShift
└── README.md          # Este archivo
```

## 🚀 Despliegue en OpenShift

### 1. Construir y publicar la imagen Docker

```bash
# Construir la imagen
docker build -t jesusnicolassierra/mi-app-flask:build-<TAG> .

# Publicar en Docker Hub
docker push jesusnicolassierra/mi-app-flask:build-<TAG>
```

### 2. Aplicar los manifiestos de Kubernetes

```bash
# Reemplazar el tag en el archivo YAML
sed 's/{{ tag }}/<TU_TAG>/g' oc.yaml > oc-deploy.yaml

# Aplicar todos los recursos
oc apply -f oc-deploy.yaml
```

### 3. Verificar el despliegue

```bash
# Verificar el estado del deployment
oc get deployment mi-deployment-practica -n nicolas-sierra-dev

# Verificar los pods
oc get pods -l app=mi-app-practica -n nicolas-sierra-dev

# Verificar el servicio
oc get svc mi-servicio-practica -n nicolas-sierra-dev
```

## 🔧 Configuración

### Variables de Entorno (ConfigMap)

- `DATABASE`: Dirección IP de la base de datos (192.168.1.1)

### Secretos

- `PASSWORD`: Contraseña codificada en base64

### Recursos del Contenedor

- **Requests**: CPU 500m, Memory 800Mi
- **Limits**: CPU 1000m, Memory 1500Mi

## 🧪 Pruebas y Validación

### 1. Port Forward para acceso local

```bash
# Hacer port forward al servicio
oc port-forward svc/mi-servicio-practica 3000:4000 -n nicolas-sierra-dev
```

### 2. Probar la aplicación

```bash
# En otra terminal, llamar al servicio
curl localhost:3000
```

### 3. Respuesta esperada

La aplicación debería devolver:

```
Hola Mundo en Practica
--- Servicio Externo (Éxito/Error) ---
URL: http://mi-servicio.nicolas-sierra-dev.svc.cluster.local:4000
Código HTTP: 200
Contenido: [Respuesta del servicio externo]
```

## 📊 Monitoreo

### Verificar logs de la aplicación

```bash
# Ver logs del deployment
oc logs deployment/mi-deployment-practica -n nicolas-sierra-dev

# Seguir logs en tiempo real
oc logs -f deployment/mi-deployment-practica -n nicolas-sierra-dev
```

### Verificar métricas de HPA

```bash
# Ver estado del auto-escalador
oc get hpa mi-hpa -n nicolas-sierra-dev

# Describir HPA para más detalles
oc describe hpa mi-hpa -n nicolas-sierra-dev
```

## 🔍 Resolución de Problemas

### Problemas comunes:

1. **Error de conexión al servicio externo**:

   - Verificar que el servicio de destino esté ejecutándose
   - Comprobar la resolución DNS del cluster

2. **Pod no inicia**:

   - Verificar que la imagen esté disponible en Docker Hub
   - Revisar los logs del pod para errores

3. **Servicio no responde**:
   - Verificar que el selector del Service coincida con las labels del Pod
   - Comprobar que el puerto del contenedor sea correcto

### Comandos útiles para debugging:

```bash
# Describir el deployment
oc describe deployment mi-deployment-practica -n nicolas-sierra-dev

# Ejecutar shell en el pod
oc exec -it deployment/mi-deployment-practica -n nicolas-sierra-dev -- /bin/bash

# Ver eventos del namespace
oc get events -n nicolas-sierra-dev
```

## 📚 Recursos Adicionales

- [Documentación oficial de OpenShift](https://docs.openshift.com/)
- [Guía de Flask](https://flask.palletsprojects.com/)
- [Best practices para Kubernetes](https://kubernetes.io/docs/concepts/configuration/overview/)

---

**Nota**: Asegúrate de reemplazar `<TAG>` con el tag específico de tu imagen antes del despliegue.
