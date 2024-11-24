# Thêm các thư viện cần thiết
import numpy
from matplotlib import pyplot

# Giới hạn không gian hai chiều cần mô phỏng
x_max = 10
x_min = 0
y_max = 10
y_min = 0

# Thiết lập số điểm lưới cần chia nhỏ không gian thành, càng nhiều càng chi tiết
nx = 80
ny = 80

# Tạo trục x với các điểm lưới phân phối đều. Hàm trả về một mảng chứa tất cả các diểm lưới
x = numpy.linspace(x_min, x_max, nx)

# Khoảng cách giữa hai điểm lưới liền kề trên trục x
dx = x[2] - x[1]

# Tạo trục y với các điểm lưới phân phối đều. Hàm trả về một mảng chứa tất cả các diểm lưới
y = numpy.linspace(y_min, y_max, ny)

# Khoảng cách giữa hai điểm lưới liền kề trên trục y
dy = y[2] - y[1]

# Tốc độ truyền sóng
c = 1

# Bước thời gian trôi qua mỗi lần tính toán (càng nhỏ càng chính xác)
dt = 0.025

# Số thời điểm cần tính toán
nt = 4000

# Hệ số cản
v = 0.02

# Hàm u dưới dạng mảng 3 chiều, với chiều thứ nhất là thời gian, chiều thứ hai và ba là không gian
u = numpy.zeros([nt, nx, ny])

for t in range(1, nt-1):
    # Tạo sóng tại điểm trung tâm của không gian trong 100 lần tính toán đầu tiên
    if(t<100):
       u[t, nx // 2, ny // 2] = numpy.sin(t/10)

    # Tính toán u(t+1) dựa trên u(t) và u(t-1)
    u[t+1, 1:-1, 1:-1] = 2*u[t, 1:-1, 1:-1] - u[t-1, 1:-1, 1:-1]  +(dt**2)*(c**2)*((u[t, 2:, 1:-1]-2*u[t, 1:-1, 1:-1]+u[t, :-2, 1:-1])/(dx**2)+(u[t,1:-1, 2:]-2*u[t, 1:-1, 1:-1]+u[t, 1:-1, :-2])/(dy**2))-v*dt*((u[t, 1:-1, 1:-1]-u[t-1, 1:-1, 1:-1]))

# Khởi tạo biểu đồ 3D
fig = pyplot.figure()
# Tạo lưới 2 chiều
X, Y = numpy.meshgrid(x, y)
# Tạo biểu đồ 3D
ax = fig.add_subplot(111, projection='3d')

# Vẽ biểu đồ 3D
for t in range(0, nt):
    # Vẽ mặt nước tại thời điểm t
    surf = ax.plot_surface(X, Y, u[t], color='b', shade=True, linewidth=0, antialiased=False)
    # Cài đặt góc nhìn quan sát mặt nước với góc 45 độ để quan sát dễ dàng
    ax.view_init(elev=45)
    # Giới hạn trục z chỉ quan sát từ bề mặt nước trở lên
    ax.set_zlim(-0.0001, 2.4)
    # Tắt hiển thị trục tọa độ
    pyplot.axis('off')
    # Hiển thị một khung hình trong 0.0001 giây
    pyplot.pause(.0001)
    # Xóa biểu đồ cũ để vẽ biểu đồ mới
    pyplot.cla()