#importing circuit python "board" ability to use GPIO pins.
import board      

#General KMK keyboard import 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

#Redox has 7 columns on left and 7 columns on right (total 14, left to right) and 5 rows, as it is COL2ROW diodes the 1N4148 diodes attach to the rows with the black side of the diode attached to the row (not the switch)
keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,         board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13)
#Columns left to right      1         2         3         4         5         6         7   |split|         8         9        10         11        12          13         14                 

keyboard.row_pins = (board.GP14,board.GP15,board.GP16,board.GP17,board.GP18)
#Rows top to bottom         1           2           3         4          5

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layers
from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

# Mouse keys
from kmk.modules.mouse_keys import MouseKeys
keyboard.modules.append(MouseKeys())

# HoldTap
from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
holdtap.tap_time = 300 # can adjust holdtap time if it is an issue
keyboard.modules.append(holdtap)

#easier to see function, empty, and transpartent keys
XXXXX = KC.NO
_____ = KC.TRNS
tog_lay1 = KC.MO(1)
tog_lay2 = KC.MO(2)

keyboard.keymap = [
    [#layer 0: Base layer
    KC.ESC,    KC.N1,      KC.N2,      KC.N3,      KC.N4,        KC.N5,      KC.GRAVE,                        KC.PGUP,    KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINUS,

    KC.TAB,    KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.EQL,                         KC.PGDN,    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,      KC.BSLS,

    KC.CAPS,   KC.A,       KC.S,       KC.D,       KC.F,       KC.G,   tog_lay1,                            KC.END,     KC.H,      KC.J,        KC.K,       KC.L,       KC.SCLN,    KC.QUOTE,

    KC.LSHIFT, KC.Z,       KC.X,        KC.C,       KC.V,       KC.B,       tog_lay2,                         KC.HOME,    KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLSH,    KC.RSHIFT,

    KC.LCTRL,  tog_lay2,  KC.LGUI,     KC.LALT,  KC.LSHIFT,   KC.HT(KC.ENTER, tog_lay2),   KC.SPACE,   KC.BSPC, KC.HT(KC.DEL, tog_lay1), KC.LSHIFT,   KC.LBRC,     KC.RBRC,    KC.RALT,    KC.RCTRL,
    ],

    [#Layer 1: Motions
    KC.RLD,  KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,       KC.F6,                          KC.F7,    KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,      KC.MINUS,

    XXXXX,    XXXXX,      KC.MS_UP,      XXXXX,      KC.MW_UP,      XXXXX,       XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    XXXXX,    KC.MS_LEFT,    KC.MS_DOWN,    KC.MS_RIGHT,  KC.MW_DOWN,      XXXXX,       XXXXX,                          XXXXX,    KC.LEFT,      KC.DOWN,      KC.UP,     KC.RGHT,      XXXXX,       XXXXX,

    XXXXX,    XXXXX,      KC.DEL,      XXXXX,      XXXXX,      XXXXX,       XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      KC.MB_LMB,       KC.MB_RMB,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    ],

    [#Layer 2: numbers 
    KC.RLD,  KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,       KC.F6,                          KC.F7,    KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,      KC.MINUS,

    KC.TILDE, KC.EXCLAIM, KC.AT,    KC.HASH,    KC.DOLLAR, KC.PERCENT,  XXXXX,                          XXXXX, KC.CIRCUMFLEX,  KC.AMPERSAND, KC.ASTERISK, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.UNDERSCORE,

    KC.GRAVE,    KC.N1,   KC.N2,   KC.N3,       KC.N4,   KC.N5,   XXXXX,                                XXXXX,   KC.N6,   KC.N7,        KC.N8,      KC.N9,      KC.N0,       KC.MINUS,    

    KC.LSHIFT,    XXXXX,      KC.DEL,      XXXXX,     KC.LBRC, KC.RBRC, XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      KC.EQL,       KC.PLUS,

    XXXXX,    XXXXX,      XXXXX,      XXXXX,      KC.LSHIFT,      XXXXX,       XXXXX,                          KC.BSPC, KC.DEL,      KC.LSHIFT,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    ],


    [#Layer X: template
    XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,                          XXXXX,    XXXXX,      XXXXX,      XXXXX,      XXXXX,      XXXXX,       XXXXX,

    ],

    ]



 
if __name__ == '__main__':
    keyboard.go()
