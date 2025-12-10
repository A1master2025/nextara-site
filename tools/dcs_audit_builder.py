#!/usr/bin/env python3
"""
NexTara DCS Audit Landing Page Builder — Enterprise Edition
Generates production-ready Astro page package with governance controls.

Version: 1.0.0-enterprise
PromptCore Alignment: v3.7
"""

import os
import sys
import json
import hashlib
import zipfile
import logging
import argparse
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class BuildConfig:
    """Immutable build configuration."""
    version: str = "1.0.0-enterprise"
    promptcore_ver: str = "v3.7"
    domain: str = "https://www.nextara-ai-solutions.com"
    page_slug: str = "digital-credibility-score-audit"
    encoding: str = "utf-8"
    zip_compression: int = zipfile.ZIP_DEFLATED
    
    # Validation thresholds
    min_astro_size: int = 5000  # bytes
    min_css_size: int = 500
    required_schema_types: tuple = ("WebPage", "Service", "FAQPage")


@dataclass
class BuildManifest:
    """Tracks all generated artifacts for reproducibility."""
    version: str
    promptcore_ver: str
    generated_at: str
    hostname: str
    artifacts: dict = field(default_factory=dict)
    checksums: dict = field(default_factory=dict)
    validation: dict = field(default_factory=dict)


# ═══════════════════════════════════════════════════════════════════════════════
# LOGGING
# ═══════════════════════════════════════════════════════════════════════════════

def setup_logging(log_path: Optional[Path] = None) -> logging.Logger:
    """Configure structured logging with optional file output."""
    logger = logging.getLogger("dcs-builder")
    logger.setLevel(logging.DEBUG)
    
    fmt = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(fmt)
    logger.addHandler(console)
    
    if log_path:
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)
    
    return logger


# ═══════════════════════════════════════════════════════════════════════════════
# CONTENT GENERATORS
# ═══════════════════════════════════════════════════════════════════════════════

