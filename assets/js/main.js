document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Animation
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    window.revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                window.revealObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    window.refreshReveal = () => {
        document.querySelectorAll('.reveal').forEach(el => window.revealObserver.observe(el));
    };

    window.refreshReveal();

    // Sticky Nav Blur Effect
    const nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                nav.classList.add('shadow-md');
            } else {
                nav.classList.remove('shadow-md');
            }
        });
    }

    // Weekly Menu Toggle Logic
    const vegBtn = document.getElementById('veg-toggle');
    const nonvegBtn = document.getElementById('nonveg-toggle');
    const mealTexts = document.querySelectorAll('.meal-text');
    const mealImages = document.querySelectorAll('.meal-image');

    function updateMenu(type) {
        if (!vegBtn || !nonvegBtn) return;

        if (type === 'veg') {
            vegBtn.classList.add('bg-dabba-maroon', 'text-white', 'shadow-lg');
            vegBtn.classList.remove('text-gray-400', 'bg-white', 'text-dabba-maroon', 'shadow-sm');
            nonvegBtn.classList.remove('bg-dabba-maroon', 'text-white', 'shadow-lg', 'bg-white', 'text-dabba-maroon', 'shadow-sm');
            nonvegBtn.classList.add('text-gray-400');
        } else {
            nonvegBtn.classList.add('bg-dabba-maroon', 'text-white', 'shadow-lg');
            nonvegBtn.classList.remove('text-gray-400', 'bg-white', 'text-dabba-maroon', 'shadow-sm');
            vegBtn.classList.remove('bg-dabba-maroon', 'text-white', 'shadow-lg', 'bg-white', 'text-dabba-maroon', 'shadow-sm');
            vegBtn.classList.add('text-gray-400');
        }

        mealTexts.forEach(meal => {
            meal.style.opacity = ''; 
            meal.classList.add('switching');
            setTimeout(() => {
                meal.textContent = meal.getAttribute(`data-${type}`);
                meal.classList.remove('switching');
            }, 400);
        });

        mealImages.forEach(img => {
            img.style.opacity = ''; 
            img.classList.add('switching');
            setTimeout(() => {
                if (img.hasAttribute(`data-${type}`)) {
                    img.src = img.getAttribute(`data-${type}`);
                }
                img.classList.remove('switching');
            }, 400);
        });
    }

    if (vegBtn) vegBtn.addEventListener('click', () => updateMenu('veg'));
    if (nonvegBtn) nonvegBtn.addEventListener('click', () => updateMenu('nonveg'));

    // Reusable drag-to-scroll for any horizontal carousel
    function initDragScroll(el) {
        if (!el) return;
        let isDown = false, startX, scrollLeft;

        el.querySelectorAll('img').forEach(img => img.draggable = false);

        el.addEventListener('mousedown', (e) => {
            isDown = true;
            el.style.scrollBehavior = 'auto';
            el.style.scrollSnapType = 'none';
            el.style.userSelect = 'none';
            startX = e.pageX - el.offsetLeft;
            scrollLeft = el.scrollLeft;
        });

        el.addEventListener('mouseleave', () => {
            if (!isDown) return;
            isDown = false;
            el.style.scrollBehavior = 'smooth';
            el.style.scrollSnapType = '';
            el.style.userSelect = '';
        });

        el.addEventListener('mouseup', () => {
            isDown = false;
            el.style.scrollBehavior = 'smooth';
            el.style.scrollSnapType = '';
            el.style.userSelect = '';
        });

        el.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - el.offsetLeft;
            const walk = (x - startX) * 2;
            el.scrollLeft = scrollLeft - walk;
        });
    }

    // Apply drag-to-scroll on carousels
    initDragScroll(document.getElementById('menu-container'));
    initDragScroll(document.getElementById('process-container'));

    // Arrow Navigation for menu carousel
    const menuSlider = document.getElementById('menu-container');
    if (menuSlider) {
        const scrollLeftBtn = document.getElementById('scroll-left');
        const scrollRightBtn = document.getElementById('scroll-right');
        
        if (scrollLeftBtn && scrollRightBtn) {
            scrollLeftBtn.addEventListener('click', () => {
                menuSlider.scrollBy({ left: -400, behavior: 'smooth' });
            });
            scrollRightBtn.addEventListener('click', () => {
                menuSlider.scrollBy({ left: 400, behavior: 'smooth' });
            });
        }

        // Mobile scroll dot indicators
        const dots = document.querySelectorAll('#menu-dots .menu-dot');
        if (dots.length) {
            menuSlider.addEventListener('scroll', () => {
                const cards = menuSlider.querySelectorAll('.menu-day');
                const scrollPos = menuSlider.scrollLeft + menuSlider.offsetWidth / 2;
                let activeIndex = 0;
                cards.forEach((card, i) => {
                    if (card.offsetLeft <= scrollPos) activeIndex = i;
                });
                dots.forEach((dot, i) => {
                    if (i === activeIndex) {
                        dot.classList.remove('bg-dabba-maroon/20');
                        dot.classList.add('bg-dabba-maroon', 'w-4');
                    } else {
                        dot.classList.remove('bg-dabba-maroon', 'w-4');
                        dot.classList.add('bg-dabba-maroon/20');
                    }
                });
            });
        }
    }

    // Highlight Current Day
    const today = new Date().getDay(); 
    const dayCards = document.querySelectorAll('.menu-day');
    dayCards.forEach(card => {
        if (parseInt(card.getAttribute('data-day')) === today) {
            card.classList.add('ring-2', 'ring-dabba-maroon', 'bg-dabba-maroon/5', 'scale-105', 'z-10');
            const dayLabel = card.querySelector('p:first-child');
            if (dayLabel) dayLabel.innerHTML += ' <span class="ml-2 bg-dabba-maroon text-white px-2 py-0.5 rounded-full text-[8px]">TODAY</span>';
        }
    });

    // FAQ Accordion Logic
    document.querySelectorAll('.faq-button').forEach(button => {
        button.addEventListener('click', () => {
            const content = button.nextElementSibling;
            const icon = button.querySelector('span:last-child');
            if (!content || !icon) return;
            
            const isOpen = content.classList.contains('open');

            document.querySelectorAll('.faq-content').forEach(otherContent => {
                if (otherContent !== content) {
                    otherContent.classList.remove('open');
                    otherContent.style.maxHeight = '0px';
                    const otherIcon = otherContent.previousElementSibling.querySelector('span:last-child');
                    if (otherIcon) otherIcon.textContent = '+';
                }
            });

            if (!isOpen) {
                content.classList.add('open');
                content.style.maxHeight = content.scrollHeight + 'px';
                icon.textContent = '−';
            } else {
                content.classList.remove('open');
                content.style.maxHeight = '0px';
                icon.textContent = '+';
            }
        });
    });

    // Dynamic "Today's Pick" in Hero
    const heroPickTitle = document.querySelector('.hero-pick-title');
    if (heroPickTitle) {
        const currentDayCard = document.querySelector(`.menu-day[data-day="${today}"]`);
        if (currentDayCard && today !== 0) {
            const mealEl = currentDayCard.querySelector('.meal-text');
            if (mealEl) {
                const lunchText = mealEl.getAttribute('data-veg');
                heroPickTitle.textContent = lunchText;
            }
        } else if (today === 0) {
            heroPickTitle.textContent = "Chef's Special Sunday Break";
        }
    }

    // Scroll to Top Logic
    const scrollTopBtn = document.getElementById('scroll-top');
    if (scrollTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                scrollTopBtn.classList.remove('translate-y-32', 'opacity-0', 'pointer-events-none');
                scrollTopBtn.classList.add('translate-y-0', 'opacity-100');
            } else {
                scrollTopBtn.classList.add('translate-y-32', 'opacity-0', 'pointer-events-none');
                scrollTopBtn.classList.remove('translate-y-0', 'opacity-100');
            }
        });

        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Scroll-Spy Logic
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    if (sections.length && navLinks.length) {
        const scrollObserverOptions = {
            threshold: 0.5,
            rootMargin: "-80px 0px 0px 0px"
        };

        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (id === 'home' && link.getAttribute('href') === '#') {
                            link.classList.add('active');
                        }
                        if (link.getAttribute('href') === `#${id}`) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }, scrollObserverOptions);

        sections.forEach(section => scrollObserver.observe(section));

        const firstSection = document.querySelector('section:first-of-type');
        if (firstSection && !firstSection.id) {
            firstSection.setAttribute('id', 'home');
            scrollObserver.observe(firstSection);
        }
    }

    // Mobile Menu Toggle Logic
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    let isMenuOpen = false;

    function toggleMenu() {
        if (!mobileMenu || !mobileMenuBtn) return;
        isMenuOpen = !isMenuOpen;
        if (isMenuOpen) {
            mobileMenu.classList.remove('pointer-events-none', 'opacity-0', '-translate-y-4');
            mobileMenuBtn.classList.add('active');
            const l1 = mobileMenuBtn.querySelector('.line-1');
            const l2 = mobileMenuBtn.querySelector('.line-2');
            const l3 = mobileMenuBtn.querySelector('.line-3');
            if (l1) l1.style.transform = 'translateY(8px) rotate(45deg)';
            if (l2) l2.style.opacity = '0';
            if (l3) l3.style.transform = 'translateY(-8px) rotate(-45deg)';
            document.body.style.overflow = 'hidden';
        } else {
            mobileMenu.classList.add('pointer-events-none', 'opacity-0', '-translate-y-4');
            mobileMenuBtn.classList.remove('active');
            const l1 = mobileMenuBtn.querySelector('.line-1');
            const l2 = mobileMenuBtn.querySelector('.line-2');
            const l3 = mobileMenuBtn.querySelector('.line-3');
            if (l1) l1.style.transform = 'none';
            if (l2) l2.style.opacity = '1';
            if (l3) l3.style.transform = 'none';
            document.body.style.overflow = '';
        }
    }

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', toggleMenu);

    // Robust Smooth Scroll for Internal Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            
            // Only handle internal home-page anchors
            if (href.startsWith('#') || href.includes('index.html#')) {
                const targetId = href.split('#')[1];
                
                if (!targetId || targetId === '') {
                    // Just '#' - scroll to top
                    e.preventDefault();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                    return;
                }

                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    e.preventDefault();
                    const headerOffset = 100;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                    
                    if (isMenuOpen) toggleMenu();
                }
            }
        });
    });
});