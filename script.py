# -*- coding: UTF-8 -*-
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser
from random import choice

class TestCase(FastHttpUser):
    weight = 1

    # este parâmetro controla o tempo entre execuções sucessivas de tasks pelos usuarios.
    # quanto mais baixo, maior será a taxa de requests por segundo por usuário
    wait_time = constant(2)
    
    categories = [
        "celular",
        "tv",
            
        # esta categoria existe. 
        # acessos a ela serão reportados como 404 na UI.
        "xpto", 
    ]

    @task(1)
    def home_buscape(this):
        # o parâmetro "name" é usado para agregar informações de acesso aos endpoints
        this.client.post("https://www.buscape.com.br", name="buscape")

    @task(5)
    def home_zoom(this):
        this.client.get("https://www.zoom.com.br", name="zoom")

    @task(1)
    def zoom_categories(this):
        # ter um access log global facilita a criação de tasks
        category = choice(TestCase.categories)
        this.client.get(f"https://www.zoom.com.br/{category}", name=category)