def generate_astro_content(config: BuildConfig) -> str:
    """Generate the Astro page content."""
    return '''---
import BaseLayout from '../layouts/BaseLayout.astro';

const pageTitle = 'Digital Credibility Score Audit | NexTara AI Solutions';
const pageDescription =
  'Request a Digital Credibility Score Audit to understand whether your current website can realistically reach a DCS 900+ standard and where your biggest gaps are.';
---

<BaseLayout title={pageTitle} description={pageDescription}>
  <main>
    {/* HERO SECTION */}
    <section class="hero-section hero-section--audit">
      <div class="container">
        <div class="hero-grid">
          <div class="hero-content">
            <h1 class="hero-title fade-up">Digital Credibility Score Audit</h1>
            <p class="hero-lead fade-up-delay-1">
              Find out if your current website can realistically earn a Digital Credibility Score of
              900+—or if you&apos;re leaving visibility, trust, and revenue on the table.
            </p>
            <ul class="hero-bullets fade-up-delay-2">
              <li>See where your site passes or fails modern AI + search tests.</li>
              <li>Understand what is blocking you from a DCS 900+ build.</li>
              <li>Get a prioritized, non-fluffy remediation roadmap.</li>
            </ul>
            <div class="hero-ctas fade-up-delay-3">
              <a href="#audit-form" class="btn btn-primary">Start My DCS Audit</a>
              <a href="/contact" class="btn btn-secondary">Talk with NexTara First</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    {/* WHAT YOU GET */}
    <section class="section">
      <div class="container">
        <h2 class="section-title">What You Get from a Digital Credibility Score Audit</h2>
        <p class="section-intro">
          This is a structured, engineering-grade audit—built to support executives, marketers, and
          technical owners who need clear answers, not another vague checklist.
        </p>
        <div class="grid grid-2">
          <ul class="feature-list">
            <li><strong>DCS Baseline Score.</strong> 0–1000 snapshot of your current credibility posture.</li>
            <li><strong>Category Breakdown.</strong> Scores across visibility, technical integrity, schema, trust, conversion, and analytics.</li>
            <li><strong>Issue Inventory.</strong> High, medium, and low–impact issues mapped to business risk.</li>
          </ul>
          <ul class="feature-list">
            <li><strong>Remediation Roadmap.</strong> Prioritized actions for your current team, agency, or NexTara to execute.</li>
            <li><strong>Readout Option.</strong> Optional review session to walk through the findings and answer questions.</li>
          </ul>
        </div>
      </div>
    </section>

    {/* EXECUTIVE SNAPSHOT */}
    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">Executive Audit Snapshot</h2>
        <p class="section-intro">
          The Digital Credibility Score Audit is delivered as a structured decision asset, not a loose
          collection of screenshots and suggestions.
        </p>
        <div class="audit-summary-grid">
          <div class="audit-summary-card">
            <h3 class="card-label">Primary Output</h3>
            <p class="card-value">Digital Credibility Score (0–1000) + Pillar Scores</p>
            <p class="card-note">Visibility, Technical Integrity, Trust, Conversion, Analytics &amp; Governance.</p>
          </div>
          <div class="audit-summary-card">
            <h3 class="card-label">Decision Question</h3>
            <p class="card-value">"Can this website support a DCS 900+ standard, or is a rebuild more efficient?"</p>
            <p class="card-note">Built to support executive &quot;fix vs. rebuild&quot; decisions.</p>
          </div>
          <div class="audit-summary-card">
            <h3 class="card-label">Deliverable Format</h3>
            <p class="card-value">Audit PDF + Issue Inventory + Roadmap</p>
            <p class="card-note">Vendor-neutral, suitable for internal teams or external agencies.</p>
          </div>
          <div class="audit-summary-card">
            <h3 class="card-label">Intended Owner</h3>
            <p class="card-value">CMO / Founder / Marketing or Operations Lead</p>
            <p class="card-note">Structured to brief stakeholders in one meeting.</p>
          </div>
        </div>
      </div>
    </section>

    {/* WHY IT MATTERS */}
    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">Why Your Digital Credibility Score Matters Now</h2>
        <p class="section-intro">
          Search engines and AI systems are reading your schema, your technical structure, your trust
          signals, and your analytics stack to decide whether your website deserves visibility.
        </p>
        <div class="grid grid-3">
          <div class="card">
            <h3 class="card-title">Visibility</h3>
            <p>If your score is low, high-intent buyers never see your pages—no matter how strong your copy is.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Efficiency</h3>
            <p>Ad spend has to fight against a weak technical foundation, driving higher CPCs and lower quality leads.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Confidence</h3>
            <p>A quantified score gives leadership a shared, objective view of the site&apos;s true readiness.</p>
          </div>
        </div>
      </div>
    </section>

    {/* WHO IT'S FOR */}
    <section class="section">
      <div class="container grid grid-2">
        <div>
          <h2 class="section-title">Who This Audit Is For</h2>
          <ul class="feature-list">
            <li>Organizations that treat their website as a growth asset, not a brochure.</li>
            <li>Teams considering a redesign and wanting proof before they commit.</li>
            <li>CMOs, founders, and marketing leaders who need clarity on "fix vs. rebuild" decisions.</li>
            <li>Businesses that want audit-grade documentation for internal stakeholders.</li>
          </ul>
        </div>
        <div class="card card-outline">
          <h3 class="card-title">When This Is Not a Fit</h3>
          <ul class="feature-list">
            <li>You want a quick checklist without implementation follow-through.</li>
            <li>No one owns the website or is accountable for acting on the findings.</li>
            <li>You are comfortable operating without measurable standards.</li>
          </ul>
        </div>
      </div>
    </section>

    {/* HOW IT WORKS */}
    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">How the Digital Credibility Score Audit Works</h2>
        <div class="steps-grid">
          <div class="step">
            <div class="step-number">1</div>
            <h3 class="step-title">Intake &amp; Context</h3>
            <p>You complete a short intake with your domain, current stack, and business priorities so the audit is aligned to reality.</p>
          </div>
          <div class="step">
            <div class="step-number">2</div>
            <h3 class="step-title">Signal Collection &amp; Scoring</h3>
            <p>We run your site through the DCS framework, covering visibility, schema, performance, trust, conversion, and analytics.</p>
          </div>
          <div class="step">
            <div class="step-number">3</div>
            <h3 class="step-title">Issue Mapping &amp; Prioritization</h3>
            <p>We identify the gaps preventing a DCS 900+ build and prioritize them by impact and effort.</p>
          </div>
          <div class="step">
            <div class="step-number">4</div>
            <h3 class="step-title">Delivery &amp; Readout</h3>
            <p>You receive the full audit PDF and score breakdown, with an optional readout session to walk through findings and next steps.</p>
          </div>
        </div>
      </div>
    </section>

    {/* FIVE PILLARS */}
    <section class="section">
      <div class="container">
        <h2 class="section-title">The Five Pillars of Your Digital Credibility Score</h2>
        <p class="section-intro">
          The DCS framework evaluates your website across five tightly-governed pillars. Each pillar
          contributes to your overall 0–1000 score and your ability to operate as a DCS 900+ website.
        </p>
        <div class="grid grid-3">
          <div class="card">
            <h3 class="card-title">1. Visibility Engine</h3>
            <p>How clearly search engines and AI systems can understand, crawl, and surface your pages. Schema structure, internal linking, and content architecture are evaluated here.</p>
          </div>
          <div class="card">
            <h3 class="card-title">2. Technical Integrity</h3>
            <p>Core Web Vitals, mobile responsiveness, rendering behavior, and code hygiene. This pillar determines whether your site meets modern performance expectations.</p>
          </div>
          <div class="card">
            <h3 class="card-title">3. Trust Layer</h3>
            <p>Brand consistency, proof assets, reviews, case studies, and compliance language. We measure whether your digital presence actually earns trust from both humans and algorithms.</p>
          </div>
          <div class="card">
            <h3 class="card-title">4. Conversion Spine</h3>
            <p>CTA hierarchy, page flow, form friction, and lead capture readiness. This is where we score how effectively your website converts qualified attention into qualified pipeline.</p>
          </div>
          <div class="card">
            <h3 class="card-title">5. Data &amp; Governance Layer</h3>
            <p>GA4, GTM, consent posture, and data hygiene. We evaluate whether your analytics and governance stack are capable of supporting accurate measurement and optimization.</p>
          </div>
        </div>
      </div>
    </section>

    {/* SAMPLE FINDINGS */}
    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">Sample Findings from a DCS Audit</h2>
        <p class="section-intro">
          The goal is not to overwhelm you with jargon—it&apos;s to give you a clear, prioritized
          picture of what must change for your site to behave like a DCS 900+ asset.
        </p>
        <div class="grid grid-3">
          <div class="card">
            <h3 class="card-title">Surface-Level Strong, Structurally Weak</h3>
            <p>"Your site is visually strong but missing the schema and internal linking required for AI and search systems to understand your services."</p>
          </div>
          <div class="card">
            <h3 class="card-title">Conversion Friction on Mobile</h3>
            <p>"Core Web Vitals are within acceptable ranges, but your lead capture flow introduces unnecessary friction on mobile."</p>
          </div>
          <div class="card">
            <h3 class="card-title">Analytics Blockers</h3>
            <p>"GTM is installed, but critical events are not being forwarded to GA4, preventing you from unlocking full measurement and optimization."</p>
          </div>
        </div>
      </div>
    </section>

    {/* RISK GRID */}
    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">How We Classify Findings</h2>
        <p class="section-intro">
          Every issue in your audit is tagged with business impact, DCS impact, and recommended
          action. This keeps the roadmap focused and executable instead of overwhelming.
        </p>
        <div class="risk-grid">
          <div class="risk-card risk-card--critical">
            <h3 class="card-title">Critical – Blocks DCS 900+</h3>
            <p class="card-note">Immediate attention required.</p>
            <ul class="feature-list">
              <li>Broken or missing analytics / key events.</li>
              <li>Structural issues that prevent key pages from being surfaced.</li>
              <li>Security, compliance, or governance gaps that impact data integrity and decision quality.</li>
            </ul>
          </div>
          <div class="risk-card risk-card--high">
            <h3 class="card-title">High – Material Performance Drag</h3>
            <p class="card-note">Schedule for near-term remediation.</p>
            <ul class="feature-list">
              <li>Weak internal linking or schema coverage on revenue-driving pages.</li>
              <li>Conversion friction on primary lead capture paths.</li>
              <li>Missing trust assets in high-intent decision flows.</li>
            </ul>
          </div>
          <div class="risk-card risk-card--medium">
            <h3 class="card-title">Medium – Optimization Opportunity</h3>
            <p class="card-note">Plan into your next iteration cycle.</p>
            <ul class="feature-list">
              <li>Non-blocking Core Web Vitals issues.</li>
              <li>Messaging gaps between ad promises and landing page content.</li>
              <li>Unclear secondary CTAs or off-ramp experiences.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    {/* TIMELINE */}
    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title">Timeline &amp; Next Steps</h2>
        <p class="section-intro">
          The DCS Audit is designed to move quickly enough for decision-making, while still meeting
          the documentation and governance standards your leadership expects.
        </p>
        <ul class="feature-list">
          <li><strong>Audit Duration.</strong> Completed within a defined timeframe after you complete the intake.</li>
          <li><strong>Format.</strong> Delivered as a structured PDF with a score breakdown and issue prioritization.</li>
          <li><strong>Ownership.</strong> You can execute internally, with your current agency, or with NexTara—our output is vendor-neutral.</li>
        </ul>
      </div>
    </section>

    {/* ABOUT NEXTARA */}
    <section class="section">
      <div class="container">
        <h2 class="section-title">Why NexTara Leads with Governance</h2>
        <p class="section-intro">
          NexTara AI Solutions operates from a governance-first mindset. We don&apos;t just look at
          how pages look—we measure how they perform against AI visibility, technical integrity,
          analytics, and compliance.
        </p>
        <p>
          The Digital Credibility Score Audit is built to support executive decision-making,
          compliance documentation, and future-proofing against changes in how search and AI systems
          evaluate your website.
        </p>
      </div>
    </section>

    {/* FAQ */}
    <section class="section">
      <div class="container">
        <h2 class="section-title">Digital Credibility Score Audit – FAQs</h2>
        <div class="faq-list">
          <article class="faq-item">
            <h3 class="faq-question">Is this just an SEO audit with a different label?</h3>
            <p class="faq-answer">No. A DCS Audit includes SEO and schema, but it also evaluates conversion, trust, analytics, and governance. The output is designed to support executive decisions about whether to optimize, rebuild, or re-platform your site.</p>
          </article>
          <article class="faq-item">
            <h3 class="faq-question">Can my current agency or developer use this audit?</h3>
            <p class="faq-answer">Yes. The audit is vendor-neutral. Many clients choose to execute the roadmap with their existing teams; others ask NexTara to own the rebuild. Either way, you keep the score, the findings, and the documentation.</p>
          </article>
          <article class="faq-item">
            <h3 class="faq-question">What if my score is already high?</h3>
            <p class="faq-answer">If your score is already in the DCS 880–920 range, the audit focuses on unlocking specific opportunities: AI visibility, conversion lift, and governance hardening. The goal is to move you from &quot;strong&quot; to &quot;enterprise-ready&quot; with a clear, prioritized set of changes.</p>
          </article>
          <article class="faq-item">
            <h3 class="faq-question">Will you try to sell me a full website rebuild?</h3>
            <p class="faq-answer">Only if the data justifies it. The DCS Audit is designed to answer a single question: &quot;Can this website realistically operate as a DCS 900+ asset?&quot; If the answer is yes, the roadmap will focus on optimization instead of rebuild.</p>
          </article>
        </div>
      </div>
    </section>

    {/* CTA + FORM */}
    <section class="section section-alt" id="audit-form">
      <div class="container grid grid-2">
        <div>
          <h2 class="section-title">Request Your Digital Credibility Score Audit</h2>
          <p class="section-intro">
            Complete the form and we&apos;ll confirm your audit, align on scope, and begin the DCS evaluation.
          </p>
          <ul class="feature-list">
            <li>Objective, vendor-neutral assessment.</li>
            <li>Actionable roadmap your team can execute.</li>
            <li>Designed for DCS 900+ websites only builds.</li>
          </ul>
        </div>
        <div>
          <form class="form audit-form" data-netlify="true" name="dcs-audit-request">
            <div class="form-field">
              <label for="name">Name</label>
              <input id="name" name="name" type="text" required autocomplete="name" />
            </div>
            <div class="form-field">
              <label for="email">Email</label>
              <input id="email" name="email" type="email" required autocomplete="email" />
            </div>
            <div class="form-field">
              <label for="company">Company / Organization</label>
              <input id="company" name="company" type="text" autocomplete="organization" />
            </div>
            <div class="form-field">
              <label for="website">Website URL</label>
              <input id="website" name="website" type="url" required placeholder="https://" />
            </div>
            <div class="form-field">
              <label for="role">Role</label>
              <select id="role" name="role">
                <option value="">Select your role</option>
                <option value="founder">Founder / Owner</option>
                <option value="cmo">CMO / Marketing Lead</option>
                <option value="ops">Operations / Practice Manager</option>
                <option value="other">Other</option>
              </select>
            </div>
            <div class="form-field">
              <label for="concern">Biggest current website concern</label>
              <textarea id="concern" name="concern" rows="4"></textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-block">Request My DCS Audit</button>
          </form>
        </div>
      </div>
    </section>
  </main>
</BaseLayout>
'''


