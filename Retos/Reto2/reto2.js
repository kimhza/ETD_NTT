/* BASE DE DATOS */
use("reto2");

/* COLECCIONES */
db.createCollection("Estado");
db.createCollection("Poblacion");
db.createCollection("Residentes");
db.createCollection("Muertes");

/* DOCUMENTOS */
db.Estado.insertMany([
  {
    _id: ObjectId("5f76a80e35bde1489a4f9e0c"),
    nombre: "Alabama",
    latitud: 33.258882,
    longitud: -86.829534,
    fecha_fundacion: "1845-03-03",
  },
  {
    _id: ObjectId("ab32e7f89c66d12abedf3a4c"),
    nombre: "Florida",
    latitud: 27.756767,
    longitud: -81.463983,
    fecha_fundacion: "1819-12-14",
  },
  {
    _id: ObjectId("78c9a1e0d34f67b8a2e59cf1"),
    nombre: "Georgia",
    latitud: 32.329381,
    longitud: -83.113737,
    fecha_fundacion: "1733-02-12",
  },
  {
    _id: ObjectId("e9d8b3a4c2f1e0d3a4c2e9f8"),
    nombre: "South Carolina",
    latitud: 33.687439,
    longitud: -80.436374,
    fecha_fundacion: "1776-03-26",
  },
]);

db.Poblacion.insertMany([
  {
    anio: 2000,
    poblacion: 4447100,
    estado_id: ObjectId("5f76a80e35bde1489a4f9e0c"),
  },
  {
    anio: 2001,
    poblacion: 4451493,
    estado_id: ObjectId("5f76a80e35bde1489a4f9e0c"),
  },
  {
    anio: 2000,
    poblacion: 15982378,
    estado_id: ObjectId("ab32e7f89c66d12abedf3a4c"),
  },
  {
    anio: 2001,
    poblacion: 17054000,
    estado_id: ObjectId("ab32e7f89c66d12abedf3a4c"),
  },
  {
    anio: 2000,
    poblacion: 8186453,
    estado_id: ObjectId("78c9a1e0d34f67b8a2e59cf1"),
  },
  {
    anio: 2001,
    poblacion: 8229823,
    estado_id: ObjectId("78c9a1e0d34f67b8a2e59cf1"),
  },
  {
    anio: 2000,
    poblacion: 4012012,
    estado_id: ObjectId("e9d8b3a4c2f1e0d3a4c2e9f8"),
  },
  {
    anio: 2001,
    poblacion: 4023438,
    estado_id: ObjectId("e9d8b3a4c2f1e0d3a4c2e9f8"),
  },
]);

db.Residentes.insertMany([
  {
    anio: 2000,
    residentes_menores_65: 3870598,
    estado_id: ObjectId("5f76a80e35bde1489a4f9e0c"),
  },
  {
    anio: 2001,
    residentes_menores_65: 3880476,
    estado_id: ObjectId("5f76a80e35bde1489a4f9e0c"),
  },
  {
    anio: 2000,
    residentes_menores_65: 13237167,
    estado_id: ObjectId("ab32e7f89c66d12abedf3a4c"),
  },
  {
    anio: 2001,
    residentes_menores_65: 13548077,
    estado_id: ObjectId("ab32e7f89c66d12abedf3a4c"),
  },
  {
    anio: 2000,
    residentes_menores_65: 7440877,
    estado_id: ObjectId("78c9a1e0d34f67b8a2e59cf1"),
  },
  {
    anio: 2001,
    residentes_menores_65: 7582146,
    estado_id: ObjectId("78c9a1e0d34f67b8a2e59cf1"),
  },
  {
    anio: 2000,
    residentes_menores_65: 3535770,
    estado_id: ObjectId("e9d8b3a4c2f1e0d3a4c2e9f8"),
  },
  {
    anio: 2001,
    residentes_menores_65: 3567172,
    estado_id: ObjectId("e9d8b3a4c2f1e0d3a4c2e9f8"),
  },
]);

db.Muertes.insertMany([
  {
    anio: 2000,
    muertes: 10622,
    estado_id: ObjectId("5f76a80e35bde1489a4f9e0c"),
  },
  {
    anio: 2001,
    muertes: 15912,
    estado_id: ObjectId("5f76a80e35bde1489a4f9e0c"),
  },
  {
    anio: 2000,
    muertes: 38103,
    estado_id: ObjectId("ab32e7f89c66d12abedf3a4c"),
  },
  {
    anio: 2001,
    muertes: 166069,
    estado_id: ObjectId("ab32e7f89c66d12abedf3a4c"),
  },
  {
    anio: 2000,
    muertes: 14804,
    estado_id: ObjectId("78c9a1e0d34f67b8a2e59cf1"),
  },
  {
    anio: 2001,
    muertes: 15000,
    estado_id: ObjectId("78c9a1e0d34f67b8a2e59cf1"),
  },
  {
    anio: 2000,
    muertes: 8581,
    estado_id: ObjectId("e9d8b3a4c2f1e0d3a4c2e9f8"),
  },
  {
    anio: 2001,
    muertes: 9500,
    estado_id: ObjectId("e9d8b3a4c2f1e0d3a4c2e9f8"),
  },
]);
