import os
import re

def get_template(filename="index.html"):
    with open(filename, "r") as f:
        content = f.read()
    # Extract everything before <section class="hero"
    pre_main = content.split('  <section class="hero"')[0]
    # Extract everything after (and including) <footer class="footer">
    post_main = "  <footer" + content.split('  <footer')[1]
    return pre_main, post_main

def build_page(filename, main_content, active_link=""):
    pre_main, post_main = get_template("index.html")
    
    # Update active navigation state if provided
    if active_link:
        # Simple string replacement to remove active class from Home and add to target
        pre_main = pre_main.replace('class="navbar__link active"', 'class="navbar__link"')
        pre_main = pre_main.replace('class="mobile-menu__link active"', 'class="mobile-menu__link"')
        
        # Add active class to the specific link (simple regex)
        pre_main = re.sub(rf'href="{active_link}" class="navbar__link"', rf'href="{active_link}" class="navbar__link active"', pre_main)
        pre_main = re.sub(rf'href="{active_link}" class="mobile-menu__link"', rf'href="{active_link}" class="mobile-menu__link active"', pre_main)

    with open(filename, "w") as f:
        f.write(pre_main + main_content + post_main)

# ==========================================
# ABOUT PAGE
# ==========================================
about_content = """
  <section class="page-hero">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <h1 class="page-hero__title animate-fade-in-up">Our Legacy</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Two decades of crafting exceptional spaces and redefining luxury living.</p>
    </div>
  </section>

  <section class="section about-story">
    <div class="container">
      <div class="about-story__grid stagger-children">
        <div class="about-story__content">
          <h2 class="section-title reveal">A Vision for Timeless Architecture</h2>
          <p class="section-desc reveal">Shree Vasudha Projects was founded on a simple yet profound philosophy: to create spaces that transcend time. For over two decades, we have been at the forefront of luxury real estate development, delivering iconic structures that combine aesthetic brilliance with uncompromising quality.</p>
          <p class="section-desc reveal">Our commitment to excellence is reflected in every project we undertake. From visionary master-planning to the intricate detailing of interiors, we strive to exceed the expectations of our discerning clientele.</p>
        </div>
        <div class="about-story__image">
          <div class="image-placeholder">Company Story Image</div>
        </div>
      </div>
    </div>
  </section>

  <section class="section mission-vision">
    <div class="container">
      <div class="mission-vision__grid stagger-children">
        <div class="card mv-card hover-lift">
          <i data-lucide="target" class="mv-card__icon"></i>
          <h3 class="mv-card__title">Our Mission</h3>
          <p class="mv-card__desc">To deliver world-class real estate developments that enhance the quality of life for our customers, creating sustainable and vibrant communities.</p>
        </div>
        <div class="card mv-card hover-lift">
          <i data-lucide="eye" class="mv-card__icon"></i>
          <h3 class="mv-card__title">Our Vision</h3>
          <p class="mv-card__desc">To be the most trusted and respected luxury real estate brand, known for architectural innovation, transparent practices, and enduring value.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section chairman">
    <div class="container">
      <div class="chairman__grid stagger-children">
        <div class="chairman__image">
          <div class="image-placeholder">Chairman Portrait</div>
        </div>
        <div class="chairman__content">
          <h2 class="section-title reveal">Chairman's Message</h2>
          <blockquote class="chairman__quote">
            "We don't just build homes; we curate lifestyles. Our dedication to craftsmanship and integrity ensures that every Shree Vasudha project is a masterpiece of its own."
          </blockquote>
          <p class="chairman__name">Mr. Vasudha Rao</p>
          <p class="chairman__title">Founder & Chairman</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section stats-section">
    <div class="container">
      <div class="stats-grid stagger-children">
        <div class="stat-item hover-lift">
          <div class="stat-item__value">20+</div>
          <div class="stat-item__label">Years of Excellence</div>
        </div>
        <div class="stat-item hover-lift">
          <div class="stat-item__value">15+</div>
          <div class="stat-item__label">Iconic Projects</div>
        </div>
        <div class="stat-item hover-lift">
          <div class="stat-item__value">5000+</div>
          <div class="stat-item__label">Happy Families</div>
        </div>
        <div class="stat-item hover-lift">
          <div class="stat-item__value">10M+</div>
          <div class="stat-item__label">Sq.Ft. Developed</div>
        </div>
      </div>
    </div>
  </section>
"""

