#!/usr/bin/env python3
"""Generate synced George Amany CV Word document from evidence-based content."""

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "assets" / "George_Amany_CV_2025.docx"

doc = Document()
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

# --- Header ---
name = doc.add_paragraph()
name.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = name.add_run("George Amany")
run.bold = True
run.font.size = Pt(22)

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run("Senior Flutter Developer | Mobile & Desktop Cross-Platform Engineer")
run.font.size = Pt(12)

contact = doc.add_paragraph()
contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
contact.add_run(
    "Cairo, Egypt | georgeamany5@gmail.com | +20 127 003 7845 | "
    "linkedin.com/in/george-amany-53b148219 | github.com/GeorgeAmany"
)

doc.add_paragraph()

# --- Professional Summary ---
doc.add_heading("Professional Summary", level=1)
doc.add_paragraph(
    "Flutter engineer with a Bachelor's degree in Computer Science and production experience "
    "building and shipping mobile and desktop applications across education, e-commerce, food "
    "services, and influencer marketing. At Neural Design Studios, delivers feature-first Clean "
    "Architecture apps using BLoC/Cubit, Dio/Retrofit REST integrations, Firebase, Hive/Floor "
    "local storage, and cross-platform desktop tooling (macOS/Windows). Published multiple apps "
    "to Google Play and the App Store, authored open-source packages on pub.dev, and set up "
    "GitHub Actions CI for automated APK builds."
)

# --- Core Skills ---
doc.add_heading("Core Skills", level=1)
skills = [
    "Flutter & Dart", "Clean Architecture", "BLoC / Cubit State Management", "GetIt / Injectable DI",
    "Dio & Retrofit REST APIs", "Firebase (Auth, Firestore, Messaging, Crashlytics, Analytics)",
    "Hive, Floor & SQLite Local Storage", "GoRouter Navigation", "Freezed & Dartz",
    "Stripe & Multi-Gateway Payments", "Pusher Real-Time", "Flutter Desktop (macOS/Windows)",
    "Git & GitHub Actions CI/CD", "Easy Localization", "Postman", "Clean Code & Code Review",
]
p = doc.add_paragraph(", ".join(skills))

# --- Experience ---
doc.add_heading("Professional Experience", level=1)

doc.add_heading("Flutter Developer — Neural Design Studios", level=2)
doc.add_paragraph("Full-time | Cairo, Egypt | Jun 2024 – Present")
bullets = [
    "Shipped production Flutter apps across education, e-commerce, food, and influencer marketing domains with feature-first Clean Architecture (data/domain/presentation layers, repository pattern, use cases).",
    "Led development on Fuse (influencer marketing platform, 185+ commits): dual-app architecture for agencies and influencers with Cubit, Injectable DI, Freezed models, Dio networking, Firebase Auth/Realtime DB, and Storyly integration.",
    "Built Taleem student and employee apps (300+ combined commits) for Islamic education: REST v2 API integration, Quran local SQLite databases, attendance/memorization/evaluation modules, and GitHub Actions CI pipeline for automated debug APK builds on Flutter 3.35.7.",
    "Enhanced Noor Institute app (v3.7.0, 63+ commits): Stripe payment flow, Pusher real-time chat, Floor local DB, Retrofit API layer, Syncfusion calendar, and Firebase push notifications.",
    "Delivered cross-platform desktop apps: Zahran POS (offline invoice sync, PDF printing, Hive storage) and Proposal Desktop (PDF document builder with flutter_bloc and window_manager).",
    "Integrated REST APIs, Firebase services, Google/Apple Sign-In, Google Maps, and payment gateways (Stripe, Amazon Payment Services) across Schupply, Zahran, Binge, and Al Wefaq Foods apps.",
    "Published and maintained open-source Flutter packages on pub.dev: animated_contact_us (v0.0.8) and liquid_wave_indicator (v0.2.2).",
    "Applied maintainability practices: dependency injection, typed API clients, localization (easy_localization), structured error handling, and consistent feature module boundaries.",
]
for b in bullets:
    doc.add_paragraph(b, style="List Bullet")

doc.add_heading("Flutter Developer — Neural Design Studios", level=2)
doc.add_paragraph("Part-time | Cairo, Egypt | Feb 2024 – Jun 2024")
for b in [
    "Collaborated with cross-functional teams to deliver responsive, production-ready Flutter applications.",
    "Implemented UI performance optimizations and scalable state management patterns.",
]:
    doc.add_paragraph(b, style="List Bullet")

# --- Key Projects ---
doc.add_heading("Key Projects", level=1)

