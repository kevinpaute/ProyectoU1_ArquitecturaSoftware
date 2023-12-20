# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.1].define(version: 2023_12_09_220317) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "categoria", force: :cascade do |t|
    t.string "nombre"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "movimiento_inventarios", force: :cascade do |t|
    t.bigint "producto_id", null: false
    t.integer "cantidad"
    t.datetime "fecha_movimiento"
    t.string "tipo_movimiento"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["producto_id"], name: "index_movimiento_inventarios_on_producto_id"
  end

  create_table "productos", force: :cascade do |t|
    t.string "nombre"
    t.decimal "precio"
    t.integer "stock"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "productos_categoria", force: :cascade do |t|
    t.bigint "producto_id", null: false
    t.bigint "categoria_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["categoria_id"], name: "index_productos_categoria_on_categoria_id"
    t.index ["producto_id"], name: "index_productos_categoria_on_producto_id"
  end

  add_foreign_key "movimiento_inventarios", "productos"
  add_foreign_key "productos_categoria", "categoria", column: "categoria_id"
  add_foreign_key "productos_categoria", "productos"
end
