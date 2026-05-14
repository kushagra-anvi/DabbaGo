@extends('layouts.customer')

@section('title', 'Weekly Menu | DabbaGo')

@section('content')
<section class="min-h-screen bg-gray-50/50 pt-24 pb-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        
        <!-- Header Section -->
        <div class="bg-gradient-to-r from-dabba-dark to-dabba-dark/90 rounded-[3rem] p-8 md:p-16 text-white relative overflow-hidden shadow-2xl reveal">
            <div class="absolute top-0 right-0 w-96 h-96 bg-dabba-maroon/10 rounded-full blur-3xl -mr-48 -mt-48"></div>
            <div class="relative z-10">
                <p class="text-[10px] font-bold uppercase tracking-[0.4em] text-[#f9dd8a] mb-4">Maa ke Haath ka Khana</p>
                <h1 class="text-3xl md:text-6xl font-serif font-bold leading-tight">
                    Our Weekly <br><span class="text-[#f9dd8a] italic">Dabba Menu</span>
                </h1>
                <p class="mt-6 text-white/60 font-medium max-w-xl text-sm leading-relaxed">Homestyle recipes, fresh ingredients, and zero preservatives. We bring the comfort of home-cooked meals straight to your desk or doorstep.</p>
            </div>
        </div>

        <!-- Filter Bar -->
        <div class="flex flex-wrap items-center justify-between gap-6 px-10 py-6 bg-white rounded-[2rem] border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal">
            <div class="flex items-center gap-6">
                <button class="text-[10px] font-bold uppercase tracking-widest text-dabba-maroon border-b-2 border-dabba-maroon pb-1">All Menus</button>
                <button class="text-[10px] font-bold uppercase tracking-widest text-gray-400 hover:text-dabba-dark transition-colors">Pure Veg</button>
                <button class="text-[10px] font-bold uppercase tracking-widest text-gray-400 hover:text-dabba-dark transition-colors">Non-Veg</button>
            </div>
            <div class="flex items-center gap-4">
                <span class="text-[10px] font-bold uppercase tracking-widest text-gray-400">Sort By:</span>
                <select class="bg-transparent text-[10px] font-bold uppercase tracking-widest text-dabba-dark focus:outline-none cursor-pointer">
                    <option>Popularity</option>
                    <option>Traditional</option>
                </select>
            </div>
        </div>

        <!-- Meal Grid -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            @php
                $meals = [
                    [
                        'name' => 'Homestyle Paneer Masala',
                        'desc' => 'Soft cottage cheese cubes in a rich tomato-based gravy, served with 3 butter rotis and dal.',
                        'calories' => '480',
                        'type' => 'Veg',
                        'price' => 'Premium'
                    ],
                    [
                        'name' => 'Dal Tadka & Jeera Rice',
                        'desc' => 'Classic yellow lentils tempered with cumin and garlic, served with aromatic basmati rice.',
                        'calories' => '420',
                        'type' => 'Veg',
                        'price' => 'Classic'
                    ],
                    [
                        'name' => 'Ghar Jaisa Chicken Curry',
                        'desc' => 'Tender chicken pieces in a traditional spicy gravy, served with rice or rotis.',
                        'protein' => '48g',
                        'calories' => '520',
                        'type' => 'Non-Veg',
                        'price' => 'Premium'
                    ],
                    [
                        'name' => 'Aloo Gobhi Adraki',
                        'desc' => 'Fresh cauliflower and potatoes tossed with ginger and green chillies.',
                        'calories' => '350',
                        'type' => 'Veg',
                        'price' => 'Classic'
                    ],
                    [
                        'name' => 'Mutton Rogan Josh',
                        'desc' => 'Slow-cooked lamb in a rich Kashmiri spice blend. A weekend special.',
                        'calories' => '610',
                        'type' => 'Non-Veg',
                        'price' => 'Deluxe'
                    ],
                    [
                        'name' => 'Mixed Veg Melange',
                        'desc' => 'Seasonal vegetables cooked in a light, flavorful masala.',
                        'calories' => '310',
                        'type' => 'Veg',
                        'price' => 'Classic'
                    ],
                ];
            @endphp

            @foreach($meals as $meal)
                <div class="bg-white rounded-[3rem] overflow-hidden border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 group hover:shadow-2xl hover:shadow-dabba-maroon/10 transition-all reveal">
                    <div class="aspect-[4/3] bg-gray-100 relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
                        <span class="absolute top-6 left-6 px-4 py-1 rounded-full bg-white/90 backdrop-blur text-[8px] font-bold uppercase tracking-widest text-dabba-maroon shadow-sm">
                            {{ $meal['type'] }}
                        </span>
                        <span class="absolute bottom-6 right-6 px-4 py-1 rounded-full bg-dabba-maroon text-white text-[8px] font-bold uppercase tracking-widest shadow-lg shadow-dabba-maroon/20">
                            {{ $meal['price'] }}
                        </span>
                    </div>
                    <div class="p-8">
                        <h3 class="text-xl font-serif font-bold text-dabba-dark mb-3 group-hover:text-dabba-maroon transition-colors">{{ $meal['name'] }}</h3>
                        <p class="text-xs text-gray-500 leading-relaxed mb-6">{{ $meal['desc'] }}</p>
                        
                        <div class="flex items-center justify-between py-6 border-t border-gray-50">
                            <div class="flex items-center gap-2">
                                <i data-lucide="zap" class="w-4 h-4 text-dabba-maroon"></i>
                                <span class="text-sm font-bold text-dabba-dark">{{ $meal['calories'] }} kcal</span>
                            </div>
                            <button class="px-6 py-3 bg-gray-50 text-dabba-maroon rounded-full font-bold text-[9px] uppercase tracking-widest group-hover:bg-dabba-maroon group-hover:text-white transition-all">
                                View Details
                            </button>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>
    </div>
</section>
@endsection
