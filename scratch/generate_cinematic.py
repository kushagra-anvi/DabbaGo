import re
import os

order_path = "/Users/kushagra/Desktop/Projects/DabbaGo/pages/order.html"
original_path = "/Users/kushagra/Desktop/Projects/DabbaGo/pages/order_experiment.html"

# Read original production order.html to get step forms
with open(order_path, "r", encoding="utf-8") as f:
    order_html = f.read()

# Read existing experiment code if it exists (for success content fallback)
html = ""
if os.path.exists(original_path):
    with open(original_path, "r", encoding="utf-8") as f:
        html = f.read()

# Extract form steps 1 to 5 from order.html
steps = []
for i in range(1, 6):
    # Regex pattern to match each step content block inside order.html
    pattern = rf'(<div id="step-content-{i}".*?</div>)\s*(?=<div id="step-content-{i+1}"|<div class="bg-white/80|</div>\s*</div>\s*<div class="bg-white/80)'
    m = re.search(pattern, order_html, re.DOTALL)
    if not m:
        # Fallback for step 5
        pattern_s5 = r'(<div id="step-content-5".*?</div>)\s*</div>\s*</div>\s*<div class="bg-white/80'
        m = re.search(pattern_s5, order_html, re.DOTALL)
    if m:
        step_content = m.group(1).strip()
        steps.append(step_content)
    else:
        print(f"Error: Step {i} not found!")

# Combine all extracted steps
forms_content = "\n\n".join(steps)

# Convert light-theme text, borders, and backgrounds to pristine metallic dark-theme styles
forms_content = forms_content.replace("text-dabba-dark", "text-white")
forms_content = forms_content.replace("border-gray-100", "border-white/10")
forms_content = forms_content.replace("bg-gray-50/50", "bg-white/5")
forms_content = forms_content.replace("bg-gray-50", "bg-white/5")
forms_content = forms_content.replace("text-gray-500", "text-gray-400")
forms_content = forms_content.replace("group-hover:border-gray-200", "group-hover:border-white/20")
forms_content = forms_content.replace("hover:bg-gray-50", "hover:bg-white/5")
forms_content = forms_content.replace("bg-green-50", "bg-green-950/20")
forms_content = forms_content.replace("bg-red-50", "bg-red-950/20")

# Extract Success Modal
success_match = re.search(r'<!-- Beautiful Premium Success Modal overlay -->(.*?)</html>', html, re.DOTALL)
if success_match:
    success_content = success_match.group(1).strip()
else:
    # Extract from order.html as fallback
    success_match_order = re.search(r'<!-- Beautiful Premium Success Modal overlay -->(.*?)</html>', order_html, re.DOTALL)
    success_content = success_match_order.group(1).strip() if success_match_order else ""