def generate_schema(config: BuildConfig) -> dict:
    """Generate JSON-LD schema for the audit page."""
    base_url = f"{config.domain}/{config.page_slug}"
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": base_url,
                "url": base_url,
                "name": "Digital Credibility Score Audit | NexTara AI Solutions",
                "description": "Request a Digital Credibility Score Audit to understand whether your current website can realistically reach a DCS 900+ standard.",
                "isPartOf": {"@id": f"{config.domain}/#website"},
                "primaryImageOfPage": {
                    "@type": "ImageObject",
                    "@id": f"{config.domain}/#dcs-audit-hero-image"
                }
            },
            {
                "@type": "Service",
                "@id": f"{config.domain}/#dcs-audit-service",
                "name": "Digital Credibility Score Audit",
                "provider": {"@type": "Organization", "name": "NexTara AI Solutions"},
                "description": "A governance-grade diagnostic that evaluates your website across five pillars of the Digital Credibility Score framework.",
                "areaServed": {"@type": "AdministrativeArea", "name": "United States"}
            },
            {
                "@type": "FAQPage",
                "@id": f"{config.domain}/#dcs-audit-faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "Is this just an SEO audit with a different label?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "No. A DCS Audit includes SEO and schema, but it also evaluates conversion, trust, analytics, and governance."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Can my current agency or developer use this audit?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes. The audit is vendor-neutral. You keep the score, the findings, and the documentation."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "What if my score is already high?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "The audit focuses on unlocking specific opportunities: AI visibility, conversion lift, and governance hardening."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Will you try to sell me a full website rebuild?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Only if the data justifies it. The DCS Audit is designed to answer: Can this website realistically operate as a DCS 900+ asset?"
                        }
                    }
                ]
            }
        ]
    }


