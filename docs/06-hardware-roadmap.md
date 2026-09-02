# 6. Hardware development roadmap

## 6.1 Proposed complete architecture

1. A current-limited 12 V DC supply powers the transmitter.
2. An oscillator provides an approximately 100 kHz command.
3. A half-bridge gate driver controls two N-channel MOSFETs with dead time.
4. The half bridge excites the series-compensated transmitter coil.
5. The receiver coil and capacitor form the second resonator.
6. A high-frequency Schottky bridge converts AC to DC.
7. A filter capacitor and TVS limit receiver-bus disturbance.
8. A buck converter regulates the output to 5.0 V.
9. A USB charging-port controller may be needed for phone compatibility.

## 6.2 Preliminary parts, not yet validated

The preliminary concept uses an NE555 oscillator, IRS2104 half-bridge driver,
two IRLZ44N MOSFETs, polypropylene resonant capacitors, fast Schottky rectifiers
and an LM2596-class buck stage. These parts are hypotheses for Stage 2 and Stage 3,
not approved final selections.

Before hardware use, verify:

- gate-driver supply range and undervoltage lockout;
- bootstrap component values and high-side duty-cycle limitations;
- MOSFET voltage, current, switching loss and thermal margin;
- resonant capacitor RMS current and peak voltage;
- rectifier reverse voltage and loss;
- buck converter input range at every coupling and load condition;
- receiver overvoltage at no load;
- USB charging-port signalling; and
- electromagnetic and thermal behaviour.

## 6.3 Planned simulations

| Model | Purpose | Completion criterion |
|---|---|---|
| Stage 1 resonant link | Learn resonance and coupling | LTspice agrees with reference sweep |
| Half bridge with resistive load | Validate gates and dead time | No cross-conduction; acceptable loss |
| Half bridge plus resonant link | Assess coil current and voltage | Components remain within ratings |
| Rectifier and capacitor | Check DC bus and diode stress | Stable bus over load/coupling range |
| Buck and dummy load | Verify regulated output | 5.0 V within defined tolerance |
| Fault cases | Open load, short, misalignment | Protected shutdown or safe current |

## 6.4 Test progression

Begin with a low supply voltage and a strict current limit. Use a dummy load and
oscilloscope before any phone connection. Increase input voltage in small steps,
checking coil current, MOSFET temperature, resonant capacitor voltage and receiver
bus voltage at each step.

