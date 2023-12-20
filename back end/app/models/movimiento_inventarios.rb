# app/models/movimiento_inventarios.rb
class MovimientoInventarios < ApplicationRecord
  belongs_to :producto, class_name: 'Productos'
end
