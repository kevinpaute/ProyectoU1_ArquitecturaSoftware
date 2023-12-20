class Productos < ApplicationRecord
    has_many :productos_categoria
    has_many :categorias, through: :productos_categorias
    has_many :productos_categorias, foreign_key: 'producto_id'
    has_many :movimiento_inventarios
end
