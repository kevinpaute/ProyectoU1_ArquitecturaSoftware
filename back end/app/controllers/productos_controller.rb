class ProductosController < ApplicationController
    before_action :set_producto, only: [:show, :update, :destroy]
    skip_before_action :verify_authenticity_token

    # GET /productos
    def index
      @productos = Productos.all
      render json: @productos
    end

    # GET /productos/1
    def show
      render json: @producto
    end

    # POST /productos
    def create
      @producto = Productos.new(producto_params)

      if @producto.save
        render json: @producto, status: :created
      else
        render json: @producto.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /productos/1
    def update
      if @producto.update(producto_params)
        render json: @producto
      else
        render json: @producto.errors, status: :unprocessable_entity
      end
    end

    # DELETE /productos/1
    def destroy
      @producto.destroy
      head :no_content
    end

    private

    def set_producto
      @producto = Productos.find(params[:id])
    end

    def producto_params
      params.require(:producto).permit(:nombre, :precio, :stock)
    end
  end
