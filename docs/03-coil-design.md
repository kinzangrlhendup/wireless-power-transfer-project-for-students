# 3. Coil and compensation design

## 3.1 Preliminary flat-spiral estimate

Wheeler's empirical expression for a single-layer circular planar coil can provide
a starting estimate:

$$
L(\mu H)\approx\frac{r_\mathrm{avg}^2N^2}{8r_\mathrm{avg}+11w}
$$

where dimensions are in inches, $r_\mathrm{avg}$ is the average coil radius, $w$
is the radial winding width and $N$ is the number of turns.

One tentative starting geometry is:

| Parameter | Starting value |
|---|---:|
| Outside diameter | 180 mm |
| Inside diameter | 80 mm |
| Turns | approximately 14 |
| Conductor | Litz wire or multiple insulated fine strands |
| Target inductance | approximately 30 microhenry |

This is an estimate, not a manufacturing guarantee. Lead length, turn spacing and
nearby material affect the measured result.

## 3.2 Skin effect

At 100 kHz, current crowds toward the conductor surface. The copper skin depth is
approximately 0.2 mm. A thick solid conductor therefore does not use its full
cross-section efficiently. Litz wire divides current among many insulated fine
strands and can reduce AC resistance when correctly selected and terminated.

## 3.3 Selecting the resonant capacitor

After measuring inductance, calculate:

$$
C=\frac{1}{(2\pi f_r)^2L}
$$

Example for 30 microhenry at 100 kHz:

$$
C\approx84.4\,nF
$$

The initial simulation uses 82 nanofarad, producing approximately 101.5 kHz
isolated resonance. The physical design may use parallel film capacitors to obtain
the required value and ripple-current capability.

## 3.4 Capacitor technology

Use polypropylene film capacitors for the resonant network. Their low loss and
appropriate AC behaviour are preferable to electrolytic capacitors. A voltage
rating substantially above the supply is required because resonant capacitor
voltage can exceed the DC input voltage.

The preliminary bill of materials uses at least 250 V parts, subject to verification
from simulated and measured peak voltage plus an engineering margin.

## 3.5 Coupling measurement

If an LCR meter is available, connect the coils in series in aiding and opposing
orientations and measure $L_a$ and $L_o$. For two coupled inductors:

$$
M=\frac{L_a-L_o}{4}
$$

Then:

$$
k=\frac{M}{\sqrt{L_1L_2}}
$$

Record separation, lateral offset and angle with every coupling measurement.

