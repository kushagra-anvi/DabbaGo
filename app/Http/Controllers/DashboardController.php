<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class DashboardController extends Controller
{
    protected $apiBaseUrl;
    protected $apiKey;

    public function __construct()
    {
        $this->apiBaseUrl = config('services.hnh.base_url');
        $this->apiKey = config('services.hnh.api_key');
    }

    public function index()
    {
        $phone = session('user_phone') ?? '9876543210';
        
        // Fetch subscriptions from Hub
        $response = Http::withHeaders([
            'X-API-Key' => $this->apiKey,
        ])->get("{$this->apiBaseUrl}/api/v1/subscriptions", [
            'phone' => $phone
        ]);

        $subscriptions = [];
        $userData = null;

        if ($response->ok()) {
            $data = $response->json();
            $subscriptions = $data['data'] ?? [];
            $userData = $data['user'] ?? null;
        }

        // Fallback to dummy data if empty (for demonstration)
        if (empty($subscriptions) || empty($userData)) {
            $userData = [
                'name' => 'Kushagra',
                'loyalty_tier' => 'Elite Foodie',
                'wallet_balance' => 850.25,
                'journey_days' => 62,
                'total_meals' => 180
            ];

            $subscriptions = [
                [
                    'external_id' => 'SUB-DAB-001',
                    'external_subscription_id' => 'SUB-DAB-001',
                    'plan_name' => 'Authentic Homestyle Tiffin',
                    'status' => 'active',
                    'next_billing' => '2024-05-18',
                    'meals_remaining' => 8,
                    'total_meals' => 20,
                    'diet_type' => 'Veg',
                    'meal_slots' => ['lunch'],
                    'next_billing_amount' => 2800.00,
                    'next_billing_date' => 'May 18, 2024'
                ]
            ];
        }

        // Store in session for other portal pages
        session(['user_data' => $userData, 'user_phone' => $phone]);

        return view('dashboard', compact('subscriptions', 'userData', 'phone'));
    }

    public function showSubscription($externalId)
    {
        $phone = session('user_phone') ?? '9876543210';

        $response = Http::withHeaders([
            'X-API-Key' => $this->apiKey,
        ])->get("{$this->apiBaseUrl}/api/v1/subscriptions/{$externalId}");

        if ($response->ok()) {
            $subscription = $response->json()['data'];
        } else {
            // Dummy Data for Demonstration
            $subscription = [
                'subscription_number' => 'DAB-9942',
                'plan_name' => 'Authentic Homestyle Tiffin',
                'status' => 'Active',
                'total_amount' => 2800.00,
                'diet_type' => 'Pure Vegetarian',
                'meal_slots' => ['lunch'],
                'active_days' => 20,
                'meals_remaining' => 8,
                'total_meals' => 20,
                'address' => [
                    'full_name' => 'Kushagra',
                    'address_line_1' => 'Tower 5, Gachibowli',
                    'city' => 'Hyderabad',
                    'pincode' => '500032'
                ],
                'upcoming_meals' => [
                    ['date' => '2024-05-14', 'status' => 'active'],
                    ['date' => '2024-05-15', 'status' => 'active'],
                    ['date' => '2024-05-16', 'status' => 'active'],
                    ['date' => '2024-05-17', 'status' => 'active'],
                    ['date' => '2024-05-18', 'status' => 'active'],
                    ['date' => '2024-05-19', 'status' => 'completed'],
                    ['date' => '2024-05-20', 'status' => 'active'],
                ]
            ];
        }

        return view('subscription-detail', compact('subscription', 'phone'));
    }
}
