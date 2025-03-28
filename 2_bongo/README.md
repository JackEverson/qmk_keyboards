# 2% Bongo Keyboard

![PXL_20230818_053811706](https://github.com/JackEverson/keyboard_project/assets/111256162/93093edd-ed33-4a6e-9015-d0f772b49094)

This is a "2% Milk" keyboard that I made for my wife to control volume. The kit came from Custom KBD and can be found [here](https://customkbd.com/products/bongo-2?_pos=1&_ss=r). The microcontroller I used is a KB2040 (This has a RP2040 chip with the pinout and shape of an Arduino Pro Micro) from Core Electronics which can be found [here](https://core-electronics.com.au/adafruit-kb2040-rp2040-kee-boar-driver.html).

I used QMK (Quantum Mechanical Keyboard) software to program the microcontroller. The custom layout (for turning volume up and down) is in the keymap.c in this directory. Add this file to your QMK firmware in the directory `qmk_firmware/keyboards/spaceman/2_milk/keymaps/volume` (you will have to create the volume directory). You can then flash the file to the board by putting it in bootloader mode and using the following command:

`qmk flash -c -kb spaceman/2_milk -km volume -e CONVERT_TO=promicro_rp2040`
