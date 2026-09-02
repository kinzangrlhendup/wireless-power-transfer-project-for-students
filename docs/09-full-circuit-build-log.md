# 9. Full-circuit LTspice build log

## 9.1 Purpose and status

This chapter records the circuit assembled interactively on 2 September 2026.
The agreed method is to complete the schematic before running block tests. The
circuit described here is therefore **under construction and not yet validated**.
Values may change after the first controlled simulations.

The engineering target is a regulated 5 V output at up to 1 A, initially at an
approximately 10 cm coil gap. A 20 cm gap is a stretch goal. A phone must not be
connected until the output has passed regulation, ripple, transient and thermal
tests with a dummy load.

## 9.2 System signal flow

```text
12 V input -> NE555 oscillator -> complementary logic -> LTC4444 driver
           -> MOSFET half bridge -> series-tuned transmitter coil
           -> magnetic coupling -> series-tuned receiver coil
           -> Schottky bridge -> DC filter -> 5 V regulator -> dummy load
```

## 9.3 Input supply

| Reference | Value | Connection |
|---|---:|---|
| V1 | 12 V DC | Source for the transmitter electronics and half bridge |
| R_Fuse | 0.05 ohm | Simulation model of series fuse/contact resistance |
| CIN1 | 470 microfarad | Post-fuse 12 V rail to ground |
| CIN2 | 100 nanofarad | Post-fuse 12 V rail to ground |

`R_Fuse` is not a real fuse model. Hardware requires a correctly rated fuse and a
current-limited bench supply during commissioning.

## 9.4 NE555 oscillator

The NE555 is connected as an astable oscillator:

| Item | Value or connection |
|---|---|
| VCC | +12Vdc |
| GND | Transmitter ground |
| RESET | +12Vdc |
| TRIG and THRS | Joined timing node; rename consistently to `TIMING` |
| DIS to +12Vdc | RA = 1 kilohm |
| DIS to TIMING | RB = 6.8 kilohm |
| TIMING to ground | CT = 1 nanofarad |
| CV to ground | 10 nanofarad |
| OUT | `CLK_100k` |

The nominal astable frequency is

\[
f \approx \frac{1.44}{(R_A+2R_B)C_T}
  = \frac{1.44}{(1\text{ k}\Omega+2\times6.8\text{ k}\Omega)(1\text{ nF})}
  \approx 98.6\text{ kHz}.
\]

The theoretical high-state duty cycle is approximately

\[
D_H = \frac{R_A+R_B}{R_A+2R_B} \approx 53.4\%.
\]

The oscillator will later be tuned against the measured resonant frequency rather
than treated as exactly 100 kHz.

## 9.5 Complementary input stage

The LTC4444 has separate top and bottom inputs, so a 2N3904 common-emitter stage
creates the inverted signal:

| Component | Value | Connection |
|---|---:|---|
| RINV_B | 4.7 kilohm | `CLK_100k` to QINV base |
| RINV_BE | 10 kilohm | QINV base to ground |
| QINV | 2N3904 | Emitter to ground |
| RINV_PU | 4.7 kilohm | QINV collector to +12Vdc |
| Collector output | — | Label `CLK_INV` |

When `CLK_100k` is high, QINV turns on and pulls `CLK_INV` low. When
`CLK_100k` is low, RINV_PU pulls `CLK_INV` high. Propagation delay and edge shape
must be checked before hardware because logic inversion alone does not prove safe
dead time.

## 9.6 LTC4444 and half bridge

| LTC4444 pin | Connection |
|---|---|
| VCC | +12Vdc |
| GND | Transmitter ground |
| TINP | `CLK_100k` |
| BINP | `CLK_INV` |
| TG | 10 ohm resistor to high-side MOSFET gate |
| BG | 10 ohm resistor to low-side MOSFET gate |
| TS | `SW`, the half-bridge midpoint |
| BOOST | Bootstrap node |

Bootstrap and local supply components:

- 1N5819 from VCC anode to BOOST cathode;
- 220 nanofarad from BOOST to TS;
- 1 microfarad and 100 nanofarad from VCC to ground.

Power MOSFET connections:

| Device | Drain | Source | Gate network |
|---|---|---|---|
| M1 high side | +12Vdc | SW | TG through 10 ohm; 10 kilohm gate-to-SW pull-down |
| M2 low side | SW | Ground | BG through 10 ohm; 10 kilohm gate-to-ground pull-down |

