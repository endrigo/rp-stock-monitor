# Stock monitor

Proyecto de ejemplo de uso de Redpanda para el curso de Stream Processing del
diplomado de Big Data 2023.

## Links
- [Finnhub API](https://finnhub.io/docs/api/websocket-trades)
- [Websocket client](https://pypi.org/project/websocket-client/)
- [Redpanda producer/consumer tutorial](https://redpanda.com/blog/python-redpanda-kafka-api-tutorial)
- [Repanda console tutorial](https://university.redpanda.com/courses/take/hands-on-redpanda-getting-started/)
- [Github Profesor Rodrigo Parra](https://github.com/rparrapy/rp-stock-monitor)

## Clases Grabadas profesor Rodrigo Parra
 - 26_07_23: Presentacion Profesor y alumnos. Conceptos flujos de datos.
 - 31_07_23: Arquitectura, Caracteristicas, Funcionalidades Redpanda.
 - 02_08_23: Redpanda. Código Productor / Consumidor
 - 07_08_23: KsqlDB.
 - 09_08_23: No hay grabacion
 - 14_08_23: Explicación trabajo final.

## Observaciones

* El producer saca datos de finnhub.io, y coloca en Redpanda
El consumidor lee de redpanda y los muestra a consola
El KsqlDB es un consumidor.

* El productor necesita las credenciales de finnhub.io/
"wss://ws.finnhub.io?token=<api-key>",

* Consola web de Redpanda
    http://127.0.0.1:8080/overview
  
* Guia Python
    https://www.freecodecamp.org/espanol/news/el-manual-de-python/

* Consola web de Redpanda
    http://127.0.0.1:8080/overview

* Consola KsqlDB
```
    docker exec -it ksqldb-cli ksql http://ksqldb-server:8088
```


