# Board Overview

## Overview

The Bluejay is a compact, low-power FPGA development board built around the iCE40LP8K from Lattice Semiconductor.

The iCE40LP8K comes from the iCE40 LP/HX family of ultra-low power FPGAs. It is the largest FPGA in the family, featuring 7,680 Look-Up Tables (LUTs) and 128 kbits of Embedded Block RAM. The iCE40LP8K also includes two Phase Locked Loops for on-chip clock generation. When idle, the iCE40LP8K consumes just 250 µA of static power. This combination of logic capacity and energy efficiency makes it an ideal choice for low power applications, such as battery-powered devices.

## 39 Programmable I/O Pins

The board provides access to 39 of the FPGA's programmable I/O pins through two 24-pin connectors. Each pin can be independently configured as a digital input, output, or tri-state buffer. This high pin count and programmability allows the FPGA to easily interface with a wide variety of external devices, such as sensors, displays, microcontrollers, or other FPGAs.

## 12 MHz Oscillator

An onboard 12 MHz oscillator provides a clock signal for the system. The output of the oscillator can be used directly as a clock source or as a reference clock for the FPGA's internal PLLs to generate higher or lower frequencies as needed.

## Onboard Configuration Storage

The board includes a 2 Mbit SPI flash chip for storing the FPGA's configuration bitstream. This allows the bitstream to be stored onboard and loaded automatically when power is applied.

The flash can be programmed through the board's configuration interface.

## Status LEDs

The board includes two status LEDs for providing visual feedback. The **PWR** LED indicates the board is receiving power. The **USR** LED is connected to one of the FPGA's programmable I/O pins and is free for use by the application.

When used in power constrained applications, the status LEDs can be disconnected using the **LED EN** jumper.

## Multiple Configuration Modes

The board supports both master and slave configuration modes. In Master Mode, the FPGA automatically loads its configuration from the flash when power is applied to the board. In Slave Mode, an external programmer connects to the board and loads the configuration directly into the FPGA.

The configuration mode can be selected using a jumper.

## Flexible Power Options

To provide maximum flexibility, the board can be powered through the USB-C connector, the 5V pin, or the 3.3V pins.

When 5V is supplied to the board—either through the USB-C connector or the 5V power pin—an onboard low-dropout regulator (LDO) steps down the input voltage to the required 3.3V level. In these cases, the 3.3V pins can be used as power outputs to supply external circuitry (up to the LDO's current limit).

When 3.3V is supplied to the board through the 3.3V pins, the LDO is bypassed. This allows the board to be easily integrated into larger systems that already have a regulated 3.3V supply.


## Low Power Design

When idle, the board consumes approximately 600 µA. Active power consumption varies based on FPGA resource utilization and switching frequency. When clocked at the nominal 12 MHz frequency, the board will typically consume anywhere from a few milliamps to the low tens of milliamps. When the clock is boosted to its max value of 275 MHz (using one of the FPGAs intenal PLLs) and switching activity is high, the board consumes around 150 milliamps of power.

## Open Source Toolchain

The board works with completely free and open-source FPGA development tools:

- **Yosys** - RTL synthesis
- **NextPNR** - Place and route
- **Project IceStorm** - Bitstream generation and programming utilities

These tools provide a complete RTL-to-bitstream flow for Linux, macOS, and Windows (via WSL), making FPGA development accessible without expensive proprietary software.