# Create the new cinematic checkout HTML
cinematic_html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Build Your Dabba | DabbaGo</title>
    <meta name="description" content="Customize your gourmet dabba subscription. Choose your diet, plan your meals, and schedule your deliveries.">
    <link rel="icon" type="image/png" href="../assets/images/logo.webp">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="../assets/css/index.css">
    <script src="../assets/js/main.js" defer></script>
    <script src="../assets/js/components.js" defer></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'dabba-maroon': '#6f1e3b',
                        'dabba-beige': '#FFF9E5',
                        'dabba-dark': '#1A1A1A',
                    }
                }
            }
        }
    </script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        html, body {
            height: 100%;
            background-color: #0b0b0d;
            color: #f3f4f6;
            overflow-x: hidden;
        }

        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }

        /* ==========================================================================
           CINEMATIC FLOW LAYOUT & CAMERA ZOOM STATES
           ========================================================================== */
        #checkout-flow {
            perspective: 1200px;
            overflow: hidden;
            width: 100%;
            height: 680px;
            min-height: 680px;
            position: relative;
        }

        /* CAMERA: Hero Stage Zoom & Position Transitions */
        #hero-stage-wrapper {
            transition: transform 1.1s cubic-bezier(0.25, 1, 0.2, 1), opacity 0.9s ease-in-out;
            transform-origin: center center;
        }

        #active-chamber-wrapper {
            transition: transform 1.1s cubic-bezier(0.25, 1, 0.2, 1), opacity 0.9s ease-in-out, filter 1.1s ease;
            transform-origin: center center;
        }

        /* state-hero: Tiffin stack is large and center-stage, workspace forms hidden */
        .state-hero #hero-stage-wrapper {
            transform: scale(1.15) translateZ(0) translateY(0);
            opacity: 1;
            pointer-events: auto;
            filter: none;
        }
        .state-hero #active-chamber-wrapper {
            transform: scale(0.7) translateZ(-400px);
            opacity: 0;
            pointer-events: none;
            filter: blur(10px);
        }

        /* state-interior: Camera zooms deep inside the active level */
        .state-interior #hero-stage-wrapper {
            transform: scale(3.2) translateY(var(--zoom-y, 0px)) translateZ(150px);
            opacity: 0.05;
            pointer-events: none;
            filter: blur(4px);
        }
        .state-interior #active-chamber-wrapper {
            transform: scale(1) translateZ(0);
            opacity: 1;
            pointer-events: auto;
            filter: none;
        }

        /* 3D cylindrical stage frame wrapper */
        .tiffin-stage {

        /* === STANDALONE C-CLAMP CARRIER FRAME === */
        .carrier-frame {
            position: absolute;
            bottom: 12px;
            left: 50%;
            transform: translateX(-50%) translateY(-100%);
            width: 196px;
            height: 290px;
            z-index: 10;
            opacity: 0;
            transition: transform .8s cubic-bezier(.34, 1.56, .64, 1), opacity .4s ease;
            pointer-events: none;
        }

        .carrier-frame.active {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }

        .carrier-arch {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 196px;
            height: 52px;
            border: 6px solid #d8d8d8;
            border-bottom: none;
            border-radius: 98px 98px 0 0;
            box-shadow: inset 0 2px 4px rgba(255, 255, 255, .4), 0 3px 6px rgba(0, 0, 0, .2);
        }

        .carrier-arch-latch {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 22px;
            height: 10px;
            background: linear-gradient(180deg, #e0e0e0, #b0b0b0);
            border-radius: 2px 2px 0 0;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, .4), 0 1px 2px rgba(0, 0, 0, .15);
        }

        .carrier-connector {
            position: absolute;
            top: 52px;
            width: 63px;
            height: 4.5px;
            background: linear-gradient(180deg, #dcdcdc, #aaaaaa);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, .4), 0 1px 2px rgba(0, 0, 0, .2);
            border-radius: 2px;
            z-index: 9;
        }

        .carrier-connector.left { left: 0; }
        .carrier-connector.right { right: 0; }

        .carrier-rail {
            position: absolute;
            top: 52px;
            bottom: 4px;
            width: 7px;
            background: linear-gradient(90deg, #999 0%, #e0e0e0 30%, #fff 50%, #c0c0c0 75%, #888 100%);
            box-shadow: inset 0 0 1px rgba(255, 255, 255, .4), 2px 0 5px rgba(0, 0, 0, .15);
            z-index: 8;
        }

        .carrier-rail.left { left: 5px; }
        .carrier-rail.right { right: 5px; }

        .carrier-side-tab {
            position: absolute;
            width: 12px;
            height: 18px;
            background: linear-gradient(90deg, #b0b0b0, #e0e0e0, #999);
            box-shadow: 0 2px 4px rgba(0, 0, 0, .3), inset 0 1px 0 rgba(255, 255, 255, .4);
            border-radius: 3px;
        }

        .carrier-rail.left .carrier-side-tab {
            left: -2.5px;
            top: 40px;
            border-radius: 3px 0 0 3px;
        }

        .carrier-rail.right .carrier-side-tab {
            right: -2.5px;
            top: 40px;
            border-radius: 0 3px 3px 0;
        }

        .carrier-base {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 188px;
            height: 6px;
            background: linear-gradient(90deg, #888, #e0e0e0, #888);
            border-radius: 3px;
            box-shadow: 0 3px 6px rgba(0, 0, 0, .45);
        }

        .dabba-stack {
            display: flex;
            flex-direction: column-reverse;
            align-items: center;
            position: relative;
            z-index: 5;
        }

        /* Sidebar Assembly Pile Levels (180px dabbas with materialize effects) */
        .assembly-level {
            width: 180px;
            height: 62px;
            border-radius: 90px / 20px;
            margin-bottom: -20px;
            background: linear-gradient(90deg, #18181a 0%, #2d2d32 50%, #18181a 100%);
            border: 1px solid rgba(255, 255, 255, 0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            font-weight: 800;
            color: rgba(255, 255, 255, 0.15);
            text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.5);
            transition: background 0.5s ease, border-color 0.5s ease, box-shadow 0.5s ease, color 0.4s ease;
            opacity: 0.15;
            transform: translateY(0) scale(0.92);
            position: relative;
            overflow: visible;
        }

        .assembly-level.active {
            opacity: 1;
            color: #ffffff;
            background: linear-gradient(90deg,
                    #121214 0%, #33333a 8%, #484852 20%, #545460 30%,
                    #40404a 45%, #28282e 60%, #40404a 75%, #4c4c58 85%,
                    #33333a 92%, #121214 100%);
            border-color: rgba(255, 255, 255, 0.3);
            transform: translateY(0) scale(1);
            box-shadow:
                inset 0 2px 2px rgba(255, 255, 255, 0.25),
                0 8px 12px rgba(0, 0, 0, 0.6);
        }

        .assembly-level.active.veg-active {
            background: linear-gradient(90deg,
                    #0f2416 0%, #1b4327 8%, #2e7d32 20%, #388e3c 30%,
                    #2e7d32 45%, #1b4327 60%, #2e7d32 75%, #388e3c 85%,
                    #1b4327 92%, #0f2416 100%) !important;
            border-color: rgba(74, 222, 128, 0.3);
        }

        .assembly-level.active.nonveg-active {
            background: linear-gradient(90deg,
                    #2d0e11 0%, #4e191e 8%, #c62828 20%, #d32f2f 30%,
                    #c62828 45%, #4e191e 60%, #c62828 75%, #d32f2f 85%,
                    #4e191e 92%, #2d0e11 100%) !important;
            border-color: rgba(248, 113, 113, 0.3);
        }

        @keyframes dabba-materialize {
            0% { transform: translateY(-60px) scale(0.5); opacity: 0; filter: brightness(3); }
            30% { transform: translateY(8px) scale(1.06); opacity: 1; filter: brightness(1.8); }
            50% { transform: translateY(-5px) scale(0.97); filter: brightness(1.2); }
            70% { transform: translateY(3px) scale(1.02); filter: brightness(1); }
            85% { transform: translateY(-1px) scale(0.995); }
            100% { transform: translateY(0) scale(1); opacity: 1; filter: brightness(1); }
        }

        .assembly-level.materializing {
            animation: dabba-materialize 0.7s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        }

        @keyframes pulse-ring {
            0% { transform: translate(-50%, -50%) scale(0.5); opacity: 0.8; }
            100% { transform: translate(-50%, -50%) scale(2.5); opacity: 0; }
        }

        .dabba-pulse-ring {
            position: absolute;
            left: 50%;
            top: 50%;
            width: 180px;
            height: 62px;
            border-radius: 90px / 20px;
            border: 2px solid rgba(133, 39, 71, 0.6);
            pointer-events: none;
            animation: pulse-ring 0.6s ease-out forwards;
        }

        @keyframes sparkle-fly {
            0% { transform: translate(0, 0) scale(1); opacity: 1; }
            100% { transform: translate(var(--sx), var(--sy)) scale(0); opacity: 0; }
        }

        .dabba-sparkle {
            position: absolute;
            width: 4px;
            height: 4px;
            border-radius: 50%;
            background: #fca5a5;
            pointer-events: none;
            animation: sparkle-fly 0.55s ease-out forwards;
            box-shadow: 0 0 6px 2px rgba(252, 165, 165, 0.6);
        }

        .assembly-lid {
            width: 182px;
            height: 25px;
            border-radius: 50% / 8px;
            background: linear-gradient(90deg, #333 0%, #888 50%, #333 100%);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: inset 0 2px 3px rgba(255, 255, 255, 0.2), 0 -2px 3px rgba(0, 0, 0, 0.6);
            margin-bottom: -12px;
            z-index: 10;
            opacity: 0;
            left: 50%;
            transform: translateX(-50%) translateY(-80px);
            transition: all 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .assembly-lid.active {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        .stack-shadow {
            width: 100px;
            height: 14px;
            background: radial-gradient(ellipse, rgba(255, 255, 255, .05) 0%, transparent 70%);
            border-radius: 50%;
            margin-top: 8px;
            transition: all .5s ease;
        }

        /* ==========================================================================
           GIANT CHAMBER WALLS & INTERIOR VIEWPORT
           ========================================================================== */
        .active-dabba-chamber {
            max-width: 600px;
            height: 460px;
            border-radius: 40px / 24px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: linear-gradient(90deg,
                    #1e1e1e 0%, #3a3a3a 8%, #4e4e4e 18%, #5a5a5a 28%,
                    #444444 42%, #2d2d2d 58%, #444444 72%, #4e4e4e 82%,
                    #323232 92%, #1e1e1e 100%);
            box-shadow:
                inset 0 4px 12px rgba(255, 255, 255, 0.08),
                inset 0 -4px 12px rgba(0, 0, 0, 0.6),
                0 20px 40px rgba(0, 0, 0, 0.5);
            overflow: hidden;
            position: relative;
            transition: background 0.8s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .active-dabba-chamber.dabba-veg {
            background: linear-gradient(90deg,
                    #0f2416 0%, #1b4327 8%, #265c36 18%, #307243 28%,
                    #265c36 42%, #1b4327 58%, #265c36 72%, #307243 82%,
                    #1b4327 92%, #0f2416 100%) !important;
            border-color: rgba(74, 222, 128, 0.2);
        }

        .active-dabba-chamber.dabba-nonveg {
            background: linear-gradient(90deg,
                    #2d0e11 0%, #4e191e 8%, #6c2229 18%, #862b33 28%,
                    #6c2229 42%, #4e191e 58%, #6c2229 72%, #862b33 82%,
                    #4e191e 92%, #2d0e11 100%) !important;
            border-color: rgba(248, 113, 113, 0.2);
        }

        .chamber-viewport {
            scrollbar-width: thin;
            scrollbar-color: rgba(255, 255, 255, 0.15) transparent;
            box-shadow: inset 0 24px 30px -10px rgba(0,0,0,0.85), inset 0 -24px 30px -10px rgba(0,0,0,0.85);
        }

        .chamber-viewport::-webkit-scrollbar {
            width: 4px;
        }

        .chamber-viewport::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 10px;
        }

        /* Glass Navbar & Overrides */
        .glass-nav {
            background: rgba(11, 11, 13, 0.75) !important;
            backdrop-filter: blur(24px) !important;
            -webkit-backdrop-filter: blur(24px) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06) !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
        }

        .step-container .flex.items-center.gap-3 span {
            background-color: rgba(133, 39, 71, 0.25) !important;
            color: #fca5a5 !important;
            border: 1px solid rgba(133, 39, 71, 0.4) !important;
            padding: 4px 12px !important;
            border-radius: 9999px !important;
            display: inline-flex !important;
            font-weight: 700 !important;
            letter-spacing: 0.1em !important;
        }

        .step-container h2 span.italic.text-dabba-maroon {
            color: #fca5a5 !important;
            text-shadow: 0 0 10px rgba(133, 39, 71, 0.4);
            font-style: italic !important;
        }

        .serviceability-alert {
            background-color: rgba(22, 101, 52, 0.2) !important;
            color: #4ade80 !important;
            border: 1px solid rgba(22, 101, 52, 0.4) !important;
            box-shadow: 0 0 15px rgba(34, 197, 94, 0.15) !important;
        }
    </style>
</head>

<body class="bg-[#0b0b0d] text-white selection:bg-dabba-maroon selection:text-white flex flex-col min-h-screen overflow-x-hidden">

    <div id="header-placeholder"></div>

    <main class="w-full min-h-screen pt-24 pb-12 px-4 max-w-7xl mx-auto flex flex-col justify-center items-center">
        
        <!-- MAIN PERSPECTIVE CONTAINER FOR THE CAMPAIGN STATES -->
        <div id="checkout-flow" class="state-hero w-full flex flex-col items-center justify-center relative">
            
            <!-- STATE 1: HERO VIEW (Zooms stack center stage, progressive unlock reveal) -->
            <div id="hero-stage-wrapper" class="absolute inset-0 flex flex-col items-center justify-center z-10">
                <div class="text-center mb-8">
                    <p class="text-[10px] font-bold text-dabba-maroon uppercase tracking-[0.3em] mb-2">Build-A-Tiffin Experience</p>
                    <h1 class="text-3xl lg:text-4xl font-serif font-bold text-white leading-tight">
                        Assemble your <span class="italic text-[#fca5a5]">perfect subscription.</span>
                    </h1>
                </div>

                <!-- Snug Stack Box -->
                <div class="p-8 rounded-3xl bg-gradient-to-b from-[#131316] to-[#0a0a0c] border border-white/5 flex flex-col items-center justify-center relative shadow-2xl max-w-[340px] w-full">
                    <div class="absolute left-6 top-10 bottom-10 w-[1px] bg-white/5"></div>
                    <div class="absolute right-6 top-10 bottom-10 w-[1px] bg-white/5"></div>
                    
                    <div class="tiffin-stage mb-2" id="desktop-tiffin-stage">
                        <!-- Connected Carrier Frame -->
                        <div class="carrier-frame" id="desktop-carrier-frame">
                            <div class="carrier-arch"><div class="carrier-arch-latch"></div></div>
                            <div class="carrier-connector left"></div>
                            <div class="carrier-connector right"></div>
                            <div class="carrier-rail left"><div class="carrier-side-tab"></div></div>
                            <div class="carrier-rail right"><div class="carrier-side-tab"></div></div>
                            <div class="carrier-base"></div>
                        </div>

                        <!-- Lid -->
                        <div id="assembly-lid" class="assembly-lid absolute left-1/2" style="bottom: 20px;">
                            <div class="lid-knob" style="top: -12px; width: 22px; height: 10px;"></div>
                            <div class="lid-top" style="height: 12px;"></div>
                            <div class="lid-rim" style="height: 5px;"></div>
                        </div>

                        <!-- Mini Stack levels piling up bottom-to-top -->
                        <div class="dabba-stack flex flex-col-reverse items-center pb-2" id="desktop-dabba-stack">
                            <div class="assembly-level opacity-0 pointer-events-none" id="assembly-dabba-1" data-step="1">📍 PINCODE</div>
                            <div class="assembly-level opacity-0 pointer-events-none" id="assembly-dabba-2" data-step="2">🥗 DIET PREF</div>
                            <div class="assembly-level opacity-0 pointer-events-none" id="assembly-dabba-3" data-step="3">📅 PLAN SETUP</div>
                            <div class="assembly-level opacity-0 pointer-events-none" id="assembly-dabba-4" data-step="4">👤 CONTACT INFO</div>
                            <div class="assembly-level opacity-0 pointer-events-none" id="assembly-dabba-5" data-step="5">🗺️ DELIVERY ADDR</div>
                        </div>
                        <div class="stack-shadow" id="desktop-stack-shadow"></div>
                    </div>
                </div>

                <button onclick="diveIntoStep()" class="mt-8 px-10 py-4 rounded-xl bg-dabba-maroon text-white font-bold hover:bg-[#852747] hover:scale-105 transition-all flex items-center gap-2 shadow-lg shadow-dabba-maroon/20 tracking-wider text-xs uppercase">
                    Start Customizing <span id="start-btn-step-icon">→</span>
                </button>
            </div>

            <!-- STATE 2: INTERIOR FOCUS CHAMBER (Zoomed Inside) -->
            <div id="active-chamber-wrapper" class="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none">
                <div class="active-dabba-chamber w-full relative">
                    <!-- 3D Metallic Top Rim & Lip -->
                    <div class="absolute top-0 left-0 right-0 h-6 bg-gradient-to-b from-white/20 via-transparent to-black/50 border-b border-white/5 rounded-t-[40px] z-20 pointer-events-none shadow-inner"></div>
                    <!-- 3D Metallic Bottom Rim & Lip -->
                    <div class="absolute bottom-0 left-0 right-0 h-6 bg-gradient-to-t from-black/60 via-transparent to-white/10 border-t border-black/40 rounded-b-[40px] z-20 pointer-events-none shadow-inner"></div>
                    
                    <!-- Viewport with scrollable content inside metallic cylinder -->
                    <div id="chamber-viewport" class="chamber-viewport w-full h-full p-6 lg:p-12 overflow-y-auto transition-opacity duration-300 custom-scrollbar">
                        <div id="step-forms-wrapper">
                            <!-- === INSERTED STEP FORMS === -->
                            {forms_content}
                        </div>
                    </div>

                    <!-- Subtle Sub-Chamber Live Pricing strip (Only visible in steps 3-5) -->
                    <div id="sub-pricing-strip" class="absolute bottom-6 left-6 right-6 px-6 py-4 bg-black/60 backdrop-blur-md rounded-2xl border border-white/5 flex items-center justify-between z-30 transition-all duration-300 translate-y-16 opacity-0 pointer-events-none">
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-white/60 tracking-wider">LIVE PLAN PRICE:</span>
                            <span class="text-sm font-black text-white">₹<span id="price-per-meal">273</span> <span class="text-[10px] font-normal text-white/40">/ meal</span></span>
                        </div>
                        <div class="flex items-center gap-4 text-[11px] text-white/60">
                            <div><span id="summary-meals-day">1</span> meals/day</div>
                            <div>x <span id="summary-days">1</span> days</div>
                            <div>x <span id="summary-people">1</span> ppl</div>
                        </div>
                        <div class="flex items-center gap-2">
                            <div class="text-right">
                                <p class="text-[9px] text-white/40 leading-none">ORDER TOTAL</p>
                                <p class="text-sm font-black text-green-400">₹<span id="final-total">273</span></p>
                            </div>
                            <span id="save-badge" class="bg-green-500/20 text-green-400 border border-green-500/30 text-[9px] font-bold px-2 py-0.5 rounded hidden">SAVE <span id="save-percent">0</span>%</span>
                        </div>
                    </div>
                </div>

                <!-- Inside-Dabba Navigation Drawer -->
                <div class="flex justify-between items-center w-full max-w-[600px] mt-6 gap-4 pointer-events-auto">
                    <button id="prev-btn" onclick="zoomOutToHero(true)" class="px-6 py-3 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 text-white font-medium transition-all flex items-center gap-2">
                        <span>←</span> Return to Stack
                    </button>
                    <button id="next-btn" onclick="handleNextStep()" class="px-8 py-3 rounded-xl bg-dabba-maroon text-white font-bold hover:bg-[#852747] transition-all flex items-center gap-2 shadow-lg shadow-dabba-maroon/20">
                        Next <span>→</span>
                    </button>
                </div>
            </div>

        </div>
    </main>

    <script>
        // Preserved Config Object & Pricing Levels
        const config = {
            pincode: null,
            diet: null,
            duration: 1,
            people: 1,
            slots: { lunch: true, dinner: false },
            skips: [],
            pricing: {
                1: 273,
                3: 265,
                7: 251,
                14: 238,
                30: 213
            }
        };

        let currentStep = 1;
        let isAnimating = false;
        let isOrderCompleted = false;

        // Camera Vertical Offset calibration matching the stacked dabbas:
        // Stacking bottom-up, we move the stack vertically using transform translateY to align the active dabba with the viewport center.
        const zoomYOffsets = {
            1: 100,  // Level 1 (bottom)
            2: 58,   // Level 2
            3: 16,   // Level 3
            4: -26,  // Level 4
            5: -68   // Level 5 (top)
        };

        // Initialize state view transitions
        const flowContainer = document.getElementById('checkout-flow');

        function diveIntoStep() {
            console.log(`%c 🎬 [DIVE] Zooming into Dabba Level \${currentStep} `, 'background: #6f1e3b; color: #ffffff; font-weight: bold; padding: 4px; border-radius: 4px;');
            if (isAnimating) {
                console.warn('⚠️ [DIVE BLOCK] Aborted: Another animation is actively running.');
                return;
            }
            isAnimating = true;

            // Set vertical zoom height based on current step
            const zoomY = zoomYOffsets[currentStep] || 0;
            console.log(`%c 🎥 [CAMERA] Positioning stack focus offset to: \${zoomY}px`, 'color: #fca5a5; font-style: italic;');
            flowContainer.style.setProperty('--zoom-y', `\${zoomY}px`);

            // Mark active level on stack so it glows/solidifies during focus
            const currentStackLevel = document.getElementById(`assembly-dabba-\${currentStep}`);
            if (currentStackLevel) {
                currentStackLevel.classList.add('active');
                currentStackLevel.classList.remove('opacity-0', 'pointer-events-none');
            }

            // Sync color morph of focus cylinder
            updateChamberTheme();

            // Toggle visual state
            flowContainer.classList.remove('state-hero');
            flowContainer.classList.add('state-interior');

            setTimeout(() => {
                isAnimating = false;
                console.log('%c 🏁 [DIVE COMPLETED] Camera lens locked inside chamber viewport.', 'color: #4ade80;');
            }, 1100);
        }

        function zoomOutToHero(reverse = false) {
            console.log(`%c 🍿 [ZOOM OUT] Camera pulling back to Hero View `, 'background: #1e1b4b; color: #ffffff; font-weight: bold; padding: 4px; border-radius: 4px;');
            if (isAnimating) {
                console.warn('⚠️ [ZOOM OUT BLOCK] Aborted: Another animation is actively running.');
                return;
            }
            isAnimating = true;

            flowContainer.classList.remove('state-interior');
            flowContainer.classList.add('state-hero');

            // Refresh back label button
            const startBtnText = document.getElementById('start-btn-step-icon');
            if (startBtnText) {
                startBtnText.innerText = `(Resume Step \${currentStep}) →`;
            }

            setTimeout(() => {
                isAnimating = false;
                console.log('%c 🏁 [ZOOM OUT COMPLETED] Camera in full viewport hero view.', 'color: #e2e8f0;');
            }, 1100);
        }

        function executeStepTransition(onComplete) {
            console.log(`%c 🏗️ [TRANSITION] Commencing Step \${currentStep} complete/lock seq `, 'background: #14532d; color: #ffffff; font-weight: bold; padding: 4px; border-radius: 4px;');
            if (isAnimating) {
                console.warn('⚠️ [TRANSITION BLOCK] Aborted: Another animation is actively running.');
                return;
            }
            isAnimating = true;

            const targetStackLevel = document.getElementById(`assembly-dabba-\${currentStep}`);
            const viewport = document.getElementById('chamber-viewport');

            if (!targetStackLevel) {
                if (onComplete) onComplete();
                isAnimating = false;
                return;
            }

            // Phase 1: Zoom back to hero view to witness construction
            console.log('%c 🎥 [PHASE 1] Dynamic camera pull-back in action...', 'color: #94a3b8;');
            flowContainer.classList.remove('state-interior');
            flowContainer.classList.add('state-hero');

            setTimeout(() => {
                // Phase 2: Play drop-bounce & materialization on the stack
                console.log('%c 🪐 [PHASE 2] Drop-bounce elastic materialization triggered.', 'color: #a78bfa;');
                targetStackLevel.classList.remove('opacity-0', 'pointer-events-none');
                targetStackLevel.classList.add('active', 'materializing');

                if (currentStep >= 2 && config.diet) {
                    if (config.diet.toLowerCase().includes('veg') && !config.diet.toLowerCase().includes('non')) {
                        targetStackLevel.classList.add('veg-active');
                    } else {
                        targetStackLevel.classList.add('nonveg-active');
                    }
                }

                // Phase 3: Sparkle burst and pulse ring wave
                setTimeout(() => {
                    console.log('%c ✨ [PHASE 3] Sparkle particle and pulse ring wave burst!', 'color: #fbbf24;');
                    spawnSparkles(targetStackLevel);
                    spawnPulseRing(targetStackLevel);
                }, 180);

                // Phase 4: Settle down, complete step calculations, zoom camera back into the NEXT step!
                setTimeout(() => {
                    console.log('%c 📦 [PHASE 4] Dabba level locked. Moving to next...', 'color: #60a5fa;');
                    targetStackLevel.classList.remove('materializing');

                    if (onComplete) onComplete();

                    if (viewport) {
                        viewport.scrollTop = 0;
                    }

                    updateChamberTheme();
                    updateDabbaStack();

                    isAnimating = false;

                    // Auto-dive into the newly unlocked next step!
                    setTimeout(() => {
                        console.log('%c 🎬 [AUTO DIVE] Diving back in!', 'color: #4ade80;');
                        diveIntoStep();
                    }, 400);

                }, 750);
            }, 1000);
        }

        function handleNextStep() {
            console.log('%c 👉 [NEXT CLICK] Requesting step advance...', 'color: #e2e8f0; font-weight: bold;');
            if (isAnimating) return;

            if (!validateStep(currentStep)) {
                console.warn(`❌ [VALIDATION FAILED] Step \${currentStep} failed requirements.`);
                return;
            }

            if (currentStep === 5) {
                console.log('%c 🏆 [ORDER COMPLETE] Compiling final custom subscription order!', 'color: #22c55e; font-weight: bold;');
                completeOrder();
                return;
            }

            executeStepTransition(() => {
                currentStep++;
                updateStepUI();
            });
        }

        function handlePrevStep() {
            console.log('%c 👈 [PREV CLICK] Requesting step backward...', 'color: #e2e8f0; font-weight: bold;');
            if (isAnimating || currentStep === 1) return;

            // Zoom out to witness removal, step backward, and zoom inside previous
            flowContainer.classList.remove('state-interior');
            flowContainer.classList.add('state-hero');

            setTimeout(() => {
                const prevStackLevel = document.getElementById(`assembly-dabba-\${currentStep}`);
                if (prevStackLevel) {
                    prevStackLevel.classList.add('opacity-0', 'pointer-events-none');
                    prevStackLevel.classList.remove('active', 'veg-active', 'nonveg-active');
                }

                currentStep--;
                updateStepUI();
                updateChamberTheme();
                updateDabbaStack();

                setTimeout(() => {
                    diveIntoStep();
                }, 400);
            }, 1000);
        }

        function updateStepUI() {
            for (let i = 1; i <= 5; i++) {
                const content = document.getElementById(`step-content-${i}`);
                if (content) {
                    if (i === currentStep) {
                        content.classList.remove('hidden');
                        content.classList.add('block');
                    } else {
                        content.classList.remove('block');
                        content.classList.add('hidden');
                    }
                }
            }

            const prevBtn = document.getElementById('prev-btn');
            const nextBtn = document.getElementById('next-btn');

            if (prevBtn) {
                if (currentStep === 1) {
                    prevBtn.innerHTML = '<span>←</span> Return to Stack';
                    prevBtn.onclick = () => zoomOutToHero();
                } else {
                    prevBtn.innerHTML = '<span>←</span> Back';
                    prevBtn.onclick = () => handlePrevStep();
                }
            }

            if (nextBtn) {
                if (currentStep === 5) {
                    nextBtn.innerHTML = 'Confirm & Pay <span>🔒</span>';
                } else {
                    nextBtn.innerHTML = 'Next <span>→</span>';
                }
            }

            // Sync step-wise inline sub-pricing strip display (steps 3-5 only)
            const pricingStrip = document.getElementById('sub-pricing-strip');
            if (pricingStrip) {
                if (currentStep >= 3) {
                    pricingStrip.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-16');
                } else {
                    pricingStrip.classList.add('opacity-0', 'pointer-events-none', 'translate-y-16');
                }
            }
        }

        // Setup first level to show on initial load
        document.getElementById('assembly-dabba-1').classList.remove('opacity-0', 'pointer-events-none');

        /* === PRESERVED BUSINESS VALIDATION & CORE COMPUTATION LOGIC === */
        function checkServiceability() {
            const pinInput = document.getElementById('check-pincode');
            const pin = pinInput ? pinInput.value.trim() : '';
            const resultDiv = document.getElementById('pincode-result');
            const isValidPin = /^[1-9][0-9]{5}$/.test(pin);

            if (!isValidPin) {
                alert('Please enter a valid 6-digit Indian pincode.');
                return;
            }

            resultDiv.classList.remove('hidden');
            config.pincode = pin;
            document.getElementById('final-pincode').value = pin;
            const s1 = document.getElementById('step-summary-1'); if (s1) s1.innerText = pin;

            updateDabbaStack();

            resultDiv.innerHTML = `<div class="p-4 serviceability-alert rounded-xl text-xs font-bold flex items-center gap-2">
                <svg class="w-4 h-4 text-green-400 animate-pulse" fill="currentColor" viewBox="0 0 20 20"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"></path></svg>
                DabbaGo is fully operational in your area! Loading fabricator...
            </div>`;

            setTimeout(() => handleNextStep(), 1000);
        }

        function updateDiet(val) {
            config.diet = val;
            const s2 = document.getElementById('step-summary-2'); if (s2) s2.innerText = val;
            updateChamberTheme();
            calculatePricing();
            updateDabbaStack();
        }

        function toggleSlot(slot) {
            config.slots[slot] = !config.slots[slot];
            const el = document.getElementById(`slot-${slot}`);
            const check = document.getElementById(`${slot}-check`);

            if (config.slots[slot]) {
                if (el) el.classList.add('border-dabba-maroon', 'bg-dabba-maroon/5');
                if (check) {
                    check.innerHTML = '<svg class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M5 13l4 4L19 7"></path></svg>';
                    check.classList.add('bg-dabba-maroon');
                    check.classList.remove('border-2', 'border-white/10');
                }
            } else {
                if (el) el.classList.remove('border-dabba-maroon', 'bg-dabba-maroon/5');
                if (check) {
                    check.innerHTML = '';
                    check.classList.remove('bg-dabba-maroon');
                    check.classList.add('border-2', 'border-white/10');
                }
            }
            config.skips = [];
            generateCalendar();
            calculatePricing();
        }

        function updateDuration(days, el) {
            config.duration = days;
            config.skips = [];
            document.querySelectorAll('.duration-btn').forEach(btn => {
                btn.classList.remove('border-dabba-maroon', 'bg-dabba-maroon/5');
                btn.classList.add('border-white/5');
            });
            el.classList.add('border-dabba-maroon', 'bg-dabba-maroon/5');
            el.classList.remove('border-white/5');
            generateCalendar();
            calculatePricing();
            updateDabbaStack();
        }

        function updateChamberTheme() {
            const chamber = document.querySelector('.active-dabba-chamber');
            if (!chamber) return;
            chamber.classList.remove('dabba-veg', 'dabba-nonveg');
            if (currentStep >= 2 && config.diet) {
                if (config.diet.toLowerCase().includes('veg') && !config.diet.toLowerCase().includes('non')) {
                    chamber.classList.add('dabba-veg');
                } else {
                    chamber.classList.add('dabba-nonveg');
                }
            }
        }

        function spawnSparkles(targetEl) {
            const rect = targetEl.getBoundingClientRect();
            const cx = rect.left + rect.width / 2;
            const cy = rect.top + rect.height / 2;
            const count = 10;

            for (let i = 0; i < count; i++) {
                const angle = (Math.PI * 2 / count) * i;
                const dist = 40 + Math.random() * 50;
                const spark = document.createElement('div');
                spark.className = 'dabba-sparkle';
                spark.style.left = `${cx}px`;
                spark.style.top = `${cy}px`;
                spark.style.position = 'fixed';
                spark.style.setProperty('--sx', `${Math.cos(angle) * dist}px`);
                spark.style.setProperty('--sy', `${Math.sin(angle) * dist}px`);
                spark.style.animationDelay = `${Math.random() * 0.1}s`;

                if (config.diet) {
                    if (config.diet.toLowerCase().includes('veg') && !config.diet.toLowerCase().includes('non')) {
                        spark.style.background = '#4ade80';
                        spark.style.boxShadow = '0 0 6px 2px rgba(74, 222, 128, 0.6)';
                    } else {
                        spark.style.background = '#f87171';
                        spark.style.boxShadow = '0 0 6px 2px rgba(248, 113, 113, 0.6)';
                    }
                }
                document.body.appendChild(spark);
                spark.addEventListener('animationend', () => spark.remove());
            }
        }

        function spawnPulseRing(targetEl) {
            const ring = document.createElement('div');
            ring.className = 'dabba-pulse-ring';
            if (config.diet) {
                if (config.diet.toLowerCase().includes('veg') && !config.diet.toLowerCase().includes('non')) {
                    ring.style.borderColor = 'rgba(74, 222, 128, 0.5)';
                } else {
                    ring.style.borderColor = 'rgba(248, 113, 113, 0.5)';
                }
            }
            targetEl.appendChild(ring);
            ring.addEventListener('animationend', () => ring.remove());
        }

        function validateStep(step) {
            if (step === 1 && !config.pincode) {
                alert('Please check your pincode first.');
                return false;
            }
            if (step === 2 && !config.diet) {
                alert('Please select your dietary preference.');
                return false;
            }
            if (step === 3 && !config.slots.lunch && !config.slots.dinner) {
                alert('Please select at least one meal slot.');
                return false;
            }
            if (step === 4) {
                const name = document.getElementById('contact-name').value;
                const phone = document.getElementById('contact-phone').value;
                if (!name || name.length < 3) {
                    alert('Please enter your full name.');
                    return false;
                }
                if (!phone || phone.length < 10) {
                    alert('Please enter a valid phone number.');
                    return false;
                }
            }
            return true;
        }

        function sendOTP() {
            const phone = document.getElementById('contact-phone').value;
            if (!phone || phone.length < 10) {
                alert('Enter a valid phone number first.');
                return;
            }
            document.getElementById('otp-container').classList.remove('hidden');
            alert('OTP Sent to ' + phone + ' (Use any 4 digits to verify)');
        }

        function verifyOTP() {
            const otp = document.getElementById('contact-otp').value;
            if (otp.length === 4) {
                alert('Phone Number Verified Successfully!');
                document.getElementById('otp-container').innerHTML = '<div class="h-[52px] flex items-center gap-2 text-green-600 font-bold text-xs"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg> Verified</div>';
            } else {
                alert('Please enter a 4-digit OTP.');
            }
        }

        function updatePeople(change) {
            config.people = Math.max(1, config.people + change);
            const countEl = document.getElementById('people-count');
            if (countEl) countEl.innerText = config.people;
            calculatePricing();
        }

        function generateCalendar() {
            const list = document.getElementById('calendar-list');
            if (!list) return;
            list.innerHTML = '';
            const startDate = new Date();

            for (let i = 0; i < config.duration; i++) {
                const date = new Date(startDate);
                date.setDate(startDate.getDate() + i + 1);
                const dayStr = date.toLocaleDateString('en-US', { weekday: 'short', day: '2-digit' });
                const item = document.createElement('div');
                item.className = 'relative flex flex-col gap-3 p-5 bg-white/5 rounded-3xl border border-white/5 transition-all hover:border-white/10';

                let slotsHtml = '';
                if (config.slots.lunch) {
                    const isSkipped = config.skips.includes(`${i}-lunch`);
                    slotsHtml += `
                        <label class="flex items-center justify-between group cursor-pointer">
                            <div class="flex items-center gap-3">
                                <div class="w-4 h-4 rounded border border-white/20 flex items-center justify-center transition-all ${isSkipped ? 'border-white/10' : 'bg-[#6f1e3b] border-[#6f1e3b]'}">
                                    ${isSkipped ? '' : '<svg class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M5 13l4 4L19 7"></path></svg>'}
                                </div>
                                <span class="text-[10px] font-bold ${isSkipped ? 'text-gray-600 line-through' : 'text-white'} uppercase tracking-widest">Lunch</span>
                            </div>
                            <input type="checkbox" class="sr-only" ${isSkipped ? 'checked' : ''} onchange="toggleMealSkip(${i}, 'lunch')">
                            <span class="text-[9px] font-bold text-gray-500 opacity-0 group-hover:opacity-100 transition-opacity">${isSkipped ? 'Add back' : 'Skip'}</span>
                        </label>`;
                }
                if (config.slots.dinner) {
                    const isSkipped = config.skips.includes(`${i}-dinner`);
                    slotsHtml += `
                        <label class="flex items-center justify-between group cursor-pointer">
                            <div class="flex items-center gap-3">
                                <div class="w-4 h-4 rounded border border-white/20 flex items-center justify-center transition-all ${isSkipped ? 'border-white/10' : 'bg-[#6f1e3b] border-[#6f1e3b]'}">
                                    ${isSkipped ? '' : '<svg class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M5 13l4 4L19 7"></path></svg>'}
                                </div>
                                <span class="text-[10px] font-bold ${isSkipped ? 'text-gray-600 line-through' : 'text-white'} uppercase tracking-widest">Dinner</span>
                            </div>
                            <input type="checkbox" class="sr-only" ${isSkipped ? 'checked' : ''} onchange="toggleMealSkip(${i}, 'dinner')">
                            <span class="text-[9px] font-bold text-gray-500 opacity-0 group-hover:opacity-100 transition-opacity">${isSkipped ? 'Add back' : 'Skip'}</span>
                        </label>`;
                }

                item.innerHTML = `
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-[10px] font-bold text-gray-400 uppercase tracking-[0.2em]">${dayStr}</span>
                        <i data-lucide="calendar-check-2" class="w-4 h-4 text-[#6f1e3b]/60"></i>
                    </div>
                    <div class="space-y-3">
                        ${slotsHtml}
                    </div>
                `;
                list.appendChild(item);
            }
            if (window.lucide) lucide.createIcons();
        }

        function toggleMealSkip(dayIndex, slot) {
            const key = `${dayIndex}-${slot}`;
            const index = config.skips.indexOf(key);
            if (index > -1) config.skips.splice(index, 1);
            else config.skips.push(key);
            generateCalendar();
            calculatePricing();
        }

        function calculatePricing() {
            const perMeal = config.pricing[config.duration] || 273;
            const basePerMeal = config.pricing[1];
            const activeSlotsCount = (config.slots.lunch ? 1 : 0) + (config.slots.dinner ? 1 : 0);

            const totalPotentialMeals = activeSlotsCount * config.duration;
            const skippedMealsCount = config.skips.length;
            const actualMealsPerSubscription = Math.max(0, totalPotentialMeals - skippedMealsCount);

            const totalMeals = actualMealsPerSubscription * config.people;
            const finalTotal = totalMeals * perMeal;
            const oldTotal = totalMeals * basePerMeal;
            const savings = oldTotal - finalTotal;
            const savePercent = Math.round((savings / oldTotal) * 100) || 0;

            const el1 = document.getElementById('price-per-meal');
            const el2 = document.getElementById('summary-meals-day');
            const el3 = document.getElementById('summary-days');
            const el4 = document.getElementById('summary-people');
            const el5 = document.getElementById('final-total');

            if (el1) el1.innerText = perMeal;
            if (el2) el2.innerText = activeSlotsCount;
            if (el3) el3.innerText = config.duration;
            if (el4) el4.innerText = config.people;
            if (el5) el5.innerText = Math.round(finalTotal);

            const badge = document.getElementById('save-badge');
            const savePctEl = document.getElementById('save-percent');
            if (savePercent > 0 && badge) {
                badge.classList.remove('hidden');
                if (savePctEl) savePctEl.innerText = savePercent;
            } else if (badge) {
                badge.classList.add('hidden');
            }
        }

        function updateDabbaStack() {
            const pincode = config.pincode || '';
            const diet = config.diet || '';
            const duration = config.duration || 1;
            const nameInput = document.getElementById('contact-name');
            const name = nameInput ? nameInput.value : '';

            const label1 = pincode ? `📍 PIN: ${pincode}` : '📍 PINCODE';
            const label2 = diet ? (diet.toLowerCase().includes('veg') && !diet.toLowerCase().includes('non') ? '🥗 VEG' : '🍖 NON-VEG') : '🥗 DIET PREF';
            const label3 = `📅 ${duration} DAYS`;
            const label4 = name ? `👤 ${name.toUpperCase().substring(0, 12)}` : '👤 CONTACT INFO';
            const label5 = '🗺️ DELIVERY ADDR';

            const d1 = document.getElementById('assembly-dabba-1');
            const d2 = document.getElementById('assembly-dabba-2');
            const d3 = document.getElementById('assembly-dabba-3');
            const d4 = document.getElementById('assembly-dabba-4');
            const d5 = document.getElementById('assembly-dabba-5');

            if (d1) d1.innerText = label1;
            if (d2) d2.innerText = label2;
            if (d3) d3.innerText = label3;
            if (d4) d4.innerText = label4;
            if (d5) d5.innerText = label5;

            // Activate levels only up to current step
            for (let i = 1; i <= 5; i++) {
                const level = document.getElementById(`assembly-dabba-${i}`);
                if (level) {
                    if (i < currentStep || (isOrderCompleted && i === 5)) {
                        level.classList.add('active');
                        level.classList.remove('opacity-0', 'pointer-events-none');
                        if (i === 2 && diet) {
                            if (diet.toLowerCase().includes('veg') && !diet.toLowerCase().includes('non')) {
                                level.classList.add('veg-active');
                                level.classList.remove('nonveg-active');
                            } else {
                                level.classList.add('nonveg-active');
                                level.classList.remove('veg-active');
                            }
                        }
                    } else if (i > currentStep) {
                        level.classList.remove('active', 'veg-active', 'nonveg-active');
                        level.classList.add('opacity-0', 'pointer-events-none');
                    }
                }
            }

            // Sync lid bottom offset dynamically
            const assemblyLid = document.getElementById('assembly-lid');
            const dabbaStack = document.getElementById('desktop-dabba-stack');
            if (assemblyLid) {
                if (currentStep === 5 || isOrderCompleted) {
                    assemblyLid.classList.add('active');
                    if (dabbaStack) {
                        const stackH = dabbaStack.offsetHeight;
                        assemblyLid.style.bottom = `${stackH + 8}px`;
                    }
                } else {
                    assemblyLid.classList.remove('active');
                }
            }
        }

        function completeOrder() {
            if (isOrderCompleted) return;
            isOrderCompleted = true;

            updateDabbaStack();

            const name = document.getElementById('contact-name').value || 'John Doe';
            const pincode = config.pincode || '400001';
            const diet = config.diet || 'Veg';
            const duration = config.duration || 1;
            const slotText = (config.slots.lunch && config.slots.dinner) ? 'Lunch + Dinner' : (config.slots.lunch ? 'Lunch Only' : (config.slots.dinner ? 'Dinner Only' : 'None'));

            document.querySelectorAll('.success-name').forEach(el => el.innerText = name.toUpperCase());
            document.querySelectorAll('.success-name-full').forEach(el => el.innerText = name);
            document.querySelectorAll('.success-pin').forEach(el => el.innerText = pincode);
            document.querySelectorAll('.success-duration').forEach(el => el.innerText = duration);

            const successDietDabba = document.getElementById('success-dabba-diet');
            const successDietLabel = document.getElementById('success-diet-label');
            if (successDietDabba && successDietLabel) {
                if (diet.toLowerCase().includes('veg') && !diet.toLowerCase().includes('non')) {
                    successDietDabba.className = 'dabba dabba-veg active animate-in';
                    successDietLabel.innerText = '🥗 VEG';
                    document.querySelector('.success-diet-summary').innerText = '🥗 Veg Subscription';
                } else {
                    successDietDabba.className = 'dabba dabba-nonveg active animate-in';
                    successDietLabel.innerText = '🍖 NON-VEG';
                    document.querySelector('.success-diet-summary').innerText = '🍖 Non-Veg Subscription';
                }
            }

            document.querySelector('.success-duration-summary').innerText = `${duration} Days (${slotText})`;
            document.querySelector('.success-pin-summary').innerText = `PIN: ${pincode}`;

            const dkCarrier = document.getElementById('desktop-carrier-frame');
            const dkStage = document.getElementById('desktop-tiffin-stage');
            if (dkCarrier && dkStage) {
                setTimeout(() => {
                    dkCarrier.classList.add('active');
                    setTimeout(() => {
                        dkStage.classList.add('assembled');
                    }, 400);
                }, 450);
            }

            // Return to camera hero view for epic lock animation before success modal!
            flowContainer.classList.remove('state-interior');
            flowContainer.classList.add('state-hero');

            setTimeout(() => {
                const successModal = document.getElementById('success-modal');
                if (successModal) {
                    successModal.classList.remove('hidden');
                    setTimeout(() => {
                        successModal.classList.remove('opacity-0');
                    }, 50);
                }
            }, 2000);
        }

        // Initialize lists
        generateCalendar();
        calculatePricing();
        updateStepUI();
        lucide.createIcons();

        // High visibility initial load diagnostics
        console.log("%c 🎬 [DabbaGo] Cinematic Checkout Experience Initialized successfully!", "background: #6f1e3b; color: #fca5a5; font-weight: bold; padding: 6px 12px; border-radius: 8px; border: 1px solid #fca5a5;");
        console.log(`%c Current Step: ${currentStep} | Order Completed: ${isOrderCompleted}`, "color: #b0b0b5; font-weight: bold;");
    </script>

    <!-- Beautiful Premium Success Modal overlay -->
    {success_content}
</body>

</html>
"""

# Format forms in checkout page template
compiled_html = cinematic_html.replace("{forms_content}", forms_content).replace("{success_content}", success_content)

# Write out the new order_experiment.html
with open(original_path, "w", encoding="utf-8") as f:
    f.write(compiled_html)

print("SUCCESS: Cinematic Checkout page successfully compiled and written!")
