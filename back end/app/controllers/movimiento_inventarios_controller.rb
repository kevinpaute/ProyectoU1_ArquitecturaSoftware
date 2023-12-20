# app/controllers/movimiento_inventarios_controller.rb
class MovimientoInventariosController < ApplicationController
  before_action :set_movimiento, only: [:show, :update, :destroy]
  skip_before_action :verify_authenticity_token
   # GET /movimiento_inventarios
  def index
    @movimientos = MovimientoInventarios.all
    render json: @movimientos
  end
   # GET /movimiento_inventarios/1
  def show
    render json: @movimiento
  end
   # POST /movimiento_inventarios
  def create
    @movimiento = MovimientoInventarios.new(movimiento_params)

    if @movimiento.save
      render json: @movimiento, status: :created
    else
      render json: { errors: @movimiento.errors.full_messages }, status: :unprocessable_entity
    end
  end
   # PUT /movimiento_inventarios/1
  def update
    if @movimiento.update(movimiento_params)
      render json: @movimiento
    else
      render json: @movimiento.errors, status: :unprocessable_entity
    end
  end
   # DELETE /movimiento_inventarios/1
  def destroy
    @movimiento.destroy
    head :no_content
  end

  private

  def set_movimiento
    @movimiento = MovimientoInventarios.find(params[:id])
  end

  def movimiento_params
    params.require(:movimiento_inventario).permit(:producto_id, :cantidad, :fecha_movimiento, :tipo_movimiento)
  end
end
