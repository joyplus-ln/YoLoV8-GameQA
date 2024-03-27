import torch
from ultralytics import settings


print(torch.version.cuda)
print(torch.cuda.is_available())



# View all settings
print(settings)

# Return a specific setting
value = settings['runs_dir']