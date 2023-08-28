import random
import matplotlib.pyplot as plt
class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp  # 比例系数
        self.Ki = Ki  # 积分系数
        self.Kd = Kd  # 微分系数
        self.setpoint = setpoint  # 目标温度
        self.prev_error = 0  # 前一次误差
        self.integral = 0  # 积分项
        self.output = 0  # 控制输出

    def update(self, current_temperature):
        # 计算当前误差
        error = self.setpoint - current_temperature

        # 计算积分项
        self.integral += error

        # 计算微分项
        derivative = error - self.prev_error

        # 计算PID输出
        self.output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)

        # 更新前一次误差
        self.prev_error = error

        return self.output


# 模拟温度传感器
class TemperatureSensor:
    def __init__(self, initial_temperature):
        self.temperature = initial_temperature
        self.control_output  = 0

    def read_temperature(self):
        # 模拟温度的变化
        heating_effect = self.control_output * 0.1  # 假设加热器对温度的影响是线性的
        self.temperature += (5 - random.random())*0.5 + heating_effect  # 在[-0.5, 0.5]范围内随机波动
        return self.temperature


# 模拟主控制循环
def main():
    target_temperature = 30.0
    initial_temperature = 0.0

    pid = PIDController(Kp=10, Ki=0.1, Kd=0, setpoint=target_temperature)
    sensor = TemperatureSensor(initial_temperature)

    time_steps = 300
    temperatures = []  # 存储温度数据
    control_outputs = []  # 存储PID输出数据

    for _ in range(time_steps):
        current_temperature = sensor.read_temperature()
        control_output = pid.update(current_temperature)
        sensor.control_output = control_output

        temperatures.append(current_temperature)
        control_outputs.append(control_output)

        print(f"Current Temperature: {current_temperature:.2f}°C, Control Output: {control_output:.2f}")

    # 绘制温度和PID输出的图形
    time = range(time_steps)
    plt.figure(figsize=(10, 6))
    plt.plot(time, temperatures, label='Temperature', marker='o')
    plt.plot(time, control_outputs, label='Control Output', linestyle='--', marker='x')
    plt.axhline(target_temperature, color='red', linestyle=':', label='Target Temperature')
    plt.xlabel('Time Steps')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.title('PID Temperature Control')
    plt.show()
if __name__ == "__main__":
    main()

