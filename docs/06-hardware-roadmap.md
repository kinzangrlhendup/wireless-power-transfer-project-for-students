# 6. Hardware development roadmap

## 6.1 Retained architecture

The retained transmitter is a 12 V NE555/LTC4444 half bridge. One LTC4444 drives
two MOSFETs. The receiver uses a tuned coil, full-wave Schottky bridge, bulk
capacitor, LT1376-5 buck converter and voltage-controlled SHDN enable.

## 6.2 Current milestone

The present LTspice milestone is approximately 5 V at 250 mA into 20 ohm with
`k = 0.20`. The original 5 V/1 A target was not achieved. There is no physical
distance or hardware-power validation yet.

## 6.3 Simulation parts versus hardware

| Function | Simulation | Hardware decision |
|---|---|---|
| Oscillator | NE555 | Verify stability and tolerance |
| Driver | LTC4444 | Retained; second driver not required |
| MOSFETs | IRFH5406 models | Choose orderable package after loss analysis |
| Rectifier | Four 1N5819 models | Choose lower-loss, adequately rated parts |
| Regulator | LT1376-5 | Candidate; follow datasheet PCB layout |
| TVS | Simplified DTVS18 | Select after measuring no-load VRECT |
| Coils | TX 30 uH; RX 120 uH | Wind and measure before selecting capacitors |

## 6.4 Practical SHDN circuit

Replace the ideal pulse source with:

- 20 kohm from VRECT to SHDN;
- 10 kohm from SHDN to RX_NEG;
- 68 kohm from +5V_OUT to SHDN;
- 1 nF from SHDN to RX_NEG.

The nominal thresholds are approximately 7.8 V turn-on and 6.4 V turn-off. Verify
them using component tolerances, SHDN bias current and the actual receiver bus.

## 6.5 Commissioning sequence

1. Measure coil inductance and AC resistance.
2. Recalculate both resonant capacitors.
3. Test the oscillator and driver without the resonant load.
4. Verify both gate-source waveforms and dead time.
5. Start the half bridge at reduced voltage with a strict current limit.
6. Measure switch-node voltage, coil current and resonant-capacitor voltage.
7. Characterise VRECT before connecting the buck converter.
8. Install the practical SHDN network and begin with a 50 ohm load.
9. Progress to 33 ohm and 20 ohm only when voltage and temperature are safe.
10. Measure input power, output power, efficiency and temperature.
11. Test alignment and distance; do not equate `k` directly with distance.
12. Keep phones disconnected until protection and USB behaviour are validated.

Stop if the MOSFET gates overlap, VRECT exceeds a rating, the regulator chatters,
or any component heats rapidly.