def generate_css() -> str:
    """Generate CSS styles for the audit page."""
    return '''/* ═══════════════════════════════════════════════════════════════════════════
   DCS Audit Landing Page Styles — NexTara AI Solutions
   Version: 1.0.0 | PromptCore v3.7 Aligned
   ═══════════════════════════════════════════════════════════════════════════ */

/* Audit Hero Variant */
.hero-section--audit {
  /* Inherits base hero styles */
}

/* Executive Summary Grid */
.audit-summary-grid {
  display: grid;
  gap: var(--space-md, 1.5rem);
}

@media (min-width: 768px) {
  .audit-summary-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

.audit-summary-card {
  border: 1px solid var(--border-subtle, #1f2933);
  border-radius: var(--radius-lg, 1rem);
  padding: var(--space-md, 1.5rem);
  background: var(--surface-elevated, #020617);
}

.audit-summary-card .card-label {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  opacity: 0.8;
  margin-bottom: var(--space-xs, 0.5rem);
}

.audit-summary-card .card-value {
  font-weight: 600;
  margin-bottom: var(--space-xs, 0.5rem);
}

.audit-summary-card .card-note {
  font-size: 0.9rem;
  opacity: 0.9;
}

/* Process Steps */
.steps-grid {
  display: grid;
  gap: var(--space-md, 1.5rem);
}

@media (min-width: 768px) {
  .steps-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

.step {
  border-radius: var(--radius-lg, 1rem);
  padding: var(--space-md, 1.5rem);
  border: 1px solid var(--border-subtle, #1f2933);
  background: var(--surface-elevated, #020617);
}

.step-number {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  margin-bottom: var(--space-sm, 0.75rem);
  border: 1px solid var(--accent, #3b82f6);
  color: var(--accent, #3b82f6);
}

.step-title {
  margin-bottom: var(--space-xs, 0.5rem);
}

/* Risk Classification Grid */
.risk-grid {
  display: grid;
  gap: var(--space-md, 1.5rem);
}

@media (min-width: 768px) {
  .risk-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.risk-card {
  border-radius: var(--radius-lg, 1rem);
  padding: var(--space-md, 1.5rem);
  border: 1px solid var(--border-subtle, #1f2933);
  background: var(--surface-elevated, #020617);
}

.risk-card--critical { border-color: var(--critical, #ef4444); }
.risk-card--high { border-color: var(--warn, #f59e0b); }
.risk-card--medium { border-color: var(--info, #38bdf8); }

.risk-card .card-note {
  font-size: 0.9rem;
  opacity: 0.9;
  margin-bottom: var(--space-sm, 0.75rem);
}

/* FAQ Accordion */
.faq-list {
  display: grid;
  gap: var(--space-sm, 1.25rem);
}

.faq-item {
  border-radius: var(--radius-lg, 1rem);
  padding: 1.25rem var(--space-md, 1.5rem);
  border: 1px solid var(--border-subtle, #1f2933);
  background: var(--surface-elevated, #020617);
}

.faq-question {
  margin-bottom: var(--space-xs, 0.5rem);
}

.faq-answer {
  font-size: 0.95rem;
  opacity: 0.95;
}

/* Audit Form */
.audit-form .form-field {
  margin-bottom: var(--space-sm, 1rem);
}

.audit-form .btn-block {
  width: 100%;
}

/* Focus states for accessibility */
.audit-form input:focus,
.audit-form select:focus,
.audit-form textarea:focus {
  outline: 2px solid var(--accent, #3b82f6);
  outline-offset: 2px;
}
'''


