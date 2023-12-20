# app/controllers/categoria_controller.rb
class CategoriaController < ApplicationController
  before_action :set_categoria, only: [:show, :update, :destroy]
  skip_before_action :verify_authenticity_token


  # GET /categoria
  def index
    @categorias = Categoria.all
    render json: @categorias
  end
# GET /categoria/1
  def show
    render json: @categoria
  end
# POST /categoria/1
  def create
    @categoria = Categoria.new(categoria_params)

    if @categoria.save
      render json: @categoria, status: :created
    else
      render json: @categoria.errors, status: :unprocessable_entity
    end
  end
# PUT /categoria/1
  def update
    if @categoria.update(categoria_params)
      render json: @categoria
    else
      render json: @categoria.errors, status: :unprocessable_entity
    end
  end
# DELETE /categoria
  def destroy
    @categoria.destroy
    head :no_content
  end

  private

  def set_categoria
    @categoria = Categoria.find(params[:id])
  end

  def categoria_params
    params.require(:categoria).permit(:nombre)
  end
end
