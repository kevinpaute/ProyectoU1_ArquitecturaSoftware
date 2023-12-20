# app/models/productos_categoria.rb
class ProductosCategoria < ApplicationRecord
  belongs_to :producto, class_name: 'Productos', foreign_key: 'producto_id'
  belongs_to :categoria
end
