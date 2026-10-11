# ADC Divider and Code

A microcontroller's ADC can only read up to its reference voltage, often 3.3 V or 5 V. To measure a bigger voltage, such as a 12 V battery, you scale it down with two resistors (a **voltage divider**) and multiply the reading back up in code.

## The theory

A divider with R1 on top (connected to the voltage) and R2 on the bottom (connected to ground) gives **Vout = Vin × R2 ÷ (R1 + R2)**. The **scale factor** to undo it is **(R1 + R2) ÷ R2**. If the divider turns 12 V into 3.13 V, the factor is 3.83, so a reading of 3.13 V means 12 V.

Choosing the resistors involves three trade-offs:

- **Headroom.** The highest voltage must land just **under** Vref, never over. The tool lets a few percent spare, so a slightly high supply does not push the pin out of range.
- **Wasted current.** The divider draws Vin ÷ (R1 + R2) all the time. Bigger resistors save current, which matters on a battery.
- **Source impedance.** An ADC needs the signal source to be low-impedance (about 10 kΩ or less on an Arduino Uno, per the ATmega328P datasheet). A divider of two huge resistors reads incorrectly. A 100 nF capacitor from the pin to ground helps.

## Step by step

1. Open the **ADC Divider + Code** tab.
2. In **Highest voltage to measure (V)**, type the biggest voltage you will see, for example `12` (or `14.4` for a charging car battery).
3. In **ADC reference voltage (V)**, type your ADC's Vref, for example `3.3`.
4. In **Headroom below the reference (%)**, leave `5`, or raise it for more safety.
5. In **ADC resolution**, choose your converter's size.
6. In **Standard values**, choose the resistor series you own (E24 is a good start).
7. In **Min R1 + R2** and **Max R1 + R2**, set the allowed total resistance. Higher saves current, lower is better for the ADC.
8. In **Code for**, choose **Arduino**, **ESP32 (Arduino core)**, or **MicroPython**.
9. Read **R1 (top, to the voltage)** and **R2 (bottom, to ground)**, then **Voltage at the ADC pin at maximum**. The table lists alternatives, handy if you already own one of those values.
10. Press **Copy** on the code box and paste it into your sketch. The numbers for R1, R2, and Vref are already filled in.

## Worked example

Measure a 12 V battery with a 3.3 V ESP32 or Pico. The tool picks **R1 = 51 kΩ, R2 = 18 kΩ**. At 12 V the pin sees **3.13 V**, the scale factor is 3.833, the divider draws **174 µA**, and the smallest step at the input is about 3.1 mV (12-bit).

## Things to watch

- On the original **ESP32**, the ADC is only accurate over roughly 0.15 to 2.45 V at 11 dB attenuation. Design for a 2.4 V maximum instead of 3.3 V for best accuracy.
- Use ADC1 pins on the ESP32. ADC2 pins stop working while Wi-Fi is active.
- For a 5 V Arduino measuring up to 12 V, enter `5` for Vref.
- A divider that is also connected to a battery drains it slowly. For a battery that must last months, use larger resistors or a switch.

![ADC Divider and Code tool](images/adc-divider.png)
