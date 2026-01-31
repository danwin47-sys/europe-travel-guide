import os
import re

# --- Configuration ---
SOURCE_DIR = r"c:\python-training\travel"
OUTPUT_FILE = os.path.join(SOURCE_DIR, "travel_guide_offline.html")
FILES_TO_PROCESS = [
    "final_itinerary.md",
    "day_01.md",
    "day_02.md",
    "day_03.md",
    "day_04.md",
    "day_05.md",
    "day_06.md",
    "day_07.md",
    "day_08.md",
    "day_09.md",
    "day_10.md",
    "day_11.md",
    "day_12.md",
    "day_13.md",
    "packing_checklist.md",
    "survival_guide.md",
    "phrase_guide.md",
    "asian_food_guide.md",
    # Important supplementary guides
    "emergency_contacts.md",
    "restaurant_booking_guide.md",
    "budget_guide.md",
    "pre_departure_checklist.md",
    "luggage_storage_guide.md"
]

# --- Color Definitions ---
CITY_COLORS = {
    "final_itinerary": "#2c3e50",       # Dark Blue (General)
    "day_01": "#3498db",                # Bright Blue (Arrival)
    "day_02": "#2ecc71",                # Green (Königssee)
    "day_03": "#1abc9c",                # Turquoise (Lakes)
    "day_04": "#16a085",                # Dark Turquoise (Salzburg)
    "day_05": "#9b59b6",                # Purple (Moving)
    "day_06": "#8e44ad",                # Dark Purple (Innsbruck)
    "day_07": "#e74c3c",                # Red (Budapest)
    "day_08": "#c0392b",                # Dark Red (Castle)
    "day_09": "#e67e22",                # Orange (Thermal)
    "day_10": "#d35400",                # Dark Orange (Vienna)
    "day_11": "#f39c12",                # Yellow (Opera)
    "day_12": "#f1c40f",                # Bright Yellow (Art)
    "day_13": "#95a5a6",                # Grey (Departure)
    "packing_checklist": "#34495e",     # Dark Grey (Checklist)
    "survival_guide": "#e74c3c",        # Red (Emergency)
    "phrase_guide": "#27ae60",          # Green (Language)
    "asian_food_guide": "#d35400",      # Orange (Food)
    "emergency_contacts": "#c0392b",    # Dark Red (Emergency)
    "restaurant_booking_guide": "#e67e22", # Orange (Dining)
    "budget_guide": "#16a085",          # Teal (Money)
    "pre_departure_checklist": "#9b59b6", # Purple (Prep)
    "luggage_storage_guide": "#7f8c8d"  # Grey (Storage)
}

