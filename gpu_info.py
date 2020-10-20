import GPUtil
from tabulate import tabulate

print("="*40, "GPU DETAILS", "="*40)
gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    gpu_id = gpu.id
    gpu_adi = gpu.name
    gpu_yuzde = f"{gpu.load*100}%"
    gpu_bos_hafiza = f"{gpu.memoryFree}MB"
    gpu_kullanilan_hafiza = f"{gpu.memoryUsed}MB"
    gpu_toplam_hafiza = f"{gpu.memoryTotal}MB"
    gpu_sicaklik = f"{gpu.temperature} °C"
    gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_adi, gpu_yuzde, gpu_bos_hafiza, gpu_kullanilan_hafiza,
        gpu_toplam_hafiza, gpu_sicaklik, gpu_uuid
    ))
print(tabulate(list_gpus, headers=("id", "GPU Adı", "GPU Yüzde", "GPU Boş Hafıza", "GPU Kullanılan Alan",
                                   "GPU Toplam Hafıza", "GPU Sıcaklık", "uuid")))