@extends('layouts.customer')

@section('title', 'Tiffin Wallet | DabbaGo')

@section('content')
<section class="min-h-screen bg-gray-50/50 pt-24 pb-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
        
        <!-- Header -->
        <div class="reveal">
            <h1 class="text-3xl md:text-5xl font-serif font-bold text-dabba-dark leading-tight">Tiffin <span class="text-dabba-maroon italic">Wallet</span></h1>
            <p class="mt-4 text-gray-500 font-medium">Manage your balance, track refunds, and explore exclusive member credits.</p>
        </div>

        <div class="grid lg:grid-cols-3 gap-10">
            <!-- Balance Card -->
            <div class="lg:col-span-1 space-y-6">
                <div class="bg-gradient-to-br from-dabba-dark to-dabba-dark/90 rounded-[3rem] p-10 text-white relative overflow-hidden shadow-2xl reveal">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-dabba-maroon/10 rounded-full blur-3xl -mr-24 -mt-24"></div>
                    <div class="relative z-10">
                        <p class="text-[9px] font-bold uppercase tracking-[0.3em] text-[#f9dd8a] mb-4">Total Balance</p>
                        <div class="flex items-baseline gap-2 mb-10">
                            <span class="text-2xl font-serif">₹</span>
                            <span class="text-5xl font-serif font-bold tracking-tight">{{ number_format($userData['wallet_balance'] ?? 850, 2) }}</span>
                        </div>
                        
                        <div class="space-y-3">
                            <button class="w-full py-4 bg-[#f9dd8a] text-dabba-maroon rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-white hover:text-dabba-maroon transition-all shadow-xl shadow-[#f9dd8a]/20">
                                Add Credits
                            </button>
                            <button class="w-full py-4 bg-white/5 border border-white/10 text-white rounded-full font-bold text-[10px] uppercase tracking-widest hover:bg-white/10 transition-all">
                                Redeem Voucher
                            </button>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-[2.5rem] p-8 border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal">
                    <h4 class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-6">Quick Stats</h4>
                    <div class="space-y-6">
                        <div class="flex justify-between items-center">
                            <span class="text-xs font-medium text-gray-500">Total Saved</span>
                            <span class="text-sm font-bold text-dabba-dark">₹1,250.00</span>
                        </div>
                        <div class="flex justify-between items-center">
                            <span class="text-xs font-medium text-gray-500">Referral Earned</span>
                            <span class="text-sm font-bold text-green-600">₹300.00</span>
                        </div>
                        <div class="flex justify-between items-center">
                            <span class="text-xs font-medium text-gray-500">Next Auto-Topup</span>
                            <span class="text-sm font-bold text-gray-400 italic">Disabled</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Transaction History -->
            <div class="lg:col-span-2">
                <div class="bg-white rounded-[3rem] overflow-hidden border border-dabba-maroon/5 shadow-xl shadow-dabba-maroon/5 reveal">
                    <div class="px-10 py-8 border-b border-gray-50 flex items-center justify-between">
                        <h3 class="text-lg font-serif font-bold text-dabba-dark">Transaction History</h3>
                        <div class="flex items-center gap-2">
                            <span class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Filter:</span>
                            <select class="text-[10px] font-bold text-dabba-maroon uppercase tracking-widest bg-transparent focus:outline-none">
                                <option>All Types</option>
                                <option>Credits</option>
                                <option>Debits</option>
                                <option>Refunds</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="p-0">
                        @php
                            $txns = [
                                ['type' => 'credit', 'title' => 'Referral Bonus', 'date' => 'May 14, 2024', 'amount' => '+ ₹300.00', 'desc' => 'Friend Signed Up'],
                                ['type' => 'debit', 'title' => 'Special Menu Upgrade', 'date' => 'May 12, 2024', 'amount' => '- ₹60.00', 'desc' => 'Dussehra Special Dabba'],
                                ['type' => 'refund', 'title' => 'Skipped Tiffin Refund', 'date' => 'May 10, 2024', 'amount' => '+ ₹150.00', 'desc' => 'Order #9821'],
                                ['type' => 'credit', 'title' => 'Welcome Bonus', 'date' => 'May 01, 2024', 'amount' => '+ ₹100.00', 'desc' => 'New User Credits'],
                            ];
                        @endphp
                        
                        <div class="divide-y divide-gray-50">
                            @foreach($txns as $txn)
                                <div class="px-10 py-6 flex items-center justify-between hover:bg-gray-50/50 transition-colors cursor-pointer group">
                                    <div class="flex items-center gap-6">
                                        <div class="w-12 h-12 rounded-2xl flex items-center justify-center 
                                            {{ $txn['type'] === 'credit' ? 'bg-green-50 text-green-600' : ($txn['type'] === 'debit' ? 'bg-orange-50 text-orange-600' : 'bg-blue-50 text-blue-600') }}">
                                            <i data-lucide="{{ $txn['type'] === 'credit' ? 'arrow-up-right' : ($txn['type'] === 'debit' ? 'arrow-down-left' : 'rotate-ccw') }}" class="w-5 h-5"></i>
                                        </div>
                                        <div>
                                            <p class="text-sm font-bold text-dabba-dark mb-1 group-hover:text-dabba-maroon transition-colors">{{ $txn['title'] }}</p>
                                            <p class="text-[10px] text-gray-500 font-medium">{{ $txn['date'] }} · {{ $txn['desc'] }}</p>
                                        </div>
                                    </div>
                                    <div class="text-right">
                                        <p class="text-sm font-bold {{ str_contains($txn['amount'], '+') ? 'text-green-600' : 'text-dabba-dark' }}">
                                            {{ $txn['amount'] }}
                                        </p>
                                        <p class="text-[9px] font-bold text-gray-300 uppercase tracking-widest mt-1">Completed</p>
                                    </div>
                                </div>
                            @endforeach
                        </div>

                        <div class="p-10 text-center bg-gray-50/30">
                            <button class="text-[10px] font-bold text-gray-400 uppercase tracking-[0.2em] hover:text-dabba-maroon transition-colors">
                                View Full Transaction Statement →
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
@endsection
