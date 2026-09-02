#!/usr/bin/env python3
"""Reproduce the Stage 1 coupled-resonator reference sweep.

This is a transparent sinusoidal steady-state calculation. It is deliberately
kept separate from LTspice results so students can compare two methods.
"""

from pathlib import Path
import csv

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REFERENCE_DIR = ROOT / "results" / "reference"
FIGURE_DIR = ROOT / "results" / "figures"

L1 = 30e-6
L2 = 30e-6
C1 = 82e-9
C2 = 82e-9
RSOURCE = 2.0
RCOIL1 = 0.3
RCOIL2 = 0.3
RLOAD = 10.0
VSOURCE_PEAK = 5.0
VSOURCE_RMS = VSOURCE_PEAK / np.sqrt(2.0)
COUPLINGS = (0.02, 0.05, 0.10, 0.15, 0.20)
# A 50 Hz step is fine enough for this teaching model while keeping the
# committed CSV compact enough for convenient cloning and review.
FREQUENCIES = np.linspace(60e3, 140e3, 1601)


def solve_frequency_sweep(k: float) -> dict[str, np.ndarray]:
    omega = 2.0 * np.pi * FREQUENCIES
    mutual_inductance = k * np.sqrt(L1 * L2)

    z1 = RSOURCE + RCOIL1 + 1j * (omega * L1 - 1.0 / (omega * C1))
    z2 = RLOAD + RCOIL2 + 1j * (omega * L2 - 1.0 / (omega * C2))
    zin = z1 + (omega * mutual_inductance) ** 2 / z2

    i1 = VSOURCE_RMS / zin
    i2 = -1j * omega * mutual_inductance * i1 / z2
    p_load = np.abs(i2) ** 2 * RLOAD
    p_source = np.real(VSOURCE_RMS * np.conj(i1))
    efficiency = np.divide(
        p_load,
        p_source,
        out=np.zeros_like(p_load),
        where=p_source > 0,
    )

    return {
        "i1_rms": np.abs(i1),
        "i2_rms": np.abs(i2),
        "vload_rms": np.abs(i2) * RLOAD,
        "p_load": p_load,
        "p_source": p_source,
        "efficiency": efficiency,
    }


def write_results(all_results: dict[float, dict[str, np.ndarray]]) -> list[dict[str, float]]:
    REFERENCE_DIR.mkdir(parents=True, exist_ok=True)
    summary: list[dict[str, float]] = []

    with (REFERENCE_DIR / "ac-sweep-curves.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["coupling_k", "frequency_hz", "primary_current_rms_a",
             "secondary_current_rms_a", "load_voltage_rms_v", "load_power_w",
             "source_power_w", "link_efficiency_fraction"]
        )
        for k, values in all_results.items():
            for index, frequency in enumerate(FREQUENCIES):
                writer.writerow(
                    [k, frequency, values["i1_rms"][index], values["i2_rms"][index],
                     values["vload_rms"][index], values["p_load"][index],
                     values["p_source"][index], values["efficiency"][index]]
                )

            peak_index = int(np.argmax(values["p_load"]))
            summary.append(
                {
                    "coupling_k": k,
                    "peak_frequency_hz": float(FREQUENCIES[peak_index]),
                    "peak_load_power_w": float(values["p_load"][peak_index]),
                    "primary_current_rms_a": float(values["i1_rms"][peak_index]),
                    "secondary_current_rms_a": float(values["i2_rms"][peak_index]),
                    "load_voltage_rms_v": float(values["vload_rms"][peak_index]),
                    "source_power_w": float(values["p_source"][peak_index]),
                    "link_efficiency_fraction": float(values["efficiency"][peak_index]),
                }
            )

    with (REFERENCE_DIR / "ac-sweep-summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary[0].keys())
        writer.writeheader()
        writer.writerows(summary)

    return summary


def create_plots(all_results: dict[float, dict[str, np.ndarray]], summary: list[dict[str, float]]) -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")

    fig, axis = plt.subplots(figsize=(9, 5.4), constrained_layout=True)
    for k, values in all_results.items():
        axis.plot(FREQUENCIES / 1e3, values["p_load"], label=f"k = {k:.2f}")
    axis.set(title="Stage 1 load power versus frequency", xlabel="Frequency (kHz)", ylabel="Load power (W)")
    axis.legend(title="Coupling")
    fig.savefig(FIGURE_DIR / "ac-sweep-load-power.png", dpi=180)
    plt.close(fig)

    fig, axis = plt.subplots(figsize=(7.5, 5), constrained_layout=True)
    coupling = [row["coupling_k"] for row in summary]
    peak_power = [row["peak_load_power_w"] for row in summary]
    axis.plot(coupling, peak_power, marker="o")
    axis.set(title="Peak load power versus coupling", xlabel="Coupling coefficient, k", ylabel="Peak load power (W)")
    fig.savefig(FIGURE_DIR / "coupling-vs-peak-power.png", dpi=180)
    plt.close(fig)


def main() -> None:
    results = {k: solve_frequency_sweep(k) for k in COUPLINGS}
    summary = write_results(results)
    create_plots(results, summary)

    resonance = 1.0 / (2.0 * np.pi * np.sqrt(L1 * C1))
    print(f"Isolated LC resonance: {resonance / 1e3:.3f} kHz")
    for row in summary:
        print(
            f"k={row['coupling_k']:.2f}: peak {row['peak_load_power_w']:.4f} W "
            f"at {row['peak_frequency_hz'] / 1e3:.2f} kHz"
        )


if __name__ == "__main__":
    main()
