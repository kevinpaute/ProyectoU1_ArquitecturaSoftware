# app/controllers/productos_categorias_controller.rb
class ProductosCategoriaController < ApplicationController
  before_action :set_productos_categoria, only: [:show, :update, :destroy]
  skip_before_action :verify_authenticity_token

    # GET /productos_categoria
  def index
    @productos_categorias = ProductosCategoria.all
    render json: @productos_categorias
  end
    # GET /productos_categoria/1
  def show
    render json: @productos_categoria
  end
    # POST /productos_categoria
  def create
    @productos_categoria = ProductosCategoria.new(productos_categoria_params)

    if @productos_categoria.save
      render json: @productos_categoria, status: :created
    else
      render json: { errors: @productos_categoria.errors.full_messages }, status: :unprocessable_entity
    end
  end
    # PUT /productos_categoria/1
  def update
    if @productos_categoria.update(productos_categoria_params)
      render json: @productos_categoria
    else
      render json: @productos_categoria.errors, status: :unprocessable_entity
    end
  end
    # DELETE /productos_categoria/1
  def destroy
    @productos_categoria.destroy
    head :no_content
  end

  private

  def set_productos_categoria
    @productos_categoria = ProductosCategoria.find(params[:id])
  end

  def productos_categoria_params
    params.require(:productos_categoria).permit(:producto_id, :categoria_id)
  end
end