# --- CSS Styles (Enhanced Modern Design) ---
CSS_STYLES = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700&display=swap');
    
    :root {
        --primary-color: #2563eb;
        --primary-dark: #1e40af;
        --secondary-color: #06b6d4;
        --accent-color: #f59e0b;
        --bg-color: #f8fafc;
        --bg-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --text-color: #1e293b;
        --text-light: #64748b;
        --card-bg: #ffffff;
        --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --card-shadow-hover: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        --header-height: 64px;
        --border-radius: 12px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Noto Sans TC', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        line-height: 1.8;
        color: var(--text-color);
        background: var(--bg-color);
        margin: 0;
        padding-top: var(--header-height);
        padding-bottom: 80px;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        font-size: 16px;
    }
    
    .container {
        max-width: 750px;
        margin: 0 auto;
        padding: 32px 24px;
    }
    
    /* Sticky Top Header with Gradient */
    .top-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: var(--header-height);
        background: var(--bg-gradient);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 1001;
        backdrop-filter: blur(10px);
    }
    
    .header-title {
        font-size: 22px;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Modern Navigation Bar */
    .nav-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(12px);
        box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.08);
        display: flex;
        justify-content: flex-start;
        padding: 12px 8px;
        z-index: 1000;
        overflow-x: auto;
        gap: 6px;
        -webkit-overflow-scrolling: touch;
    }
    
    .nav-bar::-webkit-scrollbar {
        height: 4px;
    }
    
    .nav-bar::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 2px;
    }
    
    .nav-item {
        color: var(--text-light);
        text-decoration: none;
        font-size: 11px;
        text-align: center;
        padding: 10px 12px;
        flex: 0 0 auto;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        white-space: nowrap;
        background: #f1f5f9;
        border: 1.5px solid transparent;
        transition: var(--transition);
        min-width: 60px;
        font-weight: 500;
    }
    
    .nav-item:hover {
        background: #e2e8f0;
        transform: translateY(-3px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-color: var(--secondary-color);
    }
    
    .nav-item .day-num {
        font-weight: 700;
        font-size: 13px;
        margin-bottom: 3px;
        color: var(--text-color);
    }
    
    .nav-item .day-date {
        font-size: 9px;
        color: var(--text-light);
        font-weight: 400;
    }
    
    .nav-item .day-city {
        font-size: 8px;
        color: #94a3b8;
        margin-top: 2px;
    }
    
    .nav-item.active {
        color: white;
        font-weight: 600;
        background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
        border-color: var(--primary-color);
        box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
        transform: translateY(-4px);
    }
    
    .nav-item.active .day-num,
    .nav-item.active .day-date,
    .nav-item.active .day-city {
        color: rgba(255, 255, 255, 0.95);
    }
    
    /* Content Sections with Smooth Transitions */
    .page-section {
        display: none;
        animation: fadeInUp 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .page-section.active {
        display: block;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Typography */
    h1 {
        display: none;
    }
    
    h2 {
        color: var(--primary-color);
        font-size: 28px;
        font-weight: 700;
        border-bottom: 3px solid #e2e8f0;
        padding-bottom: 16px;
        margin: 48px 0 24px 0;
        letter-spacing: -0.5px;
        line-height: 1.3;
        cursor: pointer;
        user-select: none;
        position: relative;
        transition: all 0.3s ease;
    }
    
    h2:hover {
        color: var(--secondary-color);
    }
    
    h2::after {
        content: '▼';
        position: absolute;
        right: 10px;
        font-size: 18px;
        transition: transform 0.3s ease;
    }
    
    h2.collapsed::after {
        transform: rotate(-90deg);
    }
    
    .collapsible-content {
        max-height: 5000px;
        overflow: hidden;
        transition: max-height 0.5s ease-in-out, opacity 0.3s ease;
        opacity: 1;
    }
    
    .collapsible-content.collapsed {
        max-height: 0;
        opacity: 0;
    }
    
    h3 {
        color: var(--text-color);
        font-size: 20px;
        font-weight: 600;
        border-left: 4px solid var(--accent-color);
        padding-left: 16px;
        margin: 36px 0 20px 0;
        line-height: 1.4;
    }
    
    p {
        margin: 16px 0;
        color: var(--text-color);
        line-height: 1.8;
    }
    
    /* Lists */
    ul, ol {
        margin: 20px 0;
        padding-left: 32px;
    }
    
    li {
        margin: 12px 0;
        color: var(--text-color);
        line-height: 1.8;
    }
    
    li::marker {
        color: var(--primary-color);
        font-weight: 600;
    }
    
    /* Improved readability for list items */
    ul li, ol li {
        padding-left: 8px;
    }
    
    /* Better spacing between sections */
    .page-section > .container > *:first-child {
        margin-top: 0;
    }
    
    /* Blockquotes for better visual hierarchy */
    blockquote {
        margin: 24px 0;
        padding: 16px 20px;
        border-left: 4px solid var(--secondary-color);
        background: #f8fafc;
        border-radius: 8px;
        font-style: italic;
        color: var(--text-light);
    }
    
    /* Modern Tables with Better Readability */
    table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 28px 0;
        background: var(--card-bg);
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: var(--card-shadow);
        font-size: 15px;
        display: block;
        overflow-x: auto;
    }
    
    th, td {
        padding: 16px 14px;
        text-align: left;
        border-bottom: 1px solid #f1f5f9;
        min-width: 100px;
    }
    
    th {
        background: linear-gradient(135deg, #f8fafc, #f1f5f9);
        color: var(--text-color);
        font-weight: 600;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    tr:last-child td {
        border-bottom: none;
    }
    
    tbody tr:nth-child(even) {
        background: #fafbfc;
    }
    
    tr:hover {
        background: #f1f5f9;
    }
    
    /* Enhanced Alert Boxes with Better Readability */
    .alert {
        padding: 20px 24px;
        border-radius: var(--border-radius);
        margin: 28px 0;
        border-left: 5px solid;
        background: var(--card-bg);
        box-shadow: var(--card-shadow);
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        line-height: 1.8;
    }
    
    .alert::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        background: currentColor;
    }
    
    .alert:hover {
        box-shadow: var(--card-shadow-hover);
        transform: translateY(-2px);
    }
    
    .alert-tip {
        border-color: #3b82f6;
        background: linear-gradient(135deg, #eff6ff, #ffffff);
    }
    
    .alert-important {
        border-color: #10b981;
        background: linear-gradient(135deg, #ecfdf5, #ffffff);
    }
    
    .alert-warning {
        border-color: #f59e0b;
        background: linear-gradient(135deg, #fffbeb, #ffffff);
    }
    
    .alert strong {
        font-weight: 700;
        color: var(--text-color);
        display: block;
        margin-bottom: 8px;
    }
    
    .alert p {
        margin: 8px 0;
    }
    
    /* Checkbox Items */
    .checkbox-item {
        background: white;
        padding: 14px 16px;
        border-bottom: 1px solid #f1f5f9;
        display: flex;
        align-items: center;
        transition: var(--transition);
        border-radius: 8px;
        margin: 4px 0;
    }
    
    .checkbox-item:hover {
        background: #f8fafc;
        transform: translateX(4px);
    }
    
    .checkbox-item label {
        margin-left: 12px;
        width: 100%;
        cursor: pointer;
        color: var(--text-color);
    }
    
    input[type="checkbox"] {
        width: 20px;
        height: 20px;
        cursor: pointer;
        accent-color: var(--primary-color);
    }
    
    /* Lists */
    ul, ol {
        margin: 16px 0;
        padding-left: 28px;
    }
    
    li {
        margin: 8px 0;
        color: var(--text-color);
        line-height: 1.7;
    }
    
    /* Links */
    a {
        color: var(--primary-color);
        text-decoration: none;
        font-weight: 500;
        transition: var(--transition);
    }
    
    a:hover {
        color: var(--primary-dark);
        text-decoration: underline;
    }
    
    /* Smooth Scrolling */
    html {
        scroll-behavior: smooth;
    }
    
    /* Mobile Optimizations */
    @media (max-width: 768px) {
        .container {
            padding: 20px 16px;
        }
        
        h2 {
            font-size: 20px;
        }
        
        h3 {
            font-size: 16px;
        }
        
        .nav-item {
            min-width: 55px;
            padding: 8px 10px;
        }
    }
</style>
"""


# --- Javascript (Embedded for Interaction) ---
JS_SCRIPTS = """
<script>
    // City-specific colors
    const cityColors = {
        'final_itinerary': '#667eea',
        'day_01': '#2c3e50',
        'day_02': '#16a085',
        'day_03': '#27ae60',
        'day_04': '#2980b9',
        'day_05': '#8e44ad',
        'day_06': '#c0392b',
        'day_07': '#d35400',
        'day_08': '#f39c12',
        'day_09': '#e74c3c',
        'day_10': '#9b59b6',
        'day_11': '#3498db',
        'day_12': '#1abc9c',
        'day_13': '#34495e'
    };
    
    const cityNames = {
        'final_itinerary': '2026 中歐冬之旅',
        'day_01': 'Day 1 - 2/17 維也納→薩堡',
        'day_02': 'Day 2 - 2/18 國王湖',
        'day_03': 'Day 3 - 2/19 雙湖',
        'day_04': 'Day 4 - 2/20 薩爾茲堡',
        'day_05': 'Day 5 - 2/21 茵斯布魯克',
        'day_06': 'Day 6 - 2/22 維也納',
        'day_07': 'Day 7 - 2/23 布達佩斯',
        'day_08': 'Day 8 - 2/24 城堡山',
        'day_09': 'Day 9 - 2/25 溫泉',
        'day_10': 'Day 10 - 2/26 維也納',
        'day_11': 'Day 11 - 2/27 美泉宮',
        'day_12': 'Day 12 - 2/28 美景宮',
        'day_13': 'Day 13 - 3/1 離境'
    };
    
    function showSection(sectionId) {
        // Hide all sections
        document.querySelectorAll('.page-section').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        
        // Show target section
        document.getElementById(sectionId).classList.add('active');
        
        // Highlight nav
        const navLink = document.querySelector(`a[onclick="showSection('${sectionId}')"]`);
        if (navLink) navLink.classList.add('active');
        
        // Update Header Style & Title
        const primaryColor = cityColors[sectionId] || '#2c3e50';
        const header = document.querySelector('.top-header');
        header.style.backgroundColor = primaryColor;
        document.querySelector('.header-title').textContent = cityNames[sectionId];
        
        // Update CSS variable dynamically for headings
        document.documentElement.style.setProperty('--primary-color', primaryColor);
        
        // Scroll to top
        window.scrollTo(0,0);
        
        // Initialize collapsible sections for this page
        initCollapsible();
    }
    
    function initCollapsible() {
        // Get all H2 elements in the active section
        const activeSection = document.querySelector('.page-section.active');
        if (!activeSection) return;
        
        const h2Elements = activeSection.querySelectorAll('h2');
        
        h2Elements.forEach((h2, index) => {
            // Skip if already initialized
            if (h2.hasAttribute('data-collapsible')) return;
            h2.setAttribute('data-collapsible', 'true');
            
            // Wrap content between this h2 and next h2 (or end of section)
            const nextH2 = h2Elements[index + 1];
            const wrapper = document.createElement('div');
            wrapper.className = 'collapsible-content'; // Start expanded (removed 'collapsed')
            
            let currentElement = h2.nextElementSibling;
            const elementsToWrap = [];
            
            while (currentElement && currentElement !== nextH2) {
                elementsToWrap.push(currentElement);
                currentElement = currentElement.nextElementSibling;
            }
            
            // Insert wrapper after h2
            h2.parentNode.insertBefore(wrapper, h2.nextSibling);
            
            // Move elements into wrapper
            elementsToWrap.forEach(el => wrapper.appendChild(el));
            
            // Add collapsed class to h2 by default
            h2.classList.add('collapsed');
            
            // Add click handler
            h2.addEventListener('click', function() {
                this.classList.toggle('collapsed');
                wrapper.classList.toggle('collapsed');
            });
        });
    }
    
    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        showSection('final_itinerary');
    });
</script>
"""

# --- Simple Markdown Parser (Custom) ---
def parse_markdown(text):
    html = []
    lines = text.split('\n')
    in_table = False
    in_list = False
    in_alert = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            if in_table:
                html.append("</tbody></table>")
                in_table = False
            if in_list:
                html.append("</ul>")
                in_list = False
            if in_alert:
                html.append('</div>')
                in_alert = False
            i += 1
            continue
            
        # Headers
        if line.startswith('# '):
            pass # Skip H1 as it's used in sticky header now
        elif line.startswith('## '):
            if in_alert:
                html.append('</div>')
                in_alert = False
            html.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith('### '):
            if in_alert:
                html.append('</div>')
                in_alert = False
            html.append(f"<h3>{line[4:]}</h3>")
            
        # Alerts - Start
        elif line.startswith('> [!TIP]'):
            if in_alert:
                html.append('</div>')
            html.append('<div class="alert alert-tip"><strong>💡 TIP:</strong>')
            in_alert = True
        elif line.startswith('> [!IMPORTANT]'):
            if in_alert:
                html.append('</div>')
            html.append('<div class="alert alert-important"><strong>🔔 IMPORTANT:</strong>')
            in_alert = True
        elif line.startswith('> [!WARNING]') or line.startswith('> [!CAUTION]'):
            if in_alert:
                html.append('</div>')
            html.append('<div class="alert alert-warning"><strong>⚠️ WARNING:</strong>')
            in_alert = True
        elif line.startswith('> ') and in_alert:
            # Continue alert content
            html.append(f"{line[2:]}<br>")
        elif in_alert and not line.startswith('>'):
            # End of alert
            html.append('</div>')
            in_alert = False
            # Process this line normally (don't skip it)
            continue  # Will reprocess this line in next iteration

        # Tables
        elif '|' in line and (line.startswith('|') or ' | ' in line):
            if in_alert:
                html.append('</div>')
                in_alert = False
            cols = [c.strip() for c in line.strip('|').split('|')]
            if '---' in line:
                i += 1
                continue
            
            if not in_table:
                html.append("<table><thead><tr>")
                for c in cols: html.append(f"<th>{c}</th>")
                html.append("</tr></thead><tbody>")
                in_table = True
            else:
                html.append("<tr>")
                for c in cols: 
                    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                    html.append(f"<td>{content}</td>")
                html.append("</tr>")
        
        # Checkboxes
        elif line.startswith('- [ ] ') or line.startswith('- [x] '):
            if in_alert:
                html.append('</div>')
                in_alert = False
            checked = 'checked' if '[x]' in line else ''
            content = line[6:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html.append(f'<div class="checkbox-item"><input type="checkbox" {checked}><label>{content}</label></div>')
        
        # Lists
        elif line.startswith('- ') or line.startswith('* '):
            if in_alert:
                html.append('</div>')
                in_alert = False
            if not in_list: html.append("<ul>"); in_list = True
            content = line[2:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html.append(f"<li>{content}</li>")
        
        else:
            if not in_alert:
                line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
                line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
                html.append(f"<p>{line}</p>")
        
        i += 1
    
    # Close any remaining open tags
    if in_alert:
        html.append('</div>')
    if in_table:
        html.append("</tbody></table>")
    if in_list:
        html.append("</ul>")
        
    return "\n".join(html)

def generate_app():
    nav_items = []
    content_sections = []
    
    name_map = {
        "final_itinerary.md": "總行程表",
        "day_01.md": "Day 1 - 2/17",
        "day_02.md": "Day 2 - 2/18",
        "day_03.md": "Day 3 - 2/19",
        "day_04.md": "Day 4 - 2/20",
        "day_05.md": "Day 5 - 2/21",
        "day_06.md": "Day 6 - 2/22",
        "day_07.md": "Day 7 - 2/23",
        "day_08.md": "Day 8 - 2/24",
        "day_09.md": "Day 9 - 2/25",
        "day_10.md": "Day 10 - 2/26",
        "day_11.md": "Day 11 - 2/27",
        "day_12.md": "Day 12 - 2/28",
        "day_13.md": "Day 13 - 3/1",
        "packing_checklist.md": "行李清單",
        "survival_guide.md": "生存指南",
        "phrase_guide.md": "常用短句",
        "asian_food_guide.md": "亞洲美食",
        "emergency_contacts.md": "緊急聯絡",
        "restaurant_booking_guide.md": "餐廳預約",
        "budget_guide.md": "預算指南",
        "pre_departure_checklist.md": "出發檢查",
        "luggage_storage_guide.md": "行李寄放"
    }

    # Map Configuration: filename -> map image filename (not used for daily structure)
    map_images = {}
    
    import base64
    import json
    
    # Initialize variables
    first_section = None
    city_colors_json = json.dumps(CITY_COLORS)
    city_names_json = json.dumps({k.replace('.md',''): v for k,v in name_map.items()})

    for filename in FILES_TO_PROCESS:
        filepath = os.path.join(SOURCE_DIR, filename)
        if not os.path.exists(filepath): continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        section_id = filename.replace('.md', '')
        if first_section is None: first_section = section_id
        
        display_name = name_map.get(filename, filename)
        
        # Day metadata: date and location
        day_metadata = {
            "day_01.md": {"date": "2/17", "city": "VIE→SBG"},
            "day_02.md": {"date": "2/18", "city": "國王湖"},
            "day_03.md": {"date": "2/19", "city": "雙湖"},
            "day_04.md": {"date": "2/20", "city": "薩堡"},
            "day_05.md": {"date": "2/21", "city": "→茵堡"},
            "day_06.md": {"date": "2/22", "city": "→維也納"},
            "day_07.md": {"date": "2/23", "city": "→布達"},
            "day_08.md": {"date": "2/24", "city": "城堡山"},
            "day_09.md": {"date": "2/25", "city": "溫泉"},
            "day_10.md": {"date": "2/26", "city": "→維也納"},
            "day_11.md": {"date": "2/27", "city": "美泉宮"},
            "day_12.md": {"date": "2/28", "city": "美景宮"},
            "day_13.md": {"date": "3/1", "city": "離境"}
        }
        
        # Create navigation HTML
        if filename.startswith('day_'):
            day_num = filename.replace('day_', '').replace('.md', '')
            meta = day_metadata.get(filename, {"date": "", "city": ""})
            nav_html = f'''<a href="#" class="nav-item" onclick="showSection('{section_id}')">
                <div class="day-num">D{day_num}</div>
                <div class="day-date">{meta['date']}</div>
                <div class="day-city">{meta['city']}</div>
            </a>'''
        elif display_name == "總行程表":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">總覽</div></a>'
        elif display_name == "行李清單":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">行李</div></a>'
        elif display_name == "生存指南":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">指南</div></a>'
        elif display_name == "常用短句":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">短句</div></a>'
        elif display_name == "亞洲美食":
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><div class="day-num">美食</div></a>'
        else:
            short_name = display_name[:2] if len(display_name)>3 else display_name
            nav_html = f'<a href="#" class="nav-item" onclick="showSection(\'{section_id}\')"><span>{short_name}</span></a>'
        
        nav_items.append(nav_html)
        html_content = parse_markdown(md_content)
        
        # Inject Map if available
        map_html = ""
        if filename in map_images:
            map_path = os.path.join(SOURCE_DIR, map_images[filename])
            # Check if file exists, if not try the artifact path just in case (optional, but stick to local)
            # Actually, we rely on the copy command having run.
            # To be robust, let's look for the map file with a glob if exact match fails? No, keep it simple.
            # If map file exists, read chunks and base64 encode
            
            # Find the actual file (ignoring timestamp suffix if possible? No, users code uses fixed names)
            # Wait, the subagent saved them as map_vienna_TIMESTAMP.png
            # I instructed it to save as map_vienna.png but subagent tool output says:
            # "map_vienna_1769400332540.png"
            # I must handle this dynamic filename or rename the files during copy.
            # I will assume the COPY command used wildcards so the destination has the timestamps too.
            # I need to find the files in the directory that MATCH the pattern.
            
            # Simple approach: Search for file starting with map_vienna in SOURCE_DIR
            candidates = [f for f in os.listdir(SOURCE_DIR) if f.startswith(map_images[filename].replace('.png','')) and f.endswith('.png')]
            if candidates:
                real_map_path = os.path.join(SOURCE_DIR, candidates[0]) # Take the first match
                with open(real_map_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                    map_html = f'<div class="map-container"><img src="data:image/png;base64,{encoded_string}" alt="{display_name} Map" style="width:100%; border-radius:8px; margin-bottom:20px; box-shadow:0 2px 5px rgba(0,0,0,0.1);"></div>'

        content_sections.append(f'<div id="{section_id}" class="page-section"><div class="container">{map_html}{html_content}</div></div>')

    # Inject JSON data into JS
    final_js = JS_SCRIPTS.replace('%CITY_COLORS_JSON%', city_colors_json).replace('%CITY_NAMES_JSON%', city_names_json)

    full_html = f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>2026 中歐冬之旅</title>
        {CSS_STYLES}
    </head>
    <body>
        <div class="top-header">
            <div class="header-title">2026 中歐冬之旅</div>
        </div>
        
        <div id="app">
            {''.join(content_sections)}
        </div>
        
        <nav class="nav-bar">
            {''.join(nav_items)}
        </nav>

        {final_js}
        <script>
            // Init
            showSection('{first_section}');
        </script>
    </body>
    </html>
    """
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Generated improved offline app: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_app()
