// main.js — ISUZU High-Tech Showroom 🚘
document.addEventListener("DOMContentLoaded", () => {
  console.log("🚀 ISUZU Showroom Initialized");

  /* ===== Parallax Background ===== */
  const showroom = document.querySelector(".showroom");
  if (showroom) {
    document.addEventListener("mousemove", (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 20;
      const y = (e.clientY / window.innerHeight - 0.5) * 20;
      showroom.style.backgroundPosition = `${50 - x}% ${50 - y}%`;
    });
  }

  /* ===== Vehicle Card Hover Glow ===== */
  const cards = document.querySelectorAll(".vehicle-card");
  cards.forEach(card => {
    const glow = document.createElement("div");
    glow.classList.add("glow");
    card.appendChild(glow);

    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      glow.style.left = `${x}px`;
      glow.style.top = `${y}px`;
    });

    card.addEventListener("mouseenter", () => {
      card.classList.add("active");
    });
    card.addEventListener("mouseleave", () => {
      card.classList.remove("active");
    });
  });

  /* ===== Smooth Page Entrance ===== */
  const fadeElements = document.querySelectorAll(".vehicle-card, .hero, .title");
  fadeElements.forEach((el, index) => {
    setTimeout(() => {
      el.classList.add("visible");
    }, 150 * index);
  });

  /* ===== Scroll-triggered Animations ===== */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll(".vehicle-card").forEach(card => {
    observer.observe(card);
  });
});
