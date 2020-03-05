import arcade
arcade.open_window(800, 600, "My Minecraft World")

def dibujar_entorno():
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)#SUELO

    arcade.draw_rectangle_filled(100, 150, 80, 200, arcade.color.WOOD_BROWN)#ARBOL TRONCO
    arcade.draw_triangle_filled(20, 250, 100, 400, 180, 250, arcade.color.DARK_JUNGLE_GREEN)#ARBOL COPA
    arcade.draw_triangle_filled(20, 300, 100, 450, 180, 300, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(20, 350, 100, 500, 180, 350, arcade.color.DARK_JUNGLE_GREEN)

    arcade.draw_circle_filled(750, 550, 100, arcade.color.ORANGE)#SOL

def dibujar_zombi(x, y):
    arcade.draw_rectangle_filled(280 + x, 100 + y, 35, 120, arcade.color.PURPLE)#PIERNAS ZOMBI
    arcade.draw_rectangle_filled(320 + x, 100 + y, 35, 120, arcade.color.PURPLE)

    arcade.draw_rectangle_filled(280 + x, 40 + y, 35, 20, arcade.color.BATTLESHIP_GREY)#PIES ZOMBI
    arcade.draw_rectangle_filled(320 + x, 40 + y, 35, 20, arcade.color.BATTLESHIP_GREY)

    arcade.draw_rectangle_filled(320 + x, 225 + y, 100, 30, arcade.color.ARMY_GREEN)#BRAZO DETRAS DE ZOMBI

    arcade.draw_rectangle_filled(300 + x, 200 + y, 75, 100, arcade.color.DARK_BLUE)#PECHO ZOMBI

    arcade.draw_rectangle_filled(320 + x, 210 + y, 80, 30, arcade.color.ARMY_GREEN)#BRAZO DELANTE DE ZOMBI

    arcade.draw_rectangle_filled(300 + x, 300 + y, 100, 100, arcade.color.ARMY_GREEN)#CABEZA ZOMBI

    arcade.draw_rectangle_filled(290 + x, 310 + y, 20, 20, arcade.color.BLACK)#OJOS ZOMBI
    arcade.draw_rectangle_filled(330 + x, 310 + y, 20, 20, arcade.color.BLACK)

    arcade.draw_rectangle_filled(310 + x, 285 + y, 40, 10, arcade.color.ANDROID_GREEN)#NARIZ ZOMBI

def on_draw(delta_time):
    arcade.start_render()

    dibujar_entorno()
    dibujar_zombi(on_draw.dibujar_zombi1_x, 0)


    on_draw.dibujar_zombi1_x += 4
on_draw.dibujar_zombi1_x = 0

def inicio():
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.schedule(on_draw, 1/60)
    arcade.run()

inicio()

