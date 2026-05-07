/**
 * DabbaGo Component Loader
 * Centrally manages the Header and Footer across all pages.
 */

const components = {
    getHeader(isRoot = false) {
        const prefix = isRoot ? 'pages/' : '';
        const homeLink = isRoot ? 'index.html' : '../index.html';
        const logoPath = isRoot ? 'assets/images/logo.webp' : '../assets/images/logo.webp';

        return `
        <nav class="fixed w-full z-50 glass-nav">
            <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
                <!-- Left: Logo & Brand Name -->
                <div class="flex items-center flex-shrink-0">
                    <a href="${homeLink}" class="flex items-center gap-3">
                        <div class="h-12 w-12 overflow-hidden flex items-start justify-center">
                            <img src="${logoPath}" alt="DabbaGo Icon"
                                class="h-20 w-auto object-contain object-top max-w-none -mt-1">
                        </div>
                        <span class="text-2xl font-bold text-dabba-maroon tracking-tighter">DabbaGo</span>
                    </a>
                </div>

                <!-- Center: Links (Hidden on Mobile) -->
                <div class="hidden lg:flex items-center justify-center gap-10 text-[15px] font-medium tracking-tight mx-4">
                    <a href="${homeLink}" class="nav-link hover:text-dabba-maroon transition-colors whitespace-nowrap">Home</a>
                    <a href="${homeLink}#how-it-works" class="nav-link hover:text-dabba-maroon transition-colors whitespace-nowrap">How It Works</a>
                    <a href="${homeLink}#weekly-menu" class="nav-link hover:text-dabba-maroon transition-colors whitespace-nowrap">Menu</a>
                    <a href="${prefix}order.html" class="nav-link hover:text-dabba-maroon transition-colors whitespace-nowrap">Subscription</a>
                    <a href="${homeLink}#faq" class="nav-link hover:text-dabba-maroon transition-colors whitespace-nowrap">FAQ</a>
                </div>

                <!-- Right: Action Buttons -->
                <div class="flex items-center gap-4 lg:gap-6 flex-shrink-0">
                    <a href="${prefix}login.html" class="hidden sm:inline-block text-[15px] font-medium hover:text-dabba-maroon transition-colors">Login</a>
                    <a href="${prefix}order.html"
                        class="bg-dabba-maroon text-white py-2.5 px-7 rounded-full text-[15px] font-bold hover:scale-105 transition-transform duration-300 shadow-lg shadow-dabba-maroon/20">Order
                        Now</a>
                    <!-- Hamburger Button -->
                    <button id="mobile-menu-btn"
                        class="lg:hidden w-10 h-10 flex flex-col justify-center gap-1.5 focus:outline-none z-50">
                        <span class="line-1 w-7 h-0.5 bg-dabba-maroon transition-all duration-300"></span>
                        <span class="line-2 w-7 h-0.5 bg-dabba-maroon transition-all duration-300"></span>
                        <span class="line-3 w-7 h-0.5 bg-dabba-maroon transition-all duration-300"></span>
                    </button>
                </div>
            </div>
        </nav>

        <!-- Mobile Menu Dropdown -->
        <div id="mobile-menu"
            class="fixed top-20 left-0 w-full bg-white z-[40] border-b border-black/5 opacity-0 -translate-y-4 pointer-events-none transition-all duration-500 overflow-y-auto max-h-[calc(100vh-80px)]">
            <div class="p-6 flex flex-col gap-1">
                <a href="${homeLink}" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">Home</a>
                <a href="${homeLink}#how-it-works" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">How It Works</a>
                <a href="${homeLink}#weekly-menu" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">Menu</a>
                <a href="${prefix}order.html" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">Subscription</a>
                <a href="${homeLink}#faq" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">FAQ</a>

                <div class="mt-4 pt-6 border-t border-black/5 flex flex-col gap-3">
                    <a href="${prefix}order.html" class="w-full bg-dabba-maroon text-white py-3.5 rounded-full text-center text-[15px] font-bold shadow-lg">Order Now</a>
                    <a href="${prefix}login.html" class="w-full border-2 border-dabba-maroon text-dabba-maroon py-3.5 rounded-full text-center text-[15px] font-bold">Login</a>
                </div>
            </div>
        </div>`;
    },

    getFooter(isRoot = false) {
        const prefix = isRoot ? 'pages/' : '';
        const homeLink = isRoot ? 'index.html' : '../index.html';
        const logoPath = isRoot ? 'assets/images/logo.webp' : '../assets/images/logo.webp';

        return `
        <footer class="relative bg-[#0A0A0A] pt-16 pb-12">
            <div class="max-w-7xl mx-auto px-6 relative z-10">
                <div class="grid grid-cols-2 md:grid-cols-4 gap-8 lg:gap-16 mb-12">
                    <div class="col-span-2 md:col-span-1 reveal">
                        <div class="flex items-center gap-4 mb-8">
                            <div class="w-14 h-14">
                                <img src="${logoPath}" alt="DabbaGo" class="w-full h-full object-contain">
                            </div>
                            <span class="text-4xl font-serif font-bold text-dabba-maroon tracking-tight">DabbaGo</span>
                        </div>
                        <p class="text-sm text-gray-400 mb-8 italic max-w-xs leading-relaxed opacity-70">"Our job is to filling your tummy with delicious food and with fast and free delivery."</p>
                    </div>
                    <div class="reveal">
                        <h4 class="text-[10px] font-bold text-white uppercase tracking-[0.3em] mb-8 opacity-80">Experience</h4>
                        <nav class="flex flex-col gap-3">
                            <a href="${homeLink}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Home</a>
                            <a href="${prefix}contact.html" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Contact</a>
                            <a href="${prefix}corporate.html" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Corporate Inquiries</a>
                        </nav>
                    </div>
                    <div class="reveal">
                        <h4 class="text-[10px] font-bold text-white uppercase tracking-[0.4em] mb-8 opacity-80">Assistance</h4>
                        <nav class="flex flex-col gap-3">
                            <a href="${prefix}order-status.html" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Order Status</a>
                            <a href="${prefix}refund-policy.html" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Refund Policies</a>
                        </nav>
                    </div>
                    <div class="reveal">
                        <h4 class="text-[10px] font-bold text-white uppercase tracking-[0.4em] mb-8 opacity-80">Policies</h4>
                        <nav class="flex flex-col gap-3">
                            <a href="${prefix}shipping-policy.html" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Shipping Policies</a>
                            <a href="${prefix}privacy-policy.html" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Privacy Policies</a>
                            <a href="${prefix}terms.html" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Terms and Condition</a>
                        </nav>
                    </div>
                </div>
                <div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
                    <p class="text-sm text-gray-500">&copy; 2026 DabbaGo. Crafted for Gourmet Living.</p>
                </div>
            </div>
        </footer>`;
    },

    init() {
        const headerPlaceholder = document.getElementById('header-placeholder');
        const footerPlaceholder = document.getElementById('footer-placeholder');
        
        // Detect if we are in the root or a subfolder
        const isRoot = !window.location.pathname.includes('/pages/');

        if (headerPlaceholder) {
            headerPlaceholder.innerHTML = this.getHeader(isRoot);
        }
        if (footerPlaceholder) {
            footerPlaceholder.innerHTML = this.getFooter(isRoot);
        }

        // Initialize Mobile Menu Logic
        this.setupMobileMenu();

        // Refresh Reveal animations for newly injected components
        if (window.refreshReveal) {
            window.refreshReveal();
        }

        // Re-initialize Lucide icons if available
        if (window.lucide) {
            window.lucide.createIcons();
        }
    },

    setupMobileMenu() {
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        
        if (btn && menu) {
            btn.addEventListener('click', () => {
                menu.classList.toggle('opacity-0');
                menu.classList.toggle('-translate-y-4');
                menu.classList.toggle('pointer-events-none');
                
                // Animate hamburger lines
                const lines = btn.querySelectorAll('span');
                lines[0].classList.toggle('rotate-45');
                lines[0].classList.toggle('translate-y-2');
                lines[1].classList.toggle('opacity-0');
                lines[2].classList.toggle('-rotate-45');
                lines[2].classList.toggle('-translate-y-2');
            });

            // Close menu on link click
            menu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    menu.classList.add('opacity-0', '-translate-y-4', 'pointer-events-none');
                    const lines = btn.querySelectorAll('span');
                    lines[0].classList.remove('rotate-45', 'translate-y-2');
                    lines[1].classList.remove('opacity-0');
                    lines[2].classList.remove('-rotate-45', '-translate-y-2');
                });
            });
        }
    }
};

document.addEventListener('DOMContentLoaded', () => components.init());
