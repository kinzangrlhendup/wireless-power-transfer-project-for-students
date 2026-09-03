# Changelog

## 0.3.0 — 2026-09-03

- Recorded the 102.151 kHz NE555 result.
- Recorded the failed `k = 0.10` case with 2.557 V average VRECT.
- Retained one LTC4444 and the two-MOSFET half bridge.
- Documented the 120 uH/20 nF receiver and assumed `k = 0.20`.
- Recorded the simulated 5 V/250 mA point with a 20 ohm load.
- Marked the original 5 V/1 A target as not achieved.
- Added the captured result and machine-readable summary.
- Replaced the ideal SHDN pulse in the hardware plan with a proposed UVLO network.
- Updated the BOM, models, references, roadmap and status.

## 0.2.0 — 2026-09-02

- Documented the 12 V NE555/LTC4444 half-bridge transmitter under construction.
- Added the 2N3904 complementary-input stage and bootstrap details.
- Documented matched 30 microhenry and 82 nanofarad resonators at about 101.5 kHz.
- Added the four-diode receiver bridge, DC filter and bleeder network.
- Recorded the LT1376-5 regulator choice and why L7805 is limited to low-current teaching use.
- Added a complete build log, connection tables and pre-simulation checklist.

## 0.1.0 — 2026-09-02

- Added student-facing theory and design documentation.
- Added Stage 1 LTspice schematic and portable SPICE netlist.
- Added preliminary bill of materials and model manifest.
- Added reproducible analytical reference-simulation script.
- Added result and student-exercise structure.
