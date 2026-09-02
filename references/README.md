# Reference register

Use primary sources wherever possible. Before selecting or purchasing a component,
add the exact manufacturer datasheet URL, revision and access date to the table.

| Subject | Preferred source | Why it is needed | Status |
|---|---|---|---|
| LTspice coupled inductors | Analog Devices LTspice documentation/help | Syntax and simulation behaviour | To be added |
| NE555 | [Texas Instruments NE555 datasheet](https://www.ti.com/lit/ds/symlink/ne555.pdf) | Timing equations and operating limits | Added 2026-09-02 |
| LTC4444 | [Analog Devices LTC4444 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/4444fb.pdf) | Driver supply, bootstrap, inputs and shoot-through protection | Added 2026-09-02 |
| 2N3904 | Exact purchased-manufacturer datasheet | Pinout, gain and switching behaviour | To be confirmed before hardware |
| IRLZ44N | Infineon datasheet | Voltage, current, gate charge and thermal data | To be added |
| Receiver simulation diode | Exact 1N5819 manufacturer datasheet | Reverse voltage, forward drop and current rating | To be confirmed before hardware |
| 5 V LTspice regulator | [Analog Devices LT1376 product page](https://www.analog.com/en/products/lt1376.html) and [datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/13756fd.pdf) | Official LTspice model and 5 V/1 A application | Added 2026-09-02 |
| Optional linear regulator | [STMicroelectronics L78 datasheet](https://www.st.com/resource/en/datasheet/l78.pdf) | Dropout and thermal-loss comparison | Added 2026-09-02 |
| Hardware buck alternative | Exact selected module and regulator datasheet | Input range and regulator design | To be selected after receiver-bus tests |
| USB charging detection | Applicable USB charging specification/controller datasheet | Phone compatibility | To be added |

Marketplace listings are not substitutes for manufacturer datasheets.
