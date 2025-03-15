from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP0,  # column
    source=board.GP8, # row
    midi=False,
    mouse=False,
    storage=True,
    usb_id=('KMK Keyboards', 'Badger_redox'),
)
