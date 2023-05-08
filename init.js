db = db.getSiblingDB('db')

db.createCollection('camaras');

db.camaras.insertMany([
 {
  nombre: '09NC39TV01',
  coordenadas: {
  latitud: 40.40376974,
  longitud: -3.66657048
 },
  fichero: '09NC39TV01.jpg',
  url: 'www.mc30.es/components/com_hotspots/datos/imagenes_camaras/09NC39TV01.jpg'
 },
 {
  nombre: '15RR64TV01',
  coordenadas: {
  latitud: 40.40016472,
  longitud: -3.71215353
 },
  fichero: '15RR64TV01.jpg',
  url: 'www.mc30.es/components/com_hotspots/datos/imagenes_camaras/15RR64TV01.jpg'
 },
 {
  nombre: '13NL35TV01',
  coordenadas: {
  latitud: 40.38773066,
  longitud: -3.69609328
 },
  fichero: '13NL35TV01.jpg',
  url: 'www.mc30.es/components/com_hotspots/datos/imagenes_camaras/13NL35TV01.jpg'
 },
]);