The generic `NMOS` symbols must be replaced with real models before simulation.
The MOSFET voltage rating, gate charge, switching loss and thermal margin remain
open design items.

## 9.7 Resonant transmitter and receiver

The transmitter branch is connected directly to the half-bridge midpoint:

```text
SW -> C_TX 82 nF -> R_TX 0.3 ohm -> L_TX 30 uH -> ground
```

The receiver is a floating series branch:

```text
AC1 -> L_RX 30 uH -> R_RX 0.3 ohm -> C_RX 82 nF -> AC2
```

The isolated single-coil resonance is

\[
f_0=\frac{1}{2\pi\sqrt{LC}}
   \approx\frac{1}{2\pi\sqrt{30\,\mu\text{H}\times82\,\text{nF}}}
   \approx101.5\text{ kHz}.
\]

Initial magnetic coupling is declared with:

```spice
K1 L_TX L_RX 0.10
```

Only one `K1` directive may exist. Both inductor instance names must match the
directive exactly. A frequent construction error is entering `30n` for L_TX; the
required value is `30u`.

## 9.8 Receiver rectifier and filter

The bridge uses four 1N5819 models for the first simulation:

| Diode | Anode | Cathode |
|---|---|---|
| D_RX1 | AC1 | VRECT |
| D_RX2 | AC2 | VRECT |
| D_RX3 | RX_NEG | AC1 |
| D_RX4 | RX_NEG | AC2 |

The 1N5819 is a simulation convenience, not the preferred final 1 A bridge. SS34
or MBR340-class parts are hardware candidates, subject to measured voltage,
current, loss and temperature.

Filter components are connected across VRECT and RX_NEG:

| Reference | Value | Purpose |
|---|---:|---|
| C_RECT | 1000 microfarad, 35 V minimum for hardware | Bulk energy storage |
| C_RECT_HF | 100 nanofarad | High-frequency bypass |
| R_BLEED | 10 kilohm | Controlled discharge after shutdown |

## 9.9 Five-volt regulation decision

The current LTspice candidate is `LT1376-5`, a fixed 5 V buck regulator with an
official Analog Devices model and a 5 V/1 A example circuit. It is not yet placed
in the student schematic. The rectified bus must remain above the regulator's
dropout requirement and below its maximum input rating.

An L7805 was considered because it is simple and commonly available. It is not
selected for the 1 A target because its approximate loss is

\[
P_{loss}=(V_{RECT}-5\text{ V})I_{OUT}.
\]

At 10 V input and 1 A output, it dissipates approximately 5 W and is only about
50 percent efficient before accounting for quiescent current. It may be used in a
separate low-current teaching exercise at approximately 100 to 200 mA with thermal
analysis and adequate heatsinking.

## 9.10 Mandatory pre-simulation checks

- [ ] L_TX displays `30u`, not `30n`.
- [ ] L_RX displays `30u`.
- [ ] Exactly one `K1 L_TX L_RX 0.10` directive exists.
- [ ] The half-bridge midpoint uses one consistent `SW` label.
- [ ] M1 and M2 have real MOSFET models rather than generic `NMOS` values.
- [ ] TG drives only M1 and BG drives only M2.
- [ ] The high-side gate pull-down returns to SW, not ground.
- [ ] D_RX1 through D_RX4 have the polarities listed above.
- [ ] C_RECT polarity is positive at VRECT.
- [ ] The selected 5 V regulator and dummy load are present.
- [ ] A receiver reference strategy is included for SPICE convergence.
- [ ] The transient command uses a suitably small maximum timestep.

## 9.11 Planned validation order

After completing the regulator and assigning device models, test the blocks in
this order without connecting a phone:

1. Verify `CLK_100k` frequency, amplitude and duty cycle.
2. Verify `CLK_INV` polarity and transition delay.
3. Verify TG, BG and gate-source voltages; prove that M1 and M2 do not overlap.
4. Check SW with a current-limited or resistive test configuration.
5. Verify transmitter current and resonant capacitor voltage.
6. Sweep coupling coefficient and oscillator frequency.
7. Check AC1-to-AC2 voltage, VRECT ripple and diode currents.
8. Apply staged dummy loads before the final 5 ohm, 10 W test.
9. Verify 5.0 V regulation, input/output power, efficiency and device dissipation.

The phone remains disconnected throughout these tests.