# ==========================================
# PROJECTS PAGE (All)
# ==========================================
projects_content = """
  <section class="page-hero">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <h1 class="page-hero__title animate-fade-in-up">Our Signature Developments</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Discover a curated portfolio of luxury residences and commercial spaces.</p>
    </div>
  </section>

  <section class="section projects-page">
    <div class="container">
      <div class="project-filter-tabs">
        <a href="projects.html" class="filter-tab active">All Projects</a>
        <a href="projects-ongoing.html" class="filter-tab">Ongoing</a>
        <a href="projects-upcoming.html" class="filter-tab">Upcoming</a>
        <a href="projects-completed.html" class="filter-tab">Completed</a>
      </div>

      <div class="project-grid">
        <!-- Project 1 -->
        <div class="project-card hover-lift">
          <div class="project-card__img-wrapper">
            <div class="image-placeholder">The Vasudha Reserve</div>
            <div class="project-card__badge">Ongoing</div>
          </div>
          <div class="project-card__content">
            <h3 class="project-card__title">The Vasudha Reserve</h3>
            <p class="project-card__location"><i data-lucide="map-pin"></i> Financial District, Hyderabad</p>
            <p class="project-card__desc">Ultra-luxury 4 & 5 BHK villas surrounded by 10 acres of pristine greenery.</p>
            <a href="#" class="btn btn--outline project-card__btn">View Details</a>
          </div>
        </div>
        <!-- Project 2 -->
        <div class="project-card hover-lift">
          <div class="project-card__img-wrapper">
            <div class="image-placeholder">Vasudha Altamount</div>
            <div class="project-card__badge">Upcoming</div>
          </div>
          <div class="project-card__content">
            <h3 class="project-card__title">Vasudha Altamount</h3>
            <p class="project-card__location"><i data-lucide="map-pin"></i> Jubilee Hills, Hyderabad</p>
            <p class="project-card__desc">Bespoke sky mansions featuring private plunge pools and panoramic city views.</p>
            <a href="#" class="btn btn--outline project-card__btn">View Details</a>
          </div>
        </div>
        <!-- Project 3 -->
        <div class="project-card hover-lift">
          <div class="project-card__img-wrapper">
            <div class="image-placeholder">Vasudha Serenity</div>
            <div class="project-card__badge badge--completed">Completed</div>
          </div>
          <div class="project-card__content">
            <h3 class="project-card__title">Vasudha Serenity</h3>
            <p class="project-card__location"><i data-lucide="map-pin"></i> Gachibowli, Hyderabad</p>
            <p class="project-card__desc">Premium 3 BHK apartments offering a perfect blend of comfort and elegance.</p>
            <a href="#" class="btn btn--outline project-card__btn">View Details</a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# ==========================================
# PROJECTS - ONGOING
# ==========================================
ongoing_content = """
  <section class="page-hero page-hero--ongoing">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <div class="badge-large">Ongoing Development</div>
      <h1 class="page-hero__title animate-fade-in-up">The Vasudha Reserve</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Experience the pinnacle of luxury living. Expected possession in Q4 2027.</p>
      <a href="contact.html" class="btn btn--primary btn--lg mt-6">Book a Site Visit</a>
    </div>
  </section>

  <section class="section progress-section">
    <div class="container">
      <h2 class="section-title text-center reveal">Construction Progress</h2>
      <div class="progress-container">
        <div class="progress-bar-wrap">
          <div class="progress-bar" style="width: 65%;"></div>
        </div>
        <div class="progress-labels">
          <span>Foundation (100%)</span>
          <span>Structure (80%)</span>
          <span>Interiors (20%)</span>
          <span>Handover</span>
        </div>
      </div>
    </div>
  </section>
  
  <section class="section gallery-section">
    <div class="container">
      <h2 class="section-title text-center reveal">Latest Site Updates</h2>
      <div class="gallery-grid">
        <div class="image-placeholder">Site Update 1</div>
        <div class="image-placeholder">Site Update 2</div>
        <div class="image-placeholder">Site Update 3</div>
      </div>
    </div>
  </section>
