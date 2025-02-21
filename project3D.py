import numpy as np
import matplotlib.pyplot as plt

# 创建一个简单的3D体素网格
voxel_grid = np.zeros((100, 100, 100), dtype=np.uint8)
voxel_grid[40:60, 40:60, 40:60] = 1  # 在中间创建一个立方体

# 定义投影方向
projection_direction = np.array([1, 1, 1])

# 执行平行投影
def parallel_projection(voxel_grid, direction):
    projection_matrix = np.eye(3) - np.outer(direction, direction) / np.dot(direction, direction)
    projected_grid = np.sum(np.dot(voxel_grid, projection_matrix), axis=2)
    return projected_grid

# 执行投影
projected_grid = parallel_projection(voxel_grid, projection_direction)

# 绘制结果
plt.imshow(projected_grid, cmap='gray')
plt.colorbar()
plt.title('Projected Voxel Grid')
plt.show()