projects = [
    ("Noor Institute", "Education / Institute Management",
     "Production app (v3.7.0) for students, teachers, courses, homework, schedules, invoices, and chat. "
     "Clean Architecture with BLoC, Retrofit/Dio, Floor DB, Stripe payments, Pusher real-time, Firebase push.",
     "Flutter, BLoC, GetIt, Dio, Retrofit, Floor, Stripe, Pusher, Firebase, Freezed, Easy Localization",
     "Google Play & App Store"),
    ("Fuse", "Influencer Marketing",
     "Dual-role platform for agencies and influencers: profiles, content posting, service requests, stories.",
     "Flutter, Cubit, Injectable, Freezed, Dio, Hive, Firebase Auth/DB, Storyly, GoRouter",
     "Mobile App (Neural Design Studios)"),
    ("Taleem (Student & Employees)", "Islamic Education",
     "Student app (grades, absence, certificates, Quran mushaf) and staff app (halaqas, attendance, memorization, evaluations). GitHub Actions CI for APK builds.",
     "Flutter, BLoC, Dio, Hive, SQLite, Firebase Messaging, Fl Chart, Table Calendar",
     "Mobile Apps"),
    ("Schupply", "School Supplies E-Commerce",
     "School/grade package ordering with REST API, Hive caching, Google/Apple auth, deep links.",
     "Flutter, BLoC, Dio, Hive, GoRouter, Firebase Messaging",
     "Google Play"),
    ("Zahran (Mobile & Desktop POS)", "E-Commerce & Point of Sale",
     "Mobile e-commerce app and desktop POS with offline invoice sync, PDF export/printing, secure storage.",
     "Flutter, BLoC, Dio, Hive, Window Manager, Printing, PDF, Connectivity Plus",
     "Mobile & Desktop"),
    ("Binge", "Food Subscription & Meal Ordering",
     "Dishes, cart, subscriptions, wallet, loyalty program. Firebase Analytics/Crashlytics, Amazon Payment Services.",
     "Flutter, BLoC, Dio, Hive, Firebase, Google Maps, Clarity Analytics",
     "Production App"),
    ("Al Wefaq Foods", "Food Brand Mobile",
     "WebView wrapper with Firebase/OneSignal push, in-app messaging, QR scanner.",
     "Flutter, InAppWebView, MobX, Firebase, OneSignal",
     "Google Play"),
    ("Proposal Desktop", "Business Proposal Builder",
     "Desktop PDF proposal generator with editor, service packages, company info, payment methods.",
     "Flutter Desktop, BLoC, Dio, Hive, PDF, Printing, Window Manager",
     "Desktop App"),
    ("Horse Time", "On-Demand Service Booking",
     "User booking app with chat, payments, maps, and multi-gateway payment integration.",
     "Flutter, MobX, Firebase, Google Maps, Stripe/Razorpay/PayPal",
     "Mobile App"),
    ("animated_contact_us & liquid_wave_indicator", "Open Source (pub.dev)",
     "Published Flutter UI packages for animated contact widgets and liquid wave progress indicators.",
     "Flutter, Font Awesome, URL Launcher",
     "pub.dev"),
    ("Al Rassi", "Industrial / Manufacturing",
     "Published production mobile application.",
     "Flutter",
     "Google Play & App Store"),
]

for name, domain, desc, tech, platform in projects:
    doc.add_heading(name, level=2)
    doc.add_paragraph(f"Domain: {domain}")
    doc.add_paragraph(desc)
    doc.add_paragraph(f"Technologies: {tech}")
    doc.add_paragraph(f"Platform: {platform}")

# --- Education ---
doc.add_heading("Education", level=1)
doc.add_paragraph("Bachelor's Degree, Computer Science — Modern Academy Maadi, Cairo (2022)")

# --- Courses & Activities ---
doc.add_heading("Courses", level=1)
for c in [
    "Full Flutter Diploma (100 hours) — Array",
    "Flutter & Dart — Udemy",
    "Cyber Security Diploma (150 hours) — Instant",
]:
    doc.add_paragraph(c, style="List Bullet")

doc.add_heading("Community & Activities", level=1)
for a in [
    "Flutter workshop — Alalmiya Alhura, El Mansoura",
    "Flutter Forward Extended Cloud Egypt '23 — GDG Cloud Egypt",
    "Online Flutter workshop — Machinfy",
    "Penetration Tester Training (1 month) — Instant",
]:
    doc.add_paragraph(a, style="List Bullet")

doc.add_heading("Languages", level=1)
doc.add_paragraph("Arabic (Native) | English (Professional Working Proficiency)")

doc.save(OUTPUT)
print(f"Saved: {OUTPUT}")