def generate_readme(config: BuildConfig) -> str:
    """Generate implementation README."""
    return f'''# Digital Credibility Score Audit — Implementation Package

**Version:** {config.version}
**PromptCore Alignment:** {config.promptcore_ver}
**Generated:** {datetime.now(timezone.utc).isoformat()}

## Contents

- `src/pages/digital-credibility-score-audit.astro` — Page component
- `styles/audit-styles.css` — Component styles
- `public/schema-audit.json` — JSON-LD structured data
- `docs/dcs-framework.md` — Framework documentation
- `build-manifest.json` — Reproducibility manifest with checksums

## Integration Steps

1. Copy `digital-credibility-score-audit.astro` to `src/pages/`
2. Import `audit-styles.css` in your global stylesheet
3. Inject `schema-audit.json` via build-time import or script tag
4. Update homepage CTAs to link to `/digital-credibility-score-audit`
5. Configure Netlify Forms for `dcs-audit-request` form name

## Verification

Run checksums against `build-manifest.json` to verify artifact integrity.

## Form Configuration

The form includes `data-netlify="true"` and `name="dcs-audit-request"` for
automatic Netlify Forms integration. Ensure Netlify Forms is enabled in your
site settings.
'''


# ═══════════════════════════════════════════════════════════════════════════════
# VALIDATION
# ═══════════════════════════════════════════════════════════════════════════════

