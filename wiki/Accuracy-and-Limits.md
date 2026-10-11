# Accuracy and Limits

The toolkit uses standard datasheet and textbook formulas. [SOURCES.md](https://github.com/MakersWorkbench/embedded-toolkit/blob/main/SOURCES.md) lists where each one comes from.

- **Logic levels are typical values.** Real chips differ by part, supply voltage, load, and temperature. Check the datasheet for your exact part.
- **UART and timers follow the ATmega328P.** ESP32, RP2040, and STM32 differ.
- **ADC readings** have noise and error beyond the step size, and the reference voltage may not be exact. The ESP32's built-in ADC is non-linear.
- **Generated code** is a starting point. Check pin names, board settings, and library versions for your setup.

For anything that matters, measure it and read the datasheet.
