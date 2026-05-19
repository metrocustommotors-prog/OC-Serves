#!/usr/bin/env python3
"""Generate substantive, SEO-distinct city pages for OC Serves."""
import os

# Each city has genuinely distinct content: courts, context, what makes
# service there specific. This is what keeps Google from treating them
# as doorway pages.
CITIES = [
    {
        "slug": "los-angeles-ca", "city": "Los Angeles", "state": "California",
        "abbr": "CA", "region": "Los Angeles County",
        "courts": "the Stanley Mosk Courthouse and the many branches of the Los Angeles Superior Court",
        "note": "Los Angeles is one of the busiest litigation venues in the country, and service here often means navigating gated communities, high-rise buildings with strict lobby security, and studio or corporate campuses.",
        "local": "Our servers know how to work LA's high-rise doorman buildings and the realities of serving across a county this large."
    },
    {
        "slug": "san-diego-ca", "city": "San Diego", "state": "California",
        "abbr": "CA", "region": "San Diego County",
        "courts": "the San Diego Superior Court and its Hall of Justice and family law divisions",
        "note": "San Diego matters frequently involve military-connected defendants, biotech corporations, and cross-border considerations near the international boundary.",
        "local": "We handle the particular challenges of San Diego service, from military installations to the region's many corporate campuses."
    },
    {
        "slug": "san-francisco-ca", "city": "San Francisco", "state": "California",
        "abbr": "CA", "region": "the Bay Area",
        "courts": "the San Francisco Superior Court at the Civic Center",
        "note": "San Francisco service often involves technology companies, dense downtown high-rises, and registered agents for corporations headquartered in the Bay Area.",
        "local": "Our Bay Area coverage handles tech-sector corporate service and the city's secure downtown towers."
    },
    {
        "slug": "sacramento-ca", "city": "Sacramento", "state": "California",
        "abbr": "CA", "region": "Sacramento County",
        "courts": "the Sacramento County Superior Court",
        "note": "As the state capital, Sacramento is a frequent venue for service on state agencies, registered agents, and corporations that maintain a presence near the seat of government.",
        "local": "Sacramento is a key registered-agent hub — many corporations designate agents in the capital, and we serve them regularly."
    },
    {
        "slug": "new-york-ny", "city": "New York", "state": "New York",
        "abbr": "NY", "region": "the New York metro area",
        "courts": "the New York County Supreme Court and the surrounding borough courts",
        "note": "New York service is demanding work — doorman buildings, corporate headquarters, financial-sector defendants, and some of the strictest service rules in the country.",
        "local": "Through NAPPS members in New York, we handle Manhattan high-rise service and corporate headquarters with the diligence the venue requires."
    },
    {
        "slug": "chicago-il", "city": "Chicago", "state": "Illinois",
        "abbr": "IL", "region": "Cook County",
        "courts": "the Circuit Court of Cook County, one of the largest unified court systems in the world",
        "note": "Cook County litigation moves at high volume, and service in Chicago spans the Loop's corporate towers and a wide spread of residential neighborhoods.",
        "local": "Our Illinois coverage manages Cook County's volume and the realities of serving across Chicago's neighborhoods and downtown towers."
    },
    {
        "slug": "houston-tx", "city": "Houston", "state": "Texas",
        "abbr": "TX", "region": "Harris County",
        "courts": "the Harris County District Courts",
        "note": "Houston matters frequently involve energy-sector corporations and registered agents, spread across one of the largest metropolitan footprints in the nation.",
        "local": "Texas service of process has its own rules, and our NAPPS members in Houston know them and the region's sprawling geography."
    },
    {
        "slug": "dallas-tx", "city": "Dallas", "state": "Texas",
        "abbr": "TX", "region": "Dallas County",
        "courts": "the Dallas County District Courts",
        "note": "The Dallas-Fort Worth metroplex is a major corporate base, and service here often means reaching registered agents and corporate offices across a wide region.",
        "local": "We coordinate service across the DFW metroplex, from corporate campuses to residential addresses."
    },
    {
        "slug": "austin-tx", "city": "Austin", "state": "Texas",
        "abbr": "TX", "region": "Travis County",
        "courts": "the Travis County District Courts",
        "note": "As the Texas state capital and a fast-growing technology hub, Austin sees frequent service on state entities, registered agents, and tech-sector corporations.",
        "local": "Austin combines state-capital service and a booming tech sector — our members cover both."
    },
    {
        "slug": "phoenix-az", "city": "Phoenix", "state": "Arizona",
        "abbr": "AZ", "region": "Maricopa County",
        "courts": "the Maricopa County Superior Court",
        "note": "Phoenix and the surrounding Valley make up a vast service area, with many gated and master-planned communities that require an experienced server.",
        "local": "Our Arizona coverage handles the Valley's sprawl and its many gated communities."
    },
    {
        "slug": "miami-fl", "city": "Miami", "state": "Florida",
        "abbr": "FL", "region": "Miami-Dade County",
        "courts": "the Eleventh Judicial Circuit Court of Florida in Miami-Dade County",
        "note": "Miami service often involves international parties, secure condominium towers, and corporate registered agents serving a large Latin American business community.",
        "local": "Miami's secure condo towers and international defendants call for an experienced server — our NAPPS members deliver."
    },
    {
        "slug": "orlando-fl", "city": "Orlando", "state": "Florida",
        "abbr": "FL", "region": "Orange County, Florida",
        "courts": "the Ninth Judicial Circuit Court of Florida",
        "note": "Central Florida litigation spans hospitality and tourism corporations, registered agents, and a wide residential spread across the region.",
        "local": "We coordinate Central Florida service from corporate offices to residential communities across the region."
    },
    {
        "slug": "atlanta-ga", "city": "Atlanta", "state": "Georgia",
        "abbr": "GA", "region": "Fulton County",
        "courts": "the Fulton County Superior and State Courts",
        "note": "Atlanta is a major corporate headquarters city, and service frequently targets registered agents and corporate offices across the metro area.",
        "local": "Our Georgia members handle Atlanta's corporate-headquarters service and the broad metro footprint."
    },
    {
        "slug": "seattle-wa", "city": "Seattle", "state": "Washington",
        "abbr": "WA", "region": "King County",
        "courts": "the King County Superior Court",
        "note": "Seattle service often involves technology corporations, secure downtown high-rises, and registered agents for companies headquartered in the Puget Sound region.",
        "local": "Our Washington coverage manages Seattle's tech-corporate service and secure downtown buildings."
    },
    {
        "slug": "denver-co", "city": "Denver", "state": "Colorado",
        "abbr": "CO", "region": "the Denver metro area",
        "courts": "the Denver District Court and the Second Judicial District",
        "note": "Denver matters span corporate offices downtown and residential service across a metro area that climbs into the foothills.",
        "local": "Our Colorado members cover the Denver metro from downtown towers to the foothill suburbs."
    },
    {
        "slug": "las-vegas-nv", "city": "Las Vegas", "state": "Nevada",
        "abbr": "NV", "region": "Clark County",
        "courts": "the Eighth Judicial District Court of Nevada in Clark County",
        "note": "Las Vegas is a major venue for corporate registered agents — Nevada's business-friendly incorporation laws mean many entities maintain agents here — alongside hospitality-sector service.",
        "local": "Nevada is a leading state for corporate registration, and our Las Vegas members serve registered agents constantly."
    },
    {
        "slug": "boston-ma", "city": "Boston", "state": "Massachusetts",
        "abbr": "MA", "region": "Suffolk County",
        "courts": "the Suffolk County Superior Court",
        "note": "Boston service often involves universities, healthcare and biotech corporations, and dense historic neighborhoods with limited access.",
        "local": "Our Massachusetts coverage handles Boston's institutional defendants and its dense, historic streets."
    },
    {
        "slug": "philadelphia-pa", "city": "Philadelphia", "state": "Pennsylvania",
        "abbr": "PA", "region": "Philadelphia County",
        "courts": "the Philadelphia Court of Common Pleas",
        "note": "Philadelphia litigation moves at high volume, with service spanning Center City corporate towers and a wide range of residential neighborhoods.",
        "local": "Our Pennsylvania members manage Philadelphia's court volume and its varied neighborhoods."
    },
    {
        "slug": "washington-dc", "city": "Washington", "state": "District of Columbia",
        "abbr": "DC", "region": "the District of Columbia",
        "courts": "the Superior Court of the District of Columbia",
        "note": "Service in the nation's capital frequently involves federal agencies, lobbying and trade organizations, and corporate registered agents.",
        "local": "Our DC members handle the capital's mix of institutional, corporate, and residential service."
    },
    {
        "slug": "portland-or", "city": "Portland", "state": "Oregon",
        "abbr": "OR", "region": "Multnomah County",
        "courts": "the Multnomah County Circuit Court",
        "note": "Portland service spans corporate offices, registered agents, and residential addresses across a compact but busy metro area.",
        "local": "Our Oregon coverage handles Portland service from downtown offices to surrounding neighborhoods."
    },
    {
        "slug": "minneapolis-mn", "city": "Minneapolis", "state": "Minnesota",
        "abbr": "MN", "region": "Hennepin County",
        "courts": "the Hennepin County District Court",
        "note": "Minneapolis is home to numerous corporate headquarters, and service often targets registered agents and corporate offices across the Twin Cities.",
        "local": "Our Minnesota members cover the Twin Cities, including the region's many corporate headquarters."
    },
    {
        "slug": "detroit-mi", "city": "Detroit", "state": "Michigan",
        "abbr": "MI", "region": "Wayne County",
        "courts": "the Third Circuit Court of Michigan in Wayne County",
        "note": "Detroit matters frequently involve automotive-sector corporations and registered agents across a broad metropolitan area.",
        "local": "Our Michigan coverage handles Detroit's corporate service and the wider Wayne County region."
    },
    {
        "slug": "charlotte-nc", "city": "Charlotte", "state": "North Carolina",
        "abbr": "NC", "region": "Mecklenburg County",
        "courts": "the Mecklenburg County courts within North Carolina's Twenty-Sixth Judicial District",
        "note": "Charlotte is a major banking and financial center, and service often targets corporate registered agents and financial-sector offices.",
        "local": "Our North Carolina members handle Charlotte's financial-sector corporate service."
    },
    {
        "slug": "nashville-tn", "city": "Nashville", "state": "Tennessee",
        "abbr": "TN", "region": "Davidson County",
        "courts": "the Davidson County courts",
        "note": "Nashville's fast growth means service spans healthcare and entertainment corporations, registered agents, and an expanding residential footprint.",
        "local": "Our Tennessee coverage manages Nashville's growing metro and its corporate base."
    },
    {
        "slug": "newark-nj", "city": "Newark", "state": "New Jersey",
        "abbr": "NJ", "region": "Essex County",
        "courts": "the Essex County Superior Court of New Jersey",
        "note": "Newark and the surrounding region see heavy commercial litigation, with frequent service on corporate registered agents and businesses.",
        "local": "Our New Jersey members handle Newark-area corporate and commercial service."
    },
]

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Process Server in {city}, {abbr} | Legal Document Service — OC Serves</title>
<meta name="description" content="Need a process server in {city}, {state}? OC Serves coordinates professional service of process in {city} for law firms nationwide through the NAPPS network. Court-ready affidavits.">
<meta name="keywords" content="process server {city}, process serving {city} {abbr}, serve legal documents {city}, {city} process server for law firms, subpoena service {city}">
<link rel="canonical" href="https://www.ocserves.com/cities/{slug}.html">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:title" content="Process Server in {city}, {abbr} — OC Serves">
<meta property="og:description" content="Professional process serving in {city}, {state}, coordinated for law firms through the NAPPS network.">
<meta property="og:url" content="https://www.ocserves.com/cities/{slug}.html">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="../css/style.css">
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Process Serving",
  "provider": {{
    "@type": "LegalService",
    "name": "OC Serves",
    "telephone": "+1-949-423-6915",
    "email": "docs@ocserves.com",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "3857 Birch St. Ste 174",
      "addressLocality": "Newport Beach",
      "addressRegion": "CA",
      "postalCode": "92660",
      "addressCountry": "US"
    }}
  }},
  "areaServed": {{
    "@type": "City",
    "name": "{city}",
    "containedInPlace": {{ "@type": "State", "name": "{state}" }}
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.ocserves.com/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Cities", "item": "https://www.ocserves.com/cities/index.html" }},
    {{ "@type": "ListItem", "position": 3, "name": "{city}, {abbr}", "item": "https://www.ocserves.com/cities/{slug}.html" }}
  ]
}}
</script>
</head>
<body>

