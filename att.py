import glfw
from OpenGL.GL import *

# Mantemos o triângulo base original
vertices = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

def init():
    # Cor de fundo alterada para um cinza muito escuro para destacar as cores
    glClearColor(0.1, 0.1, 0.15, 1.0)

def draw_triangle():
    """Função única para desenhar o triângulo base."""
    glBegin(GL_TRIANGLES)
    for x, y in vertices:
        glVertex2f(x, y)
    glEnd()

def main():
    if not glfw.init():
        return
        
    window = glfw.create_window(800, 600, "Transformações Nativas com Cores", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    init()
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        # 1. Triângulo Original (Centro) - Cor: Branco
        glLoadIdentity() # Reseta o sistema de coordenadas para o centro (0,0)
        glColor3f(1.0, 1.0, 1.0)
        draw_triangle()
        
        # 2. Translação - Cor: Ciano
        glLoadIdentity()
        glTranslatef(-0.6, 0.2, 0.0)
        glColor3f(0.0, 1.0, 1.0)
        draw_triangle()
        
        # 3. Escala + Translação - Cor: Verde
        glLoadIdentity()
        glTranslatef(0.6, 0.2, 0.0)
        glScalef(0.5, 0.5, 1.0)
        glColor3f(0.0, 1.0, 0.0)
        draw_triangle()
        
        # 4. Reflexão (Eixo X) + Translação - Cor: Amarelo
        # Uma escala de -1 no eixo X tem o exato mesmo efeito matemático que o seu código original [-x, y]
        glLoadIdentity()
        glTranslatef(-0.6, -0.6, 0.0)
        glScalef(-1.0, 1.0, 1.0) 
        glColor3f(1.0, 1.0, 0.0)
        draw_triangle()
        
        # 5. Rotação (45 graus) + Translação - Cor: Laranja
        glLoadIdentity()
        glTranslatef(0.6, -0.6, 0.0)
        glRotatef(45, 0.0, 0.0, 1.0) # Rotaciona 45 graus no eixo Z (2D)
        glColor3f(1.0, 0.5, 0.0)
        draw_triangle()
        
        glfw.swap_buffers(window)
        
    glfw.terminate()

if __name__ == "__main__":
    main()
