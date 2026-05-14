<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title', 'DabbaGo | Gourmet Indian Meals')</title>
    
    <meta name="description" content="Experience the best of traditional Indian flavors with a modern twist. DabbaGo delivers chef-crafted, nutritionist-approved meals fresh to your doorstep.">
    
    <link rel="icon" type="image/png" href="{{ asset('assets/images/logo.webp') }}">

    <!-- Vite -->
    @vite(['resources/css/app.css', 'resources/js/app.js'])
    
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <style>
        /* Nav Link Underline Effect */
        .nav-link {
            position: relative;
            padding: 4px 0;
        }

        .nav-link::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 0;
            height: 2px;
            background-color: #6f1e3b;
            transition: width 0.3s ease-out;
        }

        .nav-link:hover::after,
        .nav-link.active::after {
            width: 100%;
        }

        .nav-link.active {
            color: #6f1e3b;
        }

        /* Mobile Nav Link Styles */
        .mobile-nav-link-dropdown {
            color: #4A5568;
        }

        .mobile-nav-link-dropdown:hover {
            background-color: rgba(111, 30, 59, 0.03);
            color: #6f1e3b;
        }
    </style>
    @stack('styles')
</head>
<body class="bg-white text-dabba-dark selection:bg-dabba-maroon selection:text-white overflow-x-hidden">

    <!-- Header -->
    <nav class="fixed w-full z-50 bg-white/95 backdrop-blur-md border-b border-black/5" x-data="{ mobileMenuOpen: false }">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between relative z-50 bg-white">
            <div class="flex items-center flex-shrink-0">
                <a href="{{ url('/') }}" class="flex items-center gap-3">
                    <div class="h-12 w-12 overflow-hidden flex items-start justify-center">
                        <img src="{{ asset('assets/images/logo.webp') }}" alt="DabbaGo Icon" class="h-20 w-auto object-contain object-top max-w-none -mt-1">
                    </div>
                    <span class="text-2xl font-bold text-dabba-maroon tracking-tighter">DabbaGo</span>
                </a>
            </div>

            <div class="hidden lg:flex items-center justify-center gap-10 text-[15px] font-medium tracking-tight mx-4">
                <a href="{{ url('/') }}" class="nav-link hover:text-dabba-maroon transition-colors">Home</a>
                <a href="{{ url('/#how-it-works') }}" class="nav-link hover:text-dabba-maroon transition-colors">How It Works</a>
                <a href="{{ url('/#weekly-menu') }}" class="nav-link hover:text-dabba-maroon transition-colors">Menu</a>
                <a href="{{ url('/order') }}" class="nav-link hover:text-dabba-maroon transition-colors">Subscription</a>
                <a href="{{ url('/#testimonials') }}" class="nav-link hover:text-dabba-maroon transition-colors">Stories</a>
                <a href="{{ url('/#faq') }}" class="nav-link hover:text-dabba-maroon transition-colors">FAQ</a>
            </div>

            <div class="flex items-center gap-4 lg:gap-6 flex-shrink-0">
                @if(session('user_phone'))
                    <a href="{{ url('/dashboard') }}" class="hidden sm:inline-block text-[15px] font-medium hover:text-dabba-maroon transition-colors">Dashboard</a>
                @else
                    <a href="{{ url('/login') }}" class="hidden sm:inline-block text-[15px] font-medium hover:text-dabba-maroon transition-colors">Login</a>
                @endif
                <a href="{{ url('/order') }}" class="bg-dabba-maroon text-[#FFF9E5] py-2.5 px-7 rounded-full text-[15px] font-bold hover:scale-105 transition-transform duration-300 shadow-lg shadow-dabba-maroon/20">Start Dabba</a>
                
                <button @click="mobileMenuOpen = !mobileMenuOpen" class="lg:hidden w-10 h-10 flex flex-col justify-center gap-1.5 focus:outline-none z-50">
                    <span class="w-7 h-0.5 bg-dabba-maroon transition-all duration-300 transform" :class="mobileMenuOpen ? 'rotate-45 translate-y-2' : ''"></span>
                    <span class="w-7 h-0.5 bg-dabba-maroon transition-all duration-300" :class="mobileMenuOpen ? 'opacity-0' : ''"></span>
                    <span class="w-7 h-0.5 bg-dabba-maroon transition-all duration-300 transform" :class="mobileMenuOpen ? '-rotate-45 -translate-y-2' : ''"></span>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div id="mobile-menu"
            class="fixed top-20 left-0 w-full bg-white z-[40] border-b border-black/5 transition-all duration-500 overflow-y-auto max-h-[calc(100vh-80px)] shadow-xl"
            :class="mobileMenuOpen ? 'opacity-100 translate-y-0 pointer-events-auto' : 'opacity-0 -translate-y-4 pointer-events-none'"
            x-cloak>
            <div class="p-6 flex flex-col gap-1">
                <a href="{{ url('/') }}" @click="mobileMenuOpen = false" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">Home</a>
                <a href="{{ url('/#how-it-works') }}" @click="mobileMenuOpen = false" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">How It Works</a>
                <a href="{{ url('/#weekly-menu') }}" @click="mobileMenuOpen = false" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">Menu</a>
                <a href="{{ url('/order') }}" @click="mobileMenuOpen = false" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">Subscription</a>
                <a href="{{ url('/#testimonials') }}" @click="mobileMenuOpen = false" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">Stories</a>
                <a href="{{ url('/#faq') }}" @click="mobileMenuOpen = false" class="mobile-nav-link-dropdown px-6 py-3 rounded-xl text-[15px] font-semibold transition-all">FAQ</a>

                <div class="mt-4 pt-6 border-t border-black/5 flex flex-col gap-3">
                    <a href="{{ url('/order') }}" @click="mobileMenuOpen = false" class="w-full bg-dabba-maroon text-[#FFF9E5] py-3.5 rounded-full text-center text-[15px] font-bold shadow-lg">Order Now</a>
                    <a href="{{ url('/login') }}" @click="mobileMenuOpen = false" class="w-full border-2 border-dabba-maroon text-dabba-maroon py-3.5 rounded-full text-center text-[15px] font-bold">Login</a>
                </div>
            </div>
        </div>
    </nav>

    <main>
        @yield('content')
    </main>

    <footer class="relative bg-[#0A0A0A] pt-16 pb-12 text-white">
        <div class="max-w-7xl mx-auto px-6 relative z-10">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 lg:gap-16 mb-12">
                <div class="col-span-2 md:col-span-1">
                    <div class="flex items-center gap-4 mb-8">
                        <div class="w-14 h-14">
                            <img src="{{ asset('assets/images/logo.webp') }}" alt="DabbaGo" class="w-full h-full object-contain">
                        </div>
                        <span class="text-4xl font-serif font-bold text-dabba-maroon tracking-tight">DabbaGo</span>
                    </div>
                    <p class="text-sm text-gray-400 mb-8 italic max-w-xs leading-relaxed opacity-70">"Gourmet, nutritionist-approved home-style meals delivered fresh in sustainable, modern dabbas—elevating your daily lunch experience."</p>
                </div>
                <div>
                    <h4 class="text-[10px] font-bold text-white uppercase tracking-[0.3em] mb-8 opacity-80">Experience</h4>
                    <nav class="flex flex-col gap-3">
                        <a href="{{ url('/') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Home</a>
                        <a href="{{ url('/contact') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Contact</a>
                        <a href="{{ url('/corporate') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Corporate Inquiries</a>
                    </nav>
                </div>
                <div>
                    <h4 class="text-[10px] font-bold text-white uppercase tracking-[0.4em] mb-8 opacity-80">Assistance</h4>
                    <nav class="flex flex-col gap-3">
                        <a href="{{ url('/order-status') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Order Status</a>
                        <a href="{{ url('/refund-policy') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Refund Policies</a>
                    </nav>
                </div>
                <div>
                    <h4 class="text-[10px] font-bold text-white uppercase tracking-[0.4em] mb-8 opacity-80">Policies</h4>
                    <nav class="flex flex-col gap-3">
                        <a href="{{ url('/shipping-policy') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Shipping Policies</a>
                        <a href="{{ url('/privacy-policy') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Privacy Policies</a>
                        <a href="{{ url('/terms') }}" class="text-sm font-bold text-gray-500 hover:text-white transition-colors">Terms and Condition</a>
                    </nav>
                </div>
            </div>
            <div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
                <p class="text-sm text-gray-500">&copy; 2026 DabbaGo. | Powered By <a href="https://olatechdigital.com/" class="hover:text-dabba-maroon transition-colors" target="_blank" rel="noopener">Olatech Digital Solution</a></p>
                
                <!-- Direct SVG Social Media Links (Universally Visible & Fully Responsive) -->
                <div class="flex items-center gap-3">
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-gray-400 hover:bg-dabba-maroon hover:text-white hover:scale-110 hover:border-dabba-maroon/30 transition-all duration-300">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-gray-400 hover:bg-dabba-maroon hover:text-white hover:scale-110 hover:border-dabba-maroon/30 transition-all duration-300">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-gray-400 hover:bg-dabba-maroon hover:text-white hover:scale-110 hover:border-dabba-maroon/30 transition-all duration-300">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-gray-400 hover:bg-dabba-maroon hover:text-white hover:scale-110 hover:border-dabba-maroon/30 transition-all duration-300">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if (window.lucide) {
                window.lucide.createIcons();
            }
        });
    </script>
    @stack('scripts')
</body>
</html>
