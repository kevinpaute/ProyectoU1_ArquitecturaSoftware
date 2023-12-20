class CreateMovimientoInventarios < ActiveRecord::Migration[7.1]
  def change
    create_table :movimiento_inventarios do |t|
      t.references :producto, null: false, foreign_key: true
      t.integer :cantidad
      t.datetime :fecha_movimiento
      t.string :tipo_movimiento

      t.timestamps
    end
  end
end
