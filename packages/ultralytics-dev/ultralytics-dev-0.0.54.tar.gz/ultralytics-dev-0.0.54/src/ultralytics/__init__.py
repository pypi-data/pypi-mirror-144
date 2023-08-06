__version__ = '0.0.54'  # print(ultralytics.__version__)


def checks(verbose=True):
    # Check system software and hardware
    print('Checking setup...')

    import os
    import shutil
    from .utils.general import check_requirements, emojis, is_colab
    from .utils.torch_utils import select_device  # imports

    check_requirements(('psutil', 'IPython'))
    import psutil
    from IPython import display  # to display images and clear console output

    if is_colab():
        shutil.rmtree('sample_data', ignore_errors=True)  # remove colab /sample_data directory

    if verbose:
        # System info
        # gb = 1 / 1000 ** 3  # bytes to GB
        gib = 1 / 1024 ** 3  # bytes to GiB
        ram = psutil.virtual_memory().total
        total, used, free = shutil.disk_usage("/")
        display.clear_output()
        s = f'({os.cpu_count()} CPUs, {ram * gib:.1f} GB RAM, {(total - free) * gib:.1f}/{total * gib:.1f} GB disk)'
    else:
        s = ''

    select_device(newline=False, version=__version__)
    print(emojis(f'Setup complete ✅ {s}'))


def login(api_key=''):
    # Login to Ultralytics HUB
    from .main import connect_to_hub
    connect_to_hub(api_key, verbose=True)


def start(api_key='ac0ab020186aeb50cc4c2a5272de17f58bbd2c05b5', model_key='RqFCDNBxgU4mOLmaBrcd'):
    # Start training models with Ultralytics HUB
    from .main import train_model
    train_model(api_key=api_key, model_key=model_key)
