import wmi

def get_cpu_serial_number():
    try:
        wmi_obj = wmi.WMI()
        cpu_info = wmi_obj.Win32_Processor()[0]
        serial_number = cpu_info.ProcessorId.strip()
        return serial_number
    except Exception as e:
        print(f"Error: {str(e)}")
    return None

# 获取 CPU 序列号
cpu_serial_number = get_cpu_serial_number()
print("CPU 序列号:", cpu_serial_number)