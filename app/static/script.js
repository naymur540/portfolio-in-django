// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Navbar background change on scroll
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar")
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled")
  } else {
    navbar.classList.remove("scrolled")
  }
})



// Animate skill bars on scroll
function animateSkillBars() {
  const skillBars = document.querySelectorAll(".progress-bar")
  const skillsSection = document.getElementById("skills")

  if (skillsSection) {
    const sectionTop = skillsSection.offsetTop
    const sectionHeight = skillsSection.offsetHeight
    const windowHeight = window.innerHeight
    const scrollTop = window.pageYOffset

    if (scrollTop > sectionTop - windowHeight + 100) {
      skillBars.forEach((bar) => {
        const width = bar.style.width
        bar.style.width = "0%"
        setTimeout(() => {
          bar.style.width = width
        }, 100)
      })
    }
  }
}

// Animate elements on scroll
function animateOnScroll() {
  const elements = document.querySelectorAll(".timeline-item, .project-card, .education-item")

  elements.forEach((element) => {
    const elementTop = element.getBoundingClientRect().top
    const elementVisible = 150

    if (elementTop < window.innerHeight - elementVisible) {
      element.classList.add("fade-in")
    }
  })
}

// Typing effect for hero section
function typeWriter(element, text, speed = 100) {
  let i = 0
  element.innerHTML = ""

  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i)
      i++
      setTimeout(type, speed)
    }
  }

  type()
}

// Initialize typing effect
document.addEventListener("DOMContentLoaded", () => {
  const heroTitle = document.querySelector(".hero-section h1")
  if (heroTitle) {
    const originalText = heroTitle.textContent
    typeWriter(heroTitle, originalText, 100)
  }
})

// Scroll event listeners
window.addEventListener("scroll", () => {
  animateSkillBars()
  animateOnScroll()
  // Active navigation link highlighting
  const sections = document.querySelectorAll("section[id]")
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link")

  let current = ""

  sections.forEach((section) => {
    const sectionTop = section.offsetTop
    const sectionHeight = section.clientHeight

    if (window.pageYOffset >= sectionTop - 200) {
      current = section.getAttribute("id")
    }
  })

  navLinks.forEach((link) => {
    link.classList.remove("active")
    if (link.getAttribute("href") === "#" + current) {
      link.classList.add("active")
    }
  })
})

// Mobile menu close on link click
document.querySelectorAll(".navbar-nav .nav-link").forEach((link) => {
  link.addEventListener("click", () => {
    const navbarCollapse = document.querySelector(".navbar-collapse")
    const bootstrap = window.bootstrap // Declare the bootstrap variable
    if (navbarCollapse.classList.contains("show")) {
      const bsCollapse = new bootstrap.Collapse(navbarCollapse)
      bsCollapse.hide()
    }
  })
})

// Add loading animation to project images
document.querySelectorAll(".project-image img").forEach((img) => {
  img.addEventListener("load", function () {
    this.style.opacity = "1"
  })
})

// Initialize tooltips if Bootstrap tooltips are needed
document.addEventListener("DOMContentLoaded", () => {
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  const bootstrap = window.bootstrap // Declare the bootstrap variable
  const tooltipList = tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl))
})



  document.addEventListener('DOMContentLoaded', function() {
    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    var toastList = toastElList.map(function(toastEl) {
      return new bootstrap.Toast(toastEl, { delay: 3000 })  // auto-hide after 3 sec
    })
    toastList.forEach(toast => toast.show())
  });


