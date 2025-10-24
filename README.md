## Hacemos un port Forward al servicio de la practica

```shell
oc port-forward svc/mi-servicio-practica 3000:4000
```

## En otra consola llamamos el servicio

```shell
curl localhost:3000
```
