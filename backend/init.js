db = db.getSiblingDB('db')

db.createCollection('users');

db.camaras.insertOne([
 {
  email: 'admin@admin.com',
  image: 'default.jpg',
  name: 'Admin',
  surname: 'Admin',
  password: 'Admin',
  age: 41,
  is_active: true,
  is_admin: true
 }
]);
