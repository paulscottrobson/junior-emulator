# junior-emulator

C256Junior emulator (Windows, Mac and Linux)

BUILDING
========

To build everything you need the following 4 repositories.

The emulator
https://github.com/paulscottrobson/junior-emulator

The tiny kernal currently used to boot the emulator
https://github.com/paulscottrobson/junior-tinykernel

Basic Repository
https://github.com/paulscottrobson/superbasic

Command Line Foenix256 uploader 
https://github.com/pweingar/FoenixMgr

New Kernel (for real hardware)

https://github.com/ghackwrench/F256_Jr_Kernel_DOS

(Only required for rebuilding the title screen and uploaded font)
https://github.com/WartyMN/Foenix-F256JR-bootscreens
https://github.com/WartyMN/Foenix-Fonts

The emulator has SDL2 as a dependency. In Windows this needs to be installed into C:\SDL2 - Windows also requires mingw-gcc, python and make
(Chocolatey is the best way of installing these)

RUNNING
=======

To run use jr256 <file> <file> <file> where <file> is a filename followed by an @ followed by a load address in hex. This load address is in
the physical memory space *not* the 6502 space.

The address can be a single letter ; B (Basic ROM Location) X (Basic Code Location) M (Monitor Location) S (Sprites Location) - note the monitor
loads to the equivalent of E000 to needs to be 8k in length..

e.g. ./jr256 basic.rom@b	dummy.code@x - the make run option/

The kernal simply initialises and jumps to $8000. So this line loads the BASIC rom to $8000 and a dummy to $3000 (because the kernal has
no save and load at the moment, the source code is loaded into memory at boot - this is just an end of file marker)

It is possible to override the start address by having boot@1000 (say) in the line - which will cause it to jump to $1000. This address is in
the 6502 space.

To track calls and returns use the command line option 'track'

To run from flash, use the command line option 'flash'

STATE
=====

Things that are implemented (mostly partially)

- Text display
- Keyboard and Interrupts
- Bitmap
- Sprites
- Memory LUT

DEBUGGER
========

F6 enters the debugger
F1 reset
F5 run
F7 step into
F8 step over
F9 set breakpoints
TAB display screen
Type 0-9A-F to change code display, shift 0-9A-F to change data display.
