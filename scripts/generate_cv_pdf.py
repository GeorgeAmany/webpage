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
LINK = "#0f766e"

CONTACT_LINKS = {
    "email": "mailto:georgeamany5@gmail.com",
    "linkedin": "https://www.linkedin.com/in/george-amany-53b148219/",
    "github": "https://github.com/GeorgeAmany",
}

PROJECT_LINKS = {
    "Noor Institute": [
        ("Google Play", "https://play.google.com/store/apps/details?id=com.softera.noor_academy"),
        ("App Store", "https://apps.apple.com/eg/app/noor-institute/id6463731504"),
    ],
    "Schupply": [
        ("Google Play", "https://play.google.com/store/apps/details?id=com.schupply.app"),
    ],
    "Binge": [
        ("Google Play", "https://play.google.com/store/apps/details?id=com.jigsaw.binge&hl=ar"),
    ],
    "Al Wefaq Foods": [
        ("Google Play", "https://play.google.com/store/apps/details?id=com.alwefaqfoods.app"),
    ],
    "Horse Time": [
        ("Google Play", "https://play.google.com/store/apps/details?id=com.horsetime.user&hl=en"),
        ("App Store", "https://apps.apple.com/eg/app/horse-time/id6758008343"),
    ],
    "Al Rassi": [
        ("Google Play", "https://play.google.com/store/apps/details?id=com.appsbunches.alrassiapp"),
        ("App Store", "https://apps.apple.com/eg/app/%D8%A7%D9%84%D8%B1%D8%B3%D9%8A-%D9%84%D9%84%D8%A7%D8%B4%D8%AC%D8%A7%D8%B1-%D8%A7%D9%84%D8%B5%D9%86%D8%A7%D8%B9%D9%8A%D8%A9/id6736564188"),
    ],
    "animated_contact_us": [
        ("pub.dev", "https://pub.dev/packages/animated_contact_us"),
        ("GitHub", "https://github.com/GeorgeAmany/animated_contact_us"),
    ],
    "liquid_wave_indicator": [
        ("pub.dev", "https://pub.dev/packages/liquid_wave_indicator"),
        ("GitHub", "https://github.com/GeorgeAmany/liquid_wave_indicator"),
    ],
}

PACKAGE_LINKS = {
    "animated_contact_us": "https://pub.dev/packages/animated_contact_us",
    "liquid_wave_indicator": "https://pub.dev/packages/liquid_wave_indicator",
}


def link(label, url):
    return f'<a href="{url}" color="{LINK}">{label}</a>'


def link_row(items):
    return " · ".join(link(label, url) for label, url in items)


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
            "Mid Flutter Developer | Mobile &amp; Desktop Cross-Platform Engineer",
            styles["title"],
        ),
        Paragraph(
            "Cairo, Egypt | "
            f'{link("georgeamany5@gmail.com", CONTACT_LINKS["email"])} | +20 127 003 7845<br/>'
            f'{link("LinkedIn", CONTACT_LINKS["linkedin"])} | '
            f'{link("GitHub", CONTACT_LINKS["github"])}',
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
                "Led Fuse: dual-app architecture for agencies and influencers with Cubit, Injectable DI, Freezed, Dio, Firebase, and Storyly.",
                "Built Taleem student and employee apps for Islamic education: REST API integration, Quran SQLite databases, attendance/memorization modules, and GitHub Actions CI for automated APK builds.",
                "Enhanced Noor Institute: Stripe payments, Pusher real-time chat, Floor local DB, Retrofit API, and Firebase push notifications.",
                "Delivered desktop apps: Zahran POS (offline invoice sync, PDF printing, Hive) and Proposal Desktop (PDF document builder with flutter_bloc).",
                "Integrated REST APIs, Firebase, social auth, maps, and payment gateways across Schupply, Zahran, Binge, and Al Wefaq Foods.",
                f'Published open-source packages on pub.dev: {link("animated_contact_us", PACKAGE_LINKS["animated_contact_us"])} and {link("liquid_wave_indicator", PACKAGE_LINKS["liquid_wave_indicator"])}.',
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
        ("Noor Institute", "Education — production app on Google Play & App Store", "Noor Institute"),
        ("Fuse", "Influencer marketing — dual-role mobile platform", None),
        ("Taleem (Student & Employees)", "Islamic education — REST API, Quran SQLite, GitHub Actions CI", None),
        ("Schupply", "School supplies e-commerce", "Schupply"),
        ("Zahran (Mobile & Desktop POS)", "E-commerce & POS — offline sync, PDF printing", None),
        ("Binge", "Food subscription — Firebase Analytics, Amazon Payment Services", "Binge"),
        ("Al Wefaq Foods", "Food brand mobile app", "Al Wefaq Foods"),
        ("Horse Time", "On-demand booking — chat, maps, multi-gateway payments", "Horse Time"),
        ("Al Rassi", "Industrial / manufacturing production app", "Al Rassi"),
        (
            "animated_contact_us & liquid_wave_indicator",
            "Open-source Flutter packages on pub.dev",
            "animated_contact_us",
        ),
    ]
    for name, desc, link_key in projects:
        line = f"<b>{name}</b> — {desc}"
        if link_key == "animated_contact_us":
            line += "<br/>" + link_row(PROJECT_LINKS["animated_contact_us"]) + " · " + link_row(PROJECT_LINKS["liquid_wave_indicator"])
        elif link_key and link_key in PROJECT_LINKS:
            line += "<br/>" + link_row(PROJECT_LINKS[link_key])
        story.append(Paragraph(line, styles["body"]))

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