"""

# ==========================================
# PROJECTS - UPCOMING
# ==========================================
upcoming_content = """
  <section class="page-hero page-hero--upcoming">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <div class="badge-large badge--gold">Coming Soon</div>
      <h1 class="page-hero__title animate-fade-in-up">Vasudha Altamount</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Bespoke sky mansions in Jubilee Hills. Launching September 2026.</p>
    </div>
  </section>

  <section class="section teaser-section">
    <div class="container teaser-container">
      <h2 class="section-title text-center reveal">A New Era of Opulence</h2>
      <p class="section-desc text-center max-w-3xl reveal" style="margin:0 auto;">Prepare to witness architectural brilliance that sets a new benchmark in ultra-luxury real estate. Vasudha Altamount will offer unparalleled privacy, exclusivity, and panoramic views of the city skyline.</p>
      
      <div class="teaser-details">
        <div class="teaser-item">
          <i data-lucide="calendar"></i>
          <h4>Launch Date</h4>
          <p>September 2026</p>
        </div>
        <div class="teaser-item">
          <i data-lucide="key"></i>
          <h4>Possession</h4>
          <p>December 2029</p>
        </div>
      </div>
      
      <div class="text-center mt-12">
        <a href="contact.html" class="btn btn--primary btn--lg">Register Interest</a>
      </div>
    </div>
  </section>
"""

# ==========================================
# PROJECTS - COMPLETED
# ==========================================
completed_content = """
  <section class="page-hero page-hero--completed">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <h1 class="page-hero__title animate-fade-in-up">A Legacy Delivered</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Explore our completed masterpieces that stand as a testament to our commitment to excellence.</p>
    </div>
  </section>

  <section class="section completed-project">
    <div class="container">
      <div class="completed-grid">
        <div class="completed-content">
          <div class="badge-large badge--completed mb-4">Delivered 2024</div>
          <h2 class="section-title reveal">Vasudha Serenity</h2>
          <p class="section-desc reveal">Vasudha Serenity has set a new standard for premium apartment living in Gachibowli. Featuring state-of-the-art amenities and lush landscapes, it is now home to over 300 happy families.</p>
          
          <ul class="project-highlights">
            <li><i data-lucide="check-circle"></i> 100% Sold Out</li>
            <li><i data-lucide="check-circle"></i> IGBC Gold Certified</li>
            <li><i data-lucide="check-circle"></i> Awarded 'Best Premium Residential Project 2024'</li>
          </ul>
        </div>
        <div class="completed-gallery">
          <div class="image-placeholder">Serenity Exterior</div>
          <div class="image-placeholder">Serenity Clubhouse</div>
        </div>
      </div>
    </div>
  </section>
