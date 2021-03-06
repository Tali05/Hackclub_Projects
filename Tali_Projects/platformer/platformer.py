import pyglet
window = pyglet.window.Window()
image = pyglet.resource.image("resources/surviv.png")
sprite = pyglet.sprite.Sprite(image)
sprite.scale_x = 0.4
spritae.scale_y = 0.4
sprite.x = 20
sprite.y = 20
@window.event
def on_draw():
    window.clear()
    sprite.draw()

    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ("v2f", [0,0, window.width,0, window.width, window.height, 0, window.height]),
        ("c3B",[0,250,0]))


pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)
speed = 500
velY = 0
jump = 500
grounded = True
G = 500

def update(dt,ex_dt):
    global velY
    global grounded
    if pressed_keys[pyglet.window.key.A]:
        sprite.x -= int(speed * dt)
    if pressed_keys[pyglet.window.key.D]:
        sprite.x += int(speed * dt)
    if pressed_keys[pyglet.window.key.W] and grounded:
        velY = jump
        grounded = False
        sprite.y += velY * dt
    if sprite.y <= 100:
        velY = 0
        grounded = True
    else:
        velY -= G * dt
pyglet.clock.schedule(update, 1/60.0)
pyglet.app.run()
