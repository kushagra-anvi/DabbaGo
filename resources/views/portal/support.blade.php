@extends('layouts.customer')

@section('title', 'Support | DabbaGo')

@section('content')
<section class="min-h-screen bg-gray-50/50 pt-20 pb-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="mb-10 reveal">
            <h1 class="text-3xl md:text-5xl font-serif font-bold text-dabba-dark leading-tight">Help & <span class="text-dabba-maroon italic">Support</span></h1>
            <p class="mt-4 text-gray-500 font-medium">We're here to make sure your home-style meals reach you on time.</p>
        </div>

        <div class="grid lg:grid-cols-3 gap-10">
            <div class="lg:col-span-2 space-y-8">
                <!-- Support Options -->
                <div class="bg-white rounded-[2.5rem] p-10 border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal">
                    <h3 class="text-lg font-serif font-bold text-dabba-dark mb-8">How can we help?</h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <a href="https://wa.me/919876543210" target="_blank" class="flex items-center gap-6 p-6 rounded-3xl bg-green-50/50 border border-green-100 hover:bg-green-50 transition-all group">
                            <div class="w-14 h-14 bg-green-500 rounded-2xl flex items-center justify-center text-white shadow-lg shadow-green-500/20 group-hover:scale-110 transition-transform">
                                <i data-lucide="message-circle" class="w-7 h-7"></i>
                            </div>
                            <div>
                                <p class="text-sm font-bold text-gray-900 mb-1">WhatsApp Support</p>
                                <p class="text-xs text-gray-500">Instant chat with our team</p>
                            </div>
                        </a>

                        <div class="flex items-center gap-6 p-6 rounded-3xl bg-dabba-maroon/5 border border-dabba-maroon/10 hover:bg-dabba-maroon/10 transition-all group cursor-pointer">
                            <div class="w-14 h-14 bg-dabba-maroon rounded-2xl flex items-center justify-center text-white shadow-lg shadow-dabba-maroon/20 group-hover:scale-110 transition-transform">
                                <i data-lucide="ticket" class="w-7 h-7"></i>
                            </div>
                            <div>
                                <p class="text-sm font-bold text-gray-900 mb-1">Raise a Ticket</p>
                                <p class="text-xs text-gray-500">For complex inquiries</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- FAQ Placeholder -->
                <div class="bg-white rounded-[2.5rem] p-10 border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal">
                    <h3 class="text-lg font-serif font-bold text-dabba-dark mb-8">Frequently Asked Questions</h3>
                    <div class="space-y-6">
                        @foreach([
                            ['q' => 'How do I skip a tiffin?', 'a' => 'You can skip any tiffin from your Tiffin Details page at least 24 hours in advance.'],
                            ['q' => 'What if my tiffin is late?', 'a' => 'Our delivery partners strive for punctuality. If delayed, you will receive a notification in your portal.']
                        ] as $faq)
                        <div class="pb-6 border-b border-gray-100 last:border-0 last:pb-0">
                            <p class="text-sm font-bold text-dabba-dark mb-2">{{ $faq['q'] }}</p>
                            <p class="text-xs text-gray-500 leading-relaxed">{{ $faq['a'] }}</p>
                        </div>
                        @endforeach
                    </div>
                </div>
            </div>

            <div class="lg:col-span-1">
                <div class="bg-[#1a3c2a] rounded-[2.5rem] p-8 text-white relative overflow-hidden shadow-2xl sticky top-24">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                    <h3 class="text-xl font-serif font-bold mb-4 relative z-10">Emergency?</h3>
                    <p class="text-sm text-white/70 leading-relaxed mb-8 relative z-10">If you have an urgent delivery concern, please use our priority WhatsApp line for immediate assistance.</p>
                    <a href="https://wa.me/919876543210" target="_blank" class="flex items-center justify-center gap-3 w-full py-4 bg-[#f9dd8a] text-dabba-maroon rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-white hover:text-dabba-maroon transition-all shadow-xl shadow-[#f9dd8a]/20">
                        Priority Support
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
@endsection
