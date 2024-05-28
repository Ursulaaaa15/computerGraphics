import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cone(height, radius):
    # Создаем массив значений угла phi
    phi = np.linspace(0, 2*np.pi, 100)
    
    # Вычисляем координаты x, y, z для точек на окружности основания конуса
    x_base = radius * np.cos(phi)
    y_base = radius * np.sin(phi)
    z_base = np.zeros_like(phi)
    
    # Создаем массив значений высоты z для точек на боковой поверхности конуса
    z_side = np.linspace(0, height, 100)
    
    # Создаем сетку для значений z и phi
    z_side, phi = np.meshgrid(z_side, phi)
    
    # Вычисляем радиус окружности для каждой высоты z на боковой поверхности
    current_radius = radius * (1 - z_side / height)
    
    # Вычисляем координаты x, y для точек на боковой поверхности конуса
    x_side = current_radius * np.cos(phi)
    y_side = current_radius * np.sin(phi)
    
    return x_base, y_base, z_base, x_side, y_side, z_side

# Параметры конуса
height = 10  # Высота конуса
radius = 5   # Радиус основания конуса

# Создаем данные для конуса
x_base, y_base, z_base, x_side, y_side, z_side = cone(height, radius)

# Визуализируем конус
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение окружности основания конуса
ax.plot(x_base, y_base, z_base, color='blue')

# Построение боковой поверхности конуса
ax.plot_surface(x_side, y_side, z_side, color='cyan', alpha=0.7)

# Новые координаты источника света (сбоку)
light_source = np.array([15, 0, height/2])  # Координаты источника света
ax.scatter(light_source[0], light_source[1], light_source[2], color='yellow', s=100)  # Источник света

# Создаем массивы координат для лучей света от источника света к каждой точке поверхности конуса
light_ray_x = np.concatenate((np.full_like(x_side.flatten(), light_source[0]), x_side.flatten()))
light_ray_y = np.concatenate((np.full_like(y_side.flatten(), light_source[1]), y_side.flatten()))
light_ray_z = np.concatenate((np.full_like(z_side.flatten(), light_source[2]), z_side.flatten()))

# Построение лучей света
ax.plot(light_ray_x, light_ray_y, light_ray_z, color='yellow', alpha=0.3)

# Включаем параллельную проекцию и устанавливаем углы поворота
ax.view_init(elev=30, azim=45)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Cone')
plt.show()