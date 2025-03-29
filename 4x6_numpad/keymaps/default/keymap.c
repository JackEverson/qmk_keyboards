// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include <stdio.h>
char wpm_str[10];

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    

    [0] = LAYOUT_ortho_4x6(
        KC_NO,              KC_NO,              KC_NO,              KC_NO,    
        KC_NUM_LOCK,        KC_KP_SLASH,        KC_KP_ASTERISK,     KC_KP_MINUS,
        KC_KP_7,            KC_KP_8,            KC_KP_9,            KC_KP_PLUS,
        KC_KP_4,            KC_KP_5,            KC_KP_6,            KC_MUTE,    // Volume Mute
        KC_KP_1,            KC_KP_2,            KC_KP_3,            KC_KP_ENTER,
        KC_KP_0,            KC_KP_DOT,          TG(1),              KC_NO   // 0, ., macro1, macro2
    ),

    [1] = LAYOUT_ortho_4x6(
        KC_NO,              KC_NO,              KC_NO,              KC_NO,    
        KC_NUM_LOCK,        KC_KP_SLASH,        KC_KP_ASTERISK,     KC_KP_MINUS,
        KC_KP_7,            KC_KP_8,            KC_KP_9,            KC_KP_PLUS,
        KC_KP_4,            KC_KP_5,            KC_KP_6,            KC_MUTE,    // Volume Mute
        KC_KP_1,            KC_KP_2,            KC_KP_3,            KC_KP_ENTER,
        KC_KP_0,            KC_KP_DOT,          TG(1),              KC_NO   // 0, ., macro1, macro2
    ),
};

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU)  },
    [1] = { ENCODER_CCW_CW(MS_WHLU, MS_WHLD) },
};
#endif


// OLED STUFF STARTS HERE
// based on https://github.com/qmk/qmk_firmware/blob/master/keyboards/kyria/keymaps/j-inc/keymap.c

// In your rules.mk make sure you have:
// OLED_DRIVER_ENABLE = yes
// WPM_ENABLE = yes

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case 0:
            oled_write_P(PSTR("Default\n"), false);
            break;
        case 1:
            oled_write_P(PSTR("FN\n"), false);
            break;
        default:
            // Or use the write_ln shortcut over adding '\n' to the end of your string
            oled_write_ln_P(PSTR("Undefined"), false);
    }

    // Host Keyboard LED Status
    led_t led_state = host_keyboard_led_state();
    oled_write_P(led_state.num_lock ? PSTR("NUM ") : PSTR("    "), false);
    oled_write_P(led_state.caps_lock ? PSTR("CAP ") : PSTR("    "), false);
    oled_write_P(led_state.scroll_lock ? PSTR("SCR ") : PSTR("    "), false);
    
    return false;
}
#endif