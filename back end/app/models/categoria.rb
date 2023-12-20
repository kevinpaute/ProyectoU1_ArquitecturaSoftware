class Categoria < ApplicationRecord
    has_many :productos_categorias
    has_many :productos, through: :productos_categorias
end
