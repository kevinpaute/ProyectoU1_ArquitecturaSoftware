class CreateProductosCategoria < ActiveRecord::Migration[7.1]
  def change
    create_table :productos_categoria do |t|
      t.references :producto, null: false, foreign_key: true
      t.references :categoria, null: false, foreign_key: true

      t.timestamps
    end
  end
end
