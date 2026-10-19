#!/usr/bin/env python3
"""
Pemeriksa kelengkapan tugas M2 — EDA KMTI21133.

Jalankan dari folder akar repositori:
    python cek_m2.py

Pemeriksaan:
- Berkas pengumpulan utama tersedia.
- Struktur folder utama tersedia.
- cleaning_log.md memiliki bagian minimal yang diharapkan.
- Dataset hasil cleaning M2 tersedia di data/processed/.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    Path("reports/data_quality_report.docx"),
    Path("notebooks/02_cleaning.ipynb"),
    Path("cleaning_log.md"),
]

REQUIRED_DIRS = [
    Path("reports"),
    Path("notebooks"),
    Path("data/raw"),
    Path("data/processed"),
]

# Berkas hasil cleaning ini merupakan pemeriksaan pendukung proyek tim.
EXPECTED_OUTPUT = Path("data/processed/supermarket_clean_m2.csv")

# Cleaning log diharapkan mencatat langkah, jumlah baris terdampak,
# alasan keputusan, dampak keseluruhan, dan reproduktibilitas.
LOG_MARKERS = [
    "langkah",
    "baris terdampak",
    "alasan",
    "dampak keseluruhan",
    "reproduktibilitas",
]


def main():
    errors = []
    warnings = []

    print("Pemeriksaan kelengkapan M2")
    print(f"Folder proyek: {ROOT}")
    print("-" * 55)

    print("\n[1] Struktur folder")
    for rel_path in REQUIRED_DIRS:
        exists = (ROOT / rel_path).is_dir()
        print(f"[{'OK' if exists else 'GAGAL'}] {rel_path}/")
        if not exists:
            errors.append(f"Folder tidak ditemukan: {rel_path}/")

    print("\n[2] Berkas wajib")
    for rel_path in REQUIRED_FILES:
        exists = (ROOT / rel_path).is_file()
        print(f"[{'OK' if exists else 'GAGAL'}] {rel_path}")
        if not exists:
            errors.append(f"Berkas wajib tidak ditemukan: {rel_path}")

    print("\n[3] Hasil cleaning M2 (pemeriksaan pendukung)")
    output_exists = (ROOT / EXPECTED_OUTPUT).is_file()
    print(f"[{'OK' if output_exists else 'PERINGATAN'}] {EXPECTED_OUTPUT}")
    if not output_exists:
        warnings.append(
            f"Hasil cleaning belum ditemukan: {EXPECTED_OUTPUT}. "
            "Pastikan nama/path sesuai dengan output notebook tim."
        )

    print("\n[4] Isi minimal cleaning_log.md")
    log_path = ROOT / "cleaning_log.md"
    if log_path.is_file():
        log_text = log_path.read_text(encoding="utf-8").lower()
        for marker in LOG_MARKERS:
            found = marker in log_text
            print(f"[{'OK' if found else 'GAGAL'}] Memuat istilah/bagian: {marker}")
            if not found:
                errors.append(
                    f"Cleaning log belum menunjukkan bagian/istilah: {marker}"
                )
    else:
        print("[GAGAL] Tidak dapat memeriksa isi karena cleaning_log.md tidak ditemukan.")

    print("\n" + "-" * 55)
    for warning in warnings:
        print(f"PERINGATAN: {warning}")

    if errors:
        print(f"\nSTATUS: GAGAL — {len(errors)} masalah perlu diperiksa.")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nSTATUS: LULUS pemeriksaan kelengkapan dasar.")
    print("Catatan: skrip ini tidak menilai kebenaran analisis atau keputusan cleaning.")
    if warnings:
        print(f"Ada {len(warnings)} peringatan yang sebaiknya ditinjau.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