"""

# ==========================================
# SERVICES
# ==========================================
services_content = """
  <section class="page-hero">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <h1 class="page-hero__title animate-fade-in-up">Bespoke Services</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Comprehensive real estate solutions tailored to your unique requirements.</p>
    </div>
  </section>

  <section class="section services-page">
    <div class="container">
      <div class="services-grid stagger-children">
        <div class="service-card hover-lift">
          <i data-lucide="home" class="service-card__icon"></i>
          <h3 class="service-card__title">Residential Projects</h3>
          <p class="service-card__desc">From ultra-luxury villas to premium high-rise apartments, we build homes that offer unparalleled comfort and elegance.</p>
        </div>
        <div class="service-card hover-lift">
          <i data-lucide="building" class="service-card__icon"></i>
          <h3 class="service-card__title">Commercial Spaces</h3>
          <p class="service-card__desc">State-of-the-art office spaces and retail environments designed to foster innovation and business growth.</p>
        </div>
        <div class="service-card hover-lift">
          <i data-lucide="map" class="service-card__icon"></i>
          <h3 class="service-card__title">Open Plots</h3>
          <p class="service-card__desc">Strategically located premium plotted developments offering high ROI and the freedom to build your dream home.</p>
        </div>
        <div class="service-card hover-lift">
          <i data-lucide="briefcase" class="service-card__icon"></i>
          <h3 class="service-card__title">Investment Consulting</h3>
          <p class="service-card__desc">Expert guidance on real estate investments, portfolio management, and market analysis to maximize your returns.</p>
        </div>
        <div class="service-card hover-lift">
          <i data-lucide="key" class="service-card__icon"></i>
          <h3 class="service-card__title">Property Management</h3>
          <p class="service-card__desc">Comprehensive post-handover services ensuring your asset is perfectly maintained and continues to appreciate.</p>
        </div>
      </div>
    </div>
  </section>
"""

# ==========================================
# AMENITIES
# ==========================================
amenities_content = """
  <section class="page-hero">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <h1 class="page-hero__title animate-fade-in-up">World-Class Amenities</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Experience a lifestyle of unparalleled luxury, wellness, and recreation.</p>
    </div>
  </section>

  <section class="section amenities-showcase">
    <div class="container">
      
      <!-- Amenity 1 -->
      <div class="amenity-row">
        <div class="amenity-content">
          <h2 class="section-title reveal">The Grand Clubhouse</h2>
          <p class="section-desc reveal">Spanning over 50,000 sq.ft., our signature clubhouse is the epicenter of luxury living. It features a grand reception, private dining lounges, a state-of-the-art gymnasium, and a temperature-controlled indoor pool.</p>
        </div>
        <div class="amenity-image">
          <div class="image-placeholder">Clubhouse</div>
        </div>
      </div>
      
      <!-- Amenity 2 -->
      <div class="amenity-row reverse">
        <div class="amenity-content">
          <h2 class="section-title reveal">Landscaped Serenity</h2>
          <p class="section-desc reveal">Over 70% of our developments are dedicated to lush green open spaces. Designed by renowned landscape architects, our gardens offer jogging tracks, yoga pavilions, and peaceful water features.</p>
        </div>
        <div class="amenity-image">
          <div class="image-placeholder">Landscaped Gardens</div>
        </div>
      </div>
      
      <!-- Amenity Grid -->
      <h2 class="section-title text-center mt-12 mb-8 reveal">More Lifestyle Features</h2>
      <div class="amenity-grid-small">
        <div class="amenity-card-small"><i data-lucide="dumbbell"></i><span>Fitness Center</span></div>
        <div class="amenity-card-small"><i data-lucide="waves"></i><span>Infinity Pool</span></div>
        <div class="amenity-card-small"><i data-lucide="shield-check"></i><span>24x7 Security</span></div>
        <div class="amenity-card-small"><i data-lucide="zap"></i><span>100% Power Backup</span></div>
        <div class="amenity-card-small"><i data-lucide="gamepad-2"></i><span>Indoor Games</span></div>
        <div class="amenity-card-small"><i data-lucide="car"></i><span>EV Parking</span></div>
      </div>
      
    </div>
  </section>
