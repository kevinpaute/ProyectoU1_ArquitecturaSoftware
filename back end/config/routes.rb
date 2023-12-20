Rails.application.routes.draw do
  resources :productos
  resources :categoria
  resources :movimiento_inventarios
  resources :productos_categoria
end
