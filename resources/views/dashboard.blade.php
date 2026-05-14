@extends('layouts.customer')

@section('title', 'Dashboard | DabbaGo')

@section('content')
<section class="min-h-screen bg-gray-50/50 pt-20 pb-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        
        <!-- HNH Style Dark Banner -->
        <div class="bg-gradient-to-br from-dabba-dark via-dabba-dark to-dabba-maroon/80 rounded-[3rem] p-8 md:p-12 text-white relative overflow-hidden shadow-2xl reveal">
            <div class="absolute top-0 right-0 w-96 h-96 bg-white/5 rounded-full blur-3xl -mr-48 -mt-48"></div>
            <div class="relative z-10 flex flex-col lg:flex-row lg:items-end lg:justify-between gap-10">
                <div class="max-w-2xl">
                    <p class="text-[10px] font-bold uppercase tracking-[0.4em] text-[#f9dd8a] mb-4">Customer Dashboard</p>
                    <h1 class="text-3xl md:text-5xl font-serif font-bold leading-tight mb-6">
                        Good {{ now()->hour < 12 ? 'morning' : (now()->hour < 17 ? 'afternoon' : 'evening') }}, <br>
                        <span class="italic text-[#f9dd8a]">{{ Str::before($userData['name'] ?? 'Customer', ' ') }}</span>
                    </h1>
                    
                    @if($userData)
                        <div class="flex flex-wrap items-center gap-6 text-sm font-medium text-white/70 mb-8">
                            <div class="flex items-center gap-2">
                                <i data-lucide="calendar" class="w-4 h-4 text-[#f9dd8a]"></i>
                                <span>Journey: Day {{ $userData['journey_days'] ?? 0 }}</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i data-lucide="award" class="w-4 h-4 text-[#f9dd8a]"></i>
                                <span>Status: {{ $userData['loyalty_tier'] ?? 'Member' }}</span>
                            </div>
                        </div>
                    @endif

                    <div class="flex flex-wrap gap-4">
                        <a href="{{ route('profile') }}" class="px-8 py-4 bg-[#f9dd8a] text-dabba-maroon rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-white hover:text-dabba-maroon transition-all shadow-xl shadow-[#f9dd8a]/20">
                            Manage Profile
                        </a>
                        <a href="{{ route('menu') }}" class="px-8 py-4 bg-white/10 backdrop-blur text-white border border-white/20 rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-white/20 transition-all">
                            Today's Menu
                        </a>
                    </div>
                </div>

                @if($userData['loyalty_tier'] ?? null)
                    <div class="min-w-[240px] rounded-[2.5rem] border border-white/10 bg-white/10 p-8 backdrop-blur shadow-xl">
                        <p class="text-[9px] font-bold uppercase tracking-[0.3em] text-[#f9dd8a] mb-2">Loyalty Tier</p>
                        <p class="text-3xl font-serif font-bold text-white mb-2">{{ $userData['loyalty_tier'] }}</p>
                        <p class="text-[10px] text-white/50 font-medium">Free Upgrades · Priority Support</p>
                    </div>
                @endif
            </div>
        </div>

        @if(empty($subscriptions))
            <div class="bg-white rounded-[3rem] p-20 border border-dashed border-dabba-maroon/20 text-center reveal">
                <div class="w-20 h-20 bg-dabba-maroon/5 rounded-full flex items-center justify-center mx-auto mb-8">
                    <i data-lucide="clipboard-list" class="w-10 h-10 text-dabba-maroon/40"></i>
                </div>
                <h3 class="text-2xl font-serif font-bold text-dabba-dark mb-4">No subscription yet</h3>
                <p class="text-gray-500 font-medium mb-10 max-w-md mx-auto">Choose your meals, confirm your delivery zone, and start your DabbaGo journey in one place.</p>
                <a href="{{ url('/order') }}" class="inline-flex items-center gap-3 px-10 py-5 bg-dabba-maroon text-white rounded-full font-bold text-[10px] uppercase tracking-widest hover:scale-105 transition-all shadow-2xl shadow-dabba-maroon/20">
                    Start Subscription <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
            </div>
        @else
            <div class="grid gap-8 xl:grid-cols-[1.15fr_0.85fr]">
                <div class="space-y-8">
                    @foreach($subscriptions as $sub)
                        <div class="bg-white rounded-[3rem] p-10 border border-dabba-maroon/5 shadow-2xl shadow-dabba-maroon/5 reveal">
                            <div class="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-8 mb-10">
                                <div>
                                    <div class="flex flex-wrap items-center gap-3 mb-4">
                                        <span class="px-3 py-1 rounded-full bg-green-50 text-green-600 text-[9px] font-bold uppercase tracking-widest border border-green-100">
                                            {{ Str::headline($sub['status']) }}
                                        </span>
                                        <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Homestyle Plan</p>
                                    </div>
                                    <h2 class="text-3xl font-serif font-bold text-dabba-dark mb-2">
                                        {{ is_array($sub['meal_slots']) ? implode(' & ', array_map('ucfirst', $sub['meal_slots'])) : ucfirst($sub['meal_slots'] ?? 'Lunch') }}
                                    </h2>
                                    <p class="text-sm text-gray-500 font-medium">
                                        {{ $sub['plan_name'] }} · {{ ucfirst($sub['diet_type'] ?? 'Standard') }}
                                    </p>
                                </div>
                                
                                <div class="min-w-[240px] rounded-[2.5rem] border border-dabba-maroon/5 bg-dabba-beige/20 p-6">
                                    <p class="text-[9px] font-bold text-gray-400 uppercase tracking-widest mb-1">Next Billing</p>
                                    <p class="text-2xl font-serif font-bold text-dabba-dark">Rs. {{ number_format($sub['next_billing_amount'] ?? 0, 2) }}</p>
                                    <p class="text-[10px] text-gray-500 font-medium mt-1">{{ $sub['next_billing_date'] ?? 'Upcoming' }}</p>
                                </div>
                            </div>

                            @php
                                $progressPercent = ($sub['total_meals'] ?? 0) > 0 
                                    ? (int) round(((($sub['total_meals'] ?? 0) - ($sub['meals_remaining'] ?? 0)) / ($sub['total_meals'] ?? 1)) * 100) 
                                    : 0;
                            @endphp

                            <div class="mb-10">
                                <div class="flex items-center justify-between text-[10px] font-bold uppercase tracking-widest mb-3">
                                    <span class="text-dabba-dark">Dabba Cycle Progress</span>
                                    <span class="text-dabba-maroon">{{ $sub['meals_remaining'] ?? 0 }} Dabbas Left</span>
                                </div>
                                <div class="w-full h-3 bg-gray-100 rounded-full overflow-hidden">
                                    <div class="h-full bg-dabba-maroon rounded-full transition-all duration-1000" style="width: {{ max(5, $progressPercent) }}%"></div>
                                </div>
                            </div>

                            <!-- Stats Row -->
                            <div class="grid grid-cols-2 md:grid-cols-3 gap-4 mb-10">
                                <div class="p-5 rounded-3xl bg-gray-50 border border-gray-100">
                                    <i data-lucide="calendar-check" class="w-5 h-5 text-dabba-maroon mb-3"></i>
                                    <p class="text-[9px] font-bold text-gray-400 uppercase tracking-widest mb-1">Status</p>
                                    <p class="text-sm font-bold text-dabba-dark">Active</p>
                                </div>
                                <div class="p-5 rounded-3xl bg-gray-50 border border-gray-100">
                                    <i data-lucide="truck" class="w-5 h-5 text-dabba-maroon mb-3"></i>
                                    <p class="text-[9px] font-bold text-gray-400 uppercase tracking-widest mb-1">Next Delivery</p>
                                    <p class="text-sm font-bold text-dabba-dark">Tomorrow</p>
                                </div>
                                <a href="{{ route('wallet') }}" class="p-5 rounded-3xl bg-gray-50 border border-gray-100 hover:bg-dabba-maroon/5 transition-all group">
                                    <i data-lucide="wallet" class="w-5 h-5 text-dabba-maroon mb-3 group-hover:scale-110 transition-transform"></i>
                                    <p class="text-[9px] font-bold text-gray-400 uppercase tracking-widest mb-1">Wallet</p>
                                    <p class="text-sm font-bold text-dabba-dark">₹{{ number_format($userData['wallet_balance'] ?? 0, 2) }}</p>
                                </a>
                            </div>

                            <div class="flex flex-wrap gap-4">
                                <a href="{{ route('subscription.show', $sub['external_subscription_id']) }}" 
                                    class="px-8 py-4 bg-dabba-dark text-white rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-dabba-maroon transition-all shadow-xl shadow-dabba-maroon/10">
                                    Manage Subscription
                                </a>
                                <a href="{{ route('calendar') }}" class="px-8 py-4 border border-dabba-dark/10 rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-gray-50 transition-all">
                                    View Calendar
                                </a>
                            </div>
                        </div>
                    @endforeach

                    <!-- Meal Planner Promo -->
                    <div class="bg-white rounded-[3rem] p-8 border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal flex flex-col md:flex-row items-center justify-between gap-6">
                        <div>
                            <p class="text-[9px] font-bold text-dabba-maroon uppercase tracking-widest mb-1">Weekly Planning</p>
                            <h3 class="text-xl font-serif font-bold text-dabba-dark">Customize your dabba schedule.</h3>
                            <p class="text-xs text-gray-500 mt-1">Pick your meals or swap upcoming deliveries in the planner.</p>
                        </div>
                        <a href="{{ route('calendar') }}" class="px-8 py-4 bg-dabba-maroon/10 text-dabba-maroon rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-dabba-maroon hover:text-white transition-all">
                            Open Planner
                        </a>
                    </div>
                </div>

                <!-- Sidebar Content -->
                <div class="space-y-8">
                    <!-- Quick Actions -->
                    <div class="bg-white rounded-[3rem] p-8 border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal">
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-[0.3em] mb-6">Quick Actions</h3>
                        <div class="grid grid-cols-2 gap-4">
                            @foreach([
                                ['icon' => 'calendar', 'label' => 'Calendar', 'route' => 'calendar'],
                                ['icon' => 'utensils', 'label' => 'Today\'s Menu', 'route' => 'menu'],
                                ['icon' => 'wallet', 'label' => 'Wallet', 'route' => 'wallet'],
                                ['icon' => 'message-circle', 'label' => 'Support', 'route' => 'support'],
                            ] as $action)
                                <a href="{{ route($action['route']) }}" class="flex flex-col items-center p-6 rounded-3xl bg-gray-50 border border-gray-100 hover:bg-dabba-maroon/5 hover:text-dabba-maroon hover:border-dabba-maroon/20 transition-all group">
                                    <i data-lucide="{{ $action['icon'] }}" class="w-6 h-6 mb-3 group-hover:scale-110 transition-transform"></i>
                                    <span class="text-[9px] font-bold uppercase tracking-widest text-center">{{ $action['label'] }}</span>
                                </a>
                            @endforeach
                        </div>
                    </div>

                    <!-- Support Card -->
                    <div class="bg-dabba-dark rounded-[3rem] p-8 text-white relative overflow-hidden shadow-2xl reveal">
                        <div class="absolute top-0 right-0 w-32 h-32 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                        <h3 class="text-2xl font-serif font-bold mb-4 relative z-10">Dabba Support</h3>
                        <p class="text-sm text-white/70 leading-relaxed mb-8 relative z-10">Need help adjusting your schedule or have a query? Our team is a tap away.</p>
                        <a href="{{ route('support') }}" class="flex items-center justify-center gap-3 w-full py-4 bg-dabba-maroon text-white rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-white hover:text-dabba-maroon transition-all shadow-xl shadow-dabba-maroon/20 relative z-10">
                            Get Help
                        </a>
                    </div>

                    <!-- Notifications -->
                    <div class="bg-white rounded-[3rem] p-8 border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal">
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-[0.3em] mb-6">Recent Alerts</h3>
                        <div class="space-y-6">
                            <div class="flex gap-4">
                                <div class="w-2 h-2 rounded-full bg-dabba-maroon mt-1.5 shrink-0"></div>
                                <div>
                                    <p class="text-xs font-bold text-dabba-dark">Welcome to DabbaGo Portal</p>
                                    <p class="text-[10px] text-gray-400 mt-0.5">Your homestyle journey has begun.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        @endif
    </div>
</section>
@endsection