<header class="site-header">
  <nav class="nav">
    <a href="../index.html" class="logo" aria-label="OC Serves home"><img src="../assets/logo.svg" alt="OC Serves — Process Serving"></a>
    <button class="nav-toggle" aria-label="Menu">☰</button>
    <ul class="nav-links">
      <li><a href="../services/process-serving.html">Services</a></li>
      <li><a href="../services/registered-agents.html">Registered Agents</a></li>
      <li><a href="../services/hoa.html">HOA Service</a></li>
      <li><a href="../services/nationwide.html">Nationwide</a></li>
      <li><a href="index.html">Cities</a></li>
      <li><a href="../about.html">About</a></li>
      <li><a href="../contact.html" class="btn btn-primary nav-cta">Request Service</a></li>
    </ul>
  </nav>
</header>

<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">{city}, {state}</span>
    <h1>Process server in<br><em>{city}, {abbr}</em></h1>
    <p class="lead">OC Serves coordinates professional service of process in {city} and throughout {region}. One point of contact, vetted local servers, and a court-ready affidavit returned to your firm.</p>
  </div>
</section>

<div class="wrap breadcrumb">
  <a href="../index.html">Home</a> / <a href="index.html">Cities</a> / <span>{city}, {abbr}</span>
</div>

<section>
  <div class="wrap">
    <div class="split">
      <div class="prose in-view">
        <h2>Service of process in {city}</h2>
        <p>OC Serves works with law firms and process serving companies that need documents served in {city}, {state}. {note}</p>
        <p>{local} Whether your matter is filed in {courts} or you simply need a defendant served at a {city} address, we place the assignment with a professional process server who knows the jurisdiction.</p>
        <p>For out-of-state firms, this is the advantage of working with OC Serves: you keep a single relationship and a single point of contact, and we handle the local coordination, the diligent attempts, and the affidavit.</p>
      </div>
      <div class="split-panel in-view">
        <h3>{city} service includes</h3>
        <ul>
          <li>Summons &amp; complaints</li>
          <li>Subpoenas &amp; deposition notices</li>
          <li>Writs, levies &amp; garnishments</li>
          <li>Corporate &amp; registered agent service</li>
          <li>Skip tracing for evasive subjects</li>
          <li>Court-ready affidavits of service</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--paper-warm);">
  <div class="wrap">
    <div class="section-head in-view">
      <span class="eyebrow">Why Firms Choose OC Serves for {city}</span>
      <h2>Out-of-state counsel, local results.</h2>
      <div class="divider"></div>
    </div>
    <div class="cards">
      <article class="card in-view">
        <span class="card-num">01</span>
        <h3>NAPPS-Vetted Servers</h3>
        <p>Service in {city} is handled by professional process servers connected through the NAPPS network — accountable and familiar with {state} rules.</p>
      </article>
      <article class="card in-view">
        <span class="card-num">02</span>
        <h3>One Point of Contact</h3>
        <p>Submit your {city} assignment to OC Serves and we manage it end to end. No need to vet a separate {state} vendor.</p>
      </article>
      <article class="card in-view">
        <span class="card-num">03</span>
        <h3>Court-Ready Returns</h3>
        <p>Your affidavit of service comes back formatted for the filing venue, with diligent attempts documented.</p>
      </article>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow">Documents for {city}?</span>
    <h2>Get your {city} service <em>started</em> today.</h2>
    <p class="lead">Send us the {city} address and your documents. We will confirm receipt and give you a realistic timeline the same business day.</p>
    <div class="cta-actions">
      <a href="../contact.html" class="btn btn-primary">Request Service in {city}</a>
      <a href="tel:+19494236915" class="btn btn-ghost">Call 949-423-6915</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="../index.html" class="logo" aria-label="OC Serves home"><img src="../assets/logo-white.svg" alt="OC Serves"></a>
        <p>Professional process serving for law firms — based in Orange County, serving nationwide through the NAPPS network.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="../services/process-serving.html">Process Serving</a></li>
          <li><a href="../services/registered-agents.html">Registered Agents</a></li>
          <li><a href="../services/hoa.html">HOA Service</a></li>
          <li><a href="../services/nationwide.html">Nationwide Service</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="../about.html">About OC Serves</a></li>
          <li><a href="index.html">Cities We Serve</a></li>
          <li><a href="../contact.html">Request Service</a></li>
        </ul>
      </div>
      <div class="footer-contact">
        <h4>Contact</h4>
        3857 Birch St. Ste 174<br>
        Newport Beach, CA 92660<br>
        <a href="tel:+19494236915">949-423-6915</a><br>
        <a href="mailto:docs@ocserves.com">docs@ocserves.com</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span class="js-year">2026</span> OC Serves. All rights reserved.</span>
      <span>Newport Beach, California · NAPPS Member</span>
    </div>
    <p class="disclaimer">OC Serves is a professional process serving company and is not a law firm. Nothing on this website constitutes legal advice. Service of process in {city}, {state} is coordinated through professional process servers and performed in accordance with applicable state and local rules.</p>
  </div>
</footer>

<script src="../js/main.js"></script>
</body>
</html>
"""

OUT = "/home/claude/ocserves/cities"
os.makedirs(OUT, exist_ok=True)

for c in CITIES:
    html = PAGE.format(**c)
    with open(os.path.join(OUT, c["slug"] + ".html"), "w") as f:
        f.write(html)
    print("wrote", c["slug"] + ".html")

print("\\nTotal city pages:", len(CITIES))