"""

# ==========================================
# TESTIMONIALS
# ==========================================
testimonials_content = """
  <section class="page-hero">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <h1 class="page-hero__title animate-fade-in-up">Client Experiences</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Hear from the families and businesses who have chosen Shree Vasudha.</p>
    </div>
  </section>

  <section class="section testimonials-page">
    <div class="container">
      <div class="rating-banner">
        <div class="rating-score">
          <h2>4.9</h2>
          <div class="stars">
            <i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i>
          </div>
        </div>
        <p>Based on 500+ Google Reviews</p>
      </div>

      <div class="testimonial-grid mt-12">
        <!-- Testimonial 1 -->
        <div class="testimonial-card premium-card hover-lift">
          <i data-lucide="quote" class="quote-icon"></i>
          <p class="testimonial-card__text">"Purchasing a villa at The Vasudha Reserve has been the best decision for our family. The attention to detail, quality of construction, and the delivery timeline were all exceptional. It truly feels like living in a resort every single day."</p>
          <div class="testimonial-card__author">
            <div class="author-avatar">RK</div>
            <div>
              <h4>Rahul K.</h4>
              <span>Resident, The Vasudha Reserve</span>
            </div>
          </div>
        </div>
        <!-- Testimonial 2 -->
        <div class="testimonial-card premium-card hover-lift">
          <i data-lucide="quote" class="quote-icon"></i>
          <p class="testimonial-card__text">"As an NRI investor, trust and transparency are paramount. The team at Shree Vasudha Projects provided end-to-end support, and the appreciation on my property in Vasudha Serenity has been phenomenal. Highly recommended."</p>
          <div class="testimonial-card__author">
            <div class="author-avatar">AS</div>
            <div>
              <h4>Anita Sharma</h4>
              <span>Investor</span>
            </div>
          </div>
        </div>
        <!-- Testimonial 3 -->
        <div class="testimonial-card premium-card hover-lift">
          <i data-lucide="quote" class="quote-icon"></i>
          <p class="testimonial-card__text">"The design aesthetic and amenities are unmatched. From the grand clubhouse to the smart home features, every aspect of our new home reflects luxury. The handover process was incredibly smooth and professional."</p>
          <div class="testimonial-card__author">
            <div class="author-avatar">MV</div>
            <div>
              <h4>Mr & Mrs Verma</h4>
              <span>Resident, Vasudha Serenity</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# ==========================================
