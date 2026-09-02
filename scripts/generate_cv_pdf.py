#!/usr/bin/env python3
"""Generate synced George Amany CV PDF (2026) from evidence-based content."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "assets" / "George_Amany_CV_2026.pdf"

ACCENT = colors.HexColor("#0f766e")
MUTED = colors.HexColor("#475569")


def build_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            spaceAfter=4,
            textColor=colors.HexColor("#0f172a"),
        ),
        "title": ParagraphStyle(
            "Title",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=4,
            textColor=MUTED,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            spaceAfter=14,
            textColor=MUTED,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            spaceBefore=10,
            spaceAfter=6,
            textColor=ACCENT,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            spaceAfter=2,
            textColor=colors.HexColor("#0f172a"),
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            spaceAfter=4,
            textColor=MUTED,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
            spaceAfter=6,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#1e293b"),
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            leftIndent=0,
            textColor=colors.HexColor("#1e293b"),
        ),
        "project": ParagraphStyle(
            "Project",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=12,
            spaceBefore=2,
            spaceAfter=1,
            textColor=colors.HexColor("#0f172a"),
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
            textColor=MUTED,
        ),
    }


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=12) for item in items],
        bulletType="bullet",
        start="•",
        leftIndent=14,
        bulletFontName="Helvetica",
        bulletFontSize=9,
        spaceBefore=0,
        spaceAfter=4,
    )


def main():
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.62 * inch,
        title="George Amany CV 2026",
        author="George Amany",
    )

    story = [
        Paragraph("George Amany", styles["name"]),
        Paragraph(
            "Senior Flutter Developer | Mobile &amp; Desktop Cross-Platform Engineer",
            styles["title"],
        ),
        Paragraph(
            "Cairo, Egypt | georgeamany5@gmail.com | +20 127 003 7845<br/>"
            "linkedin.com/in/george-amany-53b148219 | github.com/GeorgeAmany",
            styles["contact"],
        ),
        Paragraph("Professional Summary", styles["section"]),
        Paragraph(
            "Flutter engineer with a Bachelor's degree in Computer Science and production "
            "experience building and shipping mobile and desktop applications across education, "
            "e-commerce, food services, and influencer marketing. At Neural Design Studios, "
            "delivers feature-first Clean Architecture apps using BLoC/Cubit, Dio/Retrofit REST "
            "integrations, Firebase, Hive/Floor local storage, and cross-platform desktop tooling "
            "(macOS/Windows). Published multiple apps to Google Play and the App Store, authored "
            "open-source packages on pub.dev, and set up GitHub Actions CI for automated APK builds. "
            "Grew quickly under senior mentorship and now mentors interns and junior developers on "
            "Flutter, Clean Architecture, and code-quality standards.",
            styles["body"],
        ),
        Paragraph("Core Skills", styles["section"]),
        Paragraph(
            "Flutter &amp; Dart, Clean Architecture, BLoC / Cubit, GetIt / Injectable DI, "
            "Dio &amp; Retrofit REST APIs, Firebase (Auth, Firestore, Messaging, Crashlytics, Analytics), "
            "Hive, Floor &amp; SQLite, GoRouter, Freezed &amp; Dartz, Stripe &amp; Multi-Gateway Payments, "
            "Pusher Real-Time, Flutter Desktop (macOS/Windows), Git &amp; GitHub Actions CI/CD, "
            "Easy Localization, Clean Code &amp; Code Review, Mentoring Interns &amp; Junior Developers",
            styles["body"],
        ),
        Paragraph("Professional Experience", styles["section"]),
        Paragraph("Flutter Developer — Neural Design Studios", styles["role"]),
        Paragraph("Full-time | Cairo, Egypt | Jun 2024 – Present", styles["meta"]),
        bullets(
            [
                "Shipped production Flutter apps across education, e-commerce, food, and influencer marketing with feature-first Clean Architecture.",
                "Led Fuse (185+ commits): dual-app architecture for agencies and influencers with Cubit, Injectable DI, Freezed, Dio, Firebase, and Storyly.",
                "Built Taleem student and employee apps (300+ combined commits): REST v2 API, Quran SQLite databases, attendance/memorization modules, and GitHub Actions CI on Flutter 3.35.7.",
                "Enhanced Noor Institute (v3.7.0, 63+ commits): Stripe payments, Pusher real-time chat, Floor local DB, Retrofit API, and Firebase push.",
                "Delivered desktop apps: Zahran POS (offline invoice sync, PDF printing, Hive) and Proposal Desktop (PDF document builder with flutter_bloc).",
                "Integrated REST APIs, Firebase, social auth, maps, and payment gateways across Schupply, Zahran, Binge, and Al Wefaq Foods.",
                "Published open-source packages on pub.dev: animated_contact_us (v0.0.8) and liquid_wave_indicator (v0.2.2).",
                "Mentor interns and junior developers on Flutter, Clean Architecture, code review, and shipping first production features.",
            ],
            styles["bullet"],
        ),
        Paragraph("Flutter Developer — Neural Design Studios", styles["role"]),
        Paragraph("Part-time | Cairo, Egypt | Feb 2024 – Jun 2024", styles["meta"]),
        bullets(
            [
                "Collaborated with cross-functional teams to deliver responsive, production-ready Flutter applications.",
                "Implemented UI performance optimizations and scalable state management patterns.",
            ],
            styles["bullet"],
        ),
        Paragraph("Key Projects", styles["section"]),
    ]

    projects = [
        ("Noor Institute", "Education — Google Play & App Store"),
        ("Fuse", "Influencer marketing — dual-role mobile platform"),
        ("Taleem (Student & Employees)", "Islamic education — REST API, Quran SQLite, GitHub Actions CI"),
        ("Schupply", "School supplies e-commerce — Google Play"),
        ("Zahran (Mobile & Desktop POS)", "E-commerce & POS — offline sync, PDF printing"),
        ("Binge", "Food subscription — Firebase Analytics, Amazon Payment Services"),
        ("Horse Time", "On-demand booking — chat, maps, multi-gateway payments"),
        ("animated_contact_us & liquid_wave_indicator", "Open-source packages on pub.dev"),
    ]
    for name, desc in projects:
        story.append(Paragraph(f"{name} — {desc}", styles["body"]))

    story.extend(
        [
            Paragraph("Education", styles["section"]),
            Paragraph(
                "Bachelor's Degree, Computer Science — Modern Academy Maadi, Cairo (2022)",
                styles["body"],
            ),
            Paragraph("Courses &amp; Community", styles["section"]),
            bullets(
                [
                    "Full Flutter Diploma (100 hours) — Array",
                    "Flutter & Dart — Udemy",
                    "Cyber Security Diploma (150 hours) — Instant",
                    "Flutter workshop — Alalmiya Alhura, El Mansoura",
                    "Flutter Forward Extended Cloud Egypt '23 — GDG Cloud Egypt",
                ],
                styles["bullet"],
            ),
            Paragraph("Languages", styles["section"]),
            Paragraph(
                "Arabic (Native) | English (Professional Working Proficiency)",
                styles["body"],
            ),
            Spacer(1, 0.15 * inch),
            Paragraph("CV updated 2026 · George Amany", styles["footer"]),
        ]
    )

    doc.build(story)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    main()