class ValidationError(Exception):
    """Raised when content validation fails."""
    pass


def validate_astro(content: str, config: BuildConfig) -> dict:
    """Validate Astro content meets requirements."""
    results = {"passed": True, "checks": []}
    
    # Size check
    size = len(content.encode(config.encoding))
    if size < config.min_astro_size:
        results["passed"] = False
        results["checks"].append(f"FAIL: Size {size}B < {config.min_astro_size}B minimum")
    else:
        results["checks"].append(f"PASS: Size {size}B")
    
    # Required elements
    required = ["<main>", "</main>", "BaseLayout", "hero-section", "audit-form"]
    for elem in required:
        if elem in content:
            results["checks"].append(f"PASS: Contains '{elem}'")
        else:
            results["passed"] = False
            results["checks"].append(f"FAIL: Missing '{elem}'")
    
    # Accessibility checks
    if 'label for=' in content.lower() or 'label for="' in content:
        results["checks"].append("PASS: Form labels present")
    else:
        results["passed"] = False
        results["checks"].append("FAIL: Missing form labels")
    
    return results


def validate_schema(schema: dict, config: BuildConfig) -> dict:
    """Validate JSON-LD schema structure."""
    results = {"passed": True, "checks": []}
    
    # Check @context
    if schema.get("@context") == "https://schema.org":
        results["checks"].append("PASS: Valid @context")
    else:
        results["passed"] = False
        results["checks"].append("FAIL: Invalid @context")
    
    # Check required types
    graph = schema.get("@graph", [])
    found_types = {item.get("@type") for item in graph}
    
    for req_type in config.required_schema_types:
        if req_type in found_types:
            results["checks"].append(f"PASS: Contains {req_type}")
        else:
            results["passed"] = False
            results["checks"].append(f"FAIL: Missing {req_type}")
    
    return results