# CONTACT
# ==========================================
contact_content = """
  <section class="page-hero">
    <div class="page-hero__bg animate-slow-zoom"></div>
    <div class="page-hero__content">
      <h1 class="page-hero__title animate-fade-in-up">Get in Touch</h1>
      <p class="page-hero__subtitle animate-fade-in-up delay-200">Connect with our luxury real estate advisors today.</p>
    </div>
  </section>

  <section class="section contact-page">
    <div class="container">
      <div class="contact-grid stagger-children">
        
        <div class="contact-details">
          <h2 class="section-title reveal">Corporate Office</h2>
          <p class="section-desc mb-8 reveal" style="color: var(--color-text-secondary);">Visit our experience center to explore our ongoing projects in virtual reality and consult with our luxury property experts.</p>
          
          <div class="contact-info-list stagger-children" style="display:flex; flex-direction:column; gap:24px;">
            <div class="contact-info-item hover-lift" style="display:flex; gap:16px;">
              <i data-lucide="map-pin" style="color:var(--color-accent); flex-shrink:0; margin-top:4px;"></i>
              <div>
                <h4 style="font-family:var(--font-heading); font-size:18px; margin-bottom:4px;">Address</h4>
                <p style="color:var(--color-text-secondary); line-height:1.6;"><a href="https://maps.google.com?q=Shree%20vasudha%20projects,%20SKD%20Nagar,%20Self%20Finance%20Colony,%20B.N%20Reddy%20Nagar,%20Vanasthalipuram,%20Hyderabad,%20Telangana%20500070&ftid=0x3bcba1f73d3989bb:0xae71fd3b1c2998de&entry=gps&shh=CAE&lucs=,94297699,100820695,94231188,94280568,47071704,94218641,94282134,100813464,94286869,100813014&g_st=iw" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;">Plot - 285, 5th Floor<br>H.No. 5-6-190<br>Vaidhehi Nagar, Saheb Nagar Kalan<br>BN Reddy Nagar, R.R. Dist.<br>Telangana – 500070</a></p>
              </div>
            </div>
            
            <div class="contact-info-item hover-lift" style="display:flex; gap:16px;">
              <i data-lucide="phone" style="color:var(--color-accent); flex-shrink:0; margin-top:4px;"></i>
              <div>
                <h4 style="font-family:var(--font-heading); font-size:18px; margin-bottom:4px;">Phone</h4>
                <p style="color:var(--color-text-secondary); line-height:1.6;"><a href="tel:+917702436052" style="color: inherit; text-decoration: none;">+91 77024 36052</a></p>
              </div>
            </div>
            
            <div class="contact-info-item hover-lift" style="display:flex; gap:16px;">
              <i data-lucide="mail" style="color:var(--color-accent); flex-shrink:0; margin-top:4px;"></i>
              <div>
                <h4 style="font-family:var(--font-heading); font-size:18px; margin-bottom:4px;">Email</h4>
                <p style="color:var(--color-text-secondary); line-height:1.6;"><a href="mailto:shreevasudhaprojects@gmail.com" style="color: inherit; text-decoration: none;">shreevasudhaprojects@gmail.com</a></p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="contact-form-wrapper card" style="padding:40px;">
          <h3 class="mb-6" style="font-family: var(--font-heading); font-size: 24px; margin-bottom:24px;">Request a Callback</h3>
          <form class="form">
            <div class="form-group" style="margin-bottom:16px;">
              <input type="text" class="form-input" placeholder="Full Name" required style="width:100%; padding:16px; background:hsla(0,0%,100%,0.03); border:1px solid var(--color-border); border-radius:4px; color:#fff;">
            </div>
            <div class="form-group" style="margin-bottom:16px;">
              <input type="email" class="form-input" placeholder="Email Address" required style="width:100%; padding:16px; background:hsla(0,0%,100%,0.03); border:1px solid var(--color-border); border-radius:4px; color:#fff;">
            </div>
            <div class="form-group" style="margin-bottom:16px;">
              <input type="tel" class="form-input" placeholder="Phone Number" required style="width:100%; padding:16px; background:hsla(0,0%,100%,0.03); border:1px solid var(--color-border); border-radius:4px; color:#fff;">
            </div>
            <div class="form-group" style="margin-bottom:16px;">
              <select class="form-input" required style="width:100%; padding:16px; background:hsla(0,0%,100%,0.03); border:1px solid var(--color-border); border-radius:4px; color:var(--color-text-secondary);">
                <option value="">Interested Project</option>
                <option value="reserve">The Vasudha Reserve</option>
                <option value="altamount">Vasudha Altamount</option>
                <option value="other">Other Inquiry</option>
              </select>
            </div>
            <div class="form-group" style="margin-bottom:24px;">
              <textarea class="form-input" rows="4" placeholder="Your Message" style="width:100%; padding:16px; background:hsla(0,0%,100%,0.03); border:1px solid var(--color-border); border-radius:4px; color:#fff; resize:vertical;"></textarea>
            </div>
            <button type="submit" class="btn btn--primary" style="width:100%;">Submit Inquiry</button>
          </form>
        </div>
        
      </div>
    </div>
  </section>
"""

# Build all pages
print("Building HTML pages...")
build_page("about.html", about_content, "about.html")
build_page("projects.html", projects_content, "projects.html")
build_page("projects-ongoing.html", ongoing_content, "projects.html")
build_page("projects-upcoming.html", upcoming_content, "projects.html")
build_page("projects-completed.html", completed_content, "projects.html")
build_page("services.html", services_content, "services.html")
build_page("amenities.html", amenities_content, "amenities.html")
build_page("testimonials.html", testimonials_content, "testimonials.html")
build_page("contact.html", contact_content, "contact.html")
print("Build complete!")
