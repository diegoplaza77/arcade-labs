import arcade
arcade.open_window(800, 600, "My Minecraft World")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)#SUELO

arcade.draw_rectangle_filled(100, 150, 80, 200, arcade.color.WOOD_BROWN)#ARBOL TRONCO
arcade.draw_triangle_filled(20, 250, 100, 400, 180, 250, arcade.color.DARK_JUNGLE_GREEN)#ARBOL COPA
arcade.draw_triangle_filled(20, 300, 100, 450, 180, 300, arcade.color.DARK_JUNGLE_GREEN)
arcade.draw_triangle_filled(20, 350, 100, 500, 180, 350, arcade.color.DARK_JUNGLE_GREEN)

arcade.draw_rectangle_filled(280, 100, 35, 120, arcade.color.PURPLE)#PIERNAS ZOMBI
arcade.draw_rectangle_filled(320, 100, 35, 120, arcade.color.PURPLE)

arcade.draw_rectangle_filled(280, 40, 35, 20, arcade.color.BATTLESHIP_GREY)#PIES ZOMBI
arcade.draw_rectangle_filled(320, 40, 35, 20, arcade.color.BATTLESHIP_GREY)

arcade.draw_rectangle_filled(320, 225, 100, 30, arcade.color.ARMY_GREEN)#BRAZO DETRAS DE ZOMBI

arcade.draw_rectangle_filled(300, 200, 75, 100, arcade.color.DARK_BLUE)#PECHO ZOMBI

arcade.draw_rectangle_filled(320, 210, 80, 30, arcade.color.ARMY_GREEN)#BRAZO DELANTE DE ZOMBI

arcade.draw_rectangle_filled(300, 300, 100, 100, arcade.color.ARMY_GREEN)#CABEZA ZOMBI

arcade.draw_rectangle_filled(290, 310, 20, 20, arcade.color.BLACK)#OJOS ZOMBI
arcade.draw_rectangle_filled(330, 310, 20, 20, arcade.color.BLACK)

arcade.draw_rectangle_filled(310, 285, 40, 10, arcade.color.ANDROID_GREEN)#NARIZ ZOMBI

arcade.draw_circle_filled(750, 550, 100, arcade.color.ORANGE)#SOL




arcade.finish_render()
arcade.run()