def validate_css(content: str, config: BuildConfig) -> dict:
    """Validate CSS content."""
    results = {"passed": True, "checks": []}
    
    size = len(content.encode(config.encoding))
    if size < config.min_css_size:
        results["passed"] = False
        results["checks"].append(f"FAIL: Size {size}B < {config.min_css_size}B minimum")
    else:
        results["checks"].append(f"PASS: Size {size}B")
    
    # Required selectors
    required = [".audit-summary-grid", ".risk-grid", ".faq-list", ".audit-form"]
    for sel in required:
        if sel in content:
            results["checks"].append(f"PASS: Contains '{sel}'")
        else:
            results["passed"] = False
            results["checks"].append(f"FAIL: Missing '{sel}'")
    
    return results


# ═══════════════════════════════════════════════════════════════════════════════
# BUILD FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def compute_checksum(content: str, encoding: str = "utf-8") -> str:
    """Compute SHA-256 checksum of content."""
    return hashlib.sha256(content.encode(encoding)).hexdigest()


def safe_write(path: Path, content: str, encoding: str, logger: logging.Logger) -> int:
    """Safely write content to file with error handling."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding=encoding)
        size = path.stat().st_size
        logger.info(f"Wrote {path.name} ({size:,} bytes)")
        return size
    except PermissionError as e:
        logger.error(f"Permission denied writing {path}: {e}")
        raise
    except OSError as e:
        logger.error(f"OS error writing {path}: {e}")
        raise


def create_backup(path: Path, logger: logging.Logger) -> Optional[Path]:
    """Create timestamped backup of existing directory."""
    if not path.exists():
        return None
    
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = path.parent / f"{path.name}_backup_{ts}"
    
    import shutil
    shutil.copytree(path, backup)
    logger.info(f"Created backup: {backup}")
    return backup


def build_package(
    output_dir: Path,
    config: BuildConfig,
    logger: logging.Logger,
    dry_run: bool = False
) -> BuildManifest:
    """Build the complete audit landing page package."""
    
    manifest = BuildManifest(
        version=config.version,
        promptcore_ver=config.promptcore_ver,
        generated_at=datetime.now(timezone.utc).isoformat(),
        hostname=os.environ.get("COMPUTERNAME", os.environ.get("HOSTNAME", "unknown"))
    )
    
    # Define paths
    src_pages = output_dir / "src" / "pages"
    styles = output_dir / "styles"
    public = output_dir / "public"
    docs = output_dir / "docs"
    
    # Generate content
    logger.info("Generating content...")
    astro_content = generate_astro_content(config)
    schema_content = generate_schema(config)
    css_content = generate_css()
    readme_content = generate_readme(config)
    
    # Validate before writing
    logger.info("Validating content...")
    
    astro_validation = validate_astro(astro_content, config)
    manifest.validation["astro"] = astro_validation
    for check in astro_validation["checks"]:
        logger.debug(f"  Astro: {check}")
    
    schema_validation = validate_schema(schema_content, config)
    manifest.validation["schema"] = schema_validation
    for check in schema_validation["checks"]:
        logger.debug(f"  Schema: {check}")
    
    css_validation = validate_css(css_content, config)
    manifest.validation["css"] = css_validation
    for check in css_validation["checks"]:
        logger.debug(f"  CSS: {check}")
    
    # Check for validation failures
    all_passed = all([
        astro_validation["passed"],
        schema_validation["passed"],
        css_validation["passed"]
    ])
    
    if not all_passed:
        logger.error("Validation failed — aborting build")
        raise ValidationError("Content validation failed")
    
    logger.info("All validations passed")
    
    if dry_run:
        logger.info("DRY RUN — skipping file writes")
        return manifest
    
    # Write files
    logger.info("Writing files...")
    
    astro_path = src_pages / f"{config.page_slug}.astro"
    safe_write(astro_path, astro_content, config.encoding, logger)
    manifest.artifacts["astro"] = str(astro_path)
    manifest.checksums["astro"] = compute_checksum(astro_content)
    
    schema_path = public / "schema-audit.json"
    schema_str = json.dumps(schema_content, indent=2, ensure_ascii=False)
    safe_write(schema_path, schema_str, config.encoding, logger)
    manifest.artifacts["schema"] = str(schema_path)
    manifest.checksums["schema"] = compute_checksum(schema_str)
    
    css_path = styles / "audit-styles.css"
    safe_write(css_path, css_content, config.encoding, logger)
    manifest.artifacts["css"] = str(css_path)
    manifest.checksums["css"] = compute_checksum(css_content)
    
    readme_path = docs / "readme.md"
    safe_write(readme_path, readme_content, config.encoding, logger)
    manifest.artifacts["readme"] = str(readme_path)
    manifest.checksums["readme"] = compute_checksum(readme_content)
    
    # Write manifest
    manifest_path = output_dir / "build-manifest.json"
    manifest_dict = {
        "version": manifest.version,
        "promptcore_ver": manifest.promptcore_ver,
        "generated_at": manifest.generated_at,
        "hostname": manifest.hostname,
        "artifacts": manifest.artifacts,
        "checksums": manifest.checksums,
        "validation": manifest.validation
    }
    manifest_str = json.dumps(manifest_dict, indent=2)
    safe_write(manifest_path, manifest_str, config.encoding, logger)
    
    return manifest


def create_zip(
    source_dir: Path,
    output_path: Path,
    config: BuildConfig,
    logger: logging.Logger
) -> Path:
    """Create distribution ZIP with all artifacts."""
    logger.info(f"Creating ZIP archive: {output_path}")
    
    with zipfile.ZipFile(output_path, "w", config.zip_compression) as zf:
        for root, _, files in os.walk(source_dir):
            for f in files:
                full_path = Path(root) / f
                arc_name = full_path.relative_to(source_dir.parent)
                zf.write(full_path, arcname=arc_name)
                logger.debug(f"  Added: {arc_name}")
    
    size = output_path.stat().st_size
    logger.info(f"ZIP created: {size:,} bytes")
    return output_path


# ═══════════════════════════════════════════════════════════════════════════════
# CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="NexTara DCS Audit Landing Page Builder",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path.cwd() / "audit-package",
        help="Output directory (default: ./audit-package)"
    )
    parser.add_argument(
        "--zip",
        action="store_true",
        help="Create distribution ZIP after build"
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Backup existing output directory before overwriting"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate without writing files"
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        help="Write detailed log to file"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Setup
    logger = setup_logging(args.log_file)
    if args.verbose:
        logger.handlers[0].setLevel(logging.DEBUG)
    
    config = BuildConfig()
    
    logger.info("=" * 60)
    logger.info(f"NexTara DCS Audit Builder {config.version}")
    logger.info(f"PromptCore Alignment: {config.promptcore_ver}")
    logger.info("=" * 60)
    
    try:
        # Backup if requested
        if args.backup:
            create_backup(args.output, logger)
        
        # Build
        manifest = build_package(args.output, config, logger, args.dry_run)
        
        # Create ZIP if requested
        if args.zip and not args.dry_run:
            zip_path = args.output.parent / f"{args.output.name}.zip"
            create_zip(args.output, zip_path, config, logger)
        
        # Summary
        logger.info("=" * 60)
        logger.info("BUILD COMPLETE")
        logger.info(f"  Output: {args.output}")
        logger.info(f"  Artifacts: {len(manifest.artifacts)}")
        logger.info("=" * 60)
        
        return 0
        
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        return 1
    except Exception as e:
        logger.error(f"Build failed